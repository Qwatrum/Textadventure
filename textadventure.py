import time

happend = {"direction":"", "c_or_m":"", "a_or_p":""}
SLEEP_TIME = 0.03

def write(text):
    for e in text:
        print(e, end="")
        time.sleep(SLEEP_TIME)
    print()

def ask(question, possibilities, happend_key):
    time.sleep(0.2)
    next = False
    while not next:
        inp = input(f"\n{question}\n> ").lower()
        if inp == possibilities[0]:
            happend[happend_key] = possibilities[0]
            next=True
        elif inp == possibilities[1]:
            happend[happend_key] = possibilities[1]
            next=True
        else:
            print("Invalid answer! Try again.")

def start():

    print("Welcome to this text adventure! Have fun!")
    input("Hit enter to start your adventure!\n")

    time.sleep(0.5)
    write("You find yourself stranded at a beach...")
    write("Feeling the rocky surface, you try to stand up.")
    write("Not only your stomach hurts...")
    write("You look around and you see palm trees in the distance to your right...")
    write("And a small cottage to your left. Both are around 500-800 m away...")
    write("Behind you is just the emptiness of the ocean.")
    write("And right in front of you is an unclimable mountain.")

    
    ask("Where would you like to go? Left or right?", ["left", "right"], "direction")
    
    if happend["direction"] == "left":
        write("You turn to your left and start walking.")
        write("After a few minutes the ground starts to get wetter.")
        time.sleep(0.2)
        write("100 m to go and you start smelling something...")
        write("It smells terrible.")

        ask("Do you want to contine going to the cottage or go to the mountain? Cottage or Mountain?", ["cottage", "mountain"],"c_or_m")
    
    elif happend["direction"] == "right":
        write("You turn to your right and start walking.")
        time.sleep(0.2)
        write("You think that you can spot an anmial eating something not far away.")

        ask("Do you want to take a look what the animal is doing or don't change your goal and keep heading towards the palm trees? Animal or Palm trees", ["animal", "palm trees"],"a_or_p")
    
    if happend["c_or_m"] == "cottage":
        write("You head to the cottage...")
        write("You want to open the door, but in this moment a stranger opens the door.")
        write("He is nice guy and gives you some of his food!")
        write("But you are still wondering how you landed here...But you will forget everything... the food was not the best for you...\n\n...")
    
    elif happend["c_or_m"] == "mountain":
        write("Heading to the mountain, you spot someting golden 7 m in the air in the stone.")
        write("You give your best, but you can't reach it.")
        write("You try a different way, but soon you hang 6 m in the air with one hand, but no hope insight... and no safe way down...")
        write("\n\n...")

    if happend["a_or_p"] == "animal":
        write("You change directions towards the animal. It is eating something... Something red...")
        write("Suddenly, you trip over something...")
        write("It looks interessting, and you start digging...")
        write("A suitcase was burried underground.")
        write("You open it... not quite though.")
        write("You forgot the animal... But it has spotted you.")
        write("Slowly... walks it towards you.")
        write("You find mysterios things inside the suitcase... You wonder yourself what they are doing here...")
        write("But soon you will have greater worries... The animal is still hungry...\n\n...")
    
    elif happend["a_or_p"] == "palm trees":
        write("Arriving at the palm trees, you see some coconuts!")
        write("You are happy, but then a coconut falls down... and you get hurt. It was a gigantic coconut.... To big for you, and to big for your head...\n\n...")

    time.sleep(1)
    write("\n\n\n\n\nTHE END!")
    print("Thank you for playing this short version!")
        

if __name__ == "__main__":
    start()