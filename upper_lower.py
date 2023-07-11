def up_low(s):
    uppercase = 0
    lowercase = 0

    for case in s:
        if case.isupper():
            uppercase += 1
        elif case.islower():
            lowercase += 1
        else:
            pass
    print(f'Original case {s}')
    print(f'Lowercase of the given string {lowercase}')
    print(f'uppercase of the given string {uppercase}')

s = "Hello Mr. RoGgers, How are you are you at Station Road"
up_low(s)