# Solving math

# operators in python
# addition +            exp: 5+1=6
# subtaction -          exp: 5-1=4
# multipication *       exp: 5*2=10
# division /            exp: 4/2=2
# floor division //     exp: 3//2=1       # drops the decimal number.
# exponent **           exp: 5**2=25
# modulo %              exp: 5%2=1        # Gives us reminder(vhagshesh).

# we can use brakets in our math programme.

# python follows "BODMAS"/"PEMDAS" rule in case of solving math.
a=2
s=3
# we don't need to add quotes for variable a number.
 
# how to display string and number together(2 methods)-
print("I have %d cats" % 6)# %d-decimal number. if we do not do any math with numbers,they will be decimal numbers.
print("I have {0:d} cats".format(6))# format is a function which insert the value in the statement.
print("I have %3d cats" % 6 )
print("I have {0:3d} cats".format(6))
print("I have %03d cats" % 6) # 03 specify how many numbers will be displayed before the answer.
print("I have {0:03d} cats".format(6))
print("I have %f cats" % 6)# %f-float number. if we do math with numbers they will be float numbers.
print("I have {0:f} cats".format(6))
print("I have %.2f cats" % 6)# .2 specify how many numbers will be displayed after point(.).
print("I have {0:.2f} cats".format(6))

# Using format function to insert multiple values -
print("here is four numbers {0:d}, {1:d}, {2:d}, {3:d}.".format(43,42,81,96))

# we can also use !r for formating the string.
print("I see it in python expert video {!r}".format((1,2,3)))
# !r which stands for represent.
# it is mostly used in the __repr__ method in oop.

# Sometimes commands are too long to fit in a single line. In this cases, we can use a "\" to indicate a command continues on the next line.
#exp-
print("I love playing "+\
      "and coding.")
# if we use "\" between our quotes, it won't work. python will take it as a part of that string. so we must make two strings with adding "+" between them and then place the "\" arter the +.

# how to find the type of different values?
# we can use type method
a=2
print(type(a))

# how to display the absoulate value of a negative number?
# we can use abs function.
print(abs(-3))

# how to round a float value to the nearest integer value?
# we can use round function.
print(round(3.56))
# we can also pass a second argument in the round function.
print(round(3.732, 1))# this means we want to round 1st digit after the decimal.

# we can also use binary, octal and hexadecimal numbers and create them decimal number using int() method.
print(int(0b11011))
print(int(0o52))
print(int(0x7f))

# we can also explicitely tell the base by adding a second argument in the int() method.
print(int("ff7",16))

# to express big integres in scientific way 3.45X10^45 we can use this format.
print(int(3.45e45))


# extra 
# Bitwise operator
# Python provides the following bitwise operators for integers:
      # ∼   bitwise complement (prefix unary operator)
      # &   bitwise and
      # |   bitwise or
      # ˆ   bitwise exclusive-or
      # <<  shift bits left, filling in with zeros
      # >>  shift bits right, filling in with sign bit

