a = [list(map(int, input().split())) for i in range(19)]

for i in range(int(input())):
    x, y = map(int, input().split())
    for j in range(19):
        if a[j][y-1] == 1:
            a[j][y-1] = 0
        else:
            a[j][y-1] = 1
    for j in range(19):
        if a[x-1][j] == 1:
            a[x-1][j] = 0
        else:
            a[x-1][j] = 1
for i in range(19):
    for j in range(19):
        print(a[i][j], end=' ')
    print("")
