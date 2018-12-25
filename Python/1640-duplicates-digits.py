# Given an integer n, return the count of numbers that is less than
# or equal to n, and have duplicates digits.

# Refer to Leetcode 357 Count Numbers with Unique Digits

class Solution:
    """
    @param n: The integer n.
    @return: The count of numbers that <= n and have duplicates digits.
    """
    def countNumbers(self, n):
        s=str(n)
        bit=len(s)
        unique=self.countunique(bit-1)
        if bit > 10: # no longer need to consider number > 9999999999
            return n - unique

        # consider numbers with same leading digits
        li=[] # used digits
        for i in range(bit-1):
            head=int(s[i])
            lessvalue=len([x for x in li if x<head])
            # cal is the count of usable digits (multiple) in current position
            if i==0:
                cal=max(head - lessvalue -1, 0) # digit 0 cannot used as beginning
            else:
                cal=max(head - lessvalue ,0)
            unique += cal*self.certainbitunifollow(i,bit-i-1)
            if head not in li:
                li.append(head)
            else:
                return n-unique



        if len(set(list(s[:-1] )) )!=len(list(s[:-1] )): # given s (except last digit) has duplicate
            return n-unique

        head=int(s[-1])
        for i in range(head+1):
            if i not in li:
                unique +=1

        return n-unique

    def countunique(self ,bit):
        if bit == 0: return 0

        count, fk = 9, 9
        for k in xrange(2, min(bit+1,11)):
            fk *= 10-(k-1)
            count += fk
        return count
        '''
        c=0
        for i in range(1,min(bit+ 1,11)):
            c = c+self.certainbitunique(i)
        return c

    def certainbitunique(self,i):
        if i==1:
            return 9
        c=9
        start=9
        for j in range(i-1):
            c=c*start
            start-=1
        return c
        '''

    def certainbitunifollow(self,i,bit):
        if bit==0:
            return 1
        c=1
        start=9-i
        for j in range(bit):
            c=c*start
            start=start-1
        return c

print(Solution().countNumbers(21)) # 1
print(Solution().countNumbers(100)) # 10
print(Solution().countNumbers(4567)) # 2060
