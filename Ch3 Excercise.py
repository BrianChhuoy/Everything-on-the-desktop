#3-1g Excercise
#1.)
#a.)
# 1, 2, 3, 4, 5
#b.)
# 1, 2, 3
#c.)
# 1, 3, 5
#d.)
# 6, 5, 4, 3, 2,
#2.)
"""
for count in range(100):
    print("brian")
"""
#3.)
# Allows the body to know what is bering executed
#4.)
"""
for i in range(1,128):
    print(chr(i))
"""
#5.)
"""
teststring=input("Enter anything:")
for i in teststring:
    print(i,ord(i))
"""
#Chapter 3-2
#1.)
"""
amount = 24.235
print("Your salary is $%0.2f"% amount) # Will print: "Your salary is $24.23"
print("The area is $%0.1f" % amount) # will print: "The area is $24.2"
print("%7f" % amount) # will print:" 24.235" ; ACTUAL ANSWER: "24.235000"
"""
#2.)
# This might not be right but we go with it
"""
x=int(input("Number1:"))
y=int(input("Number2:"))
z=int(input("Number3:"))
print(("%6d%6d%6d") % (x,y,z))
"""
#3.)
(%0.2f) %
#4.)
"""
salaries = [1,2,3,4,5,6,7,8,9]
for numbers in salaries:
    print("%12.2f"% numbers)
"""


#Chapter 3-3g
#1.)
"""
x=3
y=5
#a.)
print(x==y) # false: since its not equal
#b.)
print(x>y-3) #True since 3>2
#c.)
print(x<=y-2) # True since 3 is = to 3
#d.)
print(x==y or x>2) # true since 3>2
#e.)
print(x != 6 and y>10) # False since it fails to meet more then one statement
#f.)
print(x>0 and x<100) # true since x is less then 100 but greater then 0
"""
#2.)
"""
x= int(input("Enter a number:"))
if x<0:
    x=-x
print(x)
"""
#3.)
"""
string= input("Enter a string:")
print(string.count(' '))
"""
#4.)
#not done
"""
x= input("Enter a sentence:")
y= input("Enter a sentence:")
for
"""
#5.)
"""
x= int(input("Enter a number:"))
if x<=0:
    print("Bruh u stupid")
else:
    print(x)
"""
#6.)
# we are gonna move pass gl brian