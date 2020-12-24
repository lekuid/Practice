def n(nums, k):
    for y in nums:
        for x in nums:
            while k == x+y:
                return True


print(n([1,3,4,9,21,37,53,4,6], 5646))