# Write a program to return - 1. zipped list from two lists 2. elements of two lists zipped together, but 2nd list in reverse order 3. elements of two lists zipped into a dictionary
name = ["John","Johnny","Hardik","Rajiv","Arshdeep"]
rollnum = [8,2,34,5,1]
list1 = list(zip(name,rollnum))
print(list1)
for x,y in zip(name,rollnum[::-1]):
    print(x,y)