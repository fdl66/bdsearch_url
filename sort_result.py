#!/usr/bin/env python
# coding=utf-8
resource_file="result.txt"
trick_file="trick_file.txt"
against_trick_file="against_trick_file.txt"

key_words=['传销','曝光','骗','千万','揭露']

#读取文件，得到搜索列表
def get_search_list():
    f = open(resource_file,'r')
    tf = open(trick_file,'w')
    af = open(against_trick_file,'w')
    done=0
    while not done:
        line1=f.readline()
        line2=f.readline()
        if line1=='' or line2=='':
            done=1
        else :
            pd=0
            for item in key_words:
                if line1.find(item)!=-1:
                    pd=1
                    break
            if pd:
                af.write(line1)
                af.write(line2)
            else :
                tf.write(line1)
                tf.write(line2)

    f.close()

get_search_list()
