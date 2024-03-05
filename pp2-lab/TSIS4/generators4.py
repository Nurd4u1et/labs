a = int(input())
b = int(input())
def func():
    for i in range (a, b+1):
        yield i ** 2
n = []
for i in func():
    n.append(i)
print(n)
