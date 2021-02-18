# decorators

# we have to learn first class function and closures concept first to learn decorators.
# decorators are very simmilar to closures.

# WHAT IS A DECORATOR?
# decorator is a function which take another function as an argument, 
# adds some kind of functionality 
# and then return another function.
# and it does all of these without altering the source code of the original function that we passed in.

def decorator_function(origin_function):
    def wrapper_function(*args,**kwargs):
        print("wrapper executed this before {}".format(origin_function.__name__))
        return origin_function(*args,**kwargs)
    return wrapper_function

def display():
    print("display function ran")

decorated_display=decorator_function(display)
# now this decorated_display variable is equal to our wrapper_function() which is waiting to be executed.

decorated_display()

# now why should we wanted to use decorators?
# decorators allow us to easily add functionality to our original function 
# by adding the functionality inside of our wrapper function.
# so without modifying our original display function here we can add more functionaity in wrapper.

# now, we are using equal to sign to use decorator and create decorated function.
# by in python, we can use @ sign to decorate a function.

@decorator_function
def display2():
    print("display function ran")

# it is the same thing saying
display2=decorator_function(display)

# so any time we use @ sign it means we are executing decorator function to the original function.
# and it is easy to read too.

# ok using the decorators here, this would not work if our originl functions take any arguments here.

@decorator_function
def display_info(name,age):
    print(f"display_info() runs successfully with the arguments {name} and {age}")

# display_info("Shawki",15)
# if we run this we can see that we are getting an error.
# it says: wrapper_function() takes 0 positional arguments but 2 were given

# so we have to need to make our wrapper ready to take any number of positional and keyword arguments.
# we can do this by adding *args and **kwargs to our wrapper_frunction() and our original_function()
display_info("Shawki",15)

# some people like to use classes as decorators instead of using functions as decorators.

class decorator_class(object):# our decorator class is a subclass of object class.object class is the base class of the class hierarchy.
    # when we pass our original function to our decorator function we used that as a argument.
    # we can do that in our class with the __init__ method.
    def __init__(self,origin_function):
        self.origin_function=origin_function
    # lastly, how do we mimik the functionality of the wrapper_function which is adding some functionality to our original function.
    # the way that we are going to do that in our class, we are going to implement the __call__  method.
    # this call method will behave just like our wrapper function behave.
    def __call__(self,*args,**kwargs):
        print("call method executed this before {}".format(self.origin_function.__name__))
        return self.origin_function(*args,**kwargs)
    # now we are using the instance. so everywhere we have used the origin_function we have to use self. before those.

# using decorator class
@decorator_class
def display_info2(name,age):
    print(f"display_info2() runs successfully with the arguments {name} and {age}")

display_info2("Shawki",15)

# thats the two way of creating decorator but functional way is used more often. 
# but decorator class have some extra functionality.

# now we have a basic idea how decorators work.
# now lets look at some practical examples.

# the most common usecase of decorators in python is LOGGING.
# lets say we want to keep track of how many times a specific function runs and what arguments are passed to that function.

def my_logger(orig_func):# here we are passing our original function.
    import logging # importing the logging module
    logging.basicConfig(filename="{}.log".format(orig_func.__name__),level=logging.INFO)# setting up a log file that matches up the name of our original function.

    def wrapper(*args,**kwargs):# here we have our wrapper function, that takes in *args and **kwargs argument.
        logging.info(
            "Run with args: {} and kwargs: {}".format(args,kwargs)# here it runs the logging. info and logs this line.
        )
        return orig_func(*args,**kwargs)# here we run our original function with *args and **kwargs and returning our original function.
    
    return wrapper # lastly we are returning the wrapper function that allows us to run our original function with added functionalities.

@my_logger
def display_info3(name,age):
    print(f"display_info3() runs successfully with the arguments {name} and {age}")

display_info3("Shawki",16)
# now we can reuse the decorator anytime we want to add this new logging functionality to any new function.
# we can imagine that how repetitive and errorful would be
# if we make the logging again and again when we want to add the logging functionality to any function.
# but now the decorator maintain our added functionality in one location and anytime we can apply it anytime we want within our codebase.

# another practical example that people often use decorator for is
# KEEP THE TRACK OF TIMING HOW LONG A FUNCTION RUNS.

def my_timer(original_function): # passing in original function
    import time # importing time module
    def wrapper(*args,**kwargs): # here we have our wrapper function, that takes in *args and **kwargs arguemnet.
        t1=time.time() # calculating the initial time
        result= original_function(*args,**kwargs) # running our original function with the *args and **kwargs and set that to result variable. 
        t2=time.time()-t1 # calculating the runtime
        print("{} ran in: {} sec".format(original_function.__name__,t2)) # printing the runtime and the function name.
        return result # print the result of the function
    return wrapper # returning wrapper function

