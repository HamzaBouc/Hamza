def mSum(limit):
    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total = total + i
            i = i + 1
    return total


userInput = int(input("Enter limiting number: "))
plusOne = userInput + 1
print(mSum(plusOne))