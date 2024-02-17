import os.path as osp

# 3rd party
import kkpyutil as util

# project
from miautil import service
from miautil import typemap as tm
_cm = util.init_repo(__file__, organization='_miatech', uselocale=True)
_serv_name = osp.basename(_cm.ancestorDirs[1])
core = util.safe_import_module(f'{_serv_name}_core', _cm.srcDir)


def get_program_info():
    description = '标准化 Wwise 工程层级中顶层节点下符合条件的所有音频素材的音量'
    examples = """
# 标准化指定 WorkUnit 下符合关键字的音频素材响度，在名字和备注中搜索关键字，并使各平台的素材源文件独立，采用默认响度标准
run.bat -R "/Actor-Mixer Hierarchy/Ambient" -i footstep animal -I -s name notes

# 同上，但仅断联 Windows/XboxOne/PS5 平台，并建立以 Windows 为主的主从关系，即再用 Windows 平台源文件覆盖从属平台源文件
run.bat -R "/Actor-Mixer Hierarchy/Ambient" -i footstep animal -I -s name notes -m Windows -l XboxOne PS5

# 寻找上一次标准化时未成功的素材，用新参数重新标准化
run.bat -L -l -23 -r 6 -d 5 -p -6 -P 3
"""
    remarks = """\
- 处理后应检查决策报表，在 Decision 列中手动处理可算作响度/峰值过关的素材，在 Notes 列中选填备注比如决策理由
"""
    return description, examples, remarks


def add_arguments(parser):
    parser.add_argument(
        '-R',
        '--root',
        action='store',
        dest='root',
        type=tm.tWobj,
        default='',
        required=False,
        help='搜索起点路径，将查找其所有下属对象；默认为当前选中对象'
    )
    # ww_find_objs
    parser.add_argument(
        '-i',
        '--keywords-in-text',
        action='store',
        type=str,
        dest='inclKeywords',
        nargs='*',
        default=[],
        required=False,
        help='用于文本查找的包含规则；可为关键字或正则表达式；多条表达式间为或关系，启用 Include All (-I) 时为与关系；默认为空'
    )
    parser.add_argument(
        '-I',
        '--include-all-keywords',
        action='store_true',
        dest='inclAllKeywords',
        default=False,
        required=False,
        help='启用后将 includes 中的多条规则视为与关系；默认为或关系'
    )
    parser.add_argument(
        '-e',
        '--keywords-not-in-text',
        action='store',
        type=str,
        dest='exclKeywords',
        nargs="*",
        default=[],
        required=False,
        help='用于文本查找的排除规则；可为关键字或正则表达式；多条表达式间为或关系；默认为空；当与包含规则冲突时，排除规则的优先级高于包含规则'
    )
    parser.add_argument(
        '-E',
        '--exclude-all-keywords',
        action='store_true',
        dest='exclAllKeywords',
        default=False,
        required=False,
        help='启用后将 excludes 中的多条规则视为与关系；默认为或关系'
    )
    parser.add_argument(
        '-s',
        '--text-search-scope',
        action='store',
        dest='textScope',
        type=str,
        choices=[
            '*',
            'name',
            'notes',
            'path',
        ],
        default=['name'],
        required=False,
        help='要用关键字搜索的对象属性范围；默认为对象名'
    )
    # ww_unlink_srcs
    parser.add_argument(
        '-M',
        '--master-platform',
        action='store',
        choices=('*', 'Windows', 'Mac', 'XboxOne', 'PS4', 'PS5', 'Switch', 'Android', 'iOS'),
        dest='masterPlat',
        type=str,
        default='*',
        required=False,
        help='既表示需要断联独立出来的平台，也表示用于建立主从关系的主平台；默认为全部，即断联所有平台且相互独立；若不用默认，则只能选择一个主平台'
    )
    parser.add_argument(
        '-L',
        '--slave-platforms',
        action='store',
        nargs='*',
        choices=('', 'Windows', 'Mac', 'XboxOne', 'PS4', 'PS5', 'Switch', 'Android', 'iOS'),
        dest='slavePlats',
        type=str,
        default=[''],
        required=False,
        help='主平台的从属平台列表，从属于 --master-platform 对应平台；默认为空，即所有平台相互独立；当 --master-platform 为 * 时，此参数会忽略'
    )
    # rp_normalize_loudness
    parser.add_argument(
        '-l',
        '--target-loudness-lufs',
        action='store',
        dest='targetLUFS',
        type=float,
        default=-16.0,
        required=False,
        help='输入文件需要达到的目标响度，低于或高于此值的文件将被修正'
    )
    parser.add_argument(
        '-r',
        '--max-loudness-gain-lufs',
        action='store',
        dest='maxLufsRaise',
        type=float,
        default=10.0,
        required=False,
        help='允许的最大响度提升，用来防止错误放大本来应该很轻的声音'
    )
    parser.add_argument(
        '-d',
        '--max-loudness-drop-lufs',
        action='store',
        dest='maxLufsDrop',
        type=float,
        default=10.0,
        required=False,
        help='允许的最大响度下降，用来防止错误缩小本来应该很响的声音'
    )
    parser.add_argument(
        '-p',
        '--target-amplitude-peak-dbfs',
        action='store',
        dest='maxPeakDB',
        type=float,
        default=-3.0,
        required=False,
        help='输入文件需要达到的目标电平峰值，高于此值视为电平溢出'
    )
    parser.add_argument(
        '-P',
        '--max-amplitude-peak-overflow-dbfs',
        action='store',
        dest='maxPeakOverflowDB',
        type=float,
        default=3.0,
        required=False,
        help='输入文件的最大电平溢出量，溢出高于此值的文件将不参加响度处理'
    )
    parser.add_argument(
        '-t',
        '--decision-table',
        action='store',
        dest='decisionTable',
        type=tm.tSpreadsheetFile,
        default='',
        required=False,
        help='响度决策表（.xlsx 后缀）的路径，采用后将忽略 --root 而直接采用未成功的 Sound SFX 对象作为待处理对象；默认不用'
    )


def main():
    desc, examples, remarks = get_program_info()
    parser = service.ArgParser(desc, examples, remarks, add_arguments)
    args = parser.main()
    core.main(args)


if __name__ == '__main__':
    main()
