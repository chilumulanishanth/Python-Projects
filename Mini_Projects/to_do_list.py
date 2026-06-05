operations=("==== To DO List ===== \n | 1.Add task    | \n | 2.View task   | \n | 3.Delete task | \n | 4.Exit        |\n -----------------")
task=["==================","LEARN PYTHON","WASH CLOTHS","CLEAN ROOM ","GO FOR WALK",]
def view_task():
    for i in task:
        print(i)
while True:
    print(operations)
    choice=int(input("Enter your choice :"))
    if choice==1:
        view_task()
        add_task=input("Enter your task :")
        task.append(add_task.upper())
        print("Task sucessfully added to list")
        view_task()
    elif choice==2:
        view_task()
    elif choice==3:
        view_task()
        delete_task=input("Enter task  to delete :")
        task.remove(delete_task.upper())
        print("Task sucessfully Deleted from list")
        view_task()
    elif choice==4:
        break
    else:
        print("------>Invalid choice")