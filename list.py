# list are know as arrays and you can mix different data types in a list
# list is denoted by []
# list index start from 0

beatles = ["Paul", "John", "George", "Ringo"]
beatles_mixed = ["Paul", "John", "George", "Ringo", 1, True] # mixing different data type in a list

print(beatles)
print(beatles_mixed)

# the type() function will tell us the data type of the variables
print(type(beatles))
print((type(beatles_mixed)))


for member in beatles:
    print(member.lower()) # print it in lower case


# append item to an existing list
beatles.append("Pete")

for member in beatles:
    print(member.upper()) # print it in upper case

# you can use negative number/index to access the list backwards
print(beatles[-1]) # print the last item => Pete
print(beatles[-2]) # print second to the last item => Ringo