# ---TimeComplexity:n+n*logn ,SpaceComplexity:n
# def sorted_squared(array):
#     #write code here.make sure to return desired array
#     res=[]
#     for i in array:
#         res.append(i*i)
#     res.sort()
#     return res
# print(sorted_squared([-3,2,3]))


# ---TimeComplexity:n ,SpaceComplexity:n
def sorted_array(arr):
    length=len(arr)
    res=[0]*length
    i=0
    j = length - 1
    k= length - 1
    while i<=j:
        first=arr[i]**2
        last=arr[j]**2
        if first>last:
            res[k]=first
            i+=1
            k-=1
        else:
            res[k]=last
            j-=1
            k-=1
    return res
print(sorted_array([-10,-8,2,4,5]))
