# Exercise 5: Access the nested key ‘salary’ from the following JSON
# 7000
# import json
# # s= """{ 
# #    "company":{ 
# #       "employee":{ 
# # # #          "name":"emma",
# # # #          "payble":{ 
# # # #             "salary":7000,
# # # #             "bonus":800
# # # #          }
# # # #       }
# # # #    }
# # # # }"""
# # # # a=json.loads(s)
# # # # print(a)
# # # # c=(a["company"]["employee"]["payble"]["salary"])
# # # # print(c)



# # # # Exercise 6: Convert the following Vehicle Object into JSON
# # # # Convert it into JSON format
# # # # Expected Output:
# # import json
# # a={
# #     "name": "Toyota Rav4",
# #     "engine": "2.5L",
# #     "price": 32000,
# # }
# # b=json.dumps(a)
# # c=open("my.json","w")
# # c.write(b)
# # print(c)



# amount=int(input("enter the amount here :"))
# note2000=note500=note100=note50=note20=note10=note5=0
# if amount>=2000:
#     note2000=amount//2000
# if amount>=500:
#     note500=amount//500
# if amount>=200:
#     note200=amount//200
# if amount>=100:
#     note100=amount//100
# if amount>=50:
#     note50=amount//50
# if amount>=20:
#     note20=amount//20
# if amount>=10:
#     note10=amount//10
# if amount>=5:
#     note5=amount//5
# print("no.of 2000 notes:",note2000) 
# print("no.of 500 notes:",note500)
# print("no.of 200 notes:",note200 )
# print("no.of 100 notes:",note100) 
# print("no.of 50 notes:",note20 )  
# print("no.of 20 notes:",note10)
# print("no.of 10 notes:",note5)