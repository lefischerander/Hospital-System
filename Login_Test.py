class user:
    def __str__(self):
        return f"{self.firstName} {self.name} ({self.userType})"
    
    def __init__(self, name, firstName, age, userType):
        self.name = name
        self.firstName= firstName
        self.age= age
        self.userType= userType
        
   


class Userservice:
    def __init__(self):
        self.users= []

    
    def create(self, creator, user):
       if creator.userType == 'admin':
           self.users.append(user)
           return user 
       
    def Create_admin(self):
        admin_user= user("Jackson","Michael", 90,"admin")
        self.users.append(admin_user)
        return admin_user

    def Get_admin_user(self):
        for person in self.users:
            if person.userType == 'admin':
                return admin_user
        return None
    
    def printUsers(self):
        for person in self.users:
           print(person)
         
    
    def get_users(self):
        return self.users
    
    def hasAdminUser(self):
        for person in self.users:
            if person.userType == 'admin':
                return True
        return False    
    
    def delete_User(self,user):
        self.users.remove(user)

        
               
        
User_service= Userservice()
if User_service.hasAdminUser():
    admin_user= User_service.Get_admin_user()
    print(f"We have an admin: {admin_user}")
    

else:
    admin_user= User_service.Create_admin()
    print(f"Admin created: {admin_user}")


user2= user("Malek", "Rami", 78, "Patient")
user3= user("Bob", "Bobby", 78, "Doctor")



#Manager.create(user2,user3)
new_user = User_service.create(admin_user,user2)
print("All users: ")
User_service.printUsers()

if new_user:
    print(f"New user created: {new_user}")
else:
    print(f"Operation failed, {user2} cannot be created")    

User_service.delete_User(user=user2)
print("Updated users: ")
User_service.printUsers()



#Manager.create(user3,user2)





        
        

    


    
    
      
    







    
