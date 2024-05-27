class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        new1 = set()
        new2 = set()

        for num in nums1:
            if num not in nums2:
                new1.add(num)

        for num in nums2:
            if num not in nums1:
                new2.add(num)

        return([list(new1), list(new2)])
