a = int(input())
b = list(map(int, input().split()))
def sortir(n):
    s = []
    if a == 1:
        return s[0]
    s.append(b[a-1])
    s.pop(b[a-1])
    print(s)
    return sortir(s)
print(sortir(b))