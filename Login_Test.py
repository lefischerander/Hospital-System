import uuid 



class user:
    def __str__(self):
        return f"{self.firstName} {self.name} ({self.user_type}) {self._id}"
    
    def __init__(self, name, firstName, age, user_type):
        self.name = name
        self.firstName= firstName
        self.age= age
        self.user_type= user_type
        self._id= uuid.uuid4()

    def get_id(self):
        return self._id    
        
   


class Userservice:
    def __init__(self):
        self.users= []

    
    def create(self, creator, user):
       if creator.user_type == 'admin' or 'doctor':
           self.users.append(user)
           return user 
       ##elif creator.user_type == 'doctor':
           ##self.users.appends(user)
           ##return user
    
    def create_admin(self):
        admin_user= user("Jackson","Michael", 90,"admin")
        self.users.append(admin_user)
        return admin_user

    def get_admin_user(self):
        for person in self.users:
            if person.user_type == 'admin':
                return admin_user
        return None
    
    def print_users(self):
        for person in self.users:
           print(person)
         
    
    def get_users(self):
        return self.users
    
    def has_admin_user(self):
        for person in self.users:
            if person.user_type == 'admin':
                return True
        return False    
    
    def delete_user(self,user):
        self.users.remove(user)
    
    def get_user_by_id(self,caller_user,id):
       personWithSpecifiedId = None
       for person in self.users: 
            if person.get_id() == id:
               personWithSpecifiedId = person   
       if personWithSpecifiedId == None:
          return None 
       callerUserType = caller_user.user_type
       if callerUserType == 'admin':
            if personWithSpecifiedId.get_id() == id:
                return personWithSpecifiedId
       elif callerUserType == 'Patient':
            if caller_user.get_id() == id :
                return personWithSpecifiedId 
            elif personWithSpecifiedId.user_type == 'Doctor':
                return personWithSpecifiedId
            raise Exception (" A patient can only get its own data")
       
 





       
               
           
           
         
        


        
               
        
user_service= Userservice()
if user_service.has_admin_user():
    admin_user= user_service.get_admin_user()
    print(f"We have an admin: {admin_user}")
    

else:
    admin_user= user_service.create_admin()
    print(f"Admin created: {admin_user}")


user2= user("Malek", "Rami", 78, "Patient")
user3= user("Bob", "Bobby", 78, "Doctor")
user4= user("Harry", "Potter", 54, "Patient")


#Manager.create(user2,user3)
new_user = user_service.create(admin_user,user2)
other_user= user_service.create(admin_user,user3)
new_other_user= user_service.create(admin_user,user4)
print("All users: ")
user_service.print_users()

if new_user:
    print(f"New user created: {new_user}")
else:
    print(f"Operation failed, {user2} cannot be created")    

#user_service.delete_user(user=user3)
print("Updated users: ")
user_service.print_users()

user_with_id = user_service.get_user_by_id(caller_user= admin_user, id= user4.get_id())
print(f"User with Id: {user_with_id}")


#Manager.create(user3,user2)





        
        

    


    
    
      
    







    
