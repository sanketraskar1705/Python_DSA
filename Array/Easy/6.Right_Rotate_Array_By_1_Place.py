# Right rotate array by 1 place

""" Method 1"""
#  - Using list slicing
# IMPORTANT NOTE:
# SLICING DOES NOT MODIFY THE ORIGINAL LIST
# It CREATES A NEW LIST in memory
# So after slicing + concatenation:
# → arr gets a NEW MEMORY ADDRESS
# → old list is discarded

arr = [1, 28, 33, 4, -5, 6, 71, 8, 9]
n = len(arr)

print(id(arr))   # Address of ORIGINAL list

# SLICING CREATES A NEW LIST (NOT IN-PLACE)
# That's why memory address changes after this line
arr = arr[-1:] + arr[0:n-1]

print(arr)
print(id(arr))   # DIFFERENT address → new list created

# To avoid this problem
"""Solution"""


print(id(arr))   # original address

# arr[:] means: modify the SAME list, not create a new reference
arr[:] = arr[-1:] + arr[:-1]

print(arr)
print(id(arr))   # SAME address ✅

# arr[:] updates the CONTENT of the list
# NOT the reference
# So memory address REMAINS SAME

"""Method 2"""
# Loop (for)
temp =arr[n-1]
for i in range(n-2,-1,-1):
    arr[i+1] = arr[i]

arr[0] = temp

print(arr)
