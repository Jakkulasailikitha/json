import json
people_string = {

"people":[
{
"emp_name": "John smith",
"emp_no.": "924367-567-23",
"emp_email": ["johnsmith@dummyemail.com"],
"has_license": "false"
},
{
"emp_name": "harshit kant",
"emp_number": "560-555-5153",
"emp_email": "null",
"has_license": "true"
}
]
}
data = json.dumps(people_string,sort_keys=True,indent=2)
print(data)
print(type(people_string))
print(type(data))