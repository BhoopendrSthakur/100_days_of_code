import random

user = int(input("choose 0 for rock , 1 for paper and 2 for scissors "))
computer = random.randint(0, 2)


def rock():
    print('''  
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) 
''')


def paper():
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

  ''')


def scissor():
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
  ''')


if user == 0 and computer == 0:
    print("You")
    rock()
    print("computer")
    rock()
    print("it's a draw")
elif user == 0 and computer == 1:
    print("You")
    rock()
    print("computer")
    paper()
    print("you lost")
elif user == 0 and computer == 2:
    print("You")
    rock()
    print("computer")
    scissor()
    print("you won")

elif user == 1 and computer == 0:
    print("You")
    paper()
    print("computer")
    rock()

    print("you won")
elif user == 1 and computer == 1:
    print("You")
    paper()
    print("computer")
    paper()

    print("it's a draw")
elif user == 1 and computer == 2:
    print("You")
    paper()
    print("computer")
    scissor()
    print("you lost")


elif user == 2 and computer == 0:
    print("You")
    scissor()
    print("computer")
    rock()

    print("you won")
elif user == 2 and computer == 1:
    print("You")
    scissor()
    print("computer")
    paper()
    print("you lost")
elif user == 2 and computer == 2:
    print("You")
    scissor()
    print("computer")
    scissor()
    print("it's a draw")