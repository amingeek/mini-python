import random

fall = [
    'fall 1 ',
    'fall 2', 
    'fall 3',
    "fall 4",
]

def draw():
    return random.choice(fall)

while True:
    choice = input("Press d for draw or q for quit : ")
    
    if choice == "d":
        print(draw())
    elif choice == "q":
        print("Happy yalda!")
        break
    else:
        print("Invalid input!")