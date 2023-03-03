"""
import pyautogui as pag
import random
import time
while true:
    x = random.randint(600,700)
    y = random.randint(200,600)
    pag.moveTo(x,y,0.5)
    time.sleep(2)
"""
#Warm-Up : Surface Area of Cube
#Analysis: Code Should be able to take one side of the cube then square it to get one area of the square then * 6 cause of the 6 sides on a cube
#Design, request one side of the cube then square it and multiply by 6
'''
side= float(input("What is the measurement of any side of the cube?: "))
area= (side**2)*6
print("The area of your cube is", area)
'''
'''
for character in "My name is brian! :D": # for loop; character is the name; "My name is brian! :D" is the sentence needing of printing 
    print(character, end= " ")
'''
'''
for count in range (6,1,-1):
    print(count, end =" ")
'''
'''
food= str(input("What do you want to eat?:"))
drink=str(input("What do you want to drink?: "))
print("Your order is a",food,"and a",drink)
'''
"""
for pussy in "Brian":
    print(pussy,ord(pussy))
"""
"""
weight= float(input("Enter your weight here in(kg): "))
height= float(input("Enter your height here(m): "))
BMI= weight/(height**2)
print(BMI)
if BMI<18.5:
    print("You are underweight.")
elif BMI<24.9:
    print("You are normal.")
elif BMI<29.9:
    print('You are overweight')
else:
    print("You are obese.")
"""
"""
for i in range(10,102): # this is a for loop talking about the range 
    if i % 2!=0: # thiss makes it so if the quotient doesn't =0 aka = 1 then it will print otherwise no bueno
        print(i)
"""
"""
for i in range(1,8):
    for j in range(1,i+1):
        print(j,end='')
    print("")
"""
"""
x=-1
y=1
while True:
    z=x+y
    print(z)
    x+=1
"""
"""
age=(int(input("How old was she?:")))
while age<13:
    print("FBI OPEN UP")
print("ight u good")
"""
"""
for x in reversed(range(1,11,1)):
    print(x)
print("Happy new Years!")
"""
# Fun little Jungle Thingy
"""
import random
league=['Fiddlestick','Gragas','Hecarim','Ammumu','Master Yi ']
lit=random.sample(league,1)
print(lit)
"""