def add (x, y):
    return x + y

def backwards (word):
    return word[::-1]

backward_word = input("Which word would you like to be inverted?: ")
print(backwards(backward_word))