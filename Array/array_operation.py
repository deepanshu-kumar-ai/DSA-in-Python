import array as arr
# 1)basic operation 
#   -create
#   -delete
#   -update
#   -select
# 2)common
#   -search
#   -insert
#   -traverse
# 3)special
#   -sort 
#   -meagre 


# ------->creating an array
arr1=arr.array("i",[1,2,3,4,5,6,7,1,3])
print(*arr1)

# ------>delet the array anas element
a=arr1.pop(2)
print(*arr1)

b=arr1.remove(3)  # it removes the duplicate vale if not duplicate in arra then give value error 
print(*arr1)

# Deleting an array
del arr1
print(arr1)

# 1)counting the array
count=arr1.count(3)
print(count)

# 2)length of  the array
len1=len(arr1)
print(len1)

# ------> Update an element
arr1[0] = 10
print(*arr1)

# ------> Select (Access) an element
print(arr1[3])

# ------> Search for an element
search_item = 5
if search_item in arr1:
    print(arr1.index(search_item))
else:
    print("Not found")

# ------> Insert an element
arr1.insert(2, 99)
print(*arr1)
    
# ------> Traverse (print all elements)
for i in arr1:
    print(i, end=" ")
print()

# ------> Sort the array
arr1 = arr.array("i", sorted(arr1))
print(*arr1)

# ------> Merge with another array
arr2 = arr.array("i", [50, 60, 70])
merged = arr1 + arr2
print(*merged)