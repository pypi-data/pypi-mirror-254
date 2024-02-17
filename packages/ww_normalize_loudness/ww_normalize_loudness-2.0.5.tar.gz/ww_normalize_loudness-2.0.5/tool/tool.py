#
# GENERATED: DO NOT EDIT
#
import os
import os.path as osp
import sys
import time
# 3rd party
from kkpyui import kkpyui as ui
import kkpyutil as util
# project
import control as ctrl


# <LOCK
@util.rerun_lock(name=__file__, folder=osp.abspath(f'{util.get_platform_tmp_dir()}/_miatech/ww_normalize_loudness'), max_instances=1)
# LOCK>
def main():
    # <VIEW
    ui.Globals.root = ui.Root('Loudness Normalization', (800, 600), osp.join(osp.dirname(__file__), 'tool.png'))
    form = ui.Form(ui.Globals.root, page_titles=['Search', 'Platform', 'Loudness', 'global', 'output'])
    ctrlr = ctrl.Controller(form)
    ui.Globals.root.set_controller(ctrlr)
    ui.Globals.root.bind_events()
    menu = ui.FormMenu(ui.Globals.root, ctrlr)
    pg_global = form.pages['global']
    pg_loudness = form.pages['loudness']
    pg_output = form.pages['output']
    pg_platform = form.pages['platform']
    pg_search = form.pages['search']
    root = ui.TextEntry(pg_search, 'root', 'Root Wwise Object', '', '搜索起点路径，将查找其所有下属对象；默认为当前选中对象', True, )
    inclkeywords = ui.TextEntry(pg_search, 'inclKeywords', 'Keywords In Text', [], '用于文本查找的包含规则；可为关键字或正则表达式；多条表达式间为或关系，启用 Include All (-I) 时为与关系；默认为空', True, )
    inclallkeywords = ui.BoolEntry(pg_search, 'inclAllKeywords', 'Include All Keywords', False, '启用后将 includes 中的多条规则视为与关系；默认为或关系', True)
    exclkeywords = ui.TextEntry(pg_search, 'exclKeywords', 'Keywords Not In Text', [], '用于文本查找的排除规则；可为关键字或正则表达式；多条表达式间为或关系；默认为空；当与包含规则冲突时，排除规则的优先级高于包含规则', True, )
    exclallkeywords = ui.BoolEntry(pg_search, 'exclAllKeywords', 'Exclude All Keywords', False, '启用后将 excludes 中的多条规则视为与关系；默认为或关系', True)
    textscope = ui.MultiOptionEntry(pg_search, 'textScope', 'Text Search Scope', ['*', 'name', 'notes', 'path'], ['name'], '要用关键字搜索的对象属性范围；默认为对象名', True)
    masterplat = ui.SingleOptionEntry(pg_platform, 'masterPlat', 'Master Platform', ['*', 'Windows', 'Mac', 'XboxOne', 'PS4', 'PS5', 'Switch', 'Android', 'iOS'], '*', '既表示需要断联独立出来的平台，也表示用于建立主从关系的主平台；默认为全部，即断联所有平台且相互独立；若不用默认，则只能选择一个主平台', True)
    slaveplats = ui.MultiOptionEntry(pg_platform, 'slavePlats', 'Slave Platforms', ['', 'Windows', 'Mac', 'XboxOne', 'PS4', 'PS5', 'Switch', 'Android', 'iOS'], [''], '主平台的从属平台列表，从属于 --master-platform 对应平台；默认为空，即所有平台相互独立；当 --master-platform 为 * 时，此参数会忽略', True)
    targetlufs = ui.FloatEntry(pg_loudness, 'targetLUFS', 'Target Loudness (LUFS)', -16.0, '输入文件需要达到的目标响度，低于或高于此值的文件将被修正', True, [-32.0, -14.0], 0.1, 1)
    maxlufsraise = ui.FloatEntry(pg_loudness, 'maxLufsRaise', 'Max Loudness Gain (LUFS)', 10.0, '允许的最大响度提升，用来防止错误放大本来应该很轻的声音', True, [0.0, 10.0], 0.1, 1)
    maxlufsdrop = ui.FloatEntry(pg_loudness, 'maxLufsDrop', 'Max Loudness Drop (LUFS)', 10.0, '允许的最大响度下降，用来防止错误缩小本来应该很响的声音', True, [0.0, 10.0], 0.1, 1)
    maxpeakdb = ui.FloatEntry(pg_loudness, 'maxPeakDB', 'Target Amplitude Peak (dBFS)', -3.0, '输入文件需要达到的目标电平峰值，高于此值视为电平溢出', True, [-18.0, 0.0], 0.1, 1)
    maxpeakoverflowdb = ui.FloatEntry(pg_loudness, 'maxPeakOverflowDB', 'Max Amplitude Peak Overflow (dBFS)', 3.0, '输入文件的最大电平溢出量，溢出高于此值的文件将不参加响度处理', True, [0.0, 7.0], 0.1, 1)
    decisiontable = ui.FileEntry(pg_search, 'decisionTable', 'Decision Table', '', '响度决策表（.xlsx 后缀）的路径，采用后将忽略 --root 而直接采用未成功的 Sound SFX 对象作为待处理对象；默认不用', True, [['Loudness Normalization Decision Table', '*.ln.xlsx']], util.get_platform_home_dir())
    save_preset = ui.BoolEntry(pg_global, 'saveConfig', 'Save Preset', True, '保存上一次成功运行的参数配置')
    dry_run = ui.BoolEntry(pg_global, 'dryRun', 'Dry Run', False, '预览服务内容而不执行具体工作')
    notify_user = ui.BoolEntry(pg_global, 'notifyUser', 'Notify User', True, '启用后执行成功时通知用户；用户需配置全局企业微信群机器人 webhook 地址，未配置则不通知；默认不通知成功结果；但失败结果一律通知')
    out_wobjlistok = ui.ReadOnlyPathEntry(pg_output, 'wobjListOK', 'Sounds: OK', '', '响度无须修正的 Wwise 对象路径，保存在此表单文本文件中')
    out_wobjlistfixed = ui.ReadOnlyPathEntry(pg_output, 'wobjListFixed', 'Sounds: Fixed', '', '响度修正成功后的 Wwise 对象路径，保存在此表单文本文件中')
    out_wobjlistneedsadjust = ui.ReadOnlyPathEntry(pg_output, 'wobjListNeedsAdjust', 'Sounds: Needs Adjustment', '', '响度修正预览失败或修正后仍然失败的 Wwise 对象路径，保存在此表单文本文件中')
    out_report = ui.ReadOnlyPathEntry(pg_output, 'report', 'Report', '', '响度修正结果报表，一般需要后续人工决策')
    action_bar = ui.FormActionBar(ui.Globals.root, ctrlr)
    progress_bar = ui.ProgressBar(ui.Globals.root, ui.Globals.progressQueue)
    progress_bar.poll()
    ui.Globals.root.mainloop()
    # VIEW>
    pass


if __name__ == "__main__":
    main()
