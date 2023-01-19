def solve():
    x = 0
    while(True):
        x+=1
        yield x

ans = solve()
print(next(ans))
print(next(ans))
print(next(ans))
