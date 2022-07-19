# def means a function with parameters or not

# function with no parameters or argument
def sayHello():
    print("Hello")

sayHello() # execute the function

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
sayHello_3("1") # works, since it has been stringify

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


# function with parameter (concrete data type specified) and retuns an implicit data type (suince it is not specified)
def sayHello_6(name : str): # expect parameter value to be a string datat type
    return "My name is " + name

result_1 = sayHello_6("Tim")
print(type(result_1)) # <class, 'str'>
print(result_1) # My name is Tim


# function with parameter (concrete data type specified) and retuns an explicit data type specified
def sayHello_7(name : str) -> str: # expect parameter value to be a string data type and its return data type to be string too
    return "My name is " + name

result_2 = sayHello_7("John")
print(type(result_2)) # <class, 'str'>
print(result_2) # My name is John