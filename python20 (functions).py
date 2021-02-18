# functions

# what will funtions do for us?
#1. aviod repetation
#2. code reuse
#3. simplify our text
#4. easier to make changes.

# What is function?
# it is a set of instructions or codes.
# Ideal defination  =(noun)A reusable section of code with name that does something.
# sometimes it is called method.
# we should create one function which can perform only one action(or 2) at a time.

# how do we create a function? 
#1. use the keyword def.(short form of define)
#2. give our function a name. we may also have parameters name.
#3. write the code in the body of the function.
#4. use the return keyword to exit the from the function.

def function1():
    print("hello World!")
print("this is outside the function")
#to run this function we have to call this function.
function1()

# or-

def main():
    function2()
    return

def function2():
    names=["Shawki","Rowad","Rohan"]
    for step in names:
        print(step)
    return

main()

# what is parameters?
# it is a mapping.
# to create a function that accepts data we use paramaters.
# a parameters is a piece of data passed into a function.
# inside a function, parameters behave like a variable.
# we can use parameters both for integer value or string value.

# differnce between parameter and argument
# when we define variables for accepting  when defining a function is called a perameter.
# when we insert values for parameters when calling a function is called an argument.

# integer
def function3(x):
    return x*2
a=function3(45)
print(a)
b=function3(7835)
print(b)

#string
names = ["Shawki","Sowad","Hasnine"]
newName = input("enter last guest name: ")
names.append(newName)
def function4(lists):
    for step in lists:
        print(step)
function4(names)

# what about multiple parameters?
# we can simply add them in, separated by commas.
# we can use multiple parameters both for integer and string.
# we can use same variable or parameter name in different function.

# integer
def function5(x,y):
    return x+y
c=function5(209,45)
print(c)

#String
def function6(greeting, person):
    messageToDisplay=greeting+","+person
    print(messageToDisplay)
function6("Hi","Shawki")

# returning data
# Functions return data using the keyword return
# we can specify the value or data we want to pass back after the return keyword.
# we can reuse names in differenr functions.
# Professional programmers do not do calculation in return line.
# Instead of that, they create a variable and do calculation in the function.

def function7(name):
    message = "Hello, "+name
    return message
d=function7("Shawki")
print(d)

# combining parameter and string in same function.
def function8(z):
    print("this is still in the function")
    print("weeee")
    return z*41
e=function8(23)
print(e)

# combining multiple functions in same programme(Advance programming)
# example1-simmilar to function7
def function9(name):
    message = name+" reads in class 9."
    return message
def function10(message):
    print(message)
    return
output=function9("Shawki")
function10(output)
#or-function10(function9("Shawki"))
#but the first trick is better.

# example2-simmilar to function 4
def main_2():
    names =function11()
    function12(names)
    return

def function11():
    names = ["Shawki","Sowad","Hasnine"]
    newName = input("enter last guest name: ")
    names.append(newName)
    return names

def function12(names):
    for steps in names:
        print(steps)
    return
main_2()

# how to run a function if it is located in another program.
# suppose a function is loacted in the programme called helpers.py.
import helpers
f=helpers.function13(4)
print(f)

# recursive function
# function recursion means calling a function in its own defination.
# recursive function is very popular because we can solve any problem faster by using it.
def factorial(n):
    if n==1:
        return 1
    # this is called the base-case of the recursive function
    else:
        return n*factorial(n-1)
print(factorial(5))

# note that, whenever we have a recursive function we need to put an if-else case.
# unless it will give us a recursion error.


# we can do this without recursive function.
def factorial1(n):
        result=1
        for i in range(2,n+1):
                result=result*i
        return result
print(factorial1(5))

#Generator Expression(yeilding data)
nums=[1,2,3,4,5,6,7,8,9]
def gen_func(nums):
    for n in nums:
        yield n**2 
my_gen=gen_func(nums)
# yeild function dont return values immidiately.
# it continues till the end of the loop and store all values in a list.
# Finally, return the list.
print(list(my_gen))

# using documentation in function.
# we can use documentation inside our function and then they will be called docstrings.
# we can print the docstrings using __doc__ attribute.
# usually, programmer use documentation for writting information about the function or what that code is doing.
def greet(line):
    """
    this function just prints out given line
    """
    print(line)
print(greet.__doc__)
print(greet("Hello World!"))

# we can write a good documentation(doc string) like this.
def square_root(n):
    """Calculate the square root of a number.

    Args:
        n: the number to get the square root of.
    Returns:
        the square root of n.
    Raises:
        TypeError: if n is not a number.
        ValueError: if n is negative.
    """
    import math
    print(math.sqrt(n))
    
# challange 11
filename_1=input("enter your filename: ")
writeInput_1=input("enter what you want to input in this file: ")

def makingFile(filename,writeInput):
    newFile=open(filename,"w")
    newFile.write(writeInput)
    return
#makingFile(filename_1,writeInput_1)

# Extra credit1
# making bmi calculater using function
name1="Shawki"
height_m1=1.75
weight_kg1=70

name2="Sowad"
height_m2=1.6
weight_kg2=75

name3="Farhan"
height_m3=2
weight_kg3=165

def bmi_calculater(name,height_m,weight_kg):
        bmi=weight_kg/(height_m**2)
        print(bmi)
        if bmi<25:
                result=name+" is not overweight"
        else:
                result=name+" is overweight"
        return result
