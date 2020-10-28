import json
#  Python JSON to dict
person = '{"name": "Bob", "languages": ["English", "Fench"]}'
person_dict = json.loads(person)
print(person_dict)
print(person_dict['languages'])

# Python read JSON file
with open('bobperson.json') as f:
  data = json.load(f)
print("Python read JSON file : ",data)

# Converting dict to JSON
person_dict = {'name': 'Bob',
'age': 12,
'children': None
}
person_json = json.dumps(person_dict)
print(person_json)

#  Writing JSON to a file
person_dict = {"name": "Bob",
"languages": ["English", "Fench"],
"married": True,
"age": 32
}

with open('personbob.txt', 'w') as json_file:
  json.dump(person_dict, json_file)