# Rotate Image

class Solution(object):
    def rotate(self, matrix):
       
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):

                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in range(len(matrix)):
            start = 0
            end = len(matrix)-1

            while start < end:

                temp = matrix[row][start]
                matrix[row][start] = matrix[row][end]
                matrix[row][end] = temp

                start +=1
                end -= 1
