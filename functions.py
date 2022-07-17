# def means a function with parameters or not

# function with no parameters or argument
def sayHello():
    print("Hello")

sayHello()

# function with parameter (non concrete data type specified)
def sayHello_2(name):
    print(name)

sayHello_2("Tim")
sayHello_2(1)

# function with parameter (non concrete data type specified)
def sayHello_3(name):
    print("My name is " + name) # trying to concatenate a string (assumption that parameter value is a string)

sayHello_3("Tim")
# sayHello_3(1) # an error (TypeError) because of data type mismatch, cannot concatenate str and int data type
sayHello_3("1")

# function with parameter (non concrete data type specified)
def sayHello_4(name):
    print("My name is " + str(name)) # str() function will convert any data type to string data type

sayHello_4("Tim")
sayHello_4(1)

# function with parameter (concrete data type specified)
def sayHello_5(name : str): # expect parameter value to be a string datat type
    print("My name is " + name)

sayHello_5("Tim")
# sayHello_5(1) # an error (TypeError) because of data type mismatch, cannot concatenate str and int data type
sayHello_5("1")


# by deafult, all the functions in python will always returns something, even though you did not explicitly returning any thing

result = sayHello()
print(type(result)) # NoneType (beacse sayHello() function is retuning nothing)
print(result) # None


# function with parameter (concrete data type specified) and retuns a string data type
def sayHello_6(name : str): # expect parameter value to be a string datat type
    return "My name is " + name

result_1 = sayHello_6("Tim")
print(type(result_1)) # <class, 'str'>
print(result_1) # My name is Tim
