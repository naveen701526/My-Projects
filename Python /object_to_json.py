import json
# a Python object (dict):
python_obj = {
  "name": "naveen",
  "class":"I",
  "age": 17  
}
print(type(python_obj))
# convert into JSON:
j_data = json.dumps(python_obj)

# result is a JSON string:
print(j_data)
