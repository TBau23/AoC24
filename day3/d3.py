import re
input = open("./day3/d3input.txt", "r")

# find all instances of mul(x,y)
# x and y need to be 1-3 digit numbers


res = 0
for line in input:
    matches = re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', line.strip())
    for match in matches:
        res += int(match.group(1)) * int(match.group(2))
print(res)