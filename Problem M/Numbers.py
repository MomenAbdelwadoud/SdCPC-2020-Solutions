def nums(x,y):
    if x == y:
        return 0
    elif (y - x) % 3 == 0:
        return (y - x) / 3
    elif (y - x - 2) % 3 == 0:
        return 1 + (y - x - 2) / 3
    else:
        return 1 + (y - x - 1) / 3

if __name__ == '__main__':
    with open('numbers.in') as f:
        t = int(f.readline())
        for j in range(t):
            _ = list(map(int,f.readline().split()))
            x = _[0]
            y = _[1]
            print(int(nums(x,y)))
    