solve = []

def next_step(n, k):
    global solve
    if n >= 0 and k >= 0 and solve[n][k] > 0:
        return solve[n][k]
    if n < 0:
        return 0
    if n <= 1 or k == 1:
        return 1
    solve[n][k] = next_step(n, k - 1) + next_step(n - k, k)
    return solve[n][k]


def exp_sum(n):
    global solve
    solve.clear()
    for i in range(n + 1):
        solve.append([-1] * (n + 1))
    return next_step(n, n)