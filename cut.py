#encoding: utf--8

import re
import os
with open('sohu_history.txt','r',encoding='utf-8') as destfile:
    cut_list = ('，','。','！','？','：','；')
    buf = destfile.readlines()
    content = ''
    for item in buf:
        content += item
    buf = content
    str = ''
    with open ('test.txt','a',encoding='utf-8') as file:
        for single_word in buf:
            str += single_word
            if(single_word in cut_list):
                file.writelines(str+'\n')
                str = ''
                