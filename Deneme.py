import sys
import random


Game = input ('Chose rock for 1 , paper for 2 , scissers for 3')
Computerchoise = random.randint(1,3)
print (Computerchoise)

if Game == '1':
    if Computerchoise == 1:
        print ('Draw')
    elif Computerchoise == 2:
        print ('Computer wins')
    elif Computerchoise == 3:
        print ('You win')
elif Game == '2':
    if Computerchoise == 1:
        print ('You win')
    elif Computerchoise == 2:
        print ('Draw')
    elif Computerchoise == 3:
        print ('Computer wins')
elif Game == '3':
    if Computerchoise == 1:
        print ('Computer wins')
    elif Computerchoise == 2:
        print ('You win')
    elif Computerchoise == 3:
        print ('Draw')
else:
    print ('Wrong input')
    