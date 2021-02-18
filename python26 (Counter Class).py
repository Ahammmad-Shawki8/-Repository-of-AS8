# Counter Class

# In different programming problems, sometimes we have to keep a count of different items in our list.
# this is pretty easy while working with small data.
# but people have to do a lot of code while doing the same thing with large data.
# But this is so common and Python has a built in class for this kind of things which is called "Counter".

# counter class situated in collections standard library.
# first we need to import that.
from collections import Counter
# now we have a counter class.
# lets create an object c for that class.
c=Counter(["python", "javascript", "c#"]) # here we need to pass a list here.
print(c)
# now if we look at the counter we can see that it said that it have a counter here which is a dictionary.
# in that it have a key "python" which is set to 1 as there is only one time python in our list and so on.
# so it is keeping count how often it sees those values.
# we can also update this counter with update method.
c.update(["python", "c++","html/css"])
print(c)
# now we can see that python has set to 2 because it has seen python twice. Other keys are set to 1.
c.update(["python", "c++","html/css"])
print(c)
# but sometimes there are lots of keys while we are working with big data.
# so we may not have to acces all the keys. we may need to know only the mos common 10 keys or three keys.
# we can do that most_common method in Conter class.
print(c.most_common(3)) # it takes one argument which is how many keys we want to display.
# this method gives us a list with paired tuples which first item is the key and second item is the value of the key.

# So it can be said that, its definately the best way and extreamly helpful to do something like this with counter.
