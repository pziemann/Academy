print("abc")
print(*"abc")

def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return (total)
print(add(3,5,7))

def about(name, age, likes):
    sentence = "Meet {}! THey are {} years old and they like {}".format(name, age, likes)
    return sentence

dictionairy = {
    "name": "Pawel",
    "age": 24,
    "likes": "Python"
}
print(about(**dictionairy))
print(about("Pawel", 24, "Python"))

def foo(**kwargs):
    for key, value in (kwargs.items()):
        print("{}:{}".format(key,value))

print (foo(huda = "Female", ziyad = "male", john = "male"))
