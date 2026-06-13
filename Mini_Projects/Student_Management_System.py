class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks

    def show_details(self):
        print("Name    :",self.name)
        print("Roll No :",self.roll_no)
        print("MArks   :",self.marks)
        print()

stu_list=[Student("Nishanth",1,98),
         Student("Chandu",2,66),
         Student("Teja",3,67),
         Student("Sai Ram",4,63),
         Student("Vamsi",5,89)]

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Marks")
    print("6. Show Topper")
    print("7. Exit")
    print()
    choice=int(input("Enter Your Choice :"))

    if choice==1:
        name=input("Enter Name :")
        roll=int(input("ENter Roll Number:"))
        marks=int(input("Enter Marks :"))
        new_stu=Student(name,roll,marks)
        stu_list.append(new_stu)

    elif choice==2:
        print("=======Student Details======")
        for stu in stu_list:
            stu.show_details()

    elif choice==3:
        found=False
        roll=int(input("Enter Roll Number :"))
        for stu in stu_list:
            if stu.roll_no==roll:
                print("=====Found Student======")
                stu.show_details()
                found=True
                break
        if not found:
                print("Student Not Found")

    elif choice==4:
        found=False
        roll=int(input("Enter Student Roll Number:"))
        for stu in stu_list:
            if stu.roll_no==roll:
                stu_list.remove(stu)
                print("Succesfully Student Deleted")
                found=True
                break
        if not found:
            print("Student Not Found")

    elif choice==5:
        found=False
        roll=int(input("Enter Student Roll Number"))
        for stu in stu_list:
            if stu.roll_no==roll:
                marks=int(input("Enter New Marks :"))
                stu.marks=marks
                print("Marks Updates Successfully")
                found=True
                break
        if not found:
            print("Enter Coorect Roll Number")
    
    elif choice==6:
        topper = stu_list[0]
        for stu in stu_list:
            if stu.marks > topper.marks:
                topper = stu
        print("======== Topper ========")
        topper.show_details()

    elif choice==7:
        print("Exiting App")
        break

    else:
        print("Enter Correct Choice")