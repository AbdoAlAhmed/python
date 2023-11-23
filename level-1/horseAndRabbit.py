# Welcome message 

print("Welcom To Our Horse🐎 And Rabbit🐇 Game")

list = [["🌳","🌳","🌳"],["🌳","🌳","🌳"],["🌳","🌳","🌳"]]

print(f"{list[0]} \n {list[1]} \n {list[2]}")

# Ask him where to put the rabbit first  and print the list
rabbit = input("Where to put the Rabbit 🐇 ?")
rowRabbit = int(rabbit[0]) - 1
coloumRabbit = int(rabbit[1]) - 1

if rowRabbit >= 0 and rowRabbit < 3 and coloumRabbit >= 0 and coloumRabbit < 3 :
    list[rowRabbit][coloumRabbit] = '🐇'
    print(f"{list[0]} \n {list[1]} \n {list[2]}")
else: 
    print("You did something wrong continue ... or try again")

# Ask him agin Where to put the hores and print 

horse = input("Where to put the Horse 🐎 ?")
rowHorse = int(horse[0]) - 1
coloumHorse = int(horse[1]) - 1

if  horse == rabbit:
    list[rowRabbit][coloumRabbit] = '🐇🐎'
    print(f"{list[0]} \n {list[1]} \n {list[2]}")   
elif rowHorse >= 0 and rowHorse < 3 and coloumHorse >= 0 and coloumHorse < 3 :
    list[rowHorse][coloumHorse] = '🐎'
    print(f"{list[0]} \n {list[1]} \n {list[2]}")   
else: 
    print("You did something wrong continue ... or try again")

# if The Rabbit And The Horse in the same position you have check and print them
