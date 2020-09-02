from dataclasses import dataclass

@dataclass
class Student:
    #Predefined object types
    name: str
    college_id: int
    gpa: float

def main():
    #__init__() and parameters are ignored, don't need to reference "self."
    #Calls student class and passes data within parenthesis to the objects
    alice = Student('Alice', 12345,3.58)
    bob = Student('Bob', 98765,3.25)

    print(alice)
    print(bob)

main()