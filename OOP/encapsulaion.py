# Python program to 
# demonstrate protected members 
# To Define a Protected member use a single underscore '_'
  
# Creating a base class

class Base:
    def __init__(self):
        
        # Protected member
        self._a = 2
    
# Creating A derived class
class Derived(Base):
    def __init__(self):

        # Call constructor of Base Class
        Base.__init__(self)
        print("Calling protected member of base class: ", self._a)

        # Modify  the protected variable 
        self._a = 4
        print("Calling modified protected members outside class: ", self._a)

object_ = Derived()

object_1 = Base()

# Calling protected member 
# Can be accessed but should not be done due to convention 
print("Accessing protected members of object One: ", object_._a)

# Accessing the protected variable outside 
print("Accessing protected member of object Two: ", object_1._a) 





# Python program to 
# demonstrate private members 
# To Define a Private member use a double underscore '__'

# Create a Base class
class Base:
    def __init__(self):
        self.a = "University of Benin"
        self.__c = "University of Benin"

# Create a Derived Class
class Derived(Base):
    def __init__(self):

        # Calling constructor of Base Class
        Base.__init__(self)
        print("Calling private memebers of base class: ")
        print(self.__c)


object_c = Base()
print(object_c.a)
  