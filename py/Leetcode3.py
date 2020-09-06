s="pwwkew"
def lengthOfLongestSubstring(self, s: str):
        max_string=[]
        i=0
        while i <len(s):
            if s[i] not in s[:i-1]:
                max_string.append(s[:i])
            else:
                i=i+1
        print(max_string)

lengthOfLongestSubstring('s')
