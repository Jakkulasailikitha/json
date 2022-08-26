# PrettyPrint following JSON data with indent level 2 
# and key-value separators should be (",", " = ").
# Expected Output:

# {
#   "key1" = "value2",
#   "key2" = "value2",
#   "key3" = "value3"

# s= {"key1": "value1", "key2": "value2"}
# import json

# s= {"key1" : "value2", "key2" : "value2", "key3" : "value3"}
# p = json.dumps(s, indent=2, separators=(":", " = "))
# print(p)





# # Sort following JSON data alphabetical order of keys
# sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
# Expected Output:
# {
#     "age": 29,
#     "id": 1,
#     "name": "value2"
# 
# import json
# a={"id" : 1, "name" : "value2", "age" : 29}
# b=json.dumps(a,indent=2,sort_keys=True)
# c=json.loads(b)
# print(c["name"])
# print(c["id"])
# print(c["age"])
# print(b)





