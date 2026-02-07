class Solution:
    def combinationSum2(self, candidates, target):
            res = []
            candidates.sort()
            curr=[]
            length=len(candidates)
            def backtrack(index,currSum):
                if currSum == target:
                    res.append(curr[:])
                    return
                if currSum>target:
                    return
                # if index > len(candidates)-1:
                #     return
                hash = {}
                for j in range(index,len(candidates)):
                    if candidates[j] not in hash:
                        hash[candidates[j]]=1
                        curr.append(candidates[j])
                        backtrack(j+1,currSum+candidates[j])
                        curr.pop()
            backtrack(0,0)
            return res
ob=Solution()
print(ob.combinationSum2([],2))
print(ob.combinationSum2([14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12],27))