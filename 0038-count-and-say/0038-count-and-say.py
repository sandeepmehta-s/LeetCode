class Solution:
    def countAndSay(self, n):
        s = "1"
        for _ in range(n - 1):
            s = self.encode(s)
        return s
    
    def encode(self, s):
        ans = ""
        i = 0

        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1

            ans += str(j - i)
            ans += s[i]

            i = j
        return ans