# encoding: utf-8
import re
from sys import argv    #在cmd中读入文件所用的库
from Exceptions import NoTextError
from Exceptions import SameTextError
from Algorithm import lcs
from Algorithm import ld
from zhon.hanzi import punctuation  #这是去除中文标点所用的库


def readin(textpath):   #处理读入文件
    str = textpath.read()
    return str


def check(file1, file2):    #将文字导入并判断是否正确导入
    maintext = readin(file1)
    comparedtext = readin(file2)
    if(len(maintext)==0|len(comparedtext)==0):
        raise NoTextError
    return maintext,comparedtext


file1 = open(argv[1], 'rt', encoding='utf-8')
file2 = open(argv[2], 'rt', encoding='utf-8')

check(file1,file2)

strfile1 = str(file1)
strfile2 = str(file2)   #把读入的IO流字符串化
maintext = re.sub("[%s]+" %punctuation, "",strfile1)
comparedtext = re.sub("[%s]+" %punctuation, "", strfile2)   #处理中文标点

file1.close()
file2.close()

AnsLcs = float(lcs(maintext,comparedtext))  #计算二者的LCS值
AnsLd = float(ld(maintext, comparedtext))   #计算二者的LD值，具体函数在Algorithm.py里
percentage = AnsLcs / (AnsLd + AnsLcs)
if (percentage==1.00):
    raise SameTextError
else:
    ans = open(argv[3], 'w', encoding='utf-8')  # 覆盖写入答案文件
    ans.write(str("%.2f" % percentage))  # 变成str并保留两位小数后写入
    ans.close()
    #print("%.2f" % S)
    #print("这是临时输出结果，正式使用时答案只会输出至ans.txt下，谢谢！")

