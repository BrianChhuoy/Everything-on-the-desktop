#example of a for loop
"""
for eachPass in range (4): #For loop is used, in range means that everytime it goes the set number *4 it will do it 4 times
    print("It's alive!",end= " ") #It's alive is the statement that it is printing; end= means it will begin on the same line everytime
"""
# A more hard example; EXACT SAME ANSWER ONE IS JUST HARDER and takes up more time
"""
print("It's alive!",end= " ")
print("It's alive!",end= " ")
print("It's alive!",end= " ")
print("It's alive!",end= " ")
"""
#For Loop
"""
number =2 # this is the number it is multiplying by
exponent =3 # this tells you how many times it will multiply
product =1 #this is the answer but it will change based on the loop
for eachPass in range (exponent): # for each time int passes it will go 3 times
    product= product*number # the equation
    print(product, end=" ") #this will print the updated product so 2^1 is 2 ; 2^2 is 4 ; 2^3 is 8 which is why it prints 3 times and end= "" makes it print on the same line
print (product) #this only prints the end result so it wont show the 2 4 8
"""
#shows how the for loop counts; Starting with 0
"""
for count in range(4): # it will count 4 times ; count is the variable and 4 is the ammount of times it will count, it doesnt count to 4 it just count 4 times
    print(count, end= " ")
"""
#count controlled loops
"""
product = 1 # it will start at 1 and update as the loop progresses going to 1 2 6 24
for count in range(4): # will count 4 times starting at 0
    product = product*(count+1)  # count starts at 0 so (0+1),(1+1),(2+1),(3+1); and product will just keep counting up with it so 1*1... 2*3 **** ALSO BY USING +1 IT MAKES IT SO IT DOESN'T START AT 0
print(product) # the solution :]
"""
#use of comma's in count controlled loops
"""
product = 1
for count in range(0,5):
    product= product *(count+1)
    print(product, end=" ")
"""
#input of a count-controlled loop
"""
lower= int(input("Enter the lower bound:")) #takes the smaller number
higher= int(input("Enter the higher bound:")) #takes the bigger number
theSum=0 # the defult number that will update
for number in range(lower, higher+1 ): # essentially like the examples above but now uses the inputs from what is put in
    theSum = theSum + number # theSum = updated ; theSum takes the update number; number is what is in the list; ex (0,5) - 0+(0+0)= 0 - 0+(0+1)=1 ; 1+(1+1)=3
print(theSum)
"""
#example of augmented assigned operations
"""
a = 17
s="hi"
a+=3 #a = a+3
a-=3 #a = a-3
a*=3 #a= a*3
a/=3 #a= a/3
a%=3 #a= a % 3
s+="there" # s= s + "there"
print (s)
"""
# introduces list
"""
print(list(range(4))) # counts from 0 -4
print(list(range(1,5))) # counts from 1-4 ; IT ALWAYS STARTS ON THE NUMBER AND ENDS BEFORE THE LAST NUMBER
"""
#shows loops in list of numbers
"""
for number in [6,4,8]:
    print(number, end= " ")
"""
#shows loop in list of letters
"""
for character in "Hi there!":
    print(character, end =  " ")
"""
# Shows counter in loop
"""
print(list(range(1,6,1))) # will count every (1) number
print(list(range(1,6,2))) # will count every (2) numbers
print(list(range(1,6,3))) # will count every (3) numbers 
"""
# compute the sum of the even numbers between 1 and 10
"""
theSum= 0
for count in range(2,11,2):
    theSum += count
print(theSum)
"""
# loop that count down
"""
for count in range(10,0,-1):
    print(count,end= " ")

print(list(range(10,0,-1)))
"""
#below shows allignment of numbers

