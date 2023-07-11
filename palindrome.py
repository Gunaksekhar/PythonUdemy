def palindrome(abc):
    abc = abc.replace(' ','')
    if abc[0:] == abc[::-1]:
        return ('{} is palindrone'.format(abc))
    else:
        return ('It is not palindrone')


palin = palindrome('mad am')
print(palin)