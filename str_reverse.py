nums = [0, 0, 0, 0, 1, 0, 1, 1, 0, 2, 3 ,4 ,5]
r_num = 0
while r_num in nums:
    nums.remove(r_num)
print(nums)
# print(list(filter(None, nums)))
# for i in nums:
#     if i != 1:
#         r_num.append(i)
# print(r_num)