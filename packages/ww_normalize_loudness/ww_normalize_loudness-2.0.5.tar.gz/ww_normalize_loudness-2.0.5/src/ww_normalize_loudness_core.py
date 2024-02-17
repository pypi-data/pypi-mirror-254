import copy
import glob
import os
import os.path as osp

# 3rd party
import dryable
import kkpyutil as util

# project
from miautil import service
from miautil import dryop
from miautil import wwise as ww
import p4_checkout.src.p4_checkout_core as p4c
import rp_normalize_loudness.src.rp_normalize_loudness_core as rpl
import ww_find_objs.src.ww_find_objs_core as wfo
import ww_unlink_srcs.src.ww_unlink_srcs_core as wuo
_cm = util.init_repo(__file__, organization='_miatech')


def main(args):
    return service.run_core_session(args, _cm.ancestorDirs[1], validate_args, Worker)


def validate_args(args, logger=_cm.logger):
    fixed_args = copy.deepcopy(args)
    res = service.Result(logger=logger)
    if args.decisionTable and not osp.isfile(args.decisionTable):
        res.throw_filenotfound(args.decisionTable, '响度决策表')
    # fixed_args = p4c.validate_args(fixed_args, logger)
    # rp_normalize_loudness
    expected_range = (-32.0, -14.0)
    if not expected_range[0] <= args.targetLUFS <= expected_range[1]:
        res.throw(ValueError, f'目标响度必须在 {expected_range[0]}LUFS 和 {expected_range[1]}LUFS 之间')
    expected_range = (0, 10)
    if not expected_range[0] < args.maxLufsRaise <= expected_range[1]:
        res.throw(ValueError, f'目标响度最大提升量必须在 {expected_range[0]}LUFS 和 {expected_range[1]}LUFS 之间')
    expected_range = (0, 10)
    if not expected_range[0] < args.maxLufsDrop <= expected_range[1]:
        res.throw(ValueError, f'目标响度最大下降量必须在 {expected_range[0]}LUFS 和 {expected_range[1]}LUFS 之间')
    expected_range = (-18.0, 0.0)
    if not expected_range[0] <= args.maxPeakDB <= expected_range[1]:
        res.throw(ValueError, f'目标电平峰值必须在 {expected_range[0]}dBFS 和 {expected_range[1]}dBFS 之间')
    expected_range = (0, 7)
    if not expected_range[0] <= args.maxPeakOverflowDB <= expected_range[1]:
        res.throw(ValueError, f'目标电平溢出量必须在 {expected_range[0]}dBFS 和 {expected_range[1]}dBFS 之间')
    # ww_find_objs
    if args.root:
        fixed_args.root = ww.normalize_wpath(fixed_args.root)
        if not ww.is_absolute_wpath(fixed_args.root):
            res.succeeded = False
            res.detail = f'root path "{fixed_args.root}" is not absolute'
            res.throw(ValueError, f'Expected root path to be absolute, got {fixed_args.root}')
    if '*' in args.textScope:
        fixed_args.textScope = ['name', 'notes']
    with ww.WaapiClient() as client:
        global _all_plats
        _all_plats = sorted(list(plat['name'] for plat in client.query_platforms()))
    if not _all_plats:
        res.throw(ValueError, f'Expected at least one supported platform, got none', 'Check your Wwise version')
    if user_specified_master := args.masterPlat != '*':
        if link_all_as_slaves := '' in args.slavePlats:
            res.throw(ValueError, f'Expected slave platforms to be specified, got empty platform', 'Specify slave platforms')
        if args.masterPlat not in _all_plats:
            res.throw(ValueError, f'Expected master platform to be one of {_all_plats}, got {args.masterPlat}', 'Check your master platform')
        if (subset := set(args.slavePlats).intersection(set(_all_plats))) != set(args.slavePlats):
            res.throw(ValueError, f'Expected slave platforms to be a subset of {_all_plats}, got subset: {subset}', 'Fix your slave platforms')
        if args.masterPlat in args.slavePlats:
            fixed_args.slavePlats.remove(args.masterPlat)
    if args.masterPlat == '*':
        fixed_args.slavePlats = []
    return fixed_args


