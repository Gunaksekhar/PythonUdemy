def add(n1,n2):
    print(n1+n2)

add(10,20)

num1 = 20
num2 = input("Enter the value: ")

print(num1,num2)
try:
    #want to attempt this code
    #may have an error
    result = 20 + 30
except:
    print("Hey it looks like aren't adding correctly")

print(result)

print()

def ask_for_int():
    while True:
        try:
            result = int(input("please provide number: "))
            print(result)
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Thank you, it is int value")
            break
        finally:
            print("End of Error Handling exception")

ask_for_int()