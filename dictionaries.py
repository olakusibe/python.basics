# dictionaries are denoted by {}
# it makes having key-value pairs possible
# keys should be unique

beatles = {
    "key":0, # here 0 is the value, an that's the syntax/structure for a dicitonary
    "Paul":1,
    "John":2,
    "George":3,
    "Ringo":4
}

print(beatles)

print(beatles["John"]) # print the value of the key (John)

beatles_2 = {
    0:"value",
    1:"Paul",
    2:"John",
    3:"George",
    4:"Ringo"
}

print(beatles_2[2]) # print the value of the key (2)

# you can also use any type of object (data type) as the value in a dicitonary

beatles_3 = {
    0:"value",
    1:"Paul",
    2:"John",
    3:"George",
    4:"Ringo",
    5:["Drums", "Guitar"] # using a list data type as the value
}

print(beatles_3[5]) # print the list at key(5)

# print the type of object each is
print(type(beatles_3)) # <class, 'dict'>
print(type(beatles_3[1])) # <class, 'str'>
print(type(beatles_3[5])) # <class, 'list'>