# Python program to demonstrate
# use of class method and static method.

from datetime import date 

class Person:
    def __init__(self, _first_name, _last_name, _age):
        self._first_name = _first_name
        self._last_name = _last_name
        self._age = _age

     # a class method to create a Person object by birth year
    @classmethod
    def from_birth_year(cls, _first_name, _last_name, year):
        return cls(_first_name, _last_name, date.today().year - year)

    # a static method to check if a Person is adult or not
    @staticmethod
    def _is_adult(_age):
        return _age > 18

person_one = Person("Maureen", "Johnson", 20)
person_two = Person.from_birth_year("Maureen", "Johnson", 2002)

print(person_one._age)
print(person_two._age)

# Print the result 
print(Person._is_adult(21))