result1= bmi_calculater(name1,height_m1,weight_kg1)
print(result1)
result2= bmi_calculater(name2,height_m2,weight_kg2)
print(result2)
result3= bmi_calculater(name3,height_m3,weight_kg3)
print(result3)

# Extra credit 2
# making miles to kilometres converter.
miles=float(input("Enter how many miles you want to convert into kilometres: "))
def converter(miles):
        km=1.61*miles
        return km
kilometres=converter(miles)
print(kilometres)

# extra credit 3
# making a function which format dates.
import datetime     
userDate=input("enter your next birthdate(mm/dd/yyyy): ")
def formatDate(user):
        date=datetime.datetime.strptime(user,"%m/%d/%Y").date()
        return date
currentDate=datetime.date.today()
daysRemaining=formatDate(userDate)-currentDate
print("There are "+ str(daysRemaining) +" left for your birthday")

# extra credit 4
# making a function which can display febonacci series(recursive)
def febonacci(n):
        if n==1 or n==2:
                return 1
        return febonacci(n-1)+febonacci(n-2)
for i in range(1,10):
        print(febonacci(i))

# extra credit 5
# making a function which can handle error.
num1=input("enter a number: ")
num2=input("enter another number: ")
def errorhandler():
    import sys
    try:
        division= float(num1)/float(num2)
        print("the answer of the division is "+str(division))
    except ZeroDivisionError:
        print("somthing went wrong. You are trying to divide the first value by zero")
    except ValueError:
        print("something went wrong. please insert a number, not a letter or symble")
    except:
        error=sys.exc_info()[0]
        print("something went wrong. couldn\'t perform the action.")
        print(error)
errorhandler()

# extra credit 6
# making a function using boolean variable.
sad=False
def are_you_sad(isRainy, dontHaveUmbrella):
    if isRainy and not dontHaveUmbrella:
        sad=True
    else:
        sad=False
    if sad:
        print("yes, i am")
are_you_sad(True, False)

# pass keyword
def hello():
        pass
# pass keyword means we dont do anything with this function now.
# but it dont throw an error for leaving it blank.

# leaving function's argument blank
def ft(greeting="hi", name="you"):
        return f"{greeting}, {name}" 
print(ft())
# if we dont pass any argument, it wont give us an error.
# instead it will give us the default value.
print(ft("hello","shawki"))
# if we give an argument, it will ignore default argument.

# *args and **kwargs
def student(*args, **kwargs):# args and kwargs are allowing us to accept an orbitory number of positional or keyword argument. 
        print(args)
        print(kwargs)
student("math","comsci",name="shawki",age=14)
# here "math" and "comsci is positional argument, and the name="shawki" and age=14 is keyword argument.
# *args give us positional argument in a tuple.
# **kwargs give us keyword arguments in a dictionary.

# we can do the same thing-
def students(*args, **kwargs): 
        print(args)
        print(kwargs)
course = ["math", "comsci"] # positional aregument will be list.
info = {"name":"shawki", "age":14} # keyword argument will be dictionary.
students(course, info)# if we run this, we wont get our exact values.
# we want to unpack those values.
# for unpacking we need to give *
students(*course, **info)

# extra credit 7
# displaying number of days in month with function.
month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
def is_leap(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#or we can also import calendar library
# import calendar
# year=calendar.isleap(2017)# finding if the year is leapyear or not.
# print(year)
def days_in_month(year,month):
        if not 1<= month <= 12:
                return "invalid month"
        elif month == 2 and is_leap(year):
                return 29
        else:
                 return month_days[month]
print(days_in_month(2020,2))

# extra credit 8
# making a BMR calculater

name=input("what is your name? -->")
sex=input("are you a girl or boy? -->")
age=int(input("how old are you? -->"))
height=float(input("what is your height? -->"))
weight=int(input("what is your weight? -->"))

def ft2cm(height):
    import math
    height_cm=height*12*2.54
    return height_cm
def bmr_calculater(name,weight,height_cm,sex,age):
    if sex=="girl":
        bmr=655+(9.6*weight)+(1.8*height_cm)-(4.7*age)
    else:
        bmr=66+(13.7*weight)+(5*height_cm)-(6.8*age)
    messege= name.capitalize()+"\'s bmr is "+str(bmr)
    return messege
    
height_cm=ft2cm(height)
print("\n")
print(bmr_calculater(name,weight,height_cm,sex,age))

# extra credit 9
# displaying prime numbers
def isprime(x):
    p=0
    for n in range (2,x):
        if x%n==0:
            p +=1
    if p>=1:
        return False
    else:
        return True

n=int(input("how many primes you want to print?\n-->"))
primesList=[]
f=2
while len(primesList)!=n:
    for x in range (f,f*2):
        if isprime(x):
            primesList.append(x)
            if len(primesList) == n:
                break
    f *=2 
for i in primesList:
    print(i) 

# extra credit 10
# lcm calculator
def lcm_calc(a,b,c,d):
    abcd=a*b*c*d
    z=abcd+1
    initial=[x for x in range(1,z)]
    lcm_list=[x for x in initial if x%a==0 and x%b==0 and x%c==0 and x%d==0]
    lcm=min(lcm_list)
    return lcm
