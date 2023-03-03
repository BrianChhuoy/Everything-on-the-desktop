import random # imports the random function
l_points =0 # variable  1
m_points=0 # variable 2
for x in range(9): # for loop that goes 9 times 1
    z=random.randint(1,201)
    if z==110:
        print('110 was generated so the game is over')
        break
    elif z%9==0:
        if (z/9)%2==0:
            print('no one gets a point! since number was',z)
            continue
    elif z%2==0:
        l_points+=1
        print("L got a point and it is at",l_points,"points","since the number was",z)
    elif z%2!=0:
        m_points+=1
        print("M got a point and has",m_points, "since the number was",z)
print("l has",l_points,"points")
print("m has",m_points,"points")