def showNumbers(limit):
    for num in range(1, limit + 1):
        if num % 2 != 0:
            print(f'{num} ODD')
        else:
            print(f'{num} EVEN')
x = 20
showNumbers(x)
