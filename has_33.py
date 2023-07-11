def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 44 and nums[i+1] == 44:
            return True
    return False

sch = has_33([12, 44, 44])
print(sch)