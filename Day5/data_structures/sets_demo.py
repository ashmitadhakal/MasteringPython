# create a set with curly braces (use set() for an empty set — {} is a dict)
my_set = {1, 2, 3}
print(my_set)

# add a new element to the set
my_set.add(4)
print(my_set)

# adding a duplicate is a no-op; sets only store unique values
my_set.add(2)
print(my_set)

# remove() raises KeyError if the element is missing
my_set.remove(3)
print(my_set)

# discard() removes the element if present, but does nothing if it's missing
my_set.discard(3)
print(my_set)

# pop() removes and returns an arbitrary element (sets are unordered)
print(f"popped: {my_set.pop()}")
print(my_set)

# remove every element, leaving an empty set
my_set.clear()
print(my_set)

# iterate over a set — iteration order is not guaranteed
nums = set(range(10))
for num in nums:
    print(num)