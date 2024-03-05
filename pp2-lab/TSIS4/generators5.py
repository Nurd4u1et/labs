def asd(n):
    for i in range(1,n+1):
        yield i
n = int(input())
list = []
for i in asd(n):
    list.append(i)
list.reverse()
print(list)

