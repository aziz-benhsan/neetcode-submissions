class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen={}
        for number in nums:
                seen[number]=nums.count(number)
        for key,value in seen.items():
            if value ==1 :
                return key
        