# if statement

answer = input("Do you buy a ice-cream for me? (yes/no)\n")
if answer =="yes": # if statement allows us to specify code that only executes if a specific condition is true.
    print("Of course. Why not?") # we have to press TAB before writing down print command.
if answer =="no": # we have to write a colon(:) after the condition.
    print("No. I don't have enough money.")
print("Have a nice day.")

# When we use if statement-
# comparisons-
# ==    equal to
# !=    not equal to
# <     less than
# >     greater then
# <=    less than or equal to
# >=    greater than or equal to 
# is    object identity

# But sometimes the user may not answer as our thought. In this case we need to manipulate the code. EXP-
team=input("what is your favourite team?\n")
if team.upper()=="REAL MADRID":
    print("That's my favourite team too!!")

# if with numbers
deposit=input("How much you want to diposit?\n")
if int(deposit) > 100 :
    print("Congratulation! you have became our special member.")
print("Have a nice day!")

# else statement
deposit=input("How much you want to diposit?\n")
if int(deposit) > 100 :
    print("Congratulation! you have became our special member.")
else: # else code is only executed if the condition is not true.
    print("Thanks for your deposit.")
print("Have a nice day!")

# boolean variables. 
# We use boolean variables to remember if a condition is true or false.
# coders call it flag.

# Initialize the variable to fix the error.
freetoaster=False

deposit=input("How much you want to diposit?\n")
if int(deposit) > 100 :
    # set the boolean variable freetoaster is true.
    freetoaster=True   
# if the variable freetoster is true the print statement is execute-
if freetoaster:
    print("enjoy your toaster!")

# what is the difference between is and == ?
# is means we are checking if both variables have same id or not. id is the number of the objects in memory.
# == means we are checking if both variables contain same values or not.
a=[1,2,3]
b=[1,2,3]
print(id(a))# we can print a variable's id by "id" function.
print(id(b))
print(a==b)# true
print(a is b)# false
# a and b doesn't have same id.
# their id are save as different object in the memory.

# can anytime two different variables id be same?
# yes.
# exp- 
a=[1,2,3]
b=a
print(id(a))
print(id(b))
print(a==b)# true
print(a is b)# true

# there are some argument which python evaluates to false.
# False Values-
#   False (keyword)
#   None  (keyword)
#   zero(0) of any numeric type.
#   any empty sequences. for example-"",(),[]
#   any empty mapping. for example-{}

# turnery operator
# we can use if else statement when we are initializing a variable. it is called teunery operator.
# this is pretty much like lambda function.
a=101
b=200 if a==100 else 300
print(b)

# we can allso use else statement with loop.
# we dont have to use if statement before.
for i in range(5):
    print(i)
else:
    print("Done")
# this else code will execute after our looping get stopped.

# we can also use  else statement after error handling.
# it will execute if certain except statement becomes False.
my_file = "/temp/test.txt"

try:
    f=open(my_file,"r")
except IOError as e:
    print("File cannot be accessed")

else:
    with f:
        print(f.read())

# all() and any() function.
# all() and any() function takes an iterable as an argument.
# all() returns true if all the values of that iterable is true, otherwise false.
# any() returns true if any of the values of that iterable is true, otherwise false.
if all([True,True,True,False]):
    print("Ok")
else:
    print("no")

if any([True,False,False,False]):
    print("ok")
else:
    print("no") 

# challange 5
# calculate shipping charges for a shoper.

ttp=input("What is the amount for your total purchase?\n")
if int(ttp) < 50:
    finaltotal=int(ttp)+10
    print("Your final total shipping charge is "+str(finaltotal)+"$")
else :
    print("your final total shipping charge is "+ttp+"$")
print("Have a nice day!")