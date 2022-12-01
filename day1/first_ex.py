
max_sum = 0
with open("input1.txt", "r") as file_in:
    curr_sum = 0
    for line in file_in.readlines():
        if line == "\n":
            if curr_sum > max_sum:
                max_sum = curr_sum
            curr_sum = 0
        else:
            curr_sum += int(line)

print(max_sum)

max_sums = [0, 0, 0]
with open("input1.txt", "r") as file_in:
    curr_sum = 0
    for line in file_in.readlines():
        if line == "\n":
            if curr_sum > max_sums[0]:
                max_sums[0] = curr_sum
            elif curr_sum > max_sums[1]:
                max_sums[1] = curr_sum
            elif curr_sum > max_sums[2]:
                max_sums[2] = curr_sum
            curr_sum = 0
        else:
            curr_sum += int(line)

print(sum(max_sums))