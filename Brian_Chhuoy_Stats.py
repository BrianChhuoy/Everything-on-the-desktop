total=0
count=0
count1=0
def mean(num):
    total=sum(num)
    count=len(num)
    return(total/count)
def median(numbers):
    sorted_numbers= sorted(numbers )
    count1=len(sorted_numbers)
    if count1 % 2 ==0:
        middle_index = count1 // 2
        return (sorted_numbers[middle_index - 1] + sorted_numbers[middle_index])/2
    else:
        middle_index = (count1-1) // 2
        return sorted_numbers[middle_index]
f=open('500DayFruitData.txt','r')
a=f.readline()
acount=[]
lisa=[]
lisb=[]
liss=[]
lisall=[]

