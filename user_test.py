import hashlib

class User:
    def __init__(self, username, password, role= 'role', department=None):
        self.username = username
        self.password = self.hash_password(password)
        self.role = role
        self.department = department

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password, role='admin')

class Patient(User):
    def __init__(self, username, password):
        super().__init__(username, password, role='patient')

class Doctor(User):
    def __init__(self, username, password, department):
        super().__init__(username, password, role='doctor', department=department)
