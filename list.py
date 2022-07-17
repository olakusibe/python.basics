# list are know as arrays and you can mix different data types in a list
# list is denoted by []

beatles = ["Paul", "John", "George", "Ringo"]
beatles_mixed = ["Paul", "John", "George", "Ringo", 1, True] # mixing different data type in a list

print(beatles)
print(beatles_mixed)

# the type() function will tell us the data type of the variables
print(type(beatles))
print((type(beatles_mixed)))


for member in beatles:
    print(member.lower()) # print it in lower case
