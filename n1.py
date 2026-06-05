class Contact:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
    def show_contact(self):
        print(f"Name :{self.name}\nNumber :{self.phone}\n")      
number=[Contact("NISHANTH",522096684209),
    Contact("TEJA",24578669865386),
    Contact("CHANDU",345346577754),
    Contact("VAMSI",64564567547545),]   
print("========= Phone COntact=========\n")
for i in number:
    i.show_contact()
search=input("Enter Name :").upper()
found = False
for i in number:
    if search==i.name:
        print("Number :",i.phone)
        found = True
        break
if not found:
    print("Contact Not Found")

    


