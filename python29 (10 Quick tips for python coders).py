# 10 quick tips for python coders.

# tip 1
# turnery operator/conditional
condition=True
x=1 if condition else 0
print(x)
# this one line of code is easy to read and understand as the if-else statement.

# tip 2
# working with large number
# we can use underscore(_) when we are working with large numbers. it doesn't effect our code.
# it is easy to count and error free.
num1=10_000_000_000
num2=100_000_000
ans=num1+num2
print(ans)
# but the uotput still doesn't have separators. So it is still hard to count the output.
# we can include separators to our output by using string formatting in f string.
print(f"{ans:,}")# here we are using colon and comma.

# tip 3
# opening and closing the file
# any time we are manually managing resources of something where we have to remember to manually close the file.
# sometimes something goes on our head that there are some easier way to do that. 
# This is called a "Code smell". it means some code which doesn't smells right or looks right even it doesn't pop out immidiately.
# so anytime we need to open or close a file we should use context manager instead of opening and closing it manually.
# context managger manage resources for us so that we dont need to remember to manage them ourselves.
# it is not only useful for files, we can use it anytime when we are setting up and terring down something.
# for example, if we are working with threads and manually acquiring and releasing looks,
# then we should use a context manager to do that for us.
# if we arae opening and closing database connections manually, then we can also look into context manager.
# so we need to train ourselve to notice that when we actually need a context manager.
# and to notice when we should pass the resource handling to be done automatically instead of doing manually.

# tip 4
# enumerate function
# we should use a enumerate function when we need a counter while we looping over something.
names=["Shawki","Arko","Munsha","Abir"]
index=0
for name in names:
    print(index,name)
    index+=1
# lots of beginners print their index by this and it works too. but this is not great.
# we can use enumerate function to print out those indexes.
for index,name in enumerate(names,start=1):
    print(index,name)
# so enumerate is a function which returns both the indexes and the values from the list that we are looping over.
# and we can use unpacking to grab this values by index,name.
# we can also pass in a start value by adding start argument, if we dont want to start counting from 0.

# tip 5
# recognizing all functions correctly.
# people often use bad code because of they dont know about any function existance.
# sometimes we need to loop over two lists at a time.
names=["Peter Parker","Clark Kent","Wade Wilson","Bruce Wayne"]
heroes=["Spiderman","Superman","Deadpool","Batman"]
# this to list is correspond to each other.
for index,name in enumerate(names):
    hero=heroes[index]
    print(f"{hero} is actually {name}!")
# this actually works but it not actually intuitive.
# the way to do something in python is to use the zip function.
# zip does actually what we are wnting here. it allows us to loop over two list at once.
# it gives us both values from both list. we need to unpack it from the beginning.
for name,hero in zip(names,heroes):
    print(f"{hero} is actually {name}!")
# its a bit more cleaner than before and we dont have to do anything claver to grab values from both list.
# even we can combine more than two lists using zip.
universes=["Marvel","DC","Marvel","DC"]
for name,hero,uni in zip(names,heroes,universes):
    print(f"{hero} is actually {name} from {uni}!")
# so using zip is definately a handy trick to know to clean our code up a bit it certain situation.
# in this case all of our list is of same length.
# if we use different lists of different lengths then our zip will stop after the shortest possible list is exhausted.
# if we want to go to the end up to the longest list, then we have to use the zip_longest function from itertools library.

# tip 6
# unpacking
# we have already done this in this module.
# we have done unpacking when we called for name,hero,uni.

# there zip is actuallyr eturning a tuple of three items and we are unpacking that.
# we could just access to that single tuple if we wanted.
for tup in zip(names,heroes,universes):
    print(tup)

# now lets us look to unpacking in details
item=(1,2)
a,b=item
print(a)
print(b)
# now if we only want to use the a variable not the b variable, then the b variable is called an unused variable.
# if we have the code leaning turned on then python will give us an error saying-
# "hey you just made an variable but why are you not using it" or something like that.
# any time we want to ignore a variable in python the convention is to use _ as the variable name.
c,_=(3,4)
print(c)
# the convention of using _ as a variable name is basically telling python and anyone else who is reading our code
# that we are not planning to use that variable in anywhere else in our code.
# what if that we want to unpack doesn't contains as much values that we want to set?
# then we are getting an ValueError: "not enough values to unpack"
# what if we get more values than variables.
# we are still getting an ValueError: "too many values to unpack"
# what if we want to make a and b equal to 1 and to and convert c to a list of the rest of the additional values?
# we can do that by adding a * before see which tells python that
a,b,*c=(1,2,3,4,5)
print(a)
print(b)
print(c)
# if we want to ignore c we can use _ instead of that.
a,b,*_=(1,2,3,4,5)
print(a)
print(b)
# there are some more advance thing that we can do with unpacking.
# we can also use same syntax with an additional variable added in to the end.
a,b,*c,d=(1,2,3,4,5)
print(a)
print(b)
print(c)# what will be c's value? it will be everything from b upto d but not including b and d.
print(d)# what will be d's value? it will set to the  last value which is 5
# as usual if we want to ignore those values we can still do that with _
a,b,*_,d=(1,2,3,4,5,6,7,8)
print(a)
print(b)
print(d)
# we can also use _ in multiple places if we want to ignore multiple values.

