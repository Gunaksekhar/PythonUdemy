try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("Type Error! Occured")

print()

x = 5
y = 0

try:
    z = x/y
except:
    print("Zero Error! Occured. Zero not divisible by other num")
finally:
    print("All Done")

def ask():

    while True:
        try:
            n = int(input("Enter a number: "))
        except:
            print("Please try again\n")
            continue
        else:
            break

    print("Your number squred is: ")
    print(n**2)
ask()
