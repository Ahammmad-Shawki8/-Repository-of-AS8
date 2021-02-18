# variable scope: understanding the LEGB rule and global_nonlocal statements
# LEGB stands for Local, Enclosing, Global, Built-in

# understanding how the scope works is one of the most important concept of knowing a language.
# because we have to use this concept almost in every program we write.
# understanding that will also help us in those situation
# where a variable not containing the value that we expexted and we need to debug our code.

# variable scope determines where a variable can be accessed from within the program and what values those variables holds in different concepts.
# there is a common abbreviation of knowing the variable scope in python and that is LEGB.

# locals are variables to find within a function.
# enclosing are variables in the local scope of enclosing functions.
# global are variables to find at the top level of a module or explecitely declared global using global keyword.
# built-in are just names that are pre-assigned in python.

# LEGB is the order which determines whatt a variable is assigned to.
# so python first checks the variables in the local scope, then the enclosing scope, then the global and lastly in the built-ins.

# instead of following this order, ets first learn about local and global scope.
# because these are most commonly confused.

# lets say in this python module we set a variable x.
x = "global x"
# now variable x is a global variable because it is in the main body of our file.

# now lets make a function.
def test():
    y = "local y"
    print(y)
# now this y variable is a local variable and it is local to this test function.
# if we execute this function.
test()
# we can see that python use the LEGB role to print out the variable y.
# first it looks and checks if we have y variable in our local scope which are variables that are defined within the function.
# and it found that local y variable and printed them out.

# now lets create another function without the print command.
def test_2():
    z = "local z"
    # now we are printing global variable x within the test_2 function.
    print(x)
# if we execute this,
test_2()
# we can see that even though we are in the test_2() function, it still print out global x.
# and the reason behind it,
# first it look for if we have a x variable in our local scope, but it didn't find it.
# it doesn't find x in the enclosing scope either.
# then it checks if we have a x variable in our global scope, then it finds the variable and prints it.

# but if we print z.
#print(z)
# we can see that we are getting an error, which says name z is not defined.

# we can think of that we have ran the test_2() function before, which should have set the z variable,
# but we can print it outside of that test_2() function.
# because python didnt find the z varibale, in local, enclosing, global or built-in.
# so then it throws the name error.

# now instead of printing the z variable outside of the test_2() function, lets print x variable.
print(x)
# now we can see that it prints the global x variable within the test_2() function and without.

# now lets create a new function.
def test_3():
    x = "local x" # here we have created a local x variable inside of a function.
    print(x)

# if we run that it might not be obious what it will print out.
test_3()
print(x)
# we can see that it ran the test_3() function here and printed out the local x.
# the it comes out of the function and prints the global x.

# sometimes we might think the global x varibale might be overwitten by the local x within the test_3() function
# but thats not happens. it just create a local x variable which lives only within this function.
# and anything outside the local scope still sees the global x variable.

# what if we want to set a new value for the global x variable for within the test function.
# to do thsi we can explicitely tell python that we want work with the global x variable.
# to do this we can write global x at the top of the function body.
def test_4():
    global x
    x = "local x"
    print(x)

test_4()
print(x)
# now if we run this we can see that it first enter the function and see that we are working with the global x 
# and set the value of x to  local x and then it prints it.
# after the function, the value of our global x variable is also changed.

# but the naming here is misleading, because it is no longer in the local scope it is in the global scope.

# another thing we need to know is that, we dont need to set a global variable previousely defined to work with it inside of the function.
def test_5():
    global w
    w = "global w"
    print(w)

test_5()
print(w)
# we can see that it was still able to find and print the global w variable even though it doesn't exits outside of the function.
# that will only work if we set a global variable inside of the function.
def test_6():
    v = "local v"
    print(v)

test_6()
#print(v)
# we can see that it prints out the local v form the test_6() function and then raise a name error for the v that we print outside of the test_6() function.

# NOTE: we dont need to use global keyword often. if we use it often then we are probably doing something wrong.
# because it would be very difficult to maintain out code if we use the flobal statement often and we have worried about the values outside of that function.
# local scope allows us to not worrying about whats going outside of the function.
# so, Not overusing global scope and using local scope is recommanded.


# now lets see functions with arguments.
def test_7(a):
    w = "local w"
    print(a)

test_7("local a")
#print(w)

# a is going to be a local variable within the test_7() function also.
# its not going to exits outside of that function. it is simmilar to when we set a local x variable inside our function.
# the only difference is that a is a function parameter which vcan now be assigned values passed to our test_7() function.

# if we run this we can see that we are passing in the local a variabel inside the function 
# and it first look to its local scope and it found that local a
# then it print out the local a variable.

# if we print that outside of the function,
#print(a)
# then it will gives us a name error.


# now lets look at build in scopes.
# this is pretty easy because it is just names that are pre assigned in python.

# for example, min is a built in function in python which defines the smallest value of an iterable.
m = min([3,6,4,5,1])
print(m)
# we are able to use min here, because it is a built in function in python.
# if we want to see the variables which in the built-in scope we can see the directory of the builtins standerd module.
import builtins
print(dir(builtins))
# we can see that it returns all of the bulit ins method and attributes here.
# a lot of these are exceptions and error names. if we scroll down we can see some others that are more used to.

# we might accidently overwritting some builtins.
# python dont prevent us from doing this. there are reason for this.
# but basically, they are trusting us with having the power to do that.
# for example, if we create a max function here.

def max():
    pass

# now if we use the max function, then we will get an type error saying max() take 0 positional argument but 1 is given.
#mx = max([3,6,4,5,1])
#print(mx)

# the reason for that is when we run the max() function here,
# python found the max() function in our global scope before it went to the built-in scope.
# so we have to careful with that.

