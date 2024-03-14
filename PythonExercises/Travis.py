known_users = ["Alice", "Bob", "Dan", "Emma", "Georgie", "Harry"]
print(len(known_users))
while True:
    print("Hi, my name is Travis")
    name = input("What is your name?: ").strip().capitalize()
    if name in known_users:
        print("Hello {}! ".format(name))
        remove = input("Would you like to be removed from the system?(y/n?) ").lower()
        if remove == "y":
            known_users.remove(name)
    else:
        print("Hmmm, i dont think i have met you yet {}".format(name))
        add_me = input("Would you like to be added to the system? (y/n?): ")
        if add_me == "y":
            known_users.append(name)