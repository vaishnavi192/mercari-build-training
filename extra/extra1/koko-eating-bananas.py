class Solution(object):
    def minEatingSpeed(self, piles, h):
        def canEatAll(piles, speed, h):
            hours = 0
            for bananas in piles:
                hours += (bananas + speed - 1) // speed
            return hours <= h
        
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if not canEatAll(piles, mid, h):
                left = mid + 1   
            else:
                right = mid       
        
        return left