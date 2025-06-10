#Operation on complex numbers
#Level: Intermediate
#You are provided with two strings containing complex numbers in the form of a+bi, 
# where a and b are real and a list of operations.
# The task is to perform those operations on the given strings.

class Solution:
    def ComplexnumOperation(self,complex1,complex2,operations):
        # Convert the complex numbers to their corresponding complex number objects
        real1 = float(complex1.split('+')[0])
        imag1 = float(complex1.split('+')[1].split('i')[0])
        real2 = float(complex2.split('+')[0])
        imag2 = float(complex2.split('+')[1].split('i')[0])                
               
        # Perform the operations on the complex numbers
        result = []
        for op in operations:
            if op == '+':
                real = real1 + real2
                imag = imag1 + imag2
            elif op == '-':
                real = real1 - real2
                imag = imag1 - imag2
            elif op == '*':
                real = real1 * real2 - imag1 * imag2
                imag = real1 * imag2 + real2 * imag1
            elif op == '/':
                real = (real1 * real2 + imag1 * imag2) / (real2*real2 + imag2*imag2)
                imag = (real2 * imag1 - real1* imag2) / (real2*real2 + imag2*imag2)                
                
            result.append(str(real) + '+' + str(imag) + 'i')
        return result     

#Example1
complex1 = "1+2i"
complex2 = "3+4i"
operations = ["*","+","-","/"]
obj=Solution()
print(obj.ComplexnumOperation(complex1,complex2,operations))
#output:['-5+10i','4+6i','-2+-2i','.44+..08i']
#Example2
complex1 = '0+2i'
complex2 = '3+4i'
operations = ['*','+','-','/']
print(obj.ComplexnumOperation(complex1,complex2,operations))
#output:['-8+6i','3+6i','-3+-2i','.32+.24i']