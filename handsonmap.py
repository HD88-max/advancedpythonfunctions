# Write a program to return the addition of numbers of two different lists. Then, display a list that is square of numbers of another list. Use the map() function here to get the desired result

def square(n):
    return n*n

list1 = [1,2,3,4,5,8,8]
list2 = [10,11,12,139,14]
result = map(lambda x,y:x+y,list1,list2)
print(list(result))
sq = list(map(square,list1))
print(sq)