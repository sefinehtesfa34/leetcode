class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        self.nums=nums
        self.target=target
        for i in range(len(self.nums)):
            if self.target in self.nums:
                return self.nums.index(self.target)
            if self.target<self.nums[0]:
                return 0
            
            if self.target>self.nums[-1]:
                    return self.nums.index(self.nums[-1])+1
            if i>0:
                if self.nums[i-1]<self.target and self.nums[i]>self.target:
                    return i

                
                
        
