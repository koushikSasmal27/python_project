
import random
'''1=snake -1=water 0=gun'''
while True:
    computer=random.choice([-1,0,1])
    you = input("Enter your choice (s for snake, w for water, g for gun): ").lower()
    d={"s":1,"w":-1,"g":0}
    younum=d[you]
    rev_d={1:"snake",-1:"water",0:"gun"}
    print(f"your choice {rev_d[younum]} and compure choice {rev_d[computer]}")
    if(computer==younum):
        print("It is draw")
    else:
        if(computer==-1 and younum==0):
            print("you lose!")
        elif(computer==-1 and younum==1):
            print("you win!")
        elif(computer==0 and younum==-1):
            print("you win!")
        elif(computer==0 and younum==1):
            print("you lose!")
        elif(computer==1 and younum==0):
            print("you win!")
        elif(computer==1 and younum==-1):
            print("you lose!")
        else:
            print("something is wrong")
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break