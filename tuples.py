
# are similar to lists but they are immutable - meaning cannot be modified(cannot add or remove items e.t.c)
# they use () brackets

# ********************************* UNPACKING ************************************************
# Powerful feature in python
# can also be used in lists
# given below a tuple and want to use the items inside

cordinates = (1, 2, 3)
# instead of using indexes............

print(cordinates[0] * cordinates[1] * cordinates[2])

# then use UNPACKING feature instead

x, y, z = cordinates
print(x * y * z)
