# A Python program to demonstrate inheritance


# Base or Super class. Note object in bracket.

# (Generally, object is made ancestor of all classes)

# In Python 3.x "class Person" is

# equivalent to "class Person(object)"





#Parent Class

class Person(object):


    #__init__ is known as constructor
    def __init__(self, _first_name, last_name, id_number):
        self.first_name = _first_name
        self.last_name = last_name
        self.id_number = id_number


    def display(self):
        print(self.first_name)
        print(self.last_name)
        print(self.id_number)


#Child class
class Employee(Person):

    def __init__(self, first_name, last_name, salary, email, post, id_number):
        self.salary = salary
        self.email = email
        self.post = post

        #Invoking the init to the Parent Class
        Person.__init__(self, first_name, last_name, id_number)


empployee_1 = Employee("Anointed", "Joseph", 34, "josephanointed@gmail.com", "Senior Software Engineer", 10)

empployee_1.display()



#super() function in OOP
##Parent class
class Person():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def display(self):
        print(self.first_name, self.last_name, self.age)

#Child class
class Student(Person):

    def __init__(self, first_name, last_name, age, department, date_of_birth):
        self.sFirstName = first_name
        self.sLastName = last_name
        self.sAge = age 
        self.department = department
        self.date_of_birth = date_of_birth

        #Inheriting the properties of the parent class
        super().__init__("Anointed", "Davids", 45)


    def display_info(self):
        print(self.sFirstName)
        print(self.sLastName)
        print(self.sAge)
        print(self.department)
        print(self.date_of_birth)


object_ = Student("Alexander", "Kiyosaki", 19, "Neuroscience & Cognitive Technology", "26-12-2045")

object_.display()

object_.display_info()



#There are five(5) types of inheritance in Python
#Single Inheritance &
#Multiple Inheritances

#Python Example to demonstrate multiple line inheritance
class Base(object):

    #Constructor
    def __init__(self, _first_name, _last_name):
        self._first_name = _first_name
        self.last_name = _last_name

    #Get Names
    def get_names(self):
        return self._first_name, self._last_name

# Inherited Class or child class
class Child(Base):

    #Constructor
    def __init__(self, _first_name, _last_name, age, email):
        Base.__init__(self, _first_name, _last_name)
        self.age = age 
        self.email = email

    #Get email and age
    def get_email_age(self):
        return self.age, self.email

# Inheritd Class from child class
class GrandChild(Child):

    #Constructor
    def __init__(self, _first_name, _last_name, age, email, _address, faculty, department, phone_no):
        Child.__init__(self, _first_name, _last_name, age, email)
        self._address = _address
        self.faculty = faculty
        self.department = department
        self.phone_no = phone_no

    #Get all User details
    def get_user_details(self):
        return self._address, self.faculty, self.department, self.phone_no

details = GrandChild("Andre", "Jason", 20, "jason.andre90@gmail.com", "89, zedalk park", "Engineering", "Deep Learning Engineering", 907878785)

print("First Name: ", details._first_name)
print("Last Name: ", details._last_name)
print("Age: ", details.age)
print("Email Address: ", details.email)
print("Address: ", details._address)
print("Faculty: ", details.faculty)
print("Department: ", details.department)
print("Mobile Number: ", details.phone_no)





