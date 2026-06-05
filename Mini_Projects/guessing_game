import random
print("======================\n","| Esay---->1 to 10  |\n","| Medim--->1 to 50  |\n","| Hard---->1 to 100 |\n","======================\n")
while True:
    level=int(input("Enter your Difficult level:"))
    if level==1:
        a,b=1,10
        break
    elif level==2:
        a,b=1,50
        break
    elif level==3:
        a,b=1,100
        break
    else:
        print("Enter correct range :")
ran_num=(random.randint(a, b))
count=0
while True:
    ran=int(input("Enter your number :"))
    count=count+1
    if ran==ran_num:
        print("You have entered coorect number")
        print("you have have taken ",count,"attemps")
        while True:
            conti=input("Do you want to continue yes/no :").strip().lower()            
            if conti=="yes":
                print("Okay generating a new number :")
                ran_num=random.randint(a, b)
                break
            elif conti=="no":
                print("Exiting App:")
                exit()
            else:
                print("Enter correct option :")         
    elif ran<ran_num:
        print("Too low")
    elif ran>ran_num:
        print("Too high")
    else:
        print("try again:")