# now lets see the enclosing scope.
# first we need to learn local and global scopes to understand enclosing scope.

# enclosing scope has to do with nested function.
# lets say we have a function we have a function within a function.

def outer():
    x = "outer x"

    def inner():
        x = "inner x"
        print(x) # printing the x within the inner function
    
    inner() # executing the inner function within the outer function.
    print(x) # printing the x within the outer function

# executing the outer function
outer()

# we can see it first prints the inner x from inner function and then it prints the outer x from the outer funtion.

# here what is going on the background?
# we came in the outer function and set the outer x variable which is local to the outer function.
# after that we initialize our inner function and then we execute the inner function.
# within the inner function we set the inner x variable which is local to our inner function and then we print that x variable.
# so it maintains the rule LEGB so it look for the local x variable which is the inner x variable and prints it.
# then we printed outer x variable and it looked if it had any local x variable and it finds the outer x variable and print it.

# now lets comment out when we set our variable in our inner function.
def outer_2():
    z = "outer z"

    def inner_2():
        #z = "inner z"
        print(z)
    
    inner_2() 
    print(z) 

outer_2()

# now if we run this we can see that it prints outer z variable twice.
# this is what the enclosing scope is.
# when we got to the inner fucntion, it first check whether it have any z variable in the local scope to that inner function.
# it doesn't find that variable since we have commented that out.         
# then it checks if it has a z variable in the local scope of any enclosing functions.   
# thats why it is called the enclosing scope. 
# so now we are looking in the local scope of any enclosing functions. 
# our enclosing function in here is the outer function and we do have a z variable in the local scope of the outer function.
# so thats why it printed out outer z.

# it is kind of simmilar to our local and global scope example except now we are inside in a function.
# so same concepts will apply.
# if we set z variable in our inner function it doesn't effect the z variable in the outer function.
# and just like our local and global scope,
# if we comment out the outer z variable and uncommon out the inner z variable,
# if we run that,
def outer_3():
    #p = "outer p"

    def inner_3():
        p = "inner p"
        print(p)
    
    inner_3() 
    #print(p) 

outer_3()
# then first it will print the inner p variable and then it will raise a key error.
# because when we tried to print the p variable outside of the inner_3() function,
# it first check for the local variables of the outer function which currently commented out,
# then it checks the enclosing scope which it doesn't have, then it checks for the global p variable which it doesn't have.
# and we do not have any z variable in the builtins.
# so it give a key error. 

# when we worked with local and global scope variables,
# we learn that we can use global keyword to explicitely tell python that we wanted to work with global variables.
# so we may be wondering if there is a way to do this with the enclosing scope as well?
# and there is a way to do that.

# lets say in our inner_4() function here, we actually wanted to change the k variable of our outer_4() function.
# we shouldnt use global because global will effect global scope.
# in this case we will use the nonlocal statement. 
# this will allow us to work with the local variable of our enclosing functions.
# in this case, it means we are now effecting the outer k variable.

def outer_4():
    k = "outer k"

    def inner_4():
        nonlocal k
        k = "inner k"
        print(k)
    
    inner_4() 
    print(k) 

outer_4()

# if we run this we can see that it run inner k twice.
# because within our inner_4() function we are actually affecting the local k variable of our enclosing function which is outer_4()


# NOTE: nonlocal statement is atually used more that the global statement.
# because nonlocal can be useful in order to change the state of the closures and decorators and things like that.

# now if we use a global scope variable in our code and run that.
j = "global j"

def outer_5():
    j = "outer j"

    def inner_5():
        j = "inner j"
        print(j)
    
    inner_5() 
    print(j) 

outer_5()
print(j)

# if we run that we can see that we are simply setting a j variable in each of this scopes and printing them out.

# now when we learn the LEGB rule, we know what will happen in these types of situation in our code
# and we will be able to overcome them easily.




# Extra NOTE:
# namespace
# it refers to a container that hold objects and the name associated with this objects.
# if we create a variable we will create an element in this name space
x = 3
# it is pretty much like a dictionary which have a key and a value.
# here x is the key to the value 3
# we can see the memory location for object x by id() function.
print(id(x))
# if we look at the memory value for 3 we will see that it is the same id.
print(id(3))
# everything we are assigning here is taking place in the global namespace
# in python there are many different namespaces located in one script.
# when we import a module, we are actually importing that modules namespace into our script.
# if we import pandas
import pandas as pd
print(pd.DataFrame)
DataFrame=3
print(DataFrame)
# here we can work with two different DataFrame object and they didn't collid
# because they are situated in different namespace.
# DataFrame=3 is situated in our global namespace and pd.DataFrame situated in the pandas namespace.
# but we can access them in the same script.
# so we can access to many different namespaces within a single script.
# we also have a local namespace which is situated in a function.
# variables in the function has their own local namespace and it is different from the global namespace.
def my_func():
    x=4
    y=5
    print(x+y)
# we can access the local variables of a function outside of that function.
# there is another type of namespace called built-ins
# that are basically the builtins reserved name for python such as mix, max, class, def etc.


# difference between namespace and scope?

# Namespace:
# It is a naming system for making names unique to avoid the code complexity and ambiguity.
# It is like an abstract container which holds unique identifiers.

# Scope:
# In technical terms, a scope is a region of program where a defined variable 
# can be accessed and beyond that region a variable can not be accessed.

# so scopes are the regions and namespace are the mapping of objects and their names in that perticular region.
# each distinct scope in python is represented using a namespace which is an abstraction.
# a namespace manages all the variables and functions that are currently defined in a given scope.
# we can see the keys which are the names within the namespace by dir method.
print(dir(pd))
# we can see both the keys and the values by vars() method
print(vars(pd))