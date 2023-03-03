knuts=int(input("How many knuts do you have:"))
if knuts<=0: 
	print("You have 0 Knuts")
elif knuts>0: 
	galleons=(knuts//493)
	galleons2=(knuts%493)
	galleons3=(galleons2//29)
	galleons4=(galleons2%29)
print("You have",galleons,"galleons",galleons3,"sickles and",galleons4,"knuts")
