#We Have two types of Constructors in Python
# * Default Constructor 
# * Parameterized Constructor

class Student:

    #default constructor
    def __init__(self):
        self.student_name = "Ted Johnson"

    #A method for printing data members
    def print_students_name(self):
        print(self.student_name)

#Create an Object for the class
object_ = Student()

#Calling instance method using the object object_
object_.print_students_name()


#Parameterized Constructor example
class Addition:
    first = 0
    second = 0
    answer = 0

    #Parameterized Constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s
    
    def display(self):
        print("First Number: " + str(self.first))
        print("Second Number: " + str(self.second))
        print("Addition of two numbers: " + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second

#Create an Object of the class 
#This will invoke parameterized constructor
object_ = Addition(200, 788)

#Create a second Object for the same class
object_1 = Addition(222, 34)

#Perform addition on object_
object_.calculate()

#Perform addition on object_1
object_1.calculate()

#Display Object_
object_.display()

#Display object_1
object_1.display()






class MyClass:
	def __init__(self, name=None):
		if name is None:
			print("Default constructor called")
		else:
			self.name = name
			print("Parameterized constructor called with name", self.name)
	
	def method(self):
		if hasattr(self, 'name'):
			print("Method called with name", self.name)
		else:
			print("Method called without a name")

# Create an object of the class using the default constructor
obj1 = MyClass()

# Call a method of the class
obj1.method()

# Create an object of the class using the parameterized constructor
obj2 = MyClass("John")

# Call a method of the class
obj2.method()
