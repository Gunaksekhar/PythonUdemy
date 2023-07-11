def user_choice():

    #Variables

    #Intial
    choice = 'Fine'
    acceptable_range = range(0, 10)
    within_range = False

#Two Conditions to check
#Digit or within_range==False
    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter a number (0:10): ")

        #Digit Check
        if choice.isdigit() == False:
            print("sorry that is not a digit")

        #Range Check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("sorry you are out of acceptable range ")
                within_range = False


    return int(choice)

cool = user_choice()
print(cool)