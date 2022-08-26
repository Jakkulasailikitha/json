# Exercise 1: Convert the following dictionary into JSON format
# data = {"key1" : "value1", "key2" : "value2"}
# Expected Output:
# data = {"key1" : "value1", "key2" : "value2"}
# import json
# data = {"key1" : "value1", "key2" : "value2"}
# print(type(data))
# c=json.dumps(data)
# print(c)
# print(type(c))




# Exercise 2: Access the value of key2 from the following JSON
# # write code to print the value of key2
# Expected Output:
# value2
import json
s= """{"key1": "value1", "key2": "value2"}"""
c=json.loads(s)
print(c)
print(c["key2"])
print(c["key1"])
