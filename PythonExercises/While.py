i = 1
while i <= 100:
    if i % 2 != 0:

        print(i)
    i += 1
    
arr = []

while len(arr) < 3:
    new_name = input("What name would you like to add to the list?: ")
    arr.append(new_name)
print(arr)