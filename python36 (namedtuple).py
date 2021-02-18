# namedtuple

# in this module, we will look what is namedtuple? and why we should use them?
# we can think named tuple kind of like a light weight object 
# that works just like a regular tuple but it is more readable.

# what do we mean by this?
# lets say we want to represent RGB color value in code and set a tuple to do this.
color=(55,155,255)
# lets say we want to print out the red value.
print(color[0])
# if someone else come and look at this code or we may read this code weeks or months later.
# here we will read this and we dont know whats going on. what are this numbers in color tuple?
# so it would be really nice if this would be more readable.
# the first idea might popped in our head is to use a dictionary.
# lets see what this look like?
color_dic={"red":55,"green":155,"blue":255}
print(color_dic["red"])
# so what is wrong eith this?
# why shouldnt we use dictionary?
# first of all may be we use tuple for a reason. because tuples are immutable.
# and also dictionary requires a little more typing here.
# if we want to create a new color we need to come in and change the entire dictionary.

# a namedtuple is kind of a good compromise between tuple and the dictionary.
# it has much readability and also offers us with the functionality of a tuple.
# to use namedtuple we need to import it from collectionas module.
from collections import namedtuple

# now lets create a namedtuple.
Color=namedtuple("Color",["red","green","blue"])

# namedtuple take two arguments. first one is typename. it is the name of generated class. 
# generally, the typename is same as the name of the namedtuple name.
# second one is the feild names of the tuple's values in a list.

# when we created a regular tuple, we just did.
color1=(55,155,255)

# now we have to add the tuple name first.
color2=Color(55,155,255)
 
# we can still use this just like a regular tuple. i mean we can just print the value with index.
print(color2[0])

# but we can also print them out by names. we are going to use the names as attributes.
print(color2.red)
# it is a lot more readable than our regular tuple.
# this is a lot less and easier typing as well than our dictionary.

# if we want to be lot more explicit, then we can use the arguments names when we are creating named tuples.
color3=Color(red=23,green=45,blue=78)
# but if we dont do that it will still work.
