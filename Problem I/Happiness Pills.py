def pills(n,T,ps,primes,p,table):    
    if T <= 0 or n <=0:
        return 0
    if table[n][T]:
        return table[n][T]
    if ps[n-1][1] > T:
        table[n][T] = pills(n-1,T,ps,primes,p,table)
    else:
        if p < 0:
            table[n][T] = max(
            ps[n-1][0] + pills(n-1,T-ps[n-1][1],ps,primes,p,table),
            pills(n-1,T,ps,primes,p,table)
            )
        else:
            table[n][T] = max(
                (primes[p] * ps[n-1][0]) + pills(n-1,T-ps[n-1][1],ps,primes,p-1,table),
                pills(n-1,T,ps,primes,p,table)
            )
        return table[n][T]


if __name__ == '__main__':
    with open('Problem I/pills.in') as f:
        _ = list(map(int,f.readline().split()))
        n = _[0]
        T = _[1]
        ps = []
        for i in range(n):
            _ = ps.append(list(map(int,f.readline().split())))
        ps.sort(key=lambda x: x[0])
        primes = [2,3,5,7,11,13,17,19,23,29]
        p = 9
        table = [[None] * (T+1)]*(n+1)
        print(pills(n,T,ps,primes,p,table))    