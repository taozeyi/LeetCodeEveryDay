# Source : https://oj.leetcode.com/problems/median-of-two-sorted-arrays/
# Author : Zeyi Tao
# Date   : 2015-08-25

###########################################################################################
# 
# There are two sorted arrays A and B of size m and n respectively. 
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#               
###########################################################################################

class Solution:
    def getKth(self, A, B, k):
        lenA = len(A); lenB = len(B)
        if lenA > lenB: return self.getKth(B, A, k)
        if lenA == 0: return B[k - 1]
        if k == 1: return min(A[0], B[0])
        pa = min(k/2, lenA); pb = k - pa
        if A[pa - 1] <= B[pb - 1]:
            return self.getKth(A[pa:], B, pb)
        else:
            return self.getKth(A, B[pb:], pa)
    
    def findMedianSortedArrays(self, A, B):
        lenA = len(A); lenB = len(B)
        if (lenA + lenB) % 2 == 1: 
            return self.getKth(A, B, (lenA + lenB)/2 + 1)
        else:
            return (self.getKth(A, B, (lenA + lenB)/2) + self.getKth(A, B, (lenA + lenB)/2 + 1)) * 0.5

list1 = [1,2,3,4]
list2 = [5,6,7,8]
s = Solution()
print s.findMedianSortedArrays(list1, list2)