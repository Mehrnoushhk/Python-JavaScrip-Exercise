def move_zeros(array):
    zero_count = 0
    new_array = []
    for element in array:
        if type(element) != bool and element == 0:
            zero_count += 1
        else:
            new_array.append(element)
    for _ in range(zero_count):
        new_array.append(0)
    return new_array


def move_zeros_refactor(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l + [0] * (len(arr) - len(l))
    

# print(move_zeros([0, 1, None, 2, False, 1, 0]))
# print(isinstance(False, float))

# *********************************************
# *********************************************
# *********************************************

def num_to_list(num_):
    arr = []
    while (num_ > 0):
        reminder = num_ % 10
        num_ = num_ // 10
        arr.append(reminder)
    return arr


def descending_order(num):
    if num == 0:
        return 0
    else:
        array = num_to_list(num)
        array.sort(reverse= True)
        result = int(''.join(map(str, array)))
    return result

# print(descending_order(456723))

# *********************************************
# *********************************************
# *********************************************

def points(games):
    score = 0
    arr = [game.split(':') for game in games]
    for item in arr:
        if int(item[0]) > int(item[1]):
            score += 3
        elif int(item[0]) == int(item[1]):
            score += 1
    return score

print(points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']))