# # Using for loop
# arr=[1,2,3]
# res=[[]]
# # hash_table=[]
# for i in arr:
#     length=len(res)
#
#     for j in range(length):
#         temp=res[j].copy()
#         # if temp not in hash_table:
#         #     hash_table.append(temp)
#             temp.append(i)
#             res.append(temp)
# print("possible SubArray:",res)




# using recursion
def power_set(nums):
    # write code here
    res = [[]]
    temp = []
    length = len(nums)

    def helper(i):
        if i == length:
            res.append(temp.copy())
        else:
            helper(i + 1)
            temp.append(nums[i])
            helper(i + 1)
            temp.pop()

    helper(0)
    return res

print(power_set([1, 2, 3]))


# subsets with duplicates {1,3,3}
def subsetsWithDup(nums):
    # write code here
    res = [[]]
    temp = []
    length = len(nums)

    def helper(i):
        if i == length:
            if temp not in res:
                res.append(temp.copy())

        else:
            helper(i + 1)
            temp.append(nums[i])
            helper(i + 1)
            temp.pop()

    helper(0)
    return res
print(subsetsWithDup([1, 3, 3]))
