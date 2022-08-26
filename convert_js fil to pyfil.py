# this is in python file want to change to json file
import json 
dict1 = '''
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": 34,
        "salary": 54000,
    },
    
    {
        "name": "Elis",
        "designation": "Trainee",
        "age": 24,
        "salary": 40000,
    },
}
'''
c=json.loads(dict1)
print(c)
# for x in c["emp1"]:
#     print(x["age"])
    