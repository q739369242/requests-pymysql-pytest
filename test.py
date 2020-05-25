'''
运行被测试系统：根目录的battle
地址：http://127.0.0.1:12356/

'''
# r=requests.get('http://127.0.0.1:12356/')
# print(r.text)

# a={'username':'liang','password':'liang'}
# r=requestInterface("http://127.0.0.1:12356")
# r.http_post('/login',data=a)
#
#
#
#
# data={'equipmentid': 10002}
# c=r.http_post('/selectEq',data)
# d=c.json()
#
# print(type(d))
d="your pick up equipmentid:10002 please select your  enemyid:\n20001:Terran\n20002:ORC\n20003:Undead"
import re
f=re.search(r'enemyid:(.*?):Terran' ,string=d)
print(f.group())

# line = "Cats are smarter than dogs";
#
# searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
#
# if searchObj:
#     print("searchObj.group() : ", searchObj.group())
#     print("searchObj.group() : ", searchObj.groups())
#     print("searchObj.group(1) : ", searchObj.group(1))
#     print("searchObj.group(2) : ", searchObj.group(2))
#
# else:
#     print("Nothing found!!")
