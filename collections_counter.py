from collections import Counter
my_lists = ('ncjndjhedbhujsdcnd')
l = Counter(my_lists)
print(l)

order = ['s','s','g','g','g',4,1,5,8,6,1,9,9]
lm = Counter(order)
print(lm)
print("Most common", lm.most_common())
print("set of order",set(lm))
print("dict of order", dict(lm))

print()

#defaultdict
from collections import defaultdict
d = defaultdict(lambda: "no value")
d['A'] = 10
d['B'] = 11
d['C']
print("dict of A: ", d['A'])
print("dict of C: ", d['C'])

#namedtuple
from collections import namedtuple
Dog = namedtuple('Dog',['Name', 'Age', 'Breed'])
s = Dog(Name='Anuskha', Age=1.6, Breed='Husky')
print(s)
print(s.Name)
print(s.Age)
print(s[2])