x={}
x["chips"]=10 
x["juice"]=20
x["biscuits"]=30 
x["mango"]=40
print(x)

#pt 2 
b=int(input("Enter the number of different items u want:"))
total=0 
for i in range(b):
	a=input("Enter item name:")
	total+=(x[a])*j
print(total,'is your total')
