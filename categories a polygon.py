# categories a polygon
# check the angle of the given polygon and categorize it accordingly, either concave or convex.
# you are provided with an array of points containing the coordinates of the polygon.

class Solution:
    def checkConvex(self, arr):
        n = len(arr)
        if n < 3:
            return "Invalid"
        if n == 3 or n == 4:
            return "Convex"
        sign = 0
        for i in range(n):
            x1, y1 = arr[i]
            x2, y2 = arr[(i + 1) % n]
            x3, y3 = arr[(i + 2) % n]
            cross_product = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
            if cross_product != 0:
                current_sign = 1 if cross_product > 0 else -1
                if sign == 0:
                    sign = current_sign
                elif sign != current_sign:
                    return "concave"
        return "Convex"


# example1
# input
points = [[0, 0], [0, 8], [4, 4], [8, 8], [8, 0]]
obj = Solution()
print(obj.checkConvex(points))
# output: concave
# example2
# input
points = [[0, 0], [0, 8], [4, 10], [8, 8], [8, 0]]
print(obj.checkConvex(points))
# output: convex
# constraints: return convex for the convex polygon and concave for the concave polygon.
