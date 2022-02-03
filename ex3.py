def licDriver(speed):
    points = 0
    overspeed = ''
    excess = ''
    if speed <= 80:
        print('Ok')
    elif speed > 80:
        overspeed = speed
        excess = overspeed - 80
        for number in range(1, excess+1):
            if number % 4 == 0:
                points += 1
        print(f'Points: {points} ')
        if points > 12:
            print('License suspended')
    return ''

speed = int(input('Your Speed: '))
licDriver(speed)