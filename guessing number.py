print("**NUMBER GUESSING GAME**")
import random
n=random.randint(1,100)
a=-1
guesses=1
while(a!=n):
    a=int(input("guess the number:"))
    if a>n:
        print("guess lower number :")
        guesses+=1
    elif a<n:
        print("guess higher number:")
        guesses+=1
print(f"you have guessed the number {n} in {guesses} atempts")
    