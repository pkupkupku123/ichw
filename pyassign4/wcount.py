#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Liye"
__pkuid__  = "1800011779"
__email__  = "pkupkupku@pku.edu.cn"
"""

import sys
import urllib.error
from urllib.request import urlopen


def wcount(lines, topn=10):    # topn参数未给出时，默认topn=10。
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """

    for punc in ['!', '@', '#', '$', '%',     # 需要替换的标点符号列表。
                 '^', '&', '*', '(', ')', 
                 '-', '_', '+', '=', '{',
                 '}', '[', ']', '/', '|', 
                 ':', '"', ';', ',', '.', 
                 '>', '?', '<', '\n']:
        lines = lines.replace(punc, ' ')    # 替换标点符号为空格，便于split将单词分割提取。
        
    lines = lines.lower()    # 将字母全改为小写，使相同单词不会因大小写不同被记为两种。
    Allwords = lines.split()    # 将修饰后的文本字符串分割为列表。
    our_dict = {}    # 创建一个字典，用于存储计数结果。
    for word in Allwords:
        if word not in our_dict:
            our_dict[word] = Allwords.count(word)    # 调用count函数计数。
            
    word_list = sorted(list(our_dict), key= lambda x: our_dict[x], \
                       reverse= True)    # 创建一个不重复的单词列表，并以计数结果降序排序。
    
    if topn <= len(word_list):    # 打印出前topn个单词及其数目。
        for word in word_list[:topn]:
            print(word, our_dict[word])
    else:    # 如果单词数目不够topn个，打印出所有单词及其数目。
        for word in word_list:
            print(word, our_dict[word])
            
            
def main():
    """Main Module
    从命令行中获取参数，并访问web获取要计数的文本，再调用wcount函数计数。
    """
    if  len(sys.argv) == 1:    # 如果没有给出URL参数，则打印出程序使用提示。
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print(' topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    else:
        try:
            doc = urlopen(sys.argv[1])
        except urllib.error.URLError as err:    # 以下3个except语句用于处理报错。
            print('URL错误:{}'.format(str(err)))
        except urllib.error.HTTPError as err:
            print('HTTP错误:{}'.format(str(err)))        
        except Exception as err:
            print('其他错误:{}'.format(str(err)))
        else:    # 未报错时，从web上获取数据，解码为字符串，调用wcount函数实现计数。
            docstr = doc.read()
            doc.close()
            jstr = docstr.decode()
            if len(sys.argv) == 2:
                wcount(jstr)
            else:
                wcount(jstr,int(sys.argv[2]))
    
if __name__ == '__main__':
    main()
