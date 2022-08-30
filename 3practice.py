def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

running = True

print('Enter number :')
while running:
    try:
        integer = int(input())
        if collatz(integer) == 1:
            running = False    
    except ValueError:
        print('must enter an integer')