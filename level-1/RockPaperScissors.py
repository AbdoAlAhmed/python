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
choise = ['rock','paper','scissor']
userChoise = input("choise between rock -- papper -- scissor ").lower()
# check if he choice right 
if userChoise in choise:
    print ("  ----    continue ...  ----")
# if wrong print and error message and quit 
else: 
    print("you choised something wrong or something happer")
# if true  make a random int from 1 - 3 and make him choics
computerChoise = random.randint(0,2)
# then assign the random number to one of the varible 
if userChoise == "rock" :
    print(rock)
elif userChoise == "scissor":
    print(scissor)
elif userChoise == "paper":
    print(paper)


if choise[computerChoise] == "rock" :
    print(rock)
elif choise[computerChoise] == "scissor":
    print(scissor)
elif choise[computerChoise] == "paper":
    print(paper)
else: 
    print("")
# check both result form random and the user input 

if choise[computerChoise] == "rock" and userChoise == "paper":
    print(" user win and computer lose")

elif choise[computerChoise] == "paper" and userChoise == "rock":    
    print(" user lose and compuer win")
    
elif choise[computerChoise] == "scissor" and userChoise == "rock":    
    print(" user lose and compuer win")
    
elif choise[computerChoise] == "rock" and userChoise == "scissor":    
    print(" user win and compuer lose")

elif choise[computerChoise] == "paper" and userChoise == "scissor":    
    print(" user win and compuer lose")
    
elif choise[computerChoise] == "scissor" and userChoise == "paper":    
    print(" user lose and compuer win")
else: 
        print(" Draw  ----")

# and decide if the user win lose or it's adraw with print both choice for the user and random method