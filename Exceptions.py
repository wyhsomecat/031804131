class NoTextError(Exception):  # 输入的文本为空

    def __init__(self):
        print("你载入了一个空文本...?")

    def __str__(self, *args, **kwargs):
        return "请检查一下文本吧"  # 为什么要加这个Exception？因为我在测试阶段真的犯过这种错


class SameTextError(Exception):  # 输入的文本差距小于一个字符，怀疑为同一文本

    def __init__(self):
        print("查重结果无限接近于100%...你是不是选择了相同的文本？")

    def __str__(self, *args, **kwargs):
        return "请检查一下文本吧"
