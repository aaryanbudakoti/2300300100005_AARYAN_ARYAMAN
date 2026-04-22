#  valid anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)    
        return sorted_s == sorted_t
    
# Write your own test cases
s=input("Enter string s: ")
t=input("Enter string t: ")  
solution = Solution()
print(solution.isAnagram(s, t))
