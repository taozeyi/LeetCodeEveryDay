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

s = "cccccc"
print lengthOfLongestSubstring(s)