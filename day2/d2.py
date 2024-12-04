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


def is_strict_increase_or_decrease(level, mode='increase'):
    compare = (lambda a, b: a < b) if mode == 'increase' else (lambda a, b: a > b)
    return all(compare(level[i], level[i + 1]) for i in range(len(level) - 1))

def check_adjacent_differences(numbers):
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) > 3 or abs(numbers[i] - numbers[i + 1]) < 1:
            return False
    return True

def is_safe(report):
    lvls = list(map(int, report.split()))
    
    for i in range(len(lvls)):
        if i == 0:
            continue
        if abs(lvls[i] - lvls[i - 1]) > 3 or abs(lvls[i] - lvls[i - 1]) < 1:
            return False
    if is_strict_increase_or_decrease(lvls, 'increase') or is_strict_increase_or_decrease(lvls, 'decrease'):
        return True
    return False

def is_safe_pt2(report):
    lvls = list(map(int, report.split()))

    if check_adjacent_differences(lvls) and (
        is_strict_increase_or_decrease(lvls, 'increase') or
        is_strict_increase_or_decrease(lvls, 'decrease')
    ):
        return True
    
    for i in range(len(lvls)):
        mod_lvls = lvls[:i] + lvls[i + 1:]

        if check_adjacent_differences(mod_lvls) and (
        is_strict_increase_or_decrease(mod_lvls, 'increase') or
        is_strict_increase_or_decrease(mod_lvls, 'decrease')
        ):
            return True
    return False
    

res = 0
for line in input:
    if is_safe_pt2(line.strip()):
        res += 1
print(res)