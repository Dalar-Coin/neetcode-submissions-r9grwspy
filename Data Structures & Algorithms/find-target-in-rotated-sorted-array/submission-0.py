class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # res = nums[0]
        # l = 0
        # r = len(nums) - 1

        # while l <= r:
        #     # asdf
        #     # check if the target exists within the leftmost val and middle

        #     if 

        #     m = (l + r) // 2
            
        #     if nums[m] >= target and nums[l] <= target:
        #         r = m - 1
        #     else:
        #         l = m + 1

        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            # left sorted portion
            elif nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
                    
            # right sorted portion
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
        return -1