from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

        Example 1:
        Input: n = 3
        Output: [[1,2,3],[8,9,4],[7,6,5]]

        Example 2:
        Input: n = 1
        Output: [[1]]
        """
        def generateNextPosAndValue(n):
            maxRow = maxColumn = n - 1
            minRow = minColumn = 0
            counter = 0

            while counter < n * n:
                # move right
                for col in range(minRow, maxColumn + 1):
                    counter += 1
                    yield (minRow, col, counter)
                minRow += 1

                # move down
                for row in range(minRow, maxRow + 1):
                    counter += 1
                    yield (row, maxColumn, counter)
                maxColumn -= 1

                # move left
                for col in range(maxColumn, minColumn -1, -1):
                    counter += 1
                    yield (maxRow, col, counter)
                maxRow -= 1

                # move up
                for row in range(maxRow, minRow - 1, -1):
                    counter += 1
                    yield (row, minColumn, counter)
                minColumn += 1

        # create empty NxN matrix
        matrix = [[None for i in range(n)] for i in range(n)]

        for row, column, value in generateNextPosAndValue(n):
            matrix[row][column] = value

        return matrix

if __name__ == '__main__':
    s = Solution()

    assert s.generateMatrix(3) == [[1,2,3],[8,9,4],[7,6,5]]
    assert s.generateMatrix(4) == [[1,2,3,4],[12, 13, 14, 5],[11, 16, 15, 6], [10, 9, 8, 7]]
    assert s.generateMatrix(1) == [[1]]

