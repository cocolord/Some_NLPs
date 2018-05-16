#encoding: utf-8
import os
import re
# 判断一个unicode是否是英文字母
def is_alphabet(uchar):         
    if (u'\u0041' <= uchar<=u'\u005a') or (u'\u0061' <= uchar<=u'\u007a'):
        return True
    else:
        return False

with open("tencent_history_single_sentence_2nd.txt","r",encoding='utf-8') as org_file:
    lines = org_file.readlines()
    with open('test.txt','w',encoding='utf-8') as dest_file:
        enchar = False
        for line in lines:  
            if len(line)<5:
                pass
            elif re.search('[A-Za-z]',line):
                pass
            else:
                dest_file.writelines(line)