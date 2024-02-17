"""
- implement callbacks on_*() defined in gui-controller prototype
"""
import os.path as osp
import types

# 3rd party
from kkpyui import kkpyui as ui
import kkpyutil as util
# project
from miautil import service, bugreport

_cm = util.init_repo(__file__, organization='_miatech', uselocale=False)
_serv_name = osp.basename(_cm.ancestorDirs[1])
core = util.safe_import_module(f'{_serv_name}_core', _cm.srcDir)


# <CONTROLLER_CLASS
class Controller(ui.FormController):
# CONTROLLER_CLASS>
    """
    - implement gui event-handlers
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.worker = None

    def prepare_session_args(self):
        """
        - full session args = sharedArgs + serviceArgs + progressCallback
        - prepare app-session args for service session
        - TODO: reflect shared args to UI
        """
        def _set_core_progress(percentage, message):
            """
            - translate progress set by worker into progress-bar updates
            """
            title, perc = '/processing', percentage
            self.set_progress(title, perc, message)

        args = types.SimpleNamespace(
            cfgFile='',  # without loading preset
            appSessionID=service.Session.generate_id(_serv_name, 'tool'),
        )
        serv_args = self.get_latest_model()
        # <TRIM_OUTPUT
        del serv_args.wobjListOK
        del serv_args.wobjListFixed
        del serv_args.wobjListNeedsAdjust
        del serv_args.report
        # TRIM_OUTPUT>
        serv_args.progress_callback = _set_core_progress
        args = util.merge_namespaces(args, serv_args)
        return args

    def on_open_help(self):
        """
        - implement this to open help URL/file in default browser
        """
        help_file = osp.join(osp.dirname(__file__), 'help.html')
        if not osp.isfile(help_file):
            return
        util.open_in_browser(help_file)

    def on_open_diagnostics(self):
        """
        - implement this to open log file in default browser
        """
        if not self.worker:
            return
        util.open_in_editor(self.worker.get_session_folder())

    def on_report_issue(self):
        """
        - implement this to receive user feedback
        - due to BIN-1496, bugreport cannot be escalated to worker class
        """
        if not self.worker:
            return
        self.worker.report_issue()
        app = 'tool'
        saved_to = self.worker.save_diagnostics(app=app)
        problem = f'{self.worker.pathMan.paths.servName}.{app}'
        reporter = bugreport.Reporter(problem, logger=self.worker.logger)
        reporter.login_jira()
        reporter.create_issue(description=f'Problem Source: {problem}')
        self.worker.pathMan.create_mounted_paths()
        reporter.upload_diagnostics(saved_to, self.worker.pathMan.paths.netdrvBugDir)
        reporter.link_diagnostics_to_issue()
        reporter.notify_dev()
        reporter.open_issue_page()
        util.safe_remove(saved_to)

    def on_startup(self):
        """
        - called just before showing root window, after all fields are initialized
        - so that fields can be used here for the first time
        """
        pass

    def on_shutdown(self, event=None) -> bool:
        """
        - called just before quitting
        - base-class safe-schedules shutdown with prompt and early-outs if user cancels
        - impelement post-user-confirm logic here, or override completely
        """
        if not super().on_shutdown():
            return False
        # IMPELEMENT POST-USER-CONFIRM LOGIC HERE
        return True

    def run_task(self, event=None):
        """
        - runs in a background thread out of the box to unblock UI
        - implement this to execute the main task in the background
        """
        self.worker = service.run_tool_session(self.prepare_session_args(), _cm.ancestorDirs[1], core.Worker)
        # <REFLECT_OUTPUT
        self.model['wobjListOK'] = self.worker.out.wobjListOK
        self.model['wobjListFixed'] = self.worker.out.wobjListFixed
        self.model['wobjListNeedsAdjust'] = self.worker.out.wobjListNeedsAdjust
        self.model['report'] = self.worker.out.report
        self.update_view()
        # REFLECT_OUTPUT>

    def on_cancel(self, event=None):
        """
        - if task-thread is alive, base-controller schedules stop-event and waits for task to finish
        - implement pre-cancel and post-cancel logic here, or override completely
        """
        # IMPLEMENT PRE-CANCELLING LOGIC HERE, E.G., DATA PROTECTION
        super().on_cancel(event)
        # IMPLEMENT POST-CANCELLING LOGIC HERE, E.G., CLEANUP
        pass
