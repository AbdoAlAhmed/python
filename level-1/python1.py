# setup 
import random

# Welcome and take the input as string and turn it to list with split

names = input("""
  Welcome to 'whose walle?'
  you will gave me a list of names , and i will pick a person to pa 
  if you're ready , enter the names seperated by a comma \n
      """)
listOfNames = names.split(", ")
# to know How many people inside this list we use len
to = len(listOfNames)
randomName = random.randint(1,to)

print(f"Ask {listOfNames[randomName]} to Pay for the dinner ")



