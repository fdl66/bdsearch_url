#!/usr/bin/python
#coding=utf-8
import json
import sys
# #
read_file="result_tmp.txt"

fr=open(read_file,'r')
data=json.loads(fr.read())
fr.close()
# print data

site={}

def get_site_info():
    cnt = 0
    for key in data:
        cnt += 1
        # print cnt
        # print str(key)+"\n\n\n"
        country = data[key]['country']
        city = data[key]['city']
        if country not in site:
            site[country] = {}
        if city in site[country]:
            site[country][city] += 1
        else:
            site[country][city] = 1
            # for item in data[key]:
            # print item
            # print data[key][item]

    for country in site:
        print country
        for city in site[country]:
            sys.stdout.write("\t")
            # sys.stdout.write(city)
            print city,
            print ":" + str(site[country][city])

def get_domain():
    for key in data:
        print data[key]['domain_name']

get_domain()

'''
RU
	K :1
CN
	guang zhou shi :2
	ji nan shi :9
	xia men shi :3
	shangyu :1
	haidianqu :1
	dong guan shi :1
	Su Zhou Shi :2
	Hefeishi :9
	Xiamenshi :17
	shanghai :5
	bei jing :12
	CHONGQING :1
	shen  shi :2
	nantongshi :1
	GZ :1
	nanjing :1
	anyangshi :1
	ZhengZhouShi :1
	zhou shi :1
	ningboshi :1
	ziboshi :1
	HongKong :2
	HangZhou :2
	chao zhou shi :1
	wlmq :1
	Cheng Du :1
	SHEN ZHEN :1
	Jin Hua :1
	handan :1
	Guangzhou :32
	zhejian :1
	shenyangshi :1
	Shi Xia Qu :1
	Shenzhen :34
	dongguan :3
	kunmingshi :1
	guangzhou :1
	bei jing shi :7
	Hangzhou :134
	KaiPing :2
	guang zhou :1
	上海市 :4
	Guangdong :2
	guangzhoushi :2
	weifang :1
	wu han shi :1
	Privacy :1
	shen zhen shi :1
	quan zhou shi :1
	shixiaqu :24
	kaifengshi :1
	china shanghai :1
	Dongguan :1
	chaoyangqu :4
	Shen Zhen Shi :2
	wen zhou shi :1
	NJS :1
	NINGBO :1
	ShanTouShi :1
	yongchengshi :1
	binzhoushi :1
	fu ding shi :2
	FZS :1
	Shang Hai Shi :1
	Beijng :1
	zhu hai shi :1
	Hengshui :1
	BEIJING :2
	ShenChouShi :1
	shijiazhuang :1
	Bei Jing Shi :6
	hai kou shi :3
	beijing :14
	beijingshi :9
	Hu He Hao Te :1
	chang sha shi :1
	Shanghai :7
	he fei shi :4
	Qin Huang Dao Shi :1
	Nanjing :7
	shang hai :6
	yi chang shi :1
	shenzhenshi :5
	BeiJingShi :10
	pudongxinqu :3
	沈阳 :2
	shang hai shi :1
	Quan Zhou Shi :2
	Beijing :93
	zhengzhoushi :1
	shenzhen :3
	haerbin :1
	changchun :1
	haerbim :1
	wenzhoushi :1
	KunMing :1
	hang zhou shi :14
	Nanjing, :1
	Chengdu :1
	JINAN :1
	NANJING :1
	HaiDianQu :1
	taiyuan :1
	fu zhou shi :1
	anshan :1
HK
	Wanchai :1
	Hong Kong :1
TW
	taipei :1
CA
	Toronto :1
US
	BREA :1
	FREMONT :1
	Washington :1
	Scottsdale :2
	Pleasanton :2
	New York :2
	Burlington :3
	Denver :1
	San Francisco :1
	Jacksonville :3
	KIRKLAND :1
KR
	Seoul :2
PA
	Panama :1
	PANAMA :3
China
	xiangchengshi :1
	Chengdu :3
	Guang Zhou :1
	HUNAN :1
	guangzhou :2
	dongguan :1
GB
	LONDON :1
BS
	Nassau :5
None
	CHENGDU :1
	None :774
cn
	beijing :1
	Shen Zhen :1
	Zhengzhou :2
	Tianjin :1
	Shanghai :3
	Hefei :1
	Jishou Shi :1
	Ma Lai Xi Ya :1
	Shenzhen :2
	Shen ZhenShi :1
	yu lin :1
	Guangzhou :3
	Quanzhou :1
	bei jing :1
	Qingdao :3
	Wenzhou :1
	qianjiang :1
	Haikou :1
	Mian Yang Shi :1
	Heshan :1
	wuhan :1
	Hangzhou :16
	shen zhen :1
	Beijing :1
	Qujing :1
	Jinan :3
	Nanjing :1
	ERDOS :1

Process finished with exit code 0
'''