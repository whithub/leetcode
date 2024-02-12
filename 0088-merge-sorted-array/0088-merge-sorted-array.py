class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Submission #1:
        # for el in nums2:
        #     nums1.append(el)
        
        # nums1.sort()

        # exclude_val = 0
        # while len(nums1) > (m + n):
        #     nums1.remove(exclude_val)

        # Submission #2: 
        #   iterate in reverse order since `nums1` has extra space at the end; allows us to directly insert vs. shift existing elements
        a = m - 1
        b = n - 1
        write_index = m + n - 1

        # Merge arrays in reverse order
        while a >= 0 and b >= 0:
            if nums1[a] >= nums2[b]:
                nums1[write_index] = nums1[a]
                a -= 1
            else:
                nums1[write_index] = nums2[b]
                b -= 1
            write_index -= 1

        # Copy remaining elements of nums2
        while b >= 0:
            nums1[write_index] = nums2[b]
            b -= 1
            write_index -= 1
