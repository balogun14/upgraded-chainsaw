items1 = dict(
    {
        "key1": 1,
        "key2": 2,
        "key3": "three",
        "key4": 4,
        "key5": 5,
    }
)

print(items1)


items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3
items2["key4"] = 4
items2["key5"] = 5
print(items2)

# print(items1["key5"])

for key, value in items2.items():
    print("Key: ", key , " value " ,value)
