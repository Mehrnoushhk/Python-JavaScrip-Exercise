# Given an array of integers, find the next greater element for every element in the array. The next greater element of an element x is the first grater number to the right of x, if there is no such number consider it -1


# Brutal Force

def find_next_greater(a):
    next_a = []
    counter = 0
    for i in range(0, len(a)):
        next_greater = -1
        for j in range(i + 1, len(a)):
            counter += 1
            if a[j] > a[i]:
                next_greater = a[j]
                break
        next_a.append(next_greater)
    print(next_a)
    print('Total number of runs is {}'.format(counter))

if __name__ == '__main__':
    find_next_greater( [2, 7, 3, 5, 4, 6, 8])
    find_next_greater([5, 4, 3, 2, 1])


