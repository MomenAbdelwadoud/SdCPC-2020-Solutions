def grid(n,strs):
    all = ''.join(strs)
    uniq = set(all)
    for i in uniq:
        if all.count(i) % n != 0:
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    with open('Problem D/equals.in') as f:
        t = int(f.readline())
        for j in range(t):
            n = int(f.readline())
            strs = []
            for i in range(n):
                strs.append(*f.readline().split())
            print(grid(n,strs))
    