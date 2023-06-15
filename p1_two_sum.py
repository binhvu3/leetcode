'''
Input = [1,2,3,4]
target = 6

Expected out put is [1,3]

1st attempts: Brute force
- Substract target from current num and
- loop through the list looking for the remainder

time complexity = O(n^2) and space O(1)
'''


class solution:
    def twoSum(self, nums, target):  # input [1,2,3,4], target=6
        for i in range(len(nums) - 1):  # i = 0
            res = [i]  # res = [0, 2]
            remainder = target - nums[i]  # remainder = 5
            start = i + 1  # start = 1
            for j in range(len(nums), start):  # j = 2
                if nums[j] == remainder:  # True
                    res.append(j)
                    print(res)
                    return res


def main():
    init = solution()
    print(init.twoSum([1, 2, 3, 4], 6))


if __name__ == "__main__":
    main()
