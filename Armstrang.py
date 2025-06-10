#Armstrang 
#Show whether a given integer N is an Armstrong number or not.
def ArmstrongNumber(N):
    #Convert the number to a string to calculate the number of digits
    num_str = str(N)
    num_digits = len(num_str)
    # Initialize the sum of digits
    sum_of_digits = 0
    # Calculate the sum of the digits raised to the power of the number of digits
    for digit in num_str:
        sum_of_digits += int(digit) ** num_digits
    # Check if the sum of digits is equal to the original number
    if sum_of_digits == N:
        return "Yes"
    else:
        return "No"
    




# Driver Code
print(ArmstrongNumber(153))
print(ArmstrongNumber(200))
print(ArmstrongNumber(371))


#
#Example 1:
#
#Input:
#
#N = 153
#Output:
#
#Yes
#
#Example 2:
#
#Input:
#
#N = 199
#Output:
#
#No
#Constraints
#Print Yes if the number is Armstrong, else, print No.