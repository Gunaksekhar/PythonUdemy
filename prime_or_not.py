num = int(input('Enter the number: '))
if num > 1:
    for i in range(2, num):
        if num%i == 0:
            print('It is not a prime number')
            break
    else:
        print('It is prime number')
else:
    print('It is not a prime number because it is less than 1')