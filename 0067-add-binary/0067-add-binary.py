class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Rules:
        #   0 + 0 = 0
        #   0 + 1 = 1
        #   1 + 0 = 0
        #   1 + 1 = 1
        # if two 1's -- there needs to be a carryover

        result = ""

        if len(a) < len(b):
            a = a.rjust(len(b),'0')
        if len(b) < len(a):
            b = b.rjust(len(a),'0')

        a = a[::-1]
        b = b[::-1]

        carryover = '0'
        for i in range(len(a)):
            a_bit = a[i]
            b_bit = b[i]

            if a_bit == b_bit:
                c = '0'
            else:
                c = '1'

            if c == carryover:
                d = '0'
            else:
                d = '1'

            result = d + result
            
            if (a_bit == '1' and b_bit == '1') or (c == '1' and carryover == '1'):
                carryover = '1'
            else:
                carryover = '0'
            
        if carryover == '1':
            result = carryover + result
        
        return result
                
