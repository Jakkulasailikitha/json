# import json
# d={
#     "name":"amla",
#     "age":45,
#     "employee":"no"
# }
# f=open("abc.json","w")
# json.dump(d,f)
# with open("abc.json","r") as f:
# #     a=json.load(f)
# # print(a)
# # # print(type(a))
# # a=open("abc.json","r")
# # b=json.load(a)
# # print(b)
# # print(type(b))

# import json
# a='''
#    {
#      "b":[
#         "value1":1,
#         "value1":4,
#    },
#    ]
# }
# '''
# c=json.loads(a)
# print(c)
# print(type(c))
# for a in c["b"]:
#     print(a["value1"])




# for x in a["apple"]:
#     print(x["name"])
#     # del x["name"]
# m=json.dumps(c,indent=2,sort_keys=True)
# print(m)


# 


# import json

# samplejson="""{"key1":"value","key2":"value2"}"""
# data=json.loads(samplejson)
# print(data["key2"])

import json
s='{"value1":1,"value2":4}'
c=json.loads(s)
print(c["value2"])


