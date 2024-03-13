
class Student:
    roll = ""
    gpa = ""
    
    def set(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa
    
    def dis(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")
        
    
    
Robiul = Student()
Robiul.set(101,3.1)
Robiul.dis()


Rabbi = Student()
Rabbi.set(102,3.2)
Rabbi.dis()


MHS = Student()
MHS.set(103,3.3)
MHS.dis()
