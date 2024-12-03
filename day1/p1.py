input = open("./day1/d1input.txt", "r")

# the input is a text file with two columns separated by a space
# need to get the two columns to each be in a sorted list

col1 = []
col2 = []

for line in input:
    
    if line.strip():  
        nums = line.split()
        col1.append(int(nums[0]))
        col2.append(int(nums[1]))

col1.sort()
col2.sort()

res = 0

for i in range(len(col1)):
    res += abs(col1[i] - col2[i])

print(res)