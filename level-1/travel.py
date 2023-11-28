# Ask for Travel 
travel = input("Wirte all country and places you want to visit or your aleardy visited and spearte using comma \n")
travelList = travel.split(", ")
aleardyTravel = []
wishTotravel = []

for country in travelList:
    isVisited = input(f"Did you visit this {country} ? (yes or no)").lower()
    if isVisited == "yes":
        print(f"I hope you enojy visiting this {country}")
        aleardyTravel.append(country)
    else: 
        print("I hope You visit it some day ")
        wishTotravel.append(country)
        
print("*" * 20)
print(f"Your Aleard you Travel To {aleardyTravel}")
print("*" * 20)
print(f"Your wish travel list is  {wishTotravel}")