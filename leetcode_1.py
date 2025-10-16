#  Zigzag Conversion
class Solution(object):
    def convert(self, s, numRows):

        if numRows == 1 or numRows >= len(s):
            return s

        L = [""] * numRows

        row = 0
        direction = 1

        for char in s:
            L[row] += char

            if row == 0:
                direction = 1
                
            elif row == numRows-1:
                direction = -1

            row += direction

        return "".join(L)
