import itertools

def next_bigger(n):
    s = str(n)
    if len(s) == 1:
        return -1
    st = ''
    is_part = False
    for c in reversed(s):
        if len(st) == 0:
            st += c
        else:
            if st[-1] > c:
                st += c
                is_part = True
                break
            else:
                st += c
    if not is_part:
        return -1
    part = s[len(s) - len(st):len(s):]
    for x in sorted(["".join(x) for x in (itertools.permutations(st))], key=int):
        if x > part:
            return int(s[:len(s) - len(st):] + x)