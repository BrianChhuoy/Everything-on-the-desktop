total = 0
count = 0
count1=0
def mean(num):
	total= sum(num)
	count=len(num)
	return(total/count)
def median (numbers):
	sorted_numbers = sorted(numbers)
	count1 = len(sorted_numbers)
	if count1 % 2 == 0:
		middle_index = count1 // 2
		return (sorted_numbers[middle_index -1] + sorted_numbers[middle_index-1])
	else:
		middle_index = (count1-1) // 2
		return sorted_numbers[middle_index]
#This will be the main
f= open('500DayFruitData.txt','r')
a=f.readline()
acount=[]
lisa=[]
lisb=[]
liss=[]
lisall=[]
for x in range(500):
	b=f.readline()
	g=b.split()
	if g[1]=='apple':
		lisa.append(int(g[2]))
	if g[1]=='banana':
		lisb.append(int(g[2]))
	if g[1]=='strawberry':
		liss.append(int(g[2]))
	if g[1]=='strawberry' or g[1]=='banana' or g[1]=='apple':
		lisall.append(int(g[2]))

print('The mean number of apples eaten is:',mean(lisa))
print('The median number of apples eaten is:',median(lisa))
print('The mean number of apples eaten is:',mean(lisb))
print('The median number of apples eaten is:',median(lisb))
print('The mean number of apples eaten is:',mean(liss))
print('The median number of apples eaten is:',median(liss))
print('The mean number of apples eaten is:',mean(lisall))
print('The median number of apples eaten is:',median(lisall))

meaapple=('The mean number of apples eaten is:'+str(mean(lisa))+'\n')
medapple=('The median number of apples eaten is:'+str(median(lisa))+'\n')
meabanana=('The mean number of banana eaten is'+str(mean(lisb))+'\n')
medbanana=('The median number of banana eaten is'+str(median(lisb))+'\n')
meastrawberry=('The mean number of strawberry eaten is'+str(mean(liss))+'\n')
medstrawberry=('The median number of strawberry eaten is'+str(median(liss))+'\n')
meaall=('The mean number of all eaten is'+str(mean(lisall))+'\n')
medall=('The median number of all eaten is'+str(mean(lisall))+'\n')
f.close()
r=open('BrianChhuoy_output.txt','w')
r.write(meaapple)
r.write(medapple)
r.write('\n')
r.write(meabanana)
r.write(medapple)
r.write('\n')
r.write(meastrawberry)
r.write(medstrawberry)
r.write('\n')
r.write(meaall)
r.write(medall)
r.close()
