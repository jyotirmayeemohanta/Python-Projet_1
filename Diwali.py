import time
from random import randint

for i in range(1,85):
    print('')
    space=''
    
for i in range(1,1000):
    count=randint(1,100)
    while(count>0):
        space+=''
        count-=1
    if(i%10==0):
        print(space+'Happy Diwali 2022 🪔')
    else:
        print(space+'***')
        space=''
        time.sleep(0.2)
                
    