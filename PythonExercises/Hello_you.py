#ask the user for name
name = input("What is your name?: ")

#ask user for age
age = input("What is your age?: ")
#ask user for city
city = input("From what city are you?: ")
#ask user what they enjoy
description = input("What do you enjoy?: ")
string ="Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name, age, city, description)
print (output)