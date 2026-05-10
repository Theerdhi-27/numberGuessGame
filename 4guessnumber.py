import random
secret_number = random.randint(1, 100)
for i in range(1,11):
    number=int(input("Guess number"))
    if(number>secret_number):
        print("number is greater then secretnumber")
    elif(number<secret_number):
        print("number is smaller then secret number")
    else:
        print("Congratulations!,You wins the game")
        break
    if(i==10):
        print("Sorry!,You loose the game")
        print("The number is ",str(secret_number))
       