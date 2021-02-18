# Array

# array ia simmilar with lists in python.
# it is another datatype where we can store multiple values and work with them.
# arrays are two types: single dimentional and multi dimentional.
# in genral arrays of python, we can work only with the single dimentional array.
# now, general arrays in python dont used often as they are pretty simmilar to list
# again, list have much functionality than python arrays.
# but we have numpy arrays which are really useful.
# in fact, they are the backbone of scientific operation in python.
# we will learn working them in numpy module.
# but now lets see the general arrays in python.

# first we have to import array library in python.
import array as arr

# lets see all the method and attributes we have in array library.
print(dir(arr.array))

# to make an array we can use the array() method.
a=arr.array("i",[9,3,4,5])
# array() takes 2 arguments.
# first one in typecode. there are different type codes for different datatypes.
# second one is the values. we have to pass the values in a list.
print(a)

# different typecodes:
# typecode      ctype          python_type     min. size in bytes
#----------    -------        -------------   --------------------
# "b"         signed char          int               1
# "B"         unsigned char        int               1
# "u"         py_UNICODE     Unicode character       2
# "h"         signed short         int               2
# "H"         unsigned short       int               2
# "i"         signed int           int               2
# "I"         unsigned int         int               2
# "l"         signed long          int               4
# "L"         unsigned long        int               4
# "f"         float               float              4
# "d"         double              float              8

# note that:
# a list can contain different types of data at a time.
# but an array contains only a certain type of data at a time.
# that means we cannot mix string, int or float in a single array.

# find the size of an array.
# we can use the buffer_info() method.
print(a.buffer_info())
# it will give us 2 values in a tuple.
# the first one is the id or the address of the array.
# second one is the size of that array, it means the number of values that the array contains.

# print the typecode
# we can print the typecode of an array by typecode attribute.
print(a.typecode)

# reverse the array
# we can reverse the array with reverse() method.
a.reverse()
print(a)

# grab single element
# we can grab elements from the array just like a list.
print(a[2])
# we can use slicing
print(a[2:])
# we can iterate over the array too.
for e in a:
    print(e)

# copying array.
# we can copy the array and create a new array too.
new_a=arr.array(a.typecode,[x for x in a])
# here we are using the typecode of a and a list comprehension.
print(new_a)

# appending values
# we can use the append() function.
b=arr.array("i",[])
b.append(3)
b.append(4)
b.append(7)
print(b)
# we can also use the insert() method to insert values to an array with certain index.
b.insert(0,6)
# here we have to pass two arguments.
# first one is the index
# second one is the value.
# insert doesnt delete any values it just shift other values.
print(b)

# removing values
# we can use the remove(), pop() or del function.
b.remove(7)
print(b)
popped=b.pop(0)
# note that, pop() takes the index of the value as an argument.
print(b)
print(popped)
del b[0]
# note that, del takes the index of the value as an argument.
print(b)

# indexing
# we can know the index of differnt values by index() method.
a=arr.array("i",[0,3,5,6,9,4,3])
print(a.index(9))
print(a.index(3))

# find the number of any certain value
# we can use the count() method
print(a.count(3))

# find the lenth of an array.
# we can use the len() method.
print(len(a))
