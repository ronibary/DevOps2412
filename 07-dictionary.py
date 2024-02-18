
details_dict = { "fname": "sami",
                 "lname": "abari",
                 "age": 32,
                 "is_married": True}

my_class = [
    {"fname":"or","lname": "shemesh"},
    {"fname": "eric", "lname": "van dam"},
]

print(details_dict.keys())
print(details_dict.values())

for student in my_class:
    print(student["fname"])

