import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
def gateways_cnt(pnt: int) -> int:
    return len((set(network_map[pnt]).intersection(set(gateways))))


def nearest_gateway(pnt: int) -> int:
    if gateways_cnt(pnt) > 0:
        return int(set(network_map[pnt]).intersection(set(gateways)).pop())
    else:
        return -1


def delete_link(pnt1, pnt2: int):
    aa = network_map[pnt1]
    aa.remove(pnt2)
    network_map[pnt1] = aa
    if len(network_map[pnt1]) == 0:
        del network_map[pnt1]


def find_path(pnt, target: int, path:[]) -> bool:
    for c in network_map[pnt]:
        if c == target:
            gateway = nearest_gateway(c)
            delete_link(c, gateway)
            delete_link(gateway, c)
            print(f'{c} {gateway}')
            return True
        elif c in gateways:
            continue
        elif c in path:
            continue
        elif gateways_cnt(c) > 0:
            path.append(c)
            if find_path(c, target, path):
                return True
    return False


network_map = dict()
gateways = set()
a = set()
n, l, e = [int(i) for i in input().split()]
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    if n1 in network_map:
        network_map[n1] = set(network_map[n1]).add(n2)
    else:
        network_map[n1] = set([n2])
    if n2 in network_map:
        network_map[n2] = set(network_map[n2]).add(n1)
        # a = set(network_map[n2])
        # a.add(n1)
        # network_map[n2] = a
    else:
        network_map[n2] = set([n1])
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gateways.add(ei)

# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # Example: 3 4 are the indices of the nodes you wish to sever the link between
    gw = nearest_gateway(si)
    if gw >= 0:
        delete_link(si, gw)
        delete_link(gw, si)
        print(f'{si} {gw}')
        continue
    is_found = False
    for f_pnt in network_map:
        if gateways_cnt(f_pnt) > 1:
            if find_path(si, f_pnt, [si]):
                is_found = True
                break
    if is_found:
        continue
    for f_pnt in network_map:
        if gateways_cnt(f_pnt) > 0:
            gw = nearest_gateway(f_pnt)
            delete_link(f_pnt, gw)
            delete_link(gw, f_pnt)
            print(f'{f_pnt} {gw}')
            break

