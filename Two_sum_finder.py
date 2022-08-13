class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Hashmap!
        hashmap={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in hashmap:
                #Returns indexes of tingz necessary
                return [hashmap[complement],i]
            #for number nums[i] it is assigned to the index i, tis how hashmap
            hashmap[nums[i]]=i
