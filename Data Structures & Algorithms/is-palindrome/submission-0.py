class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = "qwertyuipasdfghjklzxcvbnm1234567890"
        s = s.lower()
        bck = len(s) - 1
        fwd = 0
        while fwd < bck:
            if s[fwd] not in alpha:
                fwd += 1
                continue
            if s[bck] not in alpha:
                bck -= 1
                continue
            if s[fwd] != s[bck]:
                return False
            fwd += 1
            bck -= 1
        return True
