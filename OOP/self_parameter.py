

#The Self Parameter does not call it to be Self, You can use any other name instead of it.
#Here we change the self to the word individuals and the output will be the same.

class Workers:
    def __init__(individuals, company, name):
        individuals.company = company
        individuals.name = name

    def show(individuals):
        print(
            "Hi my name is " + individuals.name + " and I work in " 
            + individuals.company + "."
        )

object_1 = Workers("Apple Inc", "John Washinggton")
object_1.show()