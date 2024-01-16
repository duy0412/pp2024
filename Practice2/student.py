class Student:
    def __init__ (self, name, id, dob):
        self.std_name = name
        self.std_id = id
        self.std_dob = dob
    def toString(self):
        return f"Name: {self.std_name}\tId: {self.std_id}\tDob: {self.std_dob}"
    
    def get_std_name(self):
        return self.std_name
    
    def get_std_id(self):
        return self.std_id
    
    def get_std_dob(self):
        return self.std_dob
        