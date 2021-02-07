def vowels(s):
    vows = ['a','o','y','u','i','e']
    non_vowls = 0
    c = 0
    for i in s:
        if i not in vows:
            non_vowls += 1
        else:
            c += non_vowls
    return c




if __name__ == "__main__":
    with open('Problem B/vowels.in') as f:
        n = int(f.readline())
        s = f.readline().strip('\n')
        print(vowels(s))