
#Lowkey First project to change time to seconds
days=int(input("Enter the amount of days:"))
hours=int(input("Enter the amount of hours:"))
minutes=int(input("Enter the amount of minutes:"))
seconds=int(input("Enter the amount of seconds:"))

t1= days*24*60*60
t2= hours*60*60
t3= minutes*60
t4=seconds
time= t1+t2+t3+t4
print(time)

"""
#converts seconds to time (Including the day edition)
time= int(input("Enter number of seconds:")) # In this seconds is the ref; And will convert to a whole number
day= time//86400
hours= (time//3600)%24
minutes=(time%3600)//60
seconds=(time%3600)%60
print(time,"seconds is",day,",days",hours,",hours",minutes,",minutes",seconds,",seconds.")
"""