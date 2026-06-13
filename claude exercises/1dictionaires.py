person = {
    "name": "Alice",
    "age": 30,
    "city": "London"
}
# By key — raises KeyError if missing
print(person["name"])   # Alice

# .get() — returns None (or default) if missing
print(person.get("age"))       # 30
print(person.get("job", "N/A")) # N/A
print(person.get("job"))
