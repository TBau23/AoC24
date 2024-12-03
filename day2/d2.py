input = open("./day2/d2input.txt", "r")

# input ="""
# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
# """


# strict increase or decrease
# adjacent digits have to have a difference between 1 and 3

def strict_increase(level):
    for i in range(len(level) - 1):
        if int(level[i]) >= int(level[i + 1]):
            return False
    return True

def strict_decrease(level):
    for i in range(len(level) - 1):
        if int(level[i]) <= int(level[i + 1]):
            return False
    return True

def is_safe(report):
    lvls = report.split()
    
    for i in range(len(lvls)):
        if i == 0:
            continue
        if abs(int(lvls[i]) - int(lvls[i - 1])) > 3 or abs(int(lvls[i]) - int(lvls[i - 1])) < 1:
            return False
    if strict_increase(lvls) or strict_decrease(lvls):
        return True
    return False

res = 0
for line in input:
    if is_safe(line.strip()):
        res += 1
print(res)