def ran_check(num, low,high):
    if num in range(low, high):
        print(f'{num} is in range of {low} and {high}')
    else:
        print('Not in the range')
ran_check(2,0,10)
