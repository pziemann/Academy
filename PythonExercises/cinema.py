films = {
    "Finding DOry": [3,5],
    "Bourne": [18,5],
    "Tarzan": [15,5],
    "Ghostbusters": [12,5]
}
while True:
    choice = input("What film do you wanna watch?: ").strip().title()
    if choice in films:
        age = input("How old are you?").strip()
        age = int(age)
        #check age
        if age >= films[choice][0]:
                #check seats
                if films[choice][1] > 0:
                    films[choice][1] = films[choice][1] - 1                
                    print("Enjoy the film")
                else:
                     print("Sorry, we do not have enough seats.")
        else: 
            print("You are not old enough to watch that film")
    else:
        print("We do not have that film.")
