values = ['0', '1', '2']
def index_values(values):
    print("Here is the index value")
    print(values)

index_values(values)

def value_in_not():
    choice = 'wrogn'

    while choice not in ['0', '1', '2']:

        choice = input("Pick the value from the index of ['0', '1', '2']: ")

        if choice not in ['0', '1', '2']:
            print("sorry, invalid choice: ")

    return int(choice)

present_values = value_in_not()
print(present_values)

def replace_value(values, position):
    char = input("Select the value to replace: ")
    values[position] = char
    return values

replace = replace_value(values, 2)
print(replace)

def Choice_not():
    choice = 'wrogn'

    while choice not in ['Y', 'N']:

        choice = input("Choose value is Y or N ['Y', 'N']: ")

        if choice not in ['Y', 'N']:
            print("sorry, invalid choice: ")

    if choice == 'Y':
        return True
    else:
        return False

choose = Choice_not()
print(choose)