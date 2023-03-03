#Intro to Strings- Substrings
"""
print(len("    ")) # so print just prints; but len tells us how many characters are contained in a statement
"""
# showing index
"""
name="Brian Chhuoy" # this is the code we go off

print(name[0]) # this prints the first string in "name" which is B since it is on the 0 spot
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[-1]) # This goes in reverse starting at y
print(name[-2])
print(name[-3])

print(name[len(name)-1]) # prints out last character 
"""
# count-controlled loop to display the characters and their positions
"""
data ="Hi there!" # the variable
for index in range(len(data)): # for statement ; range of len(data) means the number of characters in hithere which is 9
    print(index,data[index]) # this prints index = 9 and data = hithere together in a for loop
"""
# example of slicing
"""
name ="myfile.txt"
print(name[0:]) #prints the whole
print(name[0:1]) #prints the 0:first character
print(name[0:2]) #prints the 0: first 2 characters
print(name[:len(name)]) # the entire string
print(name[-3:]) #prints the last 3 characters
print(name[2:6]) #prints 2-5 letters 
"""
"""
filelist= ["myfile.txt","myprogram.exe","yourfile.txt"]
for fileName in filelist: # compiles it into file name
    if ".txt" in fileName: # makes it so if it has .txt in the filename it will print otherwise assume skip
        print(fileName)
"""
"""
f= open("myfile.txt",'w')# f is the variable; open is the action; The first quote names a file; 'w' will create the file
f.write("Hi im Brian.\nBrian Chhuoy :D .\n") # this line will begin towrite \n will buffer the previous statements to the last line
f.close() #this is required otherwise data will be lost
"""
"""
import random # this brings the import function to code
f = open("integer.txt",'w') # this opens/creates a "integer.txt" file; 'w' will enable you to write in the file
for count in range(500): # for loop in the range of 500 numbers  ; this makes it so it will keep coming back
    number = random.randint(1,500) # this makes it so it picks a random number from 1-500
    f.write(str(number)+ '\n') # this will write the number as a string and create a new line
f.close() #then it closes the file to save data
"""
#in this it takes the file and reads it rather then read and prints it out
"""
f=open("myfile.txt",'r') # so this will open a file; the file it will open is named myfile.txt and it will read from the file
text=f.read() # this will take the file "f" and read it and convert it to a variable named text
print(text) # afterwards will print text
"""
#to read a file with multiple lines and print
"""
f=open("myfile.txt",'r') # takes the code from my file and reads it
for line in f: # for loop; im pretty sure it has to close it to re read so thats why there is a space
    print(line) #print line in loop
"""
"""
f= open("myfile.txt",'r') # this opens the file named "myfile.txt" and reads it
while True: # a while loop where as long as true and not false
    line=f.readline() # line is now equal to the textfile and want it to read a line
    if line=="": # if statement= space it will go to next statement
        break # if line has a space it breaks and ends loop
    print(line) # this prints whatever was recived
"""

# how this code will function is it will take a number from the previous code and it will open then take the number from each line and convert it to a integer then combine it with the Sum and at the end will print this big thing
"""
f= open("integer.txt",'r') #opens and reads the text called integer.txt
theSum=0 # makes the sum = 0
for line in f: # a for loop that will read every line; will execute after accomplishing the last line
    line=line.strip() # reads everyline individually
    number=int(line) # this takes the number red from line that is a string and converts it into a integer so the next line can properly modify
    theSum+=number # this will take the newly transformed integer and convert and add it to theSum
    print(theSum)
print("The sum is", theSum) #after the last line it will print
"""

# Same code as above but will now handle adding with spaces
"""
f = open("integer.txt",'r')
theSum=0
for line in f:
    wordlist=linesplit() #only change is this  and will now split line
    line=line.strip()
    number=int(line)
    theSum+=number
print("The sum is", theSum)
"""