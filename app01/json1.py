# import json
#
# # dic = {'name':'yang'}
# # data = json.dumps(dic)
# # f=open("hello","w")
# # f.write(data)
# # f.close()
#
# f = open("hello", "r")
# data = json.loads(f.read())
# print(data)

import getpass

pwd = getpass.getpass("请输入密码： ")
print("密码输入成功！")
print("你的密码是：%s" % pwd)
