from miautil import typemap as tm


class Output:
    def __init__(self):
        # 响度无须修正的 Wwise 对象路径，保存在此表单文本文件中
        self.wobjListOK: tm.tWobjPathList = ''
        # 响度修正成功后的 Wwise 对象路径，保存在此表单文本文件中
        self.wobjListFixed: tm.tWobjPathList = ''
        # 响度修正预览失败或修正后仍然失败的 Wwise 对象路径，保存在此表单文本文件中
        self.wobjListNeedsAdjust: tm.tWobjPathList = ''
        # 响度修正结果报表，一般需要后续人工决策
        self.report: tm.tFile = ''
