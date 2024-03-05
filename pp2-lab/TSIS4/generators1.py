def sqare_of_numbers(N):
    for i in range(N+1):
        yield i**2
N = int(input())
for i in sqare_of_numbers(N):
    print (i )