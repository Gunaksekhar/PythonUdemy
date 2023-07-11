def gensquare(n):

    for i in range(n):
        yield (i**2)


print(list(gensquare(10)))
print()
import random
we = random.randint(1, 10)
print(we)
print()
def rand_num(low, high,n):
    for i in range(n):
        yield random.randint(low, high)
for num in rand_num(1, 10, 12):
    print(num)

print(''
      ''
      '')
#iterate function
s = 'hello'
s_iter = iter(s)
print(next(s_iter))  #h
print(next(s_iter))  #e
print(next(s_iter))  #l
