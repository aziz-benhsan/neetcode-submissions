class Solution:
    def search(self, nums: List[int], target: int) -> int:
     if nums==[]:
              return -1
     elif target<nums[0] or target >nums[-1] :
              return -1
     else:
        middle=len(nums)//2
        s=set()
        while middle not in s  :
            if target > nums[middle]:
                s.add(middle)
                middle=middle+1
            elif target <nums[middle]:
                s.add(middle)
                middle-=1
            else:
                return middle
        return -1
        