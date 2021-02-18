# lists

guests=["Shawki","Ramos","Ronaldo","Marcelo"]
scores=[0,71,50,124,12]
# this is called list
# list allows us to store multiple values (multiple types of values such as str,int,bool,float)

# we can also create an empty list and add values later
games=[]
hobby=[]
#we can do the same thing by using list function.
dog=list()

# we can reference any value in the list by specifying it's position in the list.
#exp; the first value is in position 0
print(guests[0]) 

# programmers call the position of an item in the list "the index".

# we can even count backwards
# print the last entry of the guest-
print(guests[-1])

# we can also access the index of range of values.
print(guests[0:3])
# this means print values in guests list from the index 0 to 3 but not including 3.
 
# we can also blank 1 index of the values.
print(guests[:3])
# this is actually print the same thing.
#or-
print(guests[2:])
# this means print the value from the index 2 to last.


# Updating lists
# we can change a value from the list.

fun=[1,2,3,4,5,6]
print("first value is "+str(fun[0]))
fun[0]=100
print("first value is now "+str(fun[0]))

# we can add a value to a list with append() function

# add a new value to the end of the list
fun.append(1200)
# display the last value in the list
print(fun[-1])
# add a new value in the list with the location.
fun.insert(0, 23)
print(fun[0])
# insert method don't overwrite anything.
# when we apply this method all other vaules just shifted.

# adding multiple values in our list using extend method.
a=["mango","berry","cherry"]
b=["apple","banana","orange"]
a.extend(b)
print(a)
# this method extends each indiviual item in the list.

# we can remove a value from a list with remove() function.
# first method -
fun.remove(4)
print(fun[3])

# second method-
# delete the first item in the list
del fun[0] # it is delete command
print(fun[0]) # delete command takes the index as an argument.

# third method
# deleting the last item of the list using pop method.
fun.pop() # pop deletes the last item of the list.
print(fun[-1])
# we can also specify the item with index which we want to delete using pop method.
fun.pop(2)
print(fun[1])
# pop method returns the valus that it removed.
g=["ball","bat","gloves","jersy","socks"]
popped=g.pop()
print(g)
print(popped)

# searching an item in the list using index() function
# the index() function will search the list and
# return the index of the position where the value was found.
cities=["dhaka","madrid","turin","paris"]
print(cities.index("madrid"))

# what if we want to check if a value is in our list or not? 
# we can use "in" operator.
# it gives us a boolean.
cities=["dhaka","madrid","turin","paris"]
print("london" in cities)
print("paris" in cities)

# challange 8
pet =["cat","dog","dog","lion","dog","frog"]
for steps in range(3):
    pet.remove("dog")
print(pet[1])

# displaying texts using a loop
cities=["dhaka","madrid","turin","paris"]
# create a loop that executes four time because we have four values.
for steps in range(4):
    print(cities[steps])

# len() function

# we use len() function to find out how many entries are in our list. len is the short form of lenth.
numentries=len(cities)
print(numentries)
for steps in range(numentries):
    print(cities[steps])

# easiest method for displaying text 
# we can just tell the for loop  to go through our list.
cities=["dhaka","madrid","turin","paris"]
for steps in cities:
    print(steps)

# what if we want to display the values with their index?
# we can use enumerate function in our for loop.
cities=["dhaka","madrid","turin","paris"]
for index, steps in enumerate(cities):
    print(index, steps)

# we can also pass a second argument for which number we want to start the index.
cities=["dhaka","madrid","turin","paris"]
for index, steps in enumerate(cities, start=1):
    print(index, steps)

# we can sort our list in alphabetical order with sort() function.
players=["ronaldo","mbappe","bale","ramos","marcelo"]
players.sort()
for step in players:
    print(step)
# we can also sort our list in reverse alphabetical order(reversely sorted) by adding reverse argument in sort method.
players=["ronaldo","mbappe","bale","ramos","marcelo"]
players.sort(reverse=True)
for step in players:
    print(step) 

