def tonumber(n):
    for i in range(2,n):
        if i % 2 == 0:
            yield i
n = int(input())
for i in tonumber(n):
    print(i)

    