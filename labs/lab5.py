import random 
x = random.randint(1,5)
myNum = int(input("Enter number between 0-5: "))
while True:
        if myNum < x:
            print("Too Low")
            myNum = int(input(" Guess again:  "))
        elif myNum > x:
            print("Too High")
            myNum = int(input(" Guess Again:  "))
        else:
            print(" Let's go you got it!!!")
            break
          

          