# we can reverse our list using reverse method. 
# It doesn't sort our list. It only reverse it.
cities=["dhaka","madrid","turin","paris"]
cities.reverse()
print(cities)

# in all this reverse and sort method cases we sorted the original list.
# What if we want to sort the list without doing any change to our original list?
# we can use sorted function.
cities=["dhaka","madrid","turin","paris"]
cities_2=sorted(cities)
print(cities_2)
#or-
cities=["dhaka","madrid","turin","paris"]
cities_2=sorted(cities,reverse=True)
print(cities_2)
# we can reverse our list without changing it using reversed method. 
cities=["dhaka","madrid","turin","paris"]
cities_2=list(reversed(cities))# here we have to make it list because reversed method dont give us any list. it gives a location.
print(cities_2)

# how to sort accending in order to their absolute value?
# we need to and another argument which is the key argument.
ggg=[-1,-3,-7,0,1,3,2,4,5,6]
ggg1=sorted(ggg,key=abs)# we dont give any bracket next to abs function. otherwise,it will show us an error.
print (ggg1)

# swapping the first value of the list with the last value
b=["banana","apple","mango"]
temp=b[0]
b[0]=b[2]
b[2]=temp
print(b)
# short formula
b[0],b[2]=b[2],b[0]
print(b)

# displaying minimum value of a list using min function.
nums=[1,2,3,4,5,6,7,8,9,90,1111]
print(min(nums))

# displaying maximum value of a list using max function.
nums=[1,2,3,4,5,6,7,8,9,90,1111]
print(max(nums))

# displaying sum of the values in the list using sum function.
nums=[1,2,3,4,5,6,7,8,9,90,1111]
print(sum(nums))

# how to make our list into a string.
# we can use join method.
cities=["dhaka","madrid","turin","paris"]
cities_str=", ".join(cities)
print(cities_str)

# how to make our string into a list.
# we can use split method.
cities=["dhaka","madrid","turin","paris"]
cities_str=", ".join(cities)
cities_list=cities_str.split(", ")
print(cities_list)

# we can even do mathematical operations with list.
a=[1,2,3]
print(a+[4,5,6])# this is pretty much like extend() method.
print(a*3)

# challange 9
print()
print()
guest=[]
print("I will take the name of your guests and sort them in alphabetical order.")
print("When you are done with giving the name of your guests, write down'done'.")
user="shawki"
while user !="Done":
    user=input("Whom does you want to invite to your party?\n").capitalize()
    guest.append(user)
guest.remove("Done")
print()
print()
guest.sort()
print("Here are your guests' names in the alphabetical order.")
for steps in guest:
    print(steps)  

#extra credit 1
# how to make a list which have elements which are double of the elements of the given list?
a=[1,2,3,5,7,8,10,1111,2933] 
c=[]
for x in a:
    c.append(2*x) 
print(c)   

# we can do the same thing by using list comprehension in python.
d=[2*x for x in a]
print(d)

# extra credit 2
e=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
f=[x**2 for x in e]
print(f)

# extra credit 3
d=[]
for x in range(6,0,-1):
    d.append(x**2)
print(d)
#or-
d=[x**2 for x in range(6,0,-1)]
print(d)

#extra credit 4
# copy list

# method 1
# using list comprehension
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
b=[x for x in a]
print(b)

#method 2
# using copy method
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
b=a.copy()
print(b)

# method 3
# equal variable
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
b=a
print(b)

#method 4 
#using loop
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
b=[]
for x in a:
    b.append(x)
print(b)

# conditionals in if comprehension
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
b=[x for x in a if x > 10]
print(b)
c=[x for x in a if x%3==0]
print(c)
d=[x for x in a if x==1 or x==2 ]
print(d)
e=[x for x in a if x%3==0 and x%5==0]
print(e)
# we cant use else in list comprehension

# how to calculate LCM of two numbers.
a=595
b=345
ab=a*b
z=ab+1
initial_list=list(range(1,z))
lcm_list=[x for x in initial_list if x%a==0 and x%b==0]
print(min(lcm_list))

# how to calculate GCD
import math
print(math.gcd(23,78))