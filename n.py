''''n=int(input("Enter a number :"))
for i in range(1,n+1):
    left_space=(" " *(n-i))
    star=("*"*((i*2)-1))
    right_space=(" "*n)
    print(left_space + star + right_space)
n=int(input("Enter your number : "))
for i in range(n):
    num=((n-i))
    space=(" "*i)
    print(space+ (str(num)*(n-i)))
n=int(input("Enter your number :"))
for i in range(n):
    left_space =(" "*i)
    star=("*"*(n-(i+i)))
    print(left_space + (star))
n=int(input("Enter your number :"))
for i in range(1,n+1):
    num=i
    if (i==4)
    break
    corss=i
    print(num)
def inspire():
    a=("Nishanth Don't stop until you get it!")
    print(a)
    print("Nishanth you are great")

inspire()
inspire()
def show_age(name,age):
    print(name,"is",age,"year's old")

show_age("Nishanth","21")
show_age("vamsi","23")
show_age("chandu","45")

def add_numbers(a,b):
    add=(a+b)
    diff=(a-b)
    c=print(f"addtion ={add} difference={diff}")
add_numbers(3,15)
def fav_foods(food):
    a=("soyma lovees",food)
    print(a)

fav_foods("ladu")
fav_foods("Nishanth")
def multiply(a=5,b=10):
    return(a*b)
print(multiply())
print(multiply(15,45))
def string(userinput):
    vowels="aeiouAEIOU"
    count_consotant=0
    count_vowels=0
    
    for eachchar in userinput:
        if (eachchar.isalpha()):
            if(eachchar in vowels):
                count_vowels=count_vowels+1
            else:
                count_consotant+=1
    return    count_consotant,count_vowels
count_consotant,count_vowels=string("Nishanth")
print(count_consotant,count_vowels)


def add(num1,num2):
    add=(num1+num2)
    print(add)
add(5,8)
f=open("Twinkle.txt","r")
text=f.read()
text = text.lower().split()
a=input("Enter your word :").lower()
if a in text:
    print("yes")   
else:
    print("no")
f.close()


import random
a=open("high_score.txt","r")
score=int(a.read())
print(score)
ran_num=(random.randint(0,100))
if (ran_num>score):
    with open("high_score.txt", "w") as f:
        f.write(str(ran_num))
    print("you have achived highest score:",ran_num)
else:
    print("Your score is ",ran_num)

with open ("high_score.txt","r")
with open 

import os
os.mkdir("tables")
print("folder created")
for j in range(1,21):
    with open(f"tables/{j}.txt","w",) as f:
        for i in range(1,11):
            line = f"{j} X {i} = {j*i}\n"
            f.write(line)
    print(j,"table written to the file") 
    
class Student:
    def __init__(self, name, age ,Roll_num,add):
        self.name = name
        self.age = age
        self.Roll_num = Roll_num
        self.add=add

s1 = Student("Nishanth",123, 20,"nizampet")
s2 = Student("chandu",22,1234,"RGN")
print(s1.name)
print(s1.age)   
print(s1.add)
print(s1.Roll_num)
print(s2.name)
print(s2.age)

class Dog:
    def __init__(self,name,breed,age):
        self.name=name
        self.breed=breed
        self.age=age

    def show(self):
        print("Name :", self.name)
        print("Breed:", self.breed)
        print("Age  :", self.age)

#Create a class programmer for storing infermatone of few programmlas werking at mlcroseft
class Employee:
    company="Microsoft"
    def __init__(self,name,emp_id,job_role,salary):
        self.name=name
        self.emp_id=emp_id
        self.job_role=job_role
        self.salary=salary
    def show(self):
        print("Company :",Employee.company)
        print("Name :",self.name)
        print("Emp_ID :",self.emp_id)
        print("Job_role :",self.job_role)
        print("Salary :",self.salary)

emp1 = Employee("Nishanth",234414454,"software",900000)
emp2 = Employee("Teja",365256246,"Sr_Software",1300000)
emp3 = Employee("Chandu",242454236,"jr_software",700000)
print("====== All Programmer ========")
emp1.show()
emp2.show()
emp3.show()

#Write a class calculator capalle of finding square.Cube and squarerast of a runter!import math
import math
class Calculator:
    def __init__(self,squarecude,squa,root):
        self.squarecude=squarecude
        self.squaroot=squa
        self.root=root
    def show(self):
        print("Squarecude :",self.squarecude)
        print("Square :",self.squaroot)
        print("Squareroot :",self.root)
num=int(input("Enter your number :"))
cude=num*num*num
sqroot=num*num
squeare_root = math.sqrt(num)
my_cal= Calculator(cude,sqroot,squeare_root)
my_cal.show()

import random
class Train:
    
    def __init__(self,get_status,Book_ticket,Fare_info):
        self.get_status=get_status
        self.Book_ticket=Book_ticket
        self.Fare_info=Fare_info
    ran_num=(random.randint(0,100))
    def show(self):
        print("No of Seats Avalaible :",self.get_status)
        print("Status of Booking :",self.Book_ticket)
        print("Fare Information :",self.Fare_info)
ran_num=(random.randint(0,100))
amount_fare=(random.randint(2000,5000))
train1=Train(ran_num,"Booked",amount_fare)
print("====== WEllCOME TO IRTC ======") 
train1.show() 

import random

class Train:

    def __init__(self, seats, fare):
        self.seats = seats
        self.fare = fare

    def book_ticket(self):
        if self.seats > 0:
            self.seats -= 1
            print("Ticket Booked Successfully")
        else:
            print("No Seats Available")

    def get_status(self):
        print("Available Seats:", self.seats)

    def get_fare_info(self):
        print("Fare:", self.fare)


train1 = Train(random.randint(1, 100), random.randint(2000, 5000))

print("====== WELCOME TO IRCTC ======")

train1.get_status()
train1.get_fare_info()
train1.book_ticket()
train1.get_status()
    
import random
class Train:
    def __init__(self,seat,fare):
        self.seat=seat
        self.fare=fare
    def Book_ticket(self):
        if self.seat>0:
            self.seat -= 1
            print("Ticket Booked Successfully")
        else:
            print("No Seats avalaible")
    
    def get_status(self):
        print("Available Seats :",self.seat)

    def get_fare(self):
        print("Fare :",self.fare)
train1 = Train(random.randint(1, 100), random.randint(2000, 5000))
print("====== WELCOME TO IRCTC ======")
train1.get_status()
train1.get_fare()
train1.Book_ticket()
train1.get_status()

class Car:
    def __init__(self, brand, colour):
        self.brand = brand
        self.colour = colour

    def show_details(self):
        print("Brand :", self.brand)
        print("Colour :", self.colour)

c1 = Car("Toyota", "Pink")
c1.show_details()


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def show_details(self):
        print("Name :",self.name)
        print("Marks :",self.marks)
        
s1=Student("Nishanth",67)        
s1.show_details()
if s1.marks>=35:
    print("Result : Passed")
else:
    print("Result :Failed")

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print("Title :",self.title)
        print("Author :",self.author)
        print()
book1 = Book("phy","tej")
book2 = Book("chem","chandu")
book3 = Book("math","nish")

book1.display()
book2.display()
book3.display()


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_salary(self):
        print("Salary :", self.salary)

    def increment(self, amount):
        self.salary += amount
        print("Salary increased by", amount)
e1 = Employee("John", 55000)
e1.show_salary()
e1.increment(5000)
e1.show_salary()

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("Area :",3.14*self.radius*self.radius)
    def circumference(self):
        print("circumference :",2*3.14*self.radius)
num=float(input("Enter Circle Radius :"))
my_circle=Circle(num)
my_circle.area()
my_circle.circumference()

class Movie:
    def __init__(self,movie_name,rating):
        self.movie_name=movie_name
        self.rating=rating
    def is_hit(self):
        if self.rating>=8:
            print("Result : Hit")
        else:
            print("Result : Average")
mov=input("Enter Movie Name :")
rate=int(input("Enter Your Rating :"))
my_mov=Movie(mov,rate)
my_mov.is_hit()

class Product:
    def __init__(self,product_name,price):
        self.product_name=product_name
        self.price=price
    def calculate_total(self):
        print("Total Amount :",self.price)
    def total_product(self):
        print("Total Products :",1)
name=input("Enter Product Name :")
price=int(input("Enter Price of Product :"))
my_cart=Product(name,price)
my_cart.calculate_total()
my_cart.total_product()'''