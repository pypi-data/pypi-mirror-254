import linecache
from pathlib import Path


class FunctionData:
    def __init__(self) -> None:
        self.funtionName = ''      # 函数名
        self.fileName = ''         # 文件名
        self.startLineNumber = 0   # 函数开始行
        self.endLineNumber = 0     # 函数结束行
        self.comment = ''          # 代码点评
        self.source = ''           # 源代码

    def content(self) -> str:
        # 确定函数名所在的行
        functionName = self.funtionName.split('!')[1]  # 去掉!前的模块名称
        # 可能带namespace，而namespace很可能不包含在函数名所在的
        functionName = functionName.split('::')[-1] + '('

        if not self.fileName:
            return f"没有找到文件路径"

        if not Path(self.fileName).exists():
            return f"没有找到文件 {self.fileName}"

        nCount = 20
        for i in range(self.startLineNumber, 0, -1):
            line = linecache.getline(self.fileName, i)
            nCount = nCount - 1
            if functionName in line or nCount == 0:  # 最多往上搜索20行
                break

        lines = []
        for i in range(i, self.endLineNumber + 1):
            line = linecache.getline(self.fileName, i)
            lines.append(line)

        return ''.join(lines)

    def assign(self, o: dict) -> None:
        self.__dict__ = o

    def __repr__(self):
        return f"<FunctionData: {self.funtionName}: {self.fileName} ({self.startLineNumber} - {self.endLineNumber})>"


class BreakPointHit:
    def __init__(self) -> None:
        self.id = 0                # id号
        self.offset = 0            # 函数入口偏移量
        self.retOffset = 0         # 函数出口偏移量
        self.funtionName = ''      # 函数名
        self.isStart = True        # 函数入口或出口
        self.appendix = ''         # 附件信息
        self.threadId = 0          # 线程Id

    def __repr__(self):
        return f"<common.BreakPointHit offset:{self.offset}, functionName:{self.functionName}, isStart:{self.isStart}>"

    def assign(self, o: dict) -> None:
        self.__dict__ = o

    def pairWith(self, hit) -> bool:
        return self.offset == hit.offset and \
            self.threadId == hit.threadId and \
            self.isStart != hit.isStart


class BreakPointPairError(Exception):
    def __init__(self, hit: BreakPointHit):
        self.message = f"The hit {hit.id} is not matched"
        super().__init__(self.message)
