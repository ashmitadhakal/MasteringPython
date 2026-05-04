

nums=list(range(10))

even_nums=[]
for num in nums:
    if num % 2 == 0:
        even_nums.append(num)

print(even_nums)

even_nums = [num for num in nums if num % 2==0]
print(even_nums)
