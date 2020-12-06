from math import sqrt

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        """
        Given two positive integers n and k.
        A factor of an integer n is defined as an integer i where n % i == 0.
        Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

        Constraints:
        1 <= k <= n <= 1000

        https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3554/
        """
        factors = [1, n]

        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                factors.append(i)
                if n / i != i:
                    factors.append(n / i)

        if k > len(factors):
            return -1

        return sorted(factors)[k - 1]


if __name__ == '__main__':
    s = Solution()

    assert s.kthFactor(12, 3) == 3
    assert s.kthFactor(7, 2) == 7
    assert s.kthFactor(4, 4) == -1
    assert s.kthFactor(1, 1) == 1
    assert s.kthFactor(1000, 3) == 4

