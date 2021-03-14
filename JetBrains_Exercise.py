def merge(left, right):
    merged = [0 for _ in range(len(left) + len(right))]
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        merged[k] = left[i]
        i += 1
        k += 1

    return merged

left = [2, 3, 7, 8]
right = [1, 4, 5, 5]
print(merge(left, right))