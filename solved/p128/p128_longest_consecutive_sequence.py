'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9

Constraints:
    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
'''


class Solution:
    def longestConsecutive(nums: list[int]) -> int:
        nums_set = set(nums)
        res = 0

        for num in nums_set:
            # (2,3,1,6,5)
            if num-1 in nums_set:
                count = 1
                pass
            else:
                count = 0
                while num in nums_set:
                    count +=1
                    num += 1
            res = max(res, count)

        return res


            # Keep count and compare to the longest count

### ------- Run solution -------###
# CMD command: python p128_longest_consecutive_sequence.py

# Example #1
nums = [0,3,7,2,5,8,4,6,0,1]
x = Solution.longestConsecutive(nums)
print(x)

# #Example #2:
# nums = [100,4,200,1,3,2]
# x = Solution.longestConsecutive(nums)
# print(x)