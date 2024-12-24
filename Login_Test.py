class user:
    def __init__(self, name, firstName, age, userType):
        self.name = name
        self.firstName= firstName
        self.age= age
        self.userType= userType
        
   


         
        
class UsersManagement:
    def __init__(self):
        self.users= []
    
    def create(self, user):
        self.users.append(user)
        return user
    
    def printUsers(self):
        for person in self.users:
           print(person.name)
           print(person.age)


       
user1= user("Jackson","Michael", 90,"admin")
user2= user("Malek", "Rami", 78, "Patient")
user3= user("Bob", "Bobby", 78, "Doctor")

Manager= UsersManagement()

user1= Manager.create(user1)
user2= Manager.create(user2)
user3= Manager.create(user3)

Manager.printUsers()
        
        

    


    
    
      
    







    