print("%5s" % "four")   #In this example %6s tells the word where to go  ; four is  the word
print("%6s" % "four")   # in this it's the same but -6 tells it to go left
"""
for exponent in range(7,11):
    print("%3d%12d"%(exponent,10**exponent)) #in  this example %3d tells where the first word "exponent is suppose to go ; while the second "10**exponent" to go %12d
    print("%-13d%12s"%(exponent,10**exponent))
"""
"""
salary = 100.00
print("Your salary is  $"+ str(salary))
print("Your salary is  $%0.2f" % salary)
"""
"""
print("%6.1f" % 3.14)
"""
"""
name= "Stacy"
print("Hello,",name)
print("Hello, %s"% name)
"""
#Raw Example of how to use format strings
"""
print("Hello, %s %s, your current balance is $%f"%("Brian","Chhuoy", 129.21))  
"""
#cleaner example of format strings
"""
data= ("Brian","Chhuoy",503.129) #In this we have Brian Chhuoy which is represented as a string and 503129 represented as a float so decimal integers and WILL REGAURDLESS have at least 2 decimals
format_string= "Hello %s %s. Your current balance is $%.2f" # this line is the thing we are imputing so %s - Brian %s - Chhuoy %.2f means it can only go to 2 decimals and will have it or fill with 00
print(format_string % data) #this compiles and gives you the answer of: Hello Brian Chhuoy. Your current balance is $503.13
"""
#messing around
"""
print("sixsix") # 6 letter word
print("%6s" % "four") #prints it to make it 6 letters %6s means the string will make it 6
print("four") #defult where it should be with out %
print("%-6s"% "four")  #since it can go behind it stays in same place
print("%120s" % "Four") # lol
"""
#Testing
"""
for exponent in range(7,11):
    print(("%-3d%12d") % (exponent , 10 **exponent))
"""
"""
print("hello           7")
print("hello          7")
print("hello1212121121")
for exponent in range(7,11):
    print(("%-3s%12d") % ("aaa",exponent))
#----------------------------------------------------
"""
"""
for exponent in range (7,15): #from 7-11 the space decreases and at 10 it loses 2 spaces since a 0 is added to left and right side ; after 11 it stays put and puts a 0 at the end of the right side to make room 
    print(("%-3d%12d" %(exponent,10 **exponent)))
"""
"""
salary =100
#print("Your Salary is $"+ str(salary)) #in this clause it only prints 1 .0 rather then .00
print("Your Salary is $%.2d" %(salary))  #in this it prints 100.00; With %f it prints $100.00; with %s it prints $10; With %d it print $100
"""
"""
print(4==4) # does 4 = 4 ; Yes: True
print(4!=4) # does 4 not equal 4 ; No: False
print(4<5)# Is 4 Less then or equal to 5; Yes: True
print(4>=3)# Is 4 greater then or equal to 3; Yes: True
print("A"<"B")
"""
#First If-Else Statement : Use is to find area of circle; however if they were to input a 0 or negative number return a error message ; It dont know math
"""
import math # to bring the math.pi function and others
area = float(input("Enter the area:")) # Simple input that will ask for the area; float- means decimals too
if area > 0: # this makes it so the area has to be GREATER not equal or less then 0 so it must be above 0
    radius= (area/math.pi) # Math dont work
    print("The radius is ", radius ) # Print's if condition is greater then 0
else: # if condition = less then 0 then it goes to the alternative
    print("Error: The area must be a positive number") # this is the alternative to if less then 0 
"""
#this makes the code take in 2 numbers, then identifies which is bigger or smaller and prints
"""
first=float(input("Enter the first number:")) # this will take the first number; it dont matter as long as it is a number
second=float(input("Enter the second number:")) #this will take the second number 
if first > second: # if the first number is GREATER then the second number 
    maximum= first # the first will = max
    minimum= second # the second will = min
else: #other wise if the first statement isn't true 
    maximum = second # max = second 
    minimum = first  # min = first 
print("Maximum:",maximum)
print("Minimum:", minimum)
"""
#this is a simplified version of the one above this code b/c, Python includes two functions, max and min, that make the if-else statement in this example unnecessary.
"""
first= int(input("Enter the first number:"))
second= int(input("Enter the second number: "))
print("Maximum:",max(first,second))
print("Minimum:",min(first,second))
"""
#simple example of a simple if statement ; The use of the below is to turn a statement to its ABSOLUTE VALUE
"""
x=int(input("Pull up a number cuh:"))
if x < 0:
    x=-x
print(x)
"""
#this is a example of a Multi-Way if statement ; Used for grading system
"""
number= int(input("Enter the numeric grade:")) # the number will get input here
if number > 89: # if the number is greater then 89 then
    letter= "A" #Then letter = A
elif number>79: #else if it is greater then 79
    letter="B" # Then letter = B
elif number>69: #else if it is greater then 69
    letter="C" #Then letter = c
elif number>59: # Then if letter is greater then 59
    letter="D" # Then letter = D
else: #ELSE if none of the above is valid
    letter="F" # Then Letter = F
print("The letter grade is", letter) # this will print the result from above
"""
#the below shows an example of just simple error fixing things ; Useing the same example we ended a code in the front and behind
"""
number= int(input("Enter the numeric grade:")) # the number will get input here
if number > 100:
    print("Error Fucktard aint no way they at over 100.")
elif number <0:
    print("BWHHHAAAH Headass your kid must be a retarddjasijd...")
else:
    if number > 89:  # if the number is greater then 89 then
        letter = "A"  # Then letter = A
    elif number > 79:  # else if it is greater then 79
        letter = "B"  # Then letter = B
    elif number > 69:  # else if it is greater then 69
        letter = "C"  # Then letter = c
    elif number > 59:  # Then if letter is greater then 59
        letter = "D"  # Then letter = D
    else:  # ELSE if none of the above is valid
        letter = "F"  # Then Letter = F
    print("The letter grade is", letter)  # this will print the result from above
"""
#simple way of writing the above but kinda lazy way
"""
number= int(input("Enter the numeric grade:"))
if number > 100 or number < 0:
    print("Error:Grade must be between 100 and 0 ")
else:
    if number > 89:  # if the number is greater then 89 then
        letter = "A"  # Then letter = A
    elif number > 79:  # else if it is greater then 79
        letter = "B"  # Then letter = B
    elif number > 69:  # else if it is greater then 69
        letter = "C"  # Then letter = c
    elif number > 59:  # Then if letter is greater then 59
        letter = "D"  # Then letter = D
    else:  # ELSE if none of the above is valid
        letter = "F"  # Then Letter = F
    print("The letter grade is", letter)  # this will print the result from above
"""
#Shows an example of a and or and not statement
"""
A= True # so A will be True in this statement
B= False # B will be false in this statement
print(A and B) # in here it ask if A=True and B= False since B is false it results in the whole statement being False
print(A or B) # in here it ask  if A=True or B= False since all you need is one to be true the statment is resulted as True
print(not A) # in here it ask if A=True and with not statements A must be false to make the statement true so this results in FALSE
"""
"""
A=2
B=3
result= A + B*2 < 10  or B==2 # so this adds up to 8 is less then 10 which is true which overides and makes this a true statement 
print(result)
"""
#more review ig
"""
print(list(range(1,6,1))) # counts normally
print(list(range(1,6,2))) #counts by 2
print(list(range(1,6,3))) #counts by 3
"""
"""
theSum= 0 # variable
for count in range(2,11,2): #starts at 2 and counts by 2- 2,4,6,8,10
    theSum +=count # adds from the previous step so 0+2=2 ; 2+4=6;6+6=12;12+8=20
print(theSum)
"""
"""
#i was lowkey trolling top was from a earlier page
count=int(input("Enter the count:")) #take the number 
theSum=int(input("Enter the sum:")) #takes the number
if count > 0 and theSum // count >10: # must pass the first otherwise will get pased to else, to count must be greater then 0 and the sum's quotient must be greater then 10 
    print("average>10")
else:
    print("count=0 or average <=10")
"""
"""
x=int(input("Enter a number:"))
for x in ():
    x=-x
print(x)
"""
#first take on the while loop ; In this code it will indefinitely ask you to enter a number or click enter to quit in which it will take the sum of the numbers mentioned
#this is a enter-control loop
"""
theSum = 0.0 # the sum is in a string
data =input("Enter a number or just enter to quit: ") #This is the part of the code that acts as a temporary variable
while data != "":  # in this code it is responsible for looping so as long as the data isn't a space ( or u can put any symbol like q and when you type q it will end) it will keep looping
    number = float(data) # This will take the data convert it to a float then hand it over to number
    theSum+= number # in this code it makes it so the variable from number gets converted to theSum on top
    data = input("Enter a number or just enter to quit: ") # in this code it just repeats what is above and restarts the code
print("The sum is", theSum) #in this line if the code is done it will just take the sum from the above
"""

