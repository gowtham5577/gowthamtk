print("///**SNAKE WATER GUN GAME**///")
print("s-snake,w-water,g-gun")

'''1-for snake
    -1-for water
    0-for gun'''
import random
computer=random.choice([1,0,-1])
yours=input("enter your option:")

yourdic={'s':1,'w':-1,'g':0}
you=yourdic[yours]
reversedic={1:'s',-1:'w',0:'g'}
print(f"your choice :{reversedic[you]}\ncomputer choice :{reversedic[computer]}")
if computer==you:
    print("its draw")
else:
    if computer==1 and you==0:
        print("you win!")
    elif computer==0 and you==-1:
        print("compter win!")
    elif computer==-1 and you==1:
        print("computer win!")
    elif computer==0 and you==1:
        print("computer win!")
    elif computer==1 and you==-1:
        print("you win!")
    elif computer==-1 and you==0:
        print("computer win!")
    else:
        print("something went wrong..")

    