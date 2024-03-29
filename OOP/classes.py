#Python Object-Oriented Programming 
#With DataCamp.com

#What a class is called the attribute and what a class does is called the method 
class Employee:

    #__init__ is called the initializer
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
    

    def school(self):
        print("University of Benin")


    def employee_info(self):
        print("This is " + self.first_name + " " + self.last_name + " and he is " + str(self.age) + " years old" + "\nEmail:" + self.email)

    #Passing Arguments
    def birthday(self):
        self.age += 1

    def set_co_employee(self, buddy):
        self.buddy = buddy
        buddy.buddy = self
    
    
        

# To instantiate an object, type the class name,
# followed by two brackets. You can assign this to a 
# variable to keep track of the object.

employee_1 = Employee("Anointed", "Joseph", 78, "anointed.joseph67@gmail.com")
employee_2 = Employee("Williams", "Smith", 82, "smithwilliams@gmail.com")

employee_1.employee_info()
employee_2.employee_info()

#Passing argument
employee_1.set_co_employee(employee_2)
employee_2.set_co_employee(employee_1)


print(employee_1.buddy.first_name)
print(employee_1.buddy.last_name)

print(employee_2.buddy.first_name)
print(employee_2.buddy.email)

employee_1.buddy.employee_info()

#print("This is " + ozzy.name + ", he is " + str(ozzy.age) + " years old\nAnd He is " + str(ozzy.size) + " in Size")