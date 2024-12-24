class user:
    def __init__(self,name, firstName, age, address):
        self.name = name
        self.firstName= firstName
        self.age= age
        self.address= address

    def name(self):
        return self.name
    
    def surname(self):
        return self.firstName
    
class admin(user):
    def hello(self):
        print("I am the admin ")

class patient(user):
    def hello(self):
        print(" I am sick")
class personal(user):
    def hello(self):
        print("I work because i need some money to buy some milk  ")
    
a= admin("Chuck", "Notnorris", 24, "Papendiek 2")
b= patient("Drinkmilk", "Cow", 23, "Müchen-str.2")
e= personal("Raza", "Nante",22,"Zimmermanstraße 14L")
c = [a,b,e]

name_in = input("Enter your family name: ")
firstnName_in = input("Then your weird first name: ")
for human in c:
    if human.name == name_in and human.firstName == firstnName_in:
        human.hello()
print("Btw, I like Orange Juice")        
    







    
