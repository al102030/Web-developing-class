from abc import ABC, abstractmethod

class Paricipant(ABC):
    def __init__(self, code=0, name="No nmae", family="No family"):
        self.code = code
        self.name = name
        self.family = family
        super().__init__()
        
    @abstractmethod
    def show_info(self):
        pass
    
    
    

class Lecturer(Paricipant):
    def show_info(self):
        print(f"Code = {self.code} , Name = {self.name} , Family = {self.family}")
        
    def greet(self):
        print("Welcome dear Professor")
        
class Student(Paricipant):
    __city = "Rasht"
    def show_info(self):
        print(f"Code = {self.code} , Name = {self.name} , Family = {self.family} , City = {self.__city}")
        

