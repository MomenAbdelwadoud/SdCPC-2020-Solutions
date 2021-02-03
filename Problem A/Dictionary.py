def dic(s):
    if s == s[::-1]:
        return 1
    return 0


if __name__ == "__main__":
    with open('pla.in') as f:
        t = int(f.readline())
        for i in range(t):
            s = f.readline().strip('\n')
            print(dic(s))