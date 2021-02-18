# lambda expression

# lambda expression is a special kind of function which doesnt have any name.
# it is also called anonymous function.
# lambda expression always return the value, it doesnt print it.
# we can not use use lambda expression for multiline function. 
# we use lambda expression for temporary use only.

def f(x):
    return 3*x+1
print(f(2)) 

# to crate a lambda expression we need to write the keyword lambda.
lambda x:3*x+1    # the code after the colon is the expression.It is actually the return value of our anonymous function.
# but we cannot call it as it doesnt have a name.
# so we can-
g=lambda x:3*x+1
print(g(2))


# lambda expression for multiple inputs.
fullname=lambda first,last:first.strip().title()+ " " +last.strip().title()
print(fullname("     ahammad  ","   shawki              "))

#building a quadratic function with lambda expression.
def built_quadratic_function(a, b,c ):
    return lambda x:a*x**2+b*x+c # the function will return a lambda expression which is also a function.
f=built_quadratic_function(2,3,-5)#here the parametres are the value of respectively a, b, c.
print(f(0))#here 0 is the value of x
print(f(1))
print(f(2))  

# we can also use lambda as a argument in other functions.
# sorting tuples using lambda.
list1=[("eggs",1.09),("mango",0.44),("banana",3.89),("milk",8.90)]
list1.sort(key=lambda x:x[0])#here in the expression,x[0] means we want to sort them in the order of keys 
print(list1)
# instead of keys we can sort them by values.
list1.sort(key=lambda x:x[1])
print(list1)

# sorting dictionaries using lambda.
list1 = [{'make':'Ford', 'model':'Focus', 'year':2013}, {'make':'Tesla', 'model':'X', 'year':1999}, {'make':'Mercedes', 'model':'C350E', 'year':2008}]
list2 = sorted(list1,key=lambda x:x["year"])#here we need to use the key name instead of its index.
print(list2)# here we are using sorted function

# we can use lambda in map functions too.
list_square=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x:x**2,list_square)))

# conditionals in lambda
# the structure of lambda argument is-
"""lambda args(argument):a if boolean_expression else b"""
starts_with_A=lambda x:True if x.startswith("A") else False
print(starts_with_A("Ahammad"))

# we want to print the word before of the given word in our sentence.
word_before=lambda s , w:s.split()[s.split().index(w)-1] if w in s else None
sentence="hello! i am shawki."
print(word_before(sentence,"am"))

#do something function
def do_something(func,val):
    return func(val)
print(do_something(lambda x:x*4,45))

# extreame lambdas
# this is probably complex.
# we shouldn't do this with lambdas very often.
# sometimes using general functions is good.
# this only tells us what can be done with lambdas.

# we can see if it is a integer or not by isdigit function.
print("445".isdigit())

# what if we want to know if it is a number or not?
# we can use lamdas
isnumber=lambda q:q.replace(".","",1).isdigit()# here the third argument indicates that the replace command will only executes one time.
print(isnumber("233.45"))
#but thats not good enough it returns false if it is a negative number.
print(isnumber("-233.45"))
is_num=lambda x:isnumber(x[1:]) if x[0]=="-" else isnumber(x)
print(is_num("233.45"))
# converting to num
to_num=lambda s:float(s) if is_num(s) else -1
print(to_num("456f56"))
print(to_num("-233.45"),type(to_num("-233.45")))