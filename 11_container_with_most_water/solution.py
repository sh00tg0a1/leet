class Solution:
    def maxArea(self, height):
        s = 0
        for i, l in enumerate(height):
            if i == len(height) - 1:
                break

            for k, r in (enumerate(height[i+1:])):
                sn = min(l, r) * (k+1)
                if sn > s:
                    s = sn
        return s

    def maxArea_new(self, height):
        s, mark = 0, 1
        cur_left, cur_right = 0, len(height)-1
        out = False

        while 1:
            for i in range(cur_left, cur_right+1):
                if i == cur_right:
                    out = True
                if height[i] >= mark:
                    cur_left = i
                    break

            for j in range(cur_right, cur_left-1, -1):
                if j == cur_left:
                    out = True
                if height[j] >= mark:
                    cur_right = j
                    break

            if cur_left == cur_right:
                out = True

            if out:
                break

            sn = (cur_right - cur_left) * mark

            if sn > s:
                s = sn
            mark += 1

        return s
