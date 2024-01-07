def encode_rail_fence_cipher(string, n):
    if n == 1:
        return string
    if string == '':
        return ''
    lines = []
    for i in range(n):
        lines.append('')
    i_line = 0
    c_dir = 1
    for c in string:
        lines[i_line] += c
        i_line += c_dir
        if i_line == n - 1:
            c_dir = -c_dir
        if i_line == 0:
            c_dir = -c_dir
    return "".join(lines)

def decode_rail_fence_cipher(string, n):
    if n == 1:
        return string
    if string == '':
        return ''
    lines = []
    for i in range(n):
        lines.append('')
    i_line = 0
    c_dir = 1
    for x in range(len(string)):
        for y in range(n):
            if i_line == y:
                lines[y] += '*'
            else:
                lines[y] += ' '
        i_line += c_dir
        if i_line == n - 1:
            c_dir = -c_dir
        if i_line == 0:
            c_dir = -c_dir
    s = list(' ' * len(string))
    ind = 0

    for y in range(n):
        for x in range(len(string)):
            if lines[y][x] == '*':
                s[x] = string[ind]
                ind += 1
    return "".join(s)