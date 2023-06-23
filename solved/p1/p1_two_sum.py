'''
Input = [1,2,3,4]
target = 6

Expected out put is [1,3]

1st attempts: Brute force
- Substract target from current num and
- loop through the list looking for the remainder

time complexity = O(n^2) and space O(1)
'''

def twoSum( nums, target):  # input [1,2,3,4], target=6
    for i in range(len(nums) - 1):  # i = 0
        # print('outer loop')
        res = [i]  # res = [0, 2]
        remainder = target - nums[i]  # remainder = 5
        start = i + 1  # start = 1
        for j in range(start, len(nums)):  # j = 2
            # print('inner loop')
            if nums[j] == remainder:  # True
                res.append(j)
                # print(res)
                return res

'''
nums = [1,2,3,4]
target = 6
print(twoSum(nums, target))

# Test 1
nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))

# test 2
print(f'Test #2 {twoSum([3,2,4], 6)}')

# Test 3
print(f'Test #3 {twoSum([3,3], 6)}')

# Output
# [1, 3]
# [0, 1]
# Test #2 [1, 2]
# Test #3 [0, 1]

'''
