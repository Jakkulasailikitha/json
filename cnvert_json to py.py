# at here we using in json is null and for the true and # false .
# here in python it will changes in to False and True# and none
# import json
# people='''
# {
#     "apple":[
#         {
#             "name":"anitha",
#             "age":20,
#             "email":null,
#             "employee":false,
#             "batch":"red"
#         },
#         {
#             "name":"gayi",
#             "age":27,
#             "employee":true,
#             "batch":"blue",
#             "email":"abc"  
#         }
#         ]
#     }
#     '''
# c=json.loads(people)
# print(c)
# print(type(people))
# print(type(c))
# # print(type(["people"]))
# print(people["name"])
# print(people["age"])
# print(people["employee"])
# print(people["email"])
# for x in c["apple"]:
#     print(x["name"])
#     del x["name"]
# m=json.dumps(c,indent=2,sort_keys=True)
# print(m)


# import json

# samplejson="""{"key1":"value","key2":"value2"}"""
# data=json.loads(samplejson)
# print(data["key2"])




