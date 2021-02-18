# extra
# decorators with arguments

# it is a very important concept that we will see time to time.
# for example, if we see the hello world application from the flask website,
# we can see here, that there routes are defined with the app.route decorator.
# and the string get passed in is the url path.

# here we have very simple decorator here.
# here we have display_info() function here which take two arguments name and age.
# and it is decorated by the decorator_function.

def prefix_decorator(prefix):
    def decorator_function(original_function):# it takes original function as an argument.
        def wrapper_function(*args,**kwargs):# this wrapper function takes *args and **kwargs function.
            print(prefix,"Executed Before", original_function.__name__)# here we have the line before execution of our original func.
            result=original_function(*args,**kwargs)# executing the original function and saving it to a variable named result.
            print(prefix,"Executed After", original_function.__name__,"\n")# printing another line after execution of original function.
            return result # returning the result we got from the original function
        return wrapper_function # returning the wrapper function.
    return decorator_function

#@decorator_function
@prefix_decorator("TESTING:")
def display_info(name,age):
    print("display_info ran with arguments ({},{})".format(name,age))

display_info("Shawki",15)
display_info("Corey",28)

# now lets get our decorator_function to except arguments.
# lets say we want to add a customizable preffix to all of this print statement within the wrapper.
# we can think of the argument that we passed in that would be the prefix.
# in order to do this we need to add another outer layer to our decorator.
# we are going to call it prefix_decorator() function. and it will take an prefix as an argument.
# WARNING: this will be going to more harder to keep an track whats going on as there are nested over nested over...

# now everything in the decorator has an access to the prefix argument.
# we can add this before our printed line.

# now because of it is nested another level, we have to do another return and we will return our decorator_function unexecuted.
# now to use the decorator we need to use the outsidest function which is prefix_decorator.
# let us comment out our previous code. 
# now we can pass in our arguments here.
# we can change the arguments anytime we want.