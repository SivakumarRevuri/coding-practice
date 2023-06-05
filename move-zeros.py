# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

nums = [0,1,0,3,12]

zero_count = nums.count(0)

for _ in range(zero_count):
    nums.remove(0)
    nums.append(0)

print(nums) # [1, 3, 12, 0, 0]
