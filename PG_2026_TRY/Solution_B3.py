
s = input()
index = 0

def parse_sum():
    global index

    value = parse_atom()

    while index < len(s) and s[index] == '+':
        index += 1
        value += parse_atom()

    return value


def parse_mul():
    global index

    value = parse_sum()

    while index < len(s) and s[index] == '*':
        index += 1
        value *= parse_sum()

    return value


def parse_atom():
    global index

    if s[index] == 'f':
        index += 2  # skip f(

        values = [parse_mul()]

        while s[index] == ',':
            index += 1
            values.append(parse_mul())

        index += 1  # skip )

        return max(values) - min(values)

    value = 0

    while index < len(s) and s[index].isdigit():
        value = value * 10 + int(s[index])
        index += 1

    return value


print(parse_mul())
