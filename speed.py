#Task1
speed = int(input("Please enter the speed of the driver: "))
if (speed<70):print('ok')
elif(speed>70): demeritp = (speed-70)//5
print(f'The demerit point for the driver is {demeritp}')
if demeritp>12: print("the driver license gets suspended")

#Task2
a = int(input("Please provide a positive number: "))
for i in range(a+1):
    if i%2 == 0: print(f'{i} EVEN, ',end="")
    else:print(f'{i} ODD, ',end="")