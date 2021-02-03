def med_0(s,qu):
    ind = int(qu[0])
    s = s[:ind] + qu[1] + s[ind+1:]
    # s.replace(s[ind],qu[1])
    # s[ind] = qu[1]
    return s


def med_1(s,qu):
    l1,r1,l2,r2 = qu
    s = s[l1:r1] + s[l2:r2+1]
    s = sorted(s)
    med = len(s)//2
    return s[med]


if __name__ == '__main__':
    with open('median.in') as f:
        t = int(f.readline())
        for j in range(t):
            s = f.readline()[:-1]
            q = int(f.readline())
            for i in range(q):
                qu = list(f.readline().split())
                if qu[0] == '0':
                    s = med_0(s,qu[1:])
                else:
                    qu = list(map(int,qu[1:]))
                    print(med_1(s,qu))