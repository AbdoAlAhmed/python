# import random
import random

# make varible for rock paper and scissors cuz they big 
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# welcome message 
print ("""
       Welcom to  Rock Paper Scissor Game  
       Start ..
       """)
# make input that meke the user choices between help or press enter to continue
knowTheGame = input("Do you need What is the game about if so click enter otherwise writ help \n"). lower()
# if help show  a message that explain the Game
if knowTheGame == "help":
    print("""
          ------- The Rules ------
          1- You have to choices between rock and paper and scissor 
          2- the computer will also choices 
          3- if you choise paper and the computer choices rock the computer lose And the opposite is the opposite
          4- if you choise rock and the computer choices scissor the computer lose and the oppsite is the opposite
          5- if you chois scissor and the computer chise paper the computer lose and the oppsite is the opposite
          
           ---- summerize ----
           - paper cover the rock 
           - rock break the scissor
           - scissor cut the paper
          """)

    
# if enter skip to the next step ----

# ask him for input form this list ( rock - papre - scissor ) you make list first then ask
choice = ["rock","paper","scissor"]
userChoice = input("choise between rock -- paper -- scissor ").lower()
# check if he choice right 
if userChoice  in choice:
    print ("  ----    continue ...  ----")
# if wrong print and error message and quit 
else: 
    print("you choised something wrong or something happer")
# if true  make a random int from 1 - 3 and make him choics
computerChoice = random.choice(["rock","paper","scissor"])
# then assign the random number to one of the varible 
if userChoice == "rock" :
    print(rock)
elif userChoice == "scissor":
    print(scissor)
elif userChoice == "paper":
    print(paper)


if computerChoice == "rock" :
    print(rock)
elif computerChoice == "scissor":
    print(scissor)

elif computerChoice == "paper":
    print(paper)
else: 
    print(f"{computerChoice}")
# check both result form random and the user input 

if computerChoice ==  userChoice :
    print(" It's a tie !")

elif (
    computerChoice == 'rock' and userChoice == 'paper'
    or computerChoice == 'paper' and userChoice == 'scissor'
    or computerChoice == 'scissor' and userChoice == 'rock'
):
    print( f" user win cuz {userChoice} beat {computerChoice}")
else: 
    print( f" computer win cuz {computerChoice} beat {userChoice}")

# and decide if the user win lose or it's adraw with print both choice for the user and random method