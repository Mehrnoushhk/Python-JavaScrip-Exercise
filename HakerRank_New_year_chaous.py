def minimumBribes(q):
    n = len(q)
    total_bribe = 0
    too_chaotic = False

    dict_fair = {}
    for i in range(1, n + 1):
        dict_fair[i] = i -1

    dict_q = {}
    for idx, value in enumerate(q):
        dict_q[value] = idx




    def element_index(value, arr):
        """Returns the index of a value in a given list"""
        for i in range(0, len(arr)):
            if arr[i] == value:
                return i
    
                
    def first_bribe(q, f_q):
        """Finds first item which is not in fair place"""
        for key in dict_q.keys():
            if dict_q[key] < dict_fair[key]:
                return [key, dict_q[key], dict_fair[key]]


    while len(dict_fair):
        print('-----------')
        print('q is', dict_q)
        print('fair_q is', dict_fair)
        try:
            bribe_key, actual_idx, fair_idx = first_bribe(dict_q, dict_fair)
        except TypeError:
            break
        print(actual_idx, fair_idx)
        if actual_idx + 2 < fair_idx :
            too_chaotic = True
            break
        else:
            total_bribe = total_bribe + (fair_idx - actual_idx)
            dict_q.pop(bribe_key)
            for key in dict_q.keys():
                if key > 
            dict_fair.pop(bribe_key)


    if too_chaotic:
        print('Too chaotic')
    else:
        print(total_bribe)


q = [1, 2, 5, 3, 7, 8, 6, 4]
minimumBribes(q)