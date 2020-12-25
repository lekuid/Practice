'''Given an array of integers, return a new array such that each 
element at index i of the new array is the product of all the 
numbers in the original array except the one at i.'''

import numpy as np

def prod(nums):
    pos = 0
    nums_temp = nums[:]
    product = []
    while pos < len(nums)+1:
        nums = nums_temp[:]
        nums.pop(pos)
        product.append(np.product(nums))
        pos+=1
    return product

print(prod([7,1,2,3,2,9]))