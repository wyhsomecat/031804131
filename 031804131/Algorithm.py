def lcs(MainText, ComparedText):
    matrix = [''] * (len(MainText) + 1)
    for index_MT in range(len(matrix)):
        matrix[index_MT] = [''] * (len(ComparedText) + 1)

    for index_MT in range(1, len(MainText) + 1):
        for index_CT in range(1, len(ComparedText) + 1):
            if MainText[index_MT - 1] == ComparedText[index_CT - 1]:
                matrix[index_MT][index_CT] = matrix[index_MT - 1][index_CT - 1] + MainText[index_MT - 1]
            elif len(matrix[index_MT][index_CT - 1]) > len(matrix[index_MT - 1][index_CT]):
                matrix[index_MT][index_CT] = matrix[index_MT][index_CT - 1]
            else:
                matrix[index_MT][index_CT] = matrix[index_MT - 1][index_CT]

    return len(matrix[len(MainText)][len(ComparedText)])



def ld(MainText, ComparedText):
    diff_start = -1
    diff_end = -1
    len_MT = len(MainText)
    len_CT = len(ComparedText)
    short = min(len_MT, len_CT)

    # 寻找开头和结尾的共同字符串，并记录位置
    for i in range(0, short):
        if MainText[i] != ComparedText[i]:
            diff_start = i
            break
    if diff_start == -1:
        return abs(len_CT - len_MT)
    for i in range(0, short):
        if MainText[len_MT - i - 1] != ComparedText[len_CT - i - 1]:
            diff_end = i
            break
    if diff_end == -1:
        return abs(len_CT - len_MT)

    # L(A+C, B+C) = LD(A, B)
    # 除去开头以及结尾相同的字符串，构建新的字符串
    long_str = (MainText[diff_start: len_MT - diff_end] if len_MT >= len_CT else ComparedText[diff_start: len_CT - diff_end])
    short_str = (MainText[diff_start: len_MT - diff_end] if len_MT < len_CT else ComparedText[diff_start: len_CT - diff_end])
    # print long_str
    # print short_str
    long_len = len(long_str)
    short_len = len(short_str)

    # store保存迭代过程中每次计算的结果
    store = range(0, long_len + 1)

    for i in range(short_len):
        temp = [i+1] * (long_len + 1)
        for j in range(long_len):
            if long_str[j] == short_str[i]:
                temp[j+1] = store[j]
            else:
                # 注意这时各个位置数据的对应关系
                temp[j+1] = min(store[j], store[j+1], temp[j]) + 1
        store = temp
        # print store
    # 最右下角即为编辑距离
    return store[-1]


# Test
string_a = "我的作品都是源出于和现实的那一层紧张关系"
string_b = "现实的品一长源出于和我沉湎都想紧张关系"
S1 = '我的作品都是源出于和现实的那一层紧张关系'
S2 = '现实的品一长源出于和我  沉湎都想紧张关系'
print(lcs(S1,S2))
print(ld(string_a, string_b))
# Ans: float = lcs(S1,S2)/(ld(string_a,string_b)+lcs(S1,S2))
AnsLcs = float(lcs(S1,S2))
AnsLd = float(ld(string_a, string_b))
S = AnsLcs/(AnsLd+AnsLcs)
print(S)
#S(A,B)=LCS(A,B)/(LD(A,B)+LCS(A,B))