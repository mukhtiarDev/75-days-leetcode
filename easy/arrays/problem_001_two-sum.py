# DAY 1/75 â€” TWO SUM
# LeetCode: https://leetcode.com/problems/two-sum/
# Difficulty: Easy | Topic: Arrays, Hash Maps

# PROBLEM DEFINITION:
# Given an integer array nums and an integer target, return the
# indices of two different elements whose sum equals target.
# Exactly one valid answer exists. You cannot use the same element twice.

# EXAMPLE 1:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: nums[0] + nums[1] = 2 + 7 = 9.

# EXAMPLE 2:
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
# Explanation: nums[1] + nums[2] = 2 + 4 = 6.

# EXAMPLE 3:
# Input: nums = [3, 3], target = 6
# Output: [0, 1]
# Explanation: The two separate elements both have value 3.

# BRUTE FORCE:
# Check every possible pair using two nested loops.
# Time: O(n^2), Space: O(1).
# This becomes slow when the array contains many elements.

# OPTIMIZED APPROACH:
# Use a hash map to remember previously visited numbers and their indices.
# For each number, calculate complement = target - number.
# If complement exists in the map, return both indices.
# Otherwise, store the current number and its index.
# This avoids repeatedly searching the array.

# OPTIMIZED SOLUTION:
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for index, number in enumerate(nums):
            complement = target - number

            if complement in seen:
                return [seen[complement], index]

            seen[number] = index

        return []

# COMPLEXITY:
# Time: O(n) average â€” one traversal with O(1) average hash operations.
# Space: O(n) â€” the hash map can store every element.

# WHY THIS APPROACH IS GOOD:
# It trades additional memory for a major runtime improvement.
# This complement-search pattern is useful in pair-sum problems,
# frequency counting, and many array lookup problems.

# EDGE CASES:
# Duplicate values: [3,3], target 6.
# Negative values: [-3,4,3,90], target 0.
# Smallest valid array: [1,2], target 3.
# The algorithm stores an element only after checking its complement,
# so an element cannot be used twice.

# INTERVIEW TAKEAWAY:
# Whenever a problem asks for a pair satisfying a target,
# consider whether a hash map can store the complement.
# DAY 1 COMPLETE.
