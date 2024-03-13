
class Student:
    roll = ""
    gpa = ""
    
    def __init__(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa
    
    def dis(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")
        
    
    
Robiul = Student(101,3.1)
Robiul.dis()


Rabbi = Student(102,3.2)
Rabbi.dis()


MHS = Student(103,3.3)
MHS.dis()
