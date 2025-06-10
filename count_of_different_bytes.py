#count of different bytes
#You are provided with an array  arr containing non_negative integers. The task is to calculate the difference between 
# the bits when converted to binary.

def count_differing_bits(arr):
    def count_ones(x):
        return bin(x).count('1')
    
    n = len(arr)
    result = []
    # Count differing bits between first and last element
    first_last_diff = arr[0] ^ arr[-1]
    result.append(count_ones(first_last_diff))
    
    # Count differing bits between consecutive pairs
    for i in range(n - 1):
        diff = arr[i] ^ arr[i + 1]
        result.append(count_ones(diff))    
    return result

# Example 1
arr = [17, 8, 11, 14]
print(count_differing_bits(arr))
# output: [5, 3, 2, 2]
   
#Exaple 2
arr=[20,8,20,6]
print(count_differing_bits(arr))
#output: [2,3,3,2]
