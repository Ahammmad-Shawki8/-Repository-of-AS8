# reading from file

# how do we read the file content?
# use the read method
name="ReadAge.csv"
with open(name,"w") as files:
    files.write("Essam,14\n")
    files.write("Heyam,14\n")
    files.write("rajib,34\n")
    files.write("manik,75")
with open(name,"r") as bubble:
    filecontent=bubble.read()
    print(filecontent)
print()

# if we prefer we can read oneline at a time.
# use the readline method
with open(name,"r") as bubble:
    filecontentsInALine=bubble.readline()
    print(filecontentsInALine)  
# everytime we use this method we print the next line of a file.
    print(bubble.readline())
# this prints pretty awkward. it gives extra newline after each line.
# its a default system.
# we can change it through changing the end argument.
    print(bubble.readline(),end="")
    print(bubble.readline())
print()

# we can print all the contents of a file in a list by readlines method.
with open(name,"r") as bubble:
    print(bubble.readlines())
print()

# we can also iterate over the contents in a file by using a loop.
with open(name,"r") as bubble:
    for lines in bubble:
        print(lines,end="")
print("\n")

# with read method we can specify how many characters we want to print.
with open(name,"r") as bubble:
    filecontent=bubble.read(20)
    print(filecontent,end="")
# it means print first 20 characters of our file instead of printing the whole file.
# if we run it again-
    filecontent=bubble.read(20)
    print(filecontent)
# it will run from there where it stopped earliar.
# if we reach the end of the file read method will return an empty string.
# so it does not matter to do the action another time.
    filecontent=bubble.read(20)
    print(filecontent) 

# we can use this tecnic in order to read a large file.
# it is called "chunk" tecnic.
# if we dont know how long the file would be we are going to use some kind of loop that will iterate over small chunks at a time.
with open(name,"r") as bubble:
    size_to_read=(3)
    filecontent=bubble.read(size_to_read)
    while len(filecontent) > 0:# because when the file ended the read method give us a empty string and the loop will auto stop.
        print(filecontent,end="")
        filecontent=bubble.read(size_to_read)
print()
print()
# when we are reading this file it changes its position every time.
# we can see its current position through tell function.
with open(name,"r") as bubble:
    size_to_read=(3)
    filecontent=bubble.read(size_to_read)
    print(bubble.tell())
# it tells us that we are currently 3 position of our file that because we enter the size_to_read 3.
print()

# we can manipulate our current position using seek method.
# seek method change our current position to given position.
with open(name,"r") as bubble:
    size_to_read=(7)
    filecontent=bubble.read(size_to_read)
    print(filecontent,end="")
    bubble.seek(0)
    filecontent=bubble.read(size_to_read)
    print(filecontent,end="")
# as we are seeking our file to the position 0, the second time when we read it will start from beginning.
    
# extra credit 1
# copy a file
with open("equipment.txt","r") as rf:
    file_contents=rf.read()
with open("equipment_copy.txt","w") as wf:
    wf.write(file_contents)
#or-
with open("equipment.txt","r") as rf:
    with open("equipment_copy.txt","w") as wf:
        for eachline in rf:
            wf.write(eachline)
    