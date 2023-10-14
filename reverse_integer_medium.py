class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        returns
        number = x
        if (x < 0):
            number = -x
        while(number > 0):
            array.append(number % 10)
            number = int(number/10)
        digits = len(array)
        for i in range(digits):
            number+=array[i] * 10**(digits - i-1)
        if(x<0):
            number = -number
        if(number > (2**31) - 1 or number < -2**31):
            return 0
        return number
