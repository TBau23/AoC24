input = open("./day1/d1input.txt", "r")

col1 = []
col2 = []

for line in input:
    
    if line.strip():  
        nums = line.split()
        col1.append(int(nums[0]))
        col2.append(int(nums[1]))

col1.sort()
col2.sort()

p1res = 0

for i in range(len(col1)):
    p1res += abs(col1[i] - col2[i])


## pt2

col2dict = {}


for i in range(len(col2)):
    if col2[i] not in col2dict:
        col2dict[col2[i]] = 1
    else:
        col2dict[col2[i]] += 1

p2res = 0

for i in range(len(col1)):
    if col1[i] in col2dict:
        p2res += (col1[i] * col2dict[col1[i]])

print(p2res)
print(r2)