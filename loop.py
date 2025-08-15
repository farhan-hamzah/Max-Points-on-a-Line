from typing import List
from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        res = 0
        for i in range(n):
            slopes = defaultdict(int)
            duplicates = 0
            cur_max = 0
            x1, y1 = points[i]
            
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                
                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue
                
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                
                # Normalisasi tanda supaya slope konsisten
                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1
                
                slopes[(dx, dy)] += 1
                cur_max = max(cur_max, slopes[(dx, dy)])
            
            res = max(res, cur_max + duplicates + 1)
        
        return res