#this is a count control loop with a while loop
"""
theSum = 0  # Counter 1 ; will go up after adding 1,3,6,10 etc 
count = 1 #counter 2 ; will only go up by 1  ; so 1,2,3,4,5
while count <= 100000: # makes it so as long as count is under 1 it will not go over ; 
    theSum += count # adds everythigng to gether 
    count += 1 # makes the counter go by 1 
print(theSum) #prints the total 
"""
#this is a count control loop with the for loop version
"""
theSum = 0
for count in range(1,10001):
    theSum+=count
print(theSum)
"""
#counting down with a for loop
"""
for count in range (10,0,-1):
    print(count,end=" ")
"""
#counting down with a while loop
"""
count=10
while count>=1:
    print(count,end= " ")
    count-=1
"""
#intro to break
"""
theSum = 0.0
while True:
    data =input("Enter a number or press enter to quit: ")
    if data == "":
        break
    number =float(data)
    theSum+=number
print("The Sum is",theSum)
"""
#another example of break with a while loop ; in this code it will keep asking until you provide a number within 0-100
"""
number=0.0
while True: # makes it so long as it is with a condition
     number= int(input("Enter a numeric grade:"))# this ask for a number
     if number >=0 and number  <=100: # the specific rules
         break # this is what kills the program and makes it print number
     else: #this is the alternative route
         print("Error:grade must be between 100 and 0")
print(number)
"""
#boolean example of the same problem up top
"""
done = False
while not done:
    number=int(input("Enter the numeric grade:"))
    if number >=0 and number <= 100:
        done=True
    else:
        print("Error: grade must be between 100 to 0")
print(number)
"""
#intro to random; this will roll a dice and get a random answer
"""
import random #this is required to make the random module work
for roll in range (1): # this states it's a for statement as well as the number decides how many "rolls" python will do
    print(random.randint(1,6),end=" ") # this will utilize the random.randint line to print a random from (1,6)
"""
#The first Game of guess the number :D
"""
import random
smaller = int(input("Enter the smaller number:"))
larger = int(input("Enter the bigger number:"))
myNumber = random.randint(smaller,larger)
count =0
while True:
    count +=1
    userNumber = int(input("Enter your guess:"))
    if userNumber < myNumber:
        print("Too small!")
    elif userNumber > myNumber:
        print("Too large!")
    else:
        print("Congratulations! You've gotten it in",count,"tries!")
        break
"""