class Worker(service.WorkerBase):
    def __init__(self, session):
        super().__init__(session)
        self.pathMan.create_loudness_paths()
        self.waapiClient = None
        self.platSrcSndMap = None
        self.platSrcList = None
        self.afListFixed = None
        self.wprojOrgDir = None
        # USE WHEN NEEDED:
        # - call self.pathMan.create_<feature>_paths to add feature-specific paths on the fly
        # - extend _util.service.PathMan with new features by adding create_<feature>_paths() methods

    def main(self):
        with ww.WaapiClient() as self.waapiClient:
            self._retrieve_sounds()
            # self._scm_stage_files_folders()
            self._unlink_audiosources()
            self._normalize_loudness()
            self._import_results()
            # self._scm_stage_files_folders()
        self._scm_stage_files_folders()

        self.res.succeeded = True
        self.res.detail = 'DONE'
        self.res.advice = """"""
        return self.res, self.out

    def _retrieve_sounds(self):
        """
        - find sounds in hierarchy (clean run) or from given decision table version (incremental run)
        - note that user may jump back a few steps instead of just using the latest version
        - because errors made in the latest config could cause a large failure,
        - which then drives user to jump back to an even older version to start over
        """
        if self.args.decisionTable:
            cfg = osp.join(osp.dirname(self.args.decisionTable), f'{util.extract_path_stem(self.args.decisionTable)}.abp.json')
            assert osp.isfile(cfg)
            config = util.load_json(cfg)
            # retrieve sound list filled during previous report generation
            self.args.soundList = [rec['sound'] for plat_src, rec in config['batch'].items() if rec['decision']['value'] == 'Needs Adjustment']
            return self.args.soundList

        # TODO: support Sound Voice
        pm = service.PathMan.create_platform(osp.join(self.pathMan.paths.repoRoot, 'ww_find_objs'))
        args = service.init_args(schema=pm.paths.servSchema)
        util.merge_namespaces(args, self.args)
        args.objTypes = ['Sound']
        res, out = wfo.main(self.args)
        assert res.succeededa and osp.isfile(out.foundWobjList)
        self.args.soundList = util.lazy_load_listfile(out.foundWobjList)

    def _scm_stage_files_folders(self):
        """
        - must be called multiple times during a run
        - each run may start with two situations for selected sounds
          - no platform sources are not created
          - platform sources are present: each run increments the derivatives without overwriting
        - start: must checkout WorkUnits and Originals folder first for both cases
        - end: must checkout new platform sources carrying loudness fixes, and reports
        - allow for redundancies because they will be auto-dropped by p4 during submission
        """
        # workunits: given root, find all sounds, then find all workunits containing them
        snds = [snd for snd in self.waapiClient.query_objects(self.args.soundList, ['sound:originalWavFilePath', 'filePath'])]
        work_units = list({ww.safe_get_native_path(snd['filePath']) for snd in snds})
        # originals/
        self.wprojOrgDir = self.waapiClient.query_project_subfolder('Originals')
        snd_files = []
        for snd in snds:
            org = ww.extract_original_from_unlinked(ww.safe_get_native_path(snd['sound:originalWavFilePath']))
            snd_files += glob.glob(osp.abspath(f'{self.wprojOrgDir}/{util.extract_path_stem(org)}*.wav'))
        snd_list_to_checkout = [self.wprojOrgDir] + work_units + snd_files
        pm = service.PathMan.create_platform(osp.join(self.pathMan.paths.RepoRoot, 'p4_checkout'))
        args = service.init_args(schema=pm.paths.servSchema)
        args.pathList = snd_list_to_checkout
        res, out = p4c.main(self.args)
        assert res.succeeded

    def _unlink_audiosources(self):
        # TODO: export trim sheet
        pm = service.PathMan.create_platform(osp.join(self.pathMan.paths.RepoRoot, 'ww_unlink_srcs'))
        args = service.init_args(schema=pm.paths.servSchema)
        util.merge_namespaces(args, self.args)
        res, out = wuo.main(self.args)
        assert res.succeeded
        self.platSrcList = out.platSrcList
        plat_srcs = util.load_lines(self.platSrcList, rmlineend=True)
        for s, ps in enumerate(plat_srcs):
            master_bn = osp.basename(ps)
            self.platSrcSndMap[master_bn] = out.soundList[s]

    def _normalize_loudness(self):
        pm = service.PathMan.create_platform(osp.join(self.pathMan.paths.RepoRoot, 'rp_normalize_loudness'))
        args = service.init_args(schema=pm.paths.servSchema)
        util.merge_namespaces(args, self.args)
        self.args.platSrcList = self.platSrcList
        res, out = rpl.main(self.args)
        self.afListFixed = out.afListFixed

    def _import_results(self):
        """
        - rename and move loudness-fixed output files to platform sources
          - rename inside .rpp render folder for backtracking later
        - reimport the fixed latest platform sources and activate
        - import decision table and batch config
        - annotate master platform sources with loud-norm config and latest source index
        """
        # what version tag should we use as suffix?
        new_version = util.format_now()
        report_dir = osp.join(self.wprojOrgDir, '_loudness', new_version)
        os.makedirs(report_dir, exist_ok=True)
        decision_config = util.load_json(self.pathMan.paths.decisionConfig)
        # create tag using datetime now
        for af in self.afListFixed:
            # basename of master source is guaranteed to have a platform suffix
            master_bn = osp.basename(af)
            plat = master_bn.split('_')[-1].split('.')[0]
            src = osp.join(osp.dirname(af), f'{master_bn}_{new_version}.wav')
            os.rename(af, src)
            dst = osp.join(self.wprojOrgDir, f'{master_bn}_{new_version}.wav')
            self.logger.info(f'Importing loudness-normalization result: {af} -> {dst}')
            dryop.copy_file(src, dst)
            # import new normalized platform source
            self.waapiClient.import_audiosource(self.platSrcSndMap[master_bn], dst, plat=plat, activate_new_source=True)
            key = osp.join(self.wprojOrgDir, af)
            decision_config['batch'][key]['sound'] = self.platSrcSndMap[master_bn]
        # import decision table and its enhanced JSON copy
        for src in (self.pathMan.paths.decisionTable, self.pathMan.paths.decisionConfig):
            dst = osp.join(report_dir, osp.basename(src))
            dryop.copy_file(src, dst)
