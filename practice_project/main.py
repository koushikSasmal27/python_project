import random
n=random.randint(1,100)
a=-1
guesses=0
while(n!=a):
    guesses+=1
    a=int(input("Guess the number:"))
    if(a==n):
        break
    if(a>n):
        print("plase enter lower number:")
    else:
        print("palse enter higher number")
print(f"you have guess the number {n} in {guesses} attemp")