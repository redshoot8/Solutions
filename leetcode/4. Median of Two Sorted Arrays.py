from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = list(sorted(nums1 + nums2))
        if len(merged_list) % 2 != 0:
            return merged_list[len(merged_list) // 2]
        return (merged_list[len(merged_list) // 2 - 1] + merged_list[len(merged_list) // 2]) / 2