# when you need to create your own types, user defined types (udt)
# to be used in OOP or domain driven designs, you will define it as a class
# for every function/method defined in the class, you will have to pass 'self' (the instance of the object), to get acees to the instance values

class Person():

    # instance values are specified at the contructor level, after self parameter
    # though some types may be parameter-less
    # this is the constructor, also self is passed here
    def __init__(self, name, country):
        self.name = name
        self.country = country

    # this is a function/method defined in a class, and self is passed into it, to have access to the instance values
    def sing(self): 
         print(self.name + " sings")


p1 = Person("John Lennon", "UK") # how to create the instance of the object/type
p1.sing() # execute the class function/method