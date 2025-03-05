
# defined by a [] bracket
names = ['paiz' , 'diana' , 'junior' , 'ali']

# operations on list
print(names)
print(names[0])
print(names[1: ])
print(names[1: 3])
print(names[-1])
print(names[ :3])
print(names[ : ])

print('   ')


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  METHODS IN LIST >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

names.append('king')
print(names)
# adds an item to the list

names.remove('junior')
print(names)
# removes an item from the list

names.pop()
print(names)
# removes the last value/character from the list

names.insert(0, 'cheche')
print(names)
# inserts a value at a specified index...in this case is index 0

names.reverse()
print(names)
# prints the list in reverse from last index to first

list2 = names.copy()
print(list2)
# copy's the list to list2...duplicates the list

names.sort()
print(names)
# sorts the list in an orderly format...in this case will sort in alphabetical order

names.clear()
print(names)
# clears the list


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




# given the list of numbers below ,,,find the maximum number in the list

nums = [4, 5, 7, 3, 13, 60, 20, 35]
max_no = nums[0]
for num in nums:
    if num > max_no:
        max_no = num
print(max_no)

# ninimum value
min_num = max_no
for mini in nums:
    if mini < min_num:
        min_num = mini
print(min_num)


# removing duplicates from the list

free = [5, 4, 7, 8, 5, 7, 9]
non_duplicate = []
for item in free:
    if item not in non_duplicate:
        non_duplicate.append(item)
print(non_duplicate)
