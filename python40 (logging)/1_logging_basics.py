# logging basics

# we can do lots of things in logging in python.
# in this module we will learn how to get started with logging by replacing print statements to log statements.
# we will also set different log levels and also log information to file.

# we should use log whenever we need it.
# python comes with a logging module built_in. so there is no need to install anything extra.
# having good logging in place will allow us to look at behaviour and errors over time and give us a better overall picture about whats going on.
# we can also pipe in some visualization software for better prespective.

# we have some very simple function.
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

n1=10
n2=5

add_result=add(n1,n2)
print(f"add: {n1} + {n2} = {add_result}")

sub_result=sub(n1,n2)
print(f"sub: {n1} - {n2} = {sub_result}")

mul_result=mul(n1,n2)
print(f"mul: {n1} * {n2} = {mul_result}")

div_result=div(n1,n2)
print(f"div: {n1} / {n2} = {div_result}")

# here we have some print statement commented out.
# if we run it as it is it run successfully with no errors
# but we dont know if it did all thing correctly or not.
# in order to ensure that lets uncommon out the print statements and run this again.
# we can see that every thing is correct.
# this is probably how lots of checkers work as we go


# but instead of using print statement lets just add some very basic logging into this script.
# first of all we have to import this.
import logging

# before we log anything out lets learn about "logging levels".
# logging levels allows us to specify what exactly we want to log by separating this into catagories.
# there are five standerd logging levels. these are:
    # 1. debug
        # detailed information, typically of interest only when diagnosis problems.
    # 2. info
        # confirmation that things are working expected.
    # 3. warning
        # an indication that something unexpected happened, or indicative of some problem in the near future (e.g. disk space low)
        # the software is still working as expected.
    # 4. error
        # due to a more serious problem, the software has not been able to perform some function.
    # 5. critical
        # a serious error, indicating that the problem itself maybe unable to continue running.
# source: python docs

# the default level for logging is set to warning.
# that means it will capture everything that is warning or above.
# so by default, it will run warning, error, and critical and ignore debug and info.

# lets say we want to turn our print staments into logging.debug() statement.
n1=20
n2=2

add_result=add(n1,n2)
logging.debug(f"add: {n1} + {n2} = {add_result}")

sub_result=sub(n1,n2)
logging.debug(f"sub: {n1} - {n2} = {sub_result}")

mul_result=mul(n1,n2)
logging.debug(f"mul: {n1} * {n2} = {mul_result}")

div_result=div(n1,n2)
logging.debug(f"div: {n1} / {n2} = {div_result}")

# this logging statements just log them to the console or terminal.
# so right now, it is very simmilar to our print statement functionality.
# if we run this we can see that it doesn't print anything.
# thats because the default logging level is warning. so it will ignore debug and info.

# lets just change the debug() to warning and run that.
add_result=add(n1,n2)
logging.warning(f"add: {n1} + {n2} = {add_result}")

sub_result=sub(n1,n2)
logging.warning(f"sub: {n1} - {n2} = {sub_result}")

mul_result=mul(n1,n2)
logging.warning(f"mul: {n1} * {n2} = {mul_result}")

div_result=div(n1,n2)
logging.warning(f"div: {n1} / {n2} = {div_result}")

# now we can see we get some output to our console.
# this has a little more information than our print function.
# it tells us the logging level(warning) and also has the root and then we have the message.

# but we want to log this lines either debug or info.
# so we need to change our logging level.
# so we are going to change some basic configuration using basicConfig() method.
logging.basicConfig(level=logging.DEBUG)
# here we have to set the level to logging.DEBUG
# note that here DEBUG is upper case. it is different than debug() method.
# it is a constant that is a integer in the background.
# this constants just increment by 10.
# so DEBUG=10, INFO=20, WARNING=30, ERROR=40, CRITICAL=50.

# now lets change all of our warning() back to debug().
add_result=add(n1,n2)
logging.debug(f"add: {n1} + {n2} = {add_result}")

sub_result=sub(n1,n2)
logging.debug(f"sub: {n1} - {n2} = {sub_result}")

mul_result=mul(n1,n2)
logging.debug(f"mul: {n1} * {n2} = {mul_result}")

div_result=div(n1,n2)
logging.debug(f"div: {n1} / {n2} = {div_result}")
# now we can see that it is printing our debug() statement to the console.
# this is so far so good.

# but we want to see actual log files.
# log files are great way to capture information because it allows us to see our log information over time into one place.
# so instead of logging this message into console, lets just create a log file.

# it is as easy to specify a file in our basicConfig() method.
logging.basicConfig(filename="Basics_Log.log", level=logging.DEBUG)
# so the keyword we are going to use here is filename and set that equal to our filename.

# lets run this again.
add_result=add(n1,n2)
logging.debug(f"add: {n1} + {n2} = {add_result}")

sub_result=sub(n1,n2)
logging.debug(f"sub: {n1} - {n2} = {sub_result}")

mul_result=mul(n1,n2)
logging.debug(f"mul: {n1} * {n2} = {mul_result}")

div_result=div(n1,n2)
logging.debug(f"div: {n1} / {n2} = {div_result}")

# nothing showed here in our console, but we have loggignB.log file.
# and it log all the information from our script.
# now lets change the number and run this again.
# now we can see it has our previous value as well as our latest values.

# one more thing we will learn is how to change the format.
# by the format it means in our log file we have the log level and logger root and the message there.
# now to change the format within our log we need to add some special values to our basic config.
# there are lot of special values available to us. we can see that in this link:
"""https://docs.python.org/3/library/logging.html#logrecords-attributes"""

# lets say we want to change our logging format to time and level name and the message.
logging.basicConfig(filename="Basics_Log.log", level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")
# here we need to add another argument which is format.

# now if we run our logging commands again.
add_result=add(n1,n2)
logging.debug(f"add: {n1} + {n2} = {add_result}")

sub_result=sub(n1,n2)
logging.debug(f"sub: {n1} - {n2} = {sub_result}")

mul_result=mul(n1,n2)
logging.debug(f"mul: {n1} * {n2} = {mul_result}")

div_result=div(n1,n2)
logging.debug(f"div: {n1} / {n2} = {div_result}")
# now we can see that the format in our log file has changed.

# Example:
# now lets look at another module and add some logging.

import logging
logging.basicConfig(filename="Basics_Emp.log",level= logging.INFO, format="%(levelname)s:%(message)s")

class Employee: # here we have a small Employee class
    def __init__(self,first,last):
        self.first=first
        self.last=last

        logging.info("Created Employee: {} - {}".format(self.fullname,self.email)) 
        # here we are printing out that we have crated a new employee.

    @property
    def fullname(self):
        return "{} {}".format(self.first,self.last)

    @property
    def email(self):
        return f"{self.first}{self.last}@email.com"

emp1=Employee("Ahammad","Shawki")
emp2=Employee("John","Dalton")
emp3=Employee("Carl","Goog")

# if we run this we can see it tells us that we created three employees.
# now lets go ahead and add some logging.
# now lets import logging and add basicConfig and the change our print function to logign.info() function.
# now if we run this we can see it doesn't print anything in console, intead of that we have a Employee.log file.


# for small applications logging like this will be a good start.
# but there are some issues that we can run into when we are importing our other modules.
# because they all try to share same logger.
# so in next module, we will learn how to create multiple loggers and add handlers and formatters to that loggers
# and also how we can log infomartion to multiple locations.

""" go to 2_logging_advanced.py """