from collections import defaultdict

with open('test') as f:
    lines = f.read().split('\n')
lines = [(_, {char: None for char in 'wxyz'}) for _ in lines if _]

done = False


def get_last_line(char, line_nu):
    for i in range(line_nu+1):
        line, variables = lines[i]
        action, *words = line.split()
        if words[0] == char:
            return i
    return 0


def eval(line_nu):
    line, variables = lines[line_nu]
    action, *nums = line.split()
    if action == 'inp':
        ...
    elif action == 'add':
        v1, v2 = nums
        v1_line = get_last_line(v1, line_nu)
        val1 = eval(line_nu)
        try:
            val2 = int(v2)
        except ValueError:
            v2_line = get_last_line(v2, line_nu)
            val2 = eval(line_nu)
        variables[v1] = val1
        variables[v2] = val2
        return val1 + val2
    elif action == 'mul':
        v1, v2 = nums
        v1_line = get_last_line(v1, line_nu)
        try:
            val2 = int(v2)
        except ValueError:
            v2_line = get_last_line(v2, line_nu)
            val2 = eval(line_nu)
        if val2 == 0:
            variables[v1] = 0
            return 0
        val1 = eval(line_nu)
        variables[v1] = val1
        variables[v2] = val2
        return val1 * val2
    elif action == 'div':
        v1, v2 = nums
        v1_line = get_last_line(v1, line_nu)
        val1 = eval(line_nu)
        try:
            val2 = int(v2)
        except ValueError:
            v2_line = get_last_line(v2, line_nu)
            val2 = eval(line_nu)

        if v2 == 0:
            # error
            print('error')
            return
        variables[v1] = val1
        variables[v2] = val2
        return val1 // val2
    elif action == 'mod':
        v1, v2 = nums
        v1_line = get_last_line(v1, line_nu)
        val1 = eval(line_nu)
        try:
            val2 = int(v2)
        except ValueError:
            v2_line = get_last_line(v2, line_nu)
            val2 = eval(line_nu)

        if v1 < 0 or v2 <= 0:
            # error
            print('error')
            exit()
        variables[v1] = val1
        variables[v2] = val2
        return val1 % val2
    elif action == 'eql':
        v1, v2 = nums
        v1_line = get_last_line(v1, line_nu)
        val1 = eval(v1_line)
        try:
            val2 = int(v2)
        except ValueError:
            v2_line = get_last_line(v2, line_nu)
            val2 = eval(v2_line)
        variables[v1] = val1
        variables[v2] = val2
        return val1 == val2

