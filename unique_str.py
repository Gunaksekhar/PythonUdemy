sample_list = [1,1,1,1,2,2,3,3,3,3,4,5]
lists = set(sample_list)
print(list(lists))

'''
def unique_list(lst):
    return set(lst)

u = unique_list([1,1,1,2,2,3,3,3,4,5,5, 'Goat', 'Goat', 'Light', 'Fan', 'Fan'])
print(list(u))
'''
def unique_lst(lsts):

    seem = []
    for unique in lsts:
        if unique not in seem:
            seem.append(unique)
    return seem
asm = unique_lst([2, 2, 3,4, 5, 5, 6,6,'lap', 'lap', 'vote', 'vote'])
print(asm)