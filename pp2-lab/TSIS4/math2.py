def trap(first,second,height):
    area = 0.5 * (first + second) * height
    return area
first = int(input())
second = int(input())
height = int(input())
result = trap(first,second,height)
print(result)