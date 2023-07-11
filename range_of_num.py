def range_of_fun():

    dec = 'backspace'
    acceptable_range = range(0,10)
    within_range = False
    while dec.isdigit() == False or within_range == False:
        dec = input('Enter the value of numbers between (0:10):')

        if dec.isdigit() == False:
            print('It is not a number')

        if dec.isdigit() == True:
            if int(dec) in acceptable_range:
                within_range = True
            else:
                print("Sorry it is not in acceptable range")
                within_range = False


    return int(dec)

d = range_of_fun()
print(d)