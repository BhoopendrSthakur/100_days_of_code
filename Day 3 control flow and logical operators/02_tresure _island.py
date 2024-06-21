print('''  
      
                                                                           
_/  |_____________    ________ _________   ____   |__| _____|  | _____    ____    __| _/
\   __\_  __ \__  \  /  ___/  |  \_  __ \_/ __ \  |  |/  ___/  | \__  \  /    \  / __ | 
 |  |  |  | \// __ \_\___ \|  |  /|  | \/\  ___/  |  |\___ \|  |__/ __ \|   |  \/ /_/ | 
 |__|  |__|  (____  /____  >____/ |__|    \___  > |__/____  >____(____  /___|  /\____ | 
                  \/     \/                   \/          \/          \/     \/      \/ ''')
print("welcom to tresure island game ")
choice1 = input("You're at a crossroad, where do you goona go 'left' or 'right' \n").lower()
if choice1 == "left":
    choice2 = input("you've come to lake. There is an island in the middle of the lake. Type 'wait' to wait for boat. type 'swim to swim across.\n").lower()
    if choice2 =="wait":
        choice3 = input("you arrive at the island unharmed. there is a house with 3 door.One red,one yellow and one blue. which door would you like to choose?\n").lower()
        if choice3 == "red":
            print("it's a room full of fire game over\n")
        elif choice3 == "yellow":
            print("you found a treasure you win\n")
        else:
            print("it's a room full of beasts game over")

    else:
        print("you got attaked by an angry trout.Game over.")    


else:
    print("You fell into a hole. game over")
