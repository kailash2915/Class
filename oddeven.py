a = int(input("Please provide a positive number: "))
for i in range(a+1):
    if i%2 == 0: print(f'{i} EVEN, ',end="")
    else:print(f'{i} ODD, ',end="")