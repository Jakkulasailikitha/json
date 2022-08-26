# the python file changes in to json file
import json
a={
   "location": "NewPath",
   "Id": "0",
   "resultDir": "",
   "resultFile": "",
   "mode": "replay",
   "className":  "",
   "method":  "METHOD"
}
b=open("sai.json","w")
c=json.dump(a,b)
print(c)
with open("sai.json","r")as b:
  d=json.load(b)
print(d)
e=json.dumps(d,sort_keys=True)
print(e)