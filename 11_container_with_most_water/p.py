class Solution:
    def maxArea(self, height):
        s, m, n = 0, 0, 0
        for i in range(len(height)):
            for j in range(i, len(height)):
                if height[i] <= height[j]:
                    m = height[i]
                else:
                    m = height[j]
                n = j - i

                sn = m * n

                if sn > s:
                    s = sn
        
        return s

