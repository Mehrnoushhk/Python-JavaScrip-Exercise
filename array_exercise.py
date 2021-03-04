a = [1, 2, 3, 4]
print('Original array is {}'.format(a))

a.append(5)
print('New array is {}'.format(a))
# append doesn't return anything
print(a.append(6))

# pop([i]) removes the i element from a list and if the list is empty it raise IndexError

for i in range(0, 10):
    try:
        a.pop()
        print(a)
    except:
        print('Now the list is empty')
        break

a = [1, 2, 3, 4, 5, 6]
for i in range(0, 10):
    try:
        a.pop(0)
        print(a)
    except:
        print('Now the list is empty')
        break
# Remove every other element from a list
a = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(0, 10):
    try:
        a.pop(i)
        print(a)
    except:
        print('Now the list is empty')
        break