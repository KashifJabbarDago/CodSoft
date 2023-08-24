import random 

characters = "abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ?#@(!)"
while (True):
    try:
        spec_length = int(input("Specify Length Of Password "))
        for i in range(0,spec_length):
            password_gen = random.choice(characters)
            print(password_gen,end="")
        print()
    except:
        print("Please enter length in numbers")

