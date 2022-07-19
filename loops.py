beatles = ["Paul", "John", "George", "Ringo"]

# a for loop
for member in beatles:
    print(member)


# a while loop
indx = 0
while indx < len(beatles): # len() function returns the number of items in the list
    print(beatles[indx])
    indx += 1