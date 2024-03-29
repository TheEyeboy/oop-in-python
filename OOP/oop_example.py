#Object Instantiation In class

class Dog:

    #Creating a Simple class attribute
    attribute_1 = "Mammal"
    attribute_2 = "Dog"

    #Sample Method
    def fun(self):
        print("I am a ", self.attribute_1)
        print("I am also a ", self.attribute_2)

#Oject Instantiation
Rodger = Dog()

#Accessing the class attribute 
# and Method through Objects
print(Rodger.attribute_1)
Rodger.fun()
