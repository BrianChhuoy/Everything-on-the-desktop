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
		return (sorted_numbers[middle_index -1] + sorted_numbers[middle_index])/2
	else:
		middle_index = (count1-1) // 2
		return sorted_numbers[middle_index]
def mode1(lst):
	str1=''
	mode_list=[]
	freq_dict = {}
	for elem in lst:
		if elem in freq_dict:
			freq_dict[elem] += 1
		else:
			freq_dict[elem]=1
	max_freq = max(freq_dict.values())
	for hm in freq_dict:
		if freq_dict[hm]==max_freq:
			mode_list.append(hm)
	for hm1 in mode_list:
		str1=str1+ ' '+str(hm1)
	return str1
f=open('50DayFruitData.txt','r')
a=f.readline()
lisa=[]
lisb=[]
liss=[]
lisall=[]
for x in range(50):
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
"""
print(lisa)
print(lisb)
print(liss)
print(lisall)
"""
print('The mean number of apples eaten is:',mean(lisa))
print('The median number of apples eaten is:',median(lisa))
print('The mode number of apples eaten is:',mode1(lisa))
print('The mean number of banana eaten is:',mean(lisb))
print('The median number of banana eaten is:',median(lisb))
print('The mode number of banana eaten is:',mode1(lisb))
print('The mean number of strawberry eaten is:',mean(liss))
print('The median number of strawberry eaten is:',median(liss))
print('The mode number of strawberry eaten is:',mode1(liss))
print('The mean number of apples eaten is:',mean(lisall))
print('The median number of apples eaten is:',median(lisall))
print('The mode number of apples eaten is:',mode1(lisall))

meaapple=('The mean number of apples eaten is:'+str(mean(lisa))+'\n')
medapple=('The median number of apples eaten is:'+str(median(lisa))+'\n')
modapple=('The mode number of apples eaten is:'+str(mode1(lisa))+'\n')
meabanana=('The mean number of banana eaten is'+str(mean(lisb))+'\n')
medbanana=('The median number of banana eaten is'+str(median(lisb))+'\n')
modbanana=('The mode number of banana eaten is'+str(mode1(lisb))+'\n')
meastrawberry=('The mean number of strawberry eaten is'+str(mean(liss))+'\n')
medstrawberry=('The median number of strawberry eaten is'+str(median(liss))+'\n')
modstrawberry=('The mode number of strawberry eaten is'+str(mode1(liss))+'\n')
meaall=('The mean number of all eaten is'+str(mean(lisall))+'\n')
medall=('The median number of all eaten is'+str(mean(lisall))+'\n')
modall=('The median number of all eaten is'+str(mode1(lisall))+'\n')
f.close()
r=open('BrianChhuoy_output.txt','w')
r.write(meaapple)
r.write(medapple)
r.write(modapple)
r.write('\n')
r.write(meabanana)
r.write(medbanana)
r.write(modbanana)
r.write('\n')
r.write(meastrawberry)
r.write(medstrawberry)
r.write(modstrawberry)
r.write('\n')
r.write(meaall)
r.write(medall)
r.write(modall)
r.close()
