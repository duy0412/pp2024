class Course:
    def __init__(self, name, id):
        self.crs_name = name
        self.crs_id = id
    def toString(self):
        return f"{self.crs_name}\t{self.crs_id}"
    
    def get_crs_name(self):
        return self.crs_name
    
    def get_crs_id(self):
        return self.crs_id