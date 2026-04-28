#introduction to list datatype
nums = [1,2,3,4,5]
print(type(nums))
print(nums)

for num in nums:
    print(num)

nums.append(10)
for num in nums:
    print(num)

print(f"Length of nums: {len(nums)}")

print(f"Length if nums: {len(nums)}")

person = {"fn":"Bob", "ln":"Smith","age":23}

print(type(person))
print(person)

print(person["fn"])

#List of people
people = [
    {"fn":"Bob", "ln":"Smith","age":23},
    {"fn":"Alice", "ln":"Timmons","age":32},
    {"fn":"Katherine", "ln":"Jones","age":21}
]
people[0]['fn'] = "Tim"

for person in people:
    print(person)

people.append({"fn":"Philip", "ln":"Smith","age":25})

print(people)