# tip 7
# getting and setting attributes on certain object.
# we have an empty class here and an object for that class.
# we can dynamicly can add values and attributes to this objects.
class Person:
    pass

person1=Person()
person1.first="Corey"
person1.last="Shcafer"
print(person1.first)
print(person1.last)
# when we print those attributes, that looks good.
# but what if the attributes that we want to set is the value of another variable values?
# it means something like this.
first_key="first"
first_val="Ahammad"
# lets say we want to take the value of the first_key variable and use that as an attribute for our object.
# and we want to set that value to our first attribute.
# actually we want to do the exact same that we print before but instead of doing that dynamically we want to do that manually.
# we can do something like that-
person1.first_key=first_val # because it will then create an attribute of first_key not first. thats not we want.
# to order to do this we need to use a built_in function called setattr().
# setattr() is able to use a value of a variable.
setattr(person1,"first","Ahammad")
# here the first argument is the object.
# the second argument is the attrinute name.
# the third argument is the value of that attribute.
print(person1.first)
# that runs well.
# setatter() function allows us to use variable instead of the exact value.
last_key="last"
last_val="Shawki"
setattr(person1,last_key,last_val)
print(person1.last)

# Again if we want to get a value, we can use getatter() at a same way.
# if we want to get this last attribute here using that variable instead.
last=getattr(person1,last_key)
# here the first argument is the object name and the second is what we want to get.
# now if we run that-
print(last)
# but we might not see the usefulness in this but it is good to know because sometime we many need this.
person1_info={"first":"Christiano","last":"Ronaldo"}
# lets add those key and values of dictionaries to our object attributes
for keys,values in person1_info.items():# we need to use the items() method when we loop over dictionaries.
    setattr(person1,keys,values)
print(person1.first)
print(person1.last)
# if we dont have setattr() that might be of probably more time that we think.
# now if we wanted to print those attributes in a loop as well, then we can do something like this.
# so instead of printing that out we can use those keys.
for key in person1_info.keys():
    print(getattr(person1,key))

# tip 8
# inputting secret information
# we should keep sensative information in environment variables.
# what if we need to type in a password for our script?
# in order to do this python have a built_in function that will help us out.
# and that function called getpass from getpass module.
# but first look at the wrong way to do this?
username=input("Username: ")
password=input("Password: ")
print("logging you in ...........")
# when we run this code, we could see when we input our password that typed down in our screen which we definately dont want.
# if we are using our program in front of others, we simply dont want that to display that in the screen for everyone to see.
# python has a built_in module called getpass for this type of secret operation.
from getpass import getpass
# and now instead of using input in our password line here, we need to use getpass.
username=input("Username: ")
password=getpass("Password: ")
print("logging you in ...........")
# now we can see that there is a lock sign when we are typing our passwod.
# and when we are done we cant find any passworb in the terminal.
# thats a lot more secure if we want to accept password form a user. 

# tip 9
# running python with -m option.

# what does the -m option do?
# when we create a virtual environment with venv we do something like this
# python -m venv env_name
# or sending email in python, we need  to debug it first. we can do that something like that.
# python -m smtpd -c DebuggingServer -n localhost:1025
# if we run that, it will run a debug mail server.
# if we look at the python documentation then the official explanation is that-
# -m will quote search sys.path for the name to module and execute its content as the main module.
# basically it is saying that it is simply running that specific module that we specified after -m. so in that case the module will be smtpd.
# and everything after that is the argument for that module.
# but we might be wondering why we dont run those scripts like other python scripts that we write in our code?
# when we use our script in the command prompt we do something like this- python script_name.py
# we can do that because they exists in our current directory.
# other scripts dont exists in our current directory. so we cant run them like this.
# if we wanted to we could run our own script in that style as well.
# python -m script_name. here we dont have to use .py because we just need to write the module name.
# so just like the documentation said when we use -m it will search in our sys.path and impoet that module.
# now we also may wonder which arguments the code after -m takes?
# in this example, the smtpd module takes an argument of -c and -n
# now how would we know that?
# if we run that module with -m, it also means we can import that module becausse we can import anything in our sys.path.
# so if we want to learn more about that module, we can import it and further look at it.

# tip 10
# learning more about certain objects using built_in functions.
# in this case, we can import the smtpd module and learn more about it using help function.
import smtpd
print(help(smtpd))
# we can see their there is a section called options
# their we can find all the arguments and what they do.
# so anytime we see such arguments in any module that we dont know what to do with that,
# we can just print it with our help function.
# Actually, just knowing how the things work and all the operations that they can do will take us a long way in they coding world.
# actually big programmers whom seen to know all about programming, 
# they not really know anythong about it, they just know hoe to find all the informations quicly and easily.
# we can also print out only the attributes and methods which are available to us using dir() function.
print(dir(smtpd))
# if we know whetther something is an attribute or a method we can simply inspect that further. 
from datetime import datetime
print(datetime.today)
# thats how we can get more information about anything in python wshich will be very useful for us in future.
