for i in range (1,11):
    print(i)

vowels = 0
consolants = 0
for letter in "Hello":
    if letter.lower() in "aeiou":
        vowels = vowels +1
    elif letter == " ":
        pass
    else:
        consolants += 1
print(vowels, consolants)