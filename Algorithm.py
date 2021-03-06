# encoding: utf-8
def lcs(maintext, comparedtext):    #LCS的计算函数

    #建立算法矩阵
    matrix = [''] * (len(maintext) + 1)
    for index_MT in range(len(matrix)):
        matrix[index_MT] = [''] * (len(comparedtext) + 1)

    #若ai = bj，则LCS(i, j) = LCS(i - 1, j - 1) + 1
    #若ai≠bj，则LCS(i,j)=Max(LCS(i-1,j-1),LCS(i-1,j),LCS(i,j-1))
    for index_MT in range(1, len(maintext) + 1):
        for index_CT in range(1, len(comparedtext) + 1):
            if maintext[index_MT - 1] == comparedtext[index_CT - 1]:
                matrix[index_MT][index_CT] = matrix[index_MT - 1][index_CT - 1] + maintext[index_MT - 1]
            elif len(matrix[index_MT][index_CT - 1]) > len(matrix[index_MT - 1][index_CT]):
                matrix[index_MT][index_CT] = matrix[index_MT][index_CT - 1]
            else:
                matrix[index_MT][index_CT] = matrix[index_MT - 1][index_CT]

    return len(matrix[len(maintext)][len(comparedtext)])


def ld(maintext, comparedtext):     #LD的计算函数
    diff_start = -1
    diff_end = -1
    len_MT = len(maintext)
    len_CT = len(comparedtext)
    short = min(len_MT, len_CT)

    # 寻找开头和结尾的共同字符串，并记录位置
    for i in range(0, short):
        if maintext[i] != comparedtext[i]:
            diff_start = i
            break
    if diff_start == -1:
        return abs(len_CT - len_MT)
    for i in range(0, short):
        if maintext[len_MT - i - 1] != comparedtext[len_CT - i - 1]:
            diff_end = i
            break
    if diff_end == -1:
        return abs(len_CT - len_MT)

    # L(A+C, B+C) = LD(A, B)
    # 除去开头以及结尾相同的字符串，构建新的字符串
    long_str = (
        maintext[diff_start: len_MT - diff_end] if len_MT >= len_CT else comparedtext[diff_start: len_CT - diff_end])
    short_str = (
        maintext[diff_start: len_MT - diff_end] if len_MT < len_CT else comparedtext[diff_start: len_CT - diff_end])
    long_len = len(long_str)
    short_len = len(short_str)

    # store保存迭代过程中每次计算的结果
    store = range(0, long_len + 1)

    for i in range(short_len):
        temp = [i + 1] * (long_len + 1)
        for j in range(long_len):
            if long_str[j] == short_str[i]:
                temp[j + 1] = store[j]
            else:
                # 注意这时各个位置数据的对应关系
                temp[j + 1] = min(store[j], store[j + 1], temp[j]) + 1
        store = temp
    # 最右下角即为编辑距离
    return store[-1]


# Test
'''
print(lcs(S1,S2))
print(ld(string_a, string_b))
AnsLcs = float(lcs(S1,S2))
AnsLd = float(ld(string_a, string_b))
S = AnsLcs/(AnsLd+AnsLcs)
print("%.2f" % S)
'''
