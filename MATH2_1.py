#MATH
#Build an algorithm that could construct a rectangle in which area and perimeter are given. 
# The length of the rectangle should not exceed the width of the rectangle.

import numpy as np
class Solution:
   def constructrectangle(self,area,perimeter):
      discriminant = perimeter**2 - 16*area
      # Check if discriminant is non-negative to avoid complex results
      if discriminant < 0:
         return None
      length = (perimeter + np.sqrt(discriminant)) / 4
      width = area / length          # Ensure width does not exceed length
      if length >= width :
         return length, width
      else:
         return None
                               
 
# Driver Code
obj = Solution()
#Example 1
print(obj.constructrectangle(12,14))
#Output: (4, 3)
#Example 2
print(obj.constructrectangle(22,26))
#Output: (11, 2)
#Example 3
print(obj.constructrectangle(36,20))
#Output: None

