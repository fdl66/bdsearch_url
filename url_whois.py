#!/usr/bin/python
#coding=utf-8

import json
import whois
import hashlib

source_whois_file="bl.txt"
whois_file="result_tmp.txt"
url_whois_dict={}

def get_url():
    fr=open(source_whois_file,'r')
    done = 0
    while not done:
        line1 = fr.readline()
        line2 = fr.readline()
        if line1 == '' or line2 == '':
            done = 1
        else:
            m1=hashlib.md5()
            m1.update(line2)
            url_whois_dict[m1.hexdigest()]={}
            url_whois_dict[m1.hexdigest()]['info'] = line1
            url_whois_dict[m1.hexdigest()]['url'] = line2
    fr.close()

def start_whois():
    cnt=0
    fw = open(whois_file, 'w')
    fw.write("{")
    for key in url_whois_dict:
        cnt+=1
        print cnt
        try:
            w = whois.whois(url_whois_dict[key]['url'])
            url_whois_dict[key]['city'] = w['city']
            url_whois_dict[key]['country'] = w['country']
            url_whois_dict[key]['domain_name'] = w['domain_name']
            url_whois_dict[key]['state'] = w['state']
            url_whois_dict[key]['emails'] = w['emails']
            fw.write("\""+str(key)+"\" : ")
            fw.write(json.dumps(url_whois_dict[key]))
            fw.write(",")
        except whois.parser.PywhoisError, e:
            print e
        except KeyError,e:
            print e
    fw.write("}")
    fw.close()


def store_to_file():
    fw=open(whois_file,'w')
    fw.write(json.dumps(url_whois_dict))
    fw.close()

get_url()
start_whois()
# store_to_file()