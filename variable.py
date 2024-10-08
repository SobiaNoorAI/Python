#<h1>Variables</h1>
name ="wood"
print(name)
print(3+2)
print(3-2)
print(3*2)
print(3**2) #power
print (round ((3**2),4)) #round
print(3/2) #return Float value
print(3//2) #return Integer Value
print(3%2) #moduler
#String--> collection of character
nam1 = 'Steve' #single quotes
nam2 = "Jobs" #double quotes
print(nam1 + nam2) # printing two strings together
print(nam1 + "9") # printing string with int
#list--> collection of different data, int, float, complex, list that can be modify
list=[2.3,4,5,0,-3, 3+3j,[3,5]] #used [] bracket
print(list)
# access element of list
print(list[1])
# add element to list
list.append(45)
print(list)
# Remove element to list
list.remove(0)
print(list)
# clear all element from list
list.clear()
print(list)
list=[2.3,4,5,0,-3, 3+3j,[3,5]]
# change element in list
list[2] =99
print(list)
#tuple is similar to list but it cannot modify
mytuple = (1.3,4,True,'root')#used () bracket
print(mytuple)