def oxy(n,arr):
    b = 0
    s = 0
    p = -1
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[j] - arr[i] > s - b:
                s = arr[j]
                b = arr[i]
                b_day = i+1
                s_day = j+1
                p = s - b
    if p > -1:
        return ' '.join([str(b_day),str(s_day),str(p)])
    return p

if __name__ == '__main__':
    with open('Problem H/oxy.in') as f:
        n = int(f.readline())
        arr = list(map(int,f.readline().split()))
        print(oxy(n,arr))
    