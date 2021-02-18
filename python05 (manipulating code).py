# manipulate the contents of variables.

# lower, upper, swapcase are different string functions.

message="Hello world"
print(message.swapcase()) # change cases.
print(message.lower()) # all letter is in lower case.
print(message.upper()) # all letter is in upper case.
print(message.capitalize()) # capitalize the first letter of the sentence.
print(message.title()) # capitalize the first letter of every word in the string.
print(message.replace("Hello","hi") )# replace the word after comma to the place of the word before comma.
print(message.find("world")) # returns the index starting at the leftmost ccurance of the string, else -1
print(message.index("world")) # simmlar to find but raise ValueError if not found 
print(message.rfind("world")) # returns the index starting at the rightmost ccurance of the string, else -1
print(message.rindex("world")) # simmlar to rfind but raise ValueError if not found 
# the number which comes to the output means the characters before the word is that number.
# we can also tell python where to start and where to end. they are going to be the 2nd and 3rd argument.
print(message.find("l",4,-1))
print(message.count("o")) # count the number of the letter.
print("       dhaka        ".strip()) # ignore the blank space.
print("       dhaka        ".rstrip()) # ignore the blank space of right side.
print("       dhaka        ".lstrip()) # ignore the blank space of left side.
# we can also use specific character to remove by adding another argument in those above 3 methods.
print("kkkkkkkkkkkkkk foo kkkkkkkkkkkkkk".strip("k"))
print(message.center(100)) # returns the string at the center of 100 spaces.
print(message.ljust(100)) # returns the string before center of 100 spaces.
print(message.rjust(100)) # returns the string after center of 100 spaces.
print(message.zfill(30))  # return the string after 30 zeroes
print(message.startswith("H")) # gives a boolean. if a string starts with the character or not.
print(message.endswith("d")) # gives a boolean. if a string ends with the character or not.
print("    ".isspace()) # returns True if all the characters are whitespace
print("abcghja".isalpha()) # returns True if all the characters are alphabet
print("THIS".isupper()) # returns True if all characters are uppercase
print("this".islower()) # returns True if all characters are lowercase
print("1234567890".isdigit()) # returns True if all characters of nonempty strings are 0-9
print("gh67".isalnum()) # returns True if all the characters either alphabetic or numeric



# Example-
name=input("what is your name?")
country=input("which country do you live in?")
country=country.upper()
print(name+" lives in "+country+".")

# when we write down a function we can watch a pop up list. that's called intelliSense.
# Visual Studio will suggest possible functions we can call automically after we type any word.
# we can also press ctrl+space to launch intelliSense.

# programmers do not memorize all functions.
# so how do programmers find them when they need them?-
# 1.intellisense, 2.documentation, 3.internet searches.

# Challange 2
# solution-
name=input("what is your name?\n")
age=input("how old are you?\n")
place=input("where do you live in?\n")
yourclass=input("which class do you read in?\n")
pastime1=input("what is your favourite pastime?\n")
pastime2=input("write down your another favourite pastime.\n") 

print("I am "+name.capitalize()+"."+" I am "+age+" years old."+" My present address is "+place.capitalize()+"."+" I am a student of class "+yourclass+"."+" I like "+pastime1+" and "+pastime2+" during my leisure time.")
