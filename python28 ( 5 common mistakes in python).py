# 5 common mistakes in python.

# mistake 1
# mixing tabs and spaces
# people who are new to python often mix tabs and spaces and they are inconsistant in their tabs and spaces.
# and leads to indentation errors.
# but once we will get our environment variable setted properly, then its almost impossible to run in this problem.
nums=[1,2,3,4,5]
for n in nums:
    p=n**2
    print(p)
# we can solve this problem manually.
# but if we have lots more identation line in our program,
# then it is very difficult to find the spacific one and to correct it manually.
# the best way to cope with this problem is to always use the upgraded version of vs code, pycharm, jupiter notebook,sublime text.
# Actually, any good editors in python will convert our spaces to tabs automatically. 
# It is also recomended to use a tool like pylint 
# that catches more mistakes like this for us that are easy to miss just by looking to our program.

# mistake 2
# naming module
# often people name their python module the same name as something they try to import.
# if we do this our own module with the same name takes higher priority
# than the modules from standerd library or the modules that we installed using pip.
# to fix this all we have to do is to rename our current working module.
# this is very easy to catch when we have import any module from standerd library.
# this will take much time to figure out if we have imported any library or package which we have installed with pip.
# this mistake gives us an import error.
# but we can also get import error if we have something wrong in our path.
# we also can make this type of name mistakes with variable name.
# we can name any of our variable which we used previously in our code as a function, variable,  class or something like that.
# this also wont give us our expected result.

# python isn't a compiled language in the sense where it's going to pick this things up before we run the code.
# and also it doesn't hold our hand and give the developer those types of restrictions.
# it gives us lot of freedom but somtimes this freedom allows us to do mistakes like this
# where we dont think we are sure to be able actually to do this like over writing a function like this.
# so the freedom allows us to do a lot of cool things with Python and allows us to write code very quickly.
# we we can also step on to our toes if we aren't careful.

# mistake 3
# mutable default arguments
# another thing people get tripped up on is mutable default arguments.
def add_employee(emp,emp_list=[]):
    emp_list.append(emp)
    print(emp_list)
# this function takes two argument emp and also an employee list.
# and it simply going to add this employee to this employee list and then print out the emp_list.
# but we can see here the employee list has a default value which is a empty list.
# so if we dont pass any emp_list when we call the function then it should make a new empty list for us from scratch.
emps=["John","Jane"]
add_employee("Corey",emps)
# now lets add couple of more employess without any list.
add_employee("Shawki")
add_employee("Hasnine")
# we can think that we will get a new list each time.
# but if we run that we can see that we are getting-
#['Shawki']
#['Shawki', 'Hasnine']
# so instead of printing out the second employee alone in a list,
# the second employee got into the emp_list of first employee.
# and it should get going if we add another emp without providing any list.
# each time it will get longer and longer and keeps appending to the same list 
# even though we should haev the empty list by default.
# so whats going on here?
#=> in python default arguments are evaluated once at a time it creates the function.
# so its not actually creating a new empty list each time we calling the function.
# we wont notice that with immutable types like strings and things like that.
# but in muttable datatypes like list, it is using the same list that it created when the function was defined.
# so what should we do here if we want to be sure to get a empty list each time?
# so instead of passing a mutable datatype like list we will pass None.
def add_employee2(emp,emp_list=None):
    if emp_list is None:
        emp_list=[]# now this is in the function. this will get run everytime the function will run
    emp_list.append(emp)
    print(emp_list)
add_employee2("Shawki")
add_employee2("Hasnine")
# so basically default arguments are created once when the function was defined,
# it dont created every time when the function is called.

# there are some more places where we may face this problem.
import time
from datetime import datetime

def display(time=datetime.now()):# it takes time a argument. it has a default value of current time.
    print(time.strftime("%B, %D, %Y %H:%M:%S"))

display()
time.sleep(1)# here we are sleeping the code after each function call for 1 sec.
display()
time.sleep(1)
display()
# we might expect if we dont give time argument, we will always have the current time printed.
# but we can see that each time it ran it didnt update the time like we might expect.
# the reason is as before is it executes only one when the function was defined and not each time the function is run.
# to solve this problem we could do something like this.

def display_time(time=None):
    if time is None:
        time=datetime.now()# this if conditional will run each time we call the function.
    print(time.strftime("%B, %D, %Y %H:%M:%S"))

display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()

# mistake 4
# exhaust
# new people dont fully understand how iterators work and how they are exhausted.
# this also true for those people who move from python2 to python 3
# because more thing in python3 are behave like generators because those are more efficient.

names=["Peter Parker","Clark Kent","Wade Wilson","Bruce Wayne"]
heroes=["Spiderman","Superman","Deadpool","Batman"]
# here this two lists are related.
# they have corresponding indexes.
# so we can use zip function to match up items from both list.
identities=zip(names,heroes)
print(identities)
# if we run this using python2, we will get a list of these paired items.
# thats what zip function does.
# it zipped up the first item of names list to the first item of the heroes list.
# if we want to loop over these one at a time and print this.
for name,hero in identities:
    print(f"{hero} is actually {name}")
# or we can do that-
for identity in identities:
    print("{} is actually {}".format(identity[0],identity[1]))

# now lets switch over python3
# if we run the same code, it pretty much looks same.
# but now we are getting the zip object instead of that paired list.
# whats going on here is that python3 no longer returns all of those values at once.
# and thats good for efficiency because if this was a bit list, we need to save the values in memory.
# but it not look like what we expect.
# we can get all the values at once, but we need to cast them to a list.
print(list(identities))
for identity in identities:
    print("{} is actually {}".format(identity[0],identity[1]))
# but now it is not looping through our list.
# this is where people get fustrated.
# whats going in here?
# zip is a iterator and iterators can be exhausted.
# that means that we can loop through and acsess its values one time, then we cant do that again.
# but its really not a big deal.
# we can still do everything that we want to do but just have to do it in a slightly different way.
# when we converted the zip object to a list, it already loop through the iterator.
# so the iterator become empty and we could not loop over that.
# we can solve this problem by simply converted it to a list from start, and print the list and then loop over that.
new_identities=zip(names,heroes)
listed=list(new_identities)
print(listed)
for identity in listed:
    print("{} is actually {}".format(identity[0],identity[1]))
# now it has become a list and list are not exhausted.

# mistake 5
# imports
# there is a bad practise that is using an asterisks(*) when doing imports.
# an asterisks in importing imports everything in the module.

# if we dont want to print the module name everytime we can use from method.
# for each an additional function we will have to add that in our import.
from os import rename, remove

# sometime people dont aware of what they are doing and they want to import everything from that module by using *
from os import *

# but why is this a bad practice?
# first of all it will make our code hard to debug.
# people wont find where all the functions are coming from in a big program if we use *.

# it can also introduce errors in our code whenever there are two functions of same name. 
from html import *
from glob import *
# both of them are standerd library and we are importing everything from that library.
# but both of the html and glob module have an escape function.
# one escapes html special character from the html module and the other escapes special character in a path.

# in this case the html escape function will be overwritten by the glob escape function.
# we can see that by doing this-
print(help(escape))
# our output says that-
# Help on function escape in module glob:
# escape(pathname)
    # Escape all special characters.

# so using this * is extremply easy to make trouble for peoplt to running the code and its a pain to debug.
# and also it can cause issues like this.
# so anytime we need to import anything form any module it is better to import it explicitly.
# we can-
from html import escape as h_escape
from glob import escape as g_escape # we need to rename it. otherwise it will still overwrite the function.
# but the best way to do it that
import html 
import glob 
# and then working with like html.escape and glob.escape.

