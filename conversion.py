import  json

# Convertir JSON en python
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])

#Convertir python en json
x = {
  "name": "Jessica",
  "age": 20,
  "city": "Quebec"
}

# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

print(json.dumps({"name": "Jo", "age": 22}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))