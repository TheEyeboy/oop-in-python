# What is Polymorphism: The word polymorphism means having many forms.
# In programming, polymorphism means the same function name (but different signatures) being used for different types.
# The key difference is the data types and number of arguments used in function.

class Nigeria():
    def _capital(self):
        print("FCT, Abuja is the Capital of Nigeria")

    def _language(self):
        print("Pidgin is widely used in Nigeria")

    def type(self):
        print("I really can't tell what level the country is in development")

class USA():
    def _capital(self):
        print("Washington, D.C. is the capital of USA.")
 
    def _language(self):
        print("English is the primary language of USA.")
 
    def type(self):
        print("USA is a developed country.")

object_Nigeria = Nigeria()
object_USA = USA()
for country in (object_Nigeria, object_USA):
    country._capital()
    country._language()
    country.type()




# Implementing Polymorphism with a Function 

class India():
	def capital(self):
		print("New Delhi is the capital of India.")

	def language(self):
		print("Hindi is the most widely spoken language of India.")

	def type(self):
		print("India is a developing country.")

class USA():
	def capital(self):
		print("Washington, D.C. is the capital of USA.")

	def language(self):
		print("English is the primary language of USA.")

	def type(self):
		print("USA is a developed country.")

def func(obj):
	obj.capital()
	obj.language()
	obj.type()

obj_ind = India()
obj_usa = USA()

func(obj_ind)
func(obj_usa)
