list = ['1','5','three',['1','a'],'x']
print(len(list))

print(list[3:5])

print(list[1],[3])

print(list[-1])

print(list[0:3],[-2])

list.append([3])
list.insert(3,['Aljona'])
print(list[3])

tuple_1 = (1)
print(tuple_1)

list_1 = [1,2,3,4,5,6]
some_set = set(list_1)
print(some_set)
user_value = int(input('Enter some number:'))
some_set.add(12)
some_set.remove(2)


if (user_value in some_set):
    print('Your value is in the set')
else:
    print('Your value is not in the set')