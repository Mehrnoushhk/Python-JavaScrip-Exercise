def solution(num: int) -> int:
    is_negative = False
    if num == 0:
        return 0
    elif num < 0:
        num *= -1
        is_negative = True
    revered = []
    while num != 0:
        revered.append(num % 10)
        num = num // 10
    i = 0
    while revered[i] == 0:
        i += 1
    revered = revered[i:]
    n = len(revered)
    reveresed_num = 0
    for i in range(0, n):
        reveresed_num += revered[i] * (10 ** (n - 1 - i))
    if is_negative:
        reveresed_num *= -1
    if reveresed_num > 2_147_483_647 or reveresed_num < -2_147_483_648:
        return 0
    return(reveresed_num)


print(solution(4800050))
