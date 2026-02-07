
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.
# Example:
# n = 4,k=2
# Output =[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]


def combine(n, k):
    # write code here
    temp = []
    res = []
    def helper(i):
        if len(temp) == k:
            res.append(temp.copy())
        else:
            need=k-len(temp)
            for j in range(i, n-need+1):
            # for j in range(i, n + 1):
                temp.append(j)
                helper(j + 1)
                temp.pop()
    helper(1)
    return res
print(combine(4, 3))