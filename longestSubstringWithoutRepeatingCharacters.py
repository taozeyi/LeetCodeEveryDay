# Source : https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/
# Author : Zeyi Tao
# Date   : 2015-08-27

########################################################################################
# 
# Given a string, find the length of the longest substring without repeating characters. 
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", 
# which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
#               
#######################################################################################

def lengthOfLongestSubstring(s):

	lastRepeating = -1
	longestSubstring = 0
	positions = {}
	for i in range(0, len(s)):

		if s[i] in positions and lastRepeating <positions[s[i]]:
			lastRepeating = positions[s[i]]

		if i - lastRepeating > longestSubstring:
			longestSubstring = i - lastRepeating

		positions [s[i]] = i

	return longestSubstring





def otherlengthOfLongestSubstring(s):
        start = 0
        maxlen = 0
        dict = {}
        for i in range(len(s)):
            dict[s[i]] = -1
        for i in range(len(s)):
            if dict[s[i]] != -1:
                while start <= dict[s[i]]:
                    dict[s[start]] = -1
                    start += 1
            if i - start + 1 > maxlen: maxlen = i - start + 1
            dict[s[i]] = i
        return maxlen


s = "abcefghi"
print lengthOfLongestSubstring(s)
print otherlengthOfLongestSubstring(s)

#########################################################################################
# First Round:
# i = 0, s[0] not in positions, 0 - (-1) > 0 longestSubstring = 0 - (-1) = 1, positions = {(a,0)}
# Second Round:
# i = 1, s[1] not in positions, 1 - (-1) > 1 longestSubstring = 1 - (-1) = 2, positions = {(a,0), (b,1)}
# Thrid Round:
# i = 2, s[2] not in positions, 2 - (-1) > 2 longestSubstring = 2 - (-1) = 3, positions = {(a,0), (b, 1), (c,2)}
# Forth Round:
# i = 3, s[3] = a in positions, and lastRepeating = -1 < positions[s[3]] = 0, lastRepeating = 0, positions{(a,3), (b, 1), (c,2)} 
# Case 1 if "abcad"
# i = 4, s[4] no in position, 4 - (-1)