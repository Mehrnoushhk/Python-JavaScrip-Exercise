input_list = [5, 4, 2, 8]

for i in range(len(input_list)):
    input_list.sort()
    total = sum(input_list[0:2])
    input_list = input_list[2:]
    input_list.append(total)

print(input_list)