from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

        Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
        return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

        https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3555/
        """
        availableSpots = 0
        totalSpots = len(flowerbed)

        if totalSpots == 1:
            if n > 0:
                return not flowerbed[0]
            else:
                return True
        for index in range(len(flowerbed)):
            if not flowerbed[index]:
                if index == 0:
                    canFill = not flowerbed[index + 1]
                elif index == totalSpots - 1:
                    canFill = not flowerbed[index - 1]
                else:
                    canFill = not flowerbed[index - 1] and  not flowerbed[index + 1]

                if canFill:
                    availableSpots += 1
                    flowerbed[index] = 1
        return availableSpots >= n

if __name__ == '__main__':
    s = Solution()

    assert s.canPlaceFlowers([1,0,0,0,1], 1) == True
    assert s.canPlaceFlowers([1,0,0,0,1], 2) == False
    assert s.canPlaceFlowers([0,0,1,0,1], 1) == True
    assert s.canPlaceFlowers([1,0,0,0,1,0,0], 2) == True
    assert s.canPlaceFlowers([0,0,1,0,0], 1) == True
    assert s.canPlaceFlowers([0], 1) == True
    assert s.canPlaceFlowers([1], 0) == True
    assert s.canPlaceFlowers([1], 0) == True
    assert s.canPlaceFlowers([1], 1) == False