# now lets use that decorator to the same example that we used before.
@my_timer
def display_info4(name,age):
    import time
    time.sleep(2) # to ensure that it take a long time
    print(f"display_info4() runs successfully with the arguments {name} and {age}")

display_info4("Shawki",15)
 

# lets look at another example.
# here we are going to combine two of our decorators that we have here.
# what if we want to apply two decorators to a single function.
# its just easy to stacking the decorators one of each other.

def my_logger2(orig_func):
    import logging
    logging.basicConfig(filename="{}.log".format(orig_func.__name__),level=logging.INFO)

    def wrapper(*args,**kwargs):
        logging.info(
            "Run with args: {} and kwargs: {}".format(args,kwargs)
        )
        return orig_func(*args,**kwargs)
    
    return wrapper

def my_timer2(original_function):
    import time

    def wrapper(*args,**kwargs):
        t1=time.time()
        result= original_function(*args,**kwargs)
        t2=time.time()-t1
        print("{} ran in: {} sec".format(original_function.__name__,t2))
        return result
        
    return wrapper

@my_timer2
@my_logger2
def display_info5(name,age):
    import time
    time.sleep(2)
    print(f"display_info5() runs successfully with the arguments {name} and {age}")

display_info5("Shawki",15)
# we can see that it is giving us an unexpected result.
# it is saying wrapper ran in: 2.. sec
# but we expected display_info5() instead of wrapper.
# but our log file is created correctly

# but if we switch the order 
@my_logger2
@my_timer2
def display_info6(name,age):
    import time
    time.sleep(2)
    print(f"display_info6() runs successfully with the arguments {name} and {age}")

display_info6("Shawki",15)
# now we can see that it is giving us the expected result.
# but now it is creating a wrapper log file instead of display_info6() log file.
# so what is going on here?

# when we use my_logger before my_timer, it means
#display_info6=my_logger2(my_timer2(display_info6))

# when we use my_timer before my_logger, it means
#display_info6=my_timer2(my_logger2(display_info6))

# so the lower() functions are running first then the upper function.

# now lets step through this.
# first case
# we are running my_timer() first.
# my_timer() uses wrapper for adding timing functionality to our original function.
# prints out the function name and the time it took to the terminal,
# and at the end our original function is replaced with the wrapper function when we return the wrapper function.
# we can see that by __name__ method.
def display_info7(name,age):
    import time
    time.sleep(2)
    print(f"display_info7() runs successfully with the arguments {name} and {age}")
display_info7=my_timer2(display_info7)
print(display_info7.__name__)
# we can see the name is wrapper.
# because we passing our original function to my_timer()
# and my_timer() returning the wrapper.
# this isn't a big deal for our previous case.
# but now we are passing the wrapper function into our my_logger() and it is creating the log file with function name.
# and the function name is wrapper.

# and the same thing goes whenever we switch the order of those decorators.
# so how do we fix something like this?
# it is always a good idea to preserve the information of our original function whenever we use decorators.
# and we can preserve the information using the functools library and the wraps decorator.
from functools import wraps
# this going to be liitle confusing because we are going to use a decorator inside a decorator.
# but it is really not that bad after we get used to it.
# all we have to do is to decorate all of our wrappers with the wraps decorator.

def my_logger3(orig_func):
    import logging
    logging.basicConfig(filename="{}.log".format(orig_func.__name__),level=logging.INFO)

    @wraps(orig_func) # we want to wrap the orig_function
    def wrapper(*args,**kwargs):
        logging.info(
            "Run with args: {} and kwargs: {}".format(args,kwargs)
        )
        return orig_func(*args,**kwargs)
    
    return wrapper

def my_timer3(original_function):
    import time

    @wraps(original_function)
    def wrapper(*args,**kwargs):
        t1=time.time()
        result= original_function(*args,**kwargs)
        t2=time.time()-t1
        print("{} ran in: {} sec".format(original_function.__name__,t2))
        return result
        
    return wrapper

# now if we print the name,
def display_info8(name,age):
    import time
    time.sleep(2)
    print(f"display_info8() runs successfully with the arguments {name} and {age}")
display_info8=my_timer3(display_info8)
print(display_info8.__name__)
# we can see that it is no longer printing wrapper, it is giving us the name of our original function.
# now if we run our stacked decorators again, that will work fine.

# decorators are used lot in python and third party library.
# they are used for class property, web framework and all other stuffs.
# the most confusing thing about decorators is trying to keep track of 
# outer functions, original fuctions, wrappers all that kind of stuff.
