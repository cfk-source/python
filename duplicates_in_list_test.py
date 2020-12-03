list_a = [1,2,3,4,7,9]

list_b = [1,2,4,6,4]

list_new = list_a + list_b

print(list_new)
print('Duplicate items are:..')
for x in range(0, len(list_new)):
    for j in range(x+1, len(list_new)):
        if list_new[x] == list_new[j]:
            print(list_new[j])