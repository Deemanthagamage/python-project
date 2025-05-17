print("Pizza Order Programme")
print("Small pizza=100")
print("medium pizza=200")
print("Large pizza=300")
bill=0
size=input("Enter size of pizza(S/M/L) :")
if(size=="s" or size=="S"):
    bill+=100
elif(size=="m" or size=="M"):
    bill+=200
elif(size=="L" or size=="l"):
    bill+=300
else:
    print("enter correct letter")

add_pepperoni=input("Do you want peppeoni(Y/N) :")
if(add_pepperoni=="Y" or add_pepperoni=="y"):
    if(size=="S" or size=="s"):
        bill+=30
    else:
        bill+=50
extra_cheese=input("Do you want cheese(Y/N) :")
if(extra_cheese=="Y" or extra_cheese=="y"):
    bill+=50

print("Total amount :",bill)





