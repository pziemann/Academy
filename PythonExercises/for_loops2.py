students = {
    "male": [
        "Harry",
        "Charlie",
        "Frank",
        "Michal"
        ],
    "female": [
        "Sarah",
        "Huda",
        "Baracuda",
        "Emily"
    ]
}

for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)