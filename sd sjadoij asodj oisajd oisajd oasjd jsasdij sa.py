#lab4 
upper=int(input("Enter a pefered upper bound:"))
de=0 
ab=0
per=0
devsum=0
print("between 1 and", upper,"there are...")
for x in range(1, upper+1): 
    devsum=0
    for i in range(1,x):
        if x%i==0:
            devsum+=i
    if devsum==x:
        per+=1
    if devsum<x:
        de+=1
    if devsum>x:
        ab+=1
print(de,"deficient number")
print(per,"perfect number")
print(ab,"abundant number")
