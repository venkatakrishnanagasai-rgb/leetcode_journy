
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:

        mat = [[0] * n for _ in range(n)]

        left = 0
        right = n - 1
        top = 0
        bottom = n - 1

        k = 1

        while left <= right and top <= bottom:

            # Top: left -> right
            for col in range(left, right + 1):
                mat[top][col] = k
                k += 1
            top += 1

            # Right: top -> bottom
            for row in range(top, bottom + 1):
                mat[row][right] = k
                k += 1
            right -= 1

            # Bottom: right -> left
            for col in range(right, left - 1, -1):
                mat[bottom][col] = k
                k += 1
            bottom -= 1

            # Left: bottom -> top
            for row in range(bottom, top - 1, -1):
                mat[row][left] = k
                k += 1
            left += 1

        return mat