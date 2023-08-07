class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        if len(nums) < 3:
            return list(set(nums))

        t = len(nums) // 3
        dic = {}
        res = set()

        for n in nums:
            if dic.get(n):
                dic[n] += 1
            else:
                dic[n] = 1
            if dic[n] > t:
                res.add(n)

        return list(res)
        '''
        num1, num2 = None, None
        cnt1, cnt2 = 0, 0

        for n in nums:
            if n == num1:
                cnt1 += 1
            elif n == num2:
                cnt2 += 1
            elif cnt1 == 0:
                num1 = n
                cnt1 = 1
            elif cnt2 == 0:
                num2 = n
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1, cnt2 = 0, 0
        for n in nums:
            if n == num1:
                cnt1 += 1
            elif n == num2:
                cnt2 += 1

        l = len(nums)
        res = []
        if cnt1 > l // 3:
            res.append(num1)
        if cnt2 > l // 3 and num1 != num2:
            res.append(num2)

        return res