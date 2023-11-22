#  a welcome message 
# make three list in one varible and print it
# make the user choise where to move the rabbit
print("Welcome to the rabbit game ")
list = [['🌳','🌳',"🌳 "]
        , ['🌳','🌳','🌳'] 
        ,['🌳','🌳','🌳']]
print(f"{list[0]}\n{list[1]}\n{list[2]}")
where = input("where do you wanna move the rabbit ")
row = int(where[0]) 
coloum = int(where[1])
if row >= 1 and  row < 23 and   coloum >= 1 and coloum < 23 :
    list[row -1][coloum - 1] = '🐇'
    print("success ... \n \n")
    print(f"{list[0]}\n{list[1]}\n{list[2]}")
else: 
    print("You didn't enter any thing or you enter a wrong number")
    
