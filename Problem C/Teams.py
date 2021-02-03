def teams(n,s,arr):
    c = 0
    i = 0
    while i <= len(arr) - 3:
        if arr[i] + s >= arr[i+2]:
            i += 2
            c += 1
        i += 1
    return c


if __name__ == '__main__':
    with open('teams.in') as f:
        t = int(f.readline())
        for i in range(t):
            _ = list(map(int,f.readline().split()))
            n = _[0]
            s = _[1]
            arr = sorted(list(map(int,f.readline().split())))
            print(teams(n,s,arr))