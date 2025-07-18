# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
def twoSum(nums, target):
    hashmap = {8,2}  # to store num: index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
