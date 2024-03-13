def about(name, age, likes):
    sentence = "Meet {}! They are {} years old and the like {}".format(name, age, likes)
    return sentence

print(about("Jack", 24, "football"))

print(about(age = 24, name = "Jack", likes = "football"))

def about(name, age, likes = "football"):
    sentence = "Meet {}! They are {} years old and the like {}".format(name, age, likes)
    return sentence
print(about("Jack", 24))

print(about("Jack", 24, "Python"))