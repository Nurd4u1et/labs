def findarea(side , len):
    if(side % 2 == 0):
        area = len*len
        return area
    else :
        return area
side = int(input())
len = int(input())
res = findarea(side , len)
print(res) 