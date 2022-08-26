# it is in the python file to convert in to the json file
import json
dict1 ={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
}
out_file = open("myfile.json", "w")
json.dump(dict1, out_file) 
print(type(dict1))
print(type(out_file))
