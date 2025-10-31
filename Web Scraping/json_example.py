import json

json_str = '{"name": "Tom", "age": 18, "hobbies": ["music", "code"]}'
data = json.loads(json_str)

print(data["name"])     # Tom
print(data["hobbies"])  # ['music', 'code']
