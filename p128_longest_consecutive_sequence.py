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
        num_set = set()
        longest = 0

        # For loop: num in the list -> add them to the set
        for num in nums:

        # Each time num is added to set, check for longest
            num_set.add(num)
            # while there value smaller than current value or bigger than current value
            count = 1
            behind, ahead = num-1, num+1

            while (behind in num_set) or (ahead in num_set):
                if behind in num_set:
                    count +=1
                    behind -= 1
                if ahead in num_set:
                    count +=1
                    ahead +=1

            longest = max(longest, count)

        return longest


            # Keep count and compare to the longest count

### ------- Run solution -------###
# CMD command: python p128_longest_consecutive_sequence.py

# # Example #1
# nums = [0,3,7,2,5,8,4,6,0,1]
# x = Solution.longestConsecutive(nums)
# print(x)

# Example #2:
nums = [100,4,200,1,3,2]
x = Solution.longestConsecutive(nums)
print(x)