import random as rand
# quick sort in python 
arr=[2,5,1,0,4,6,7]
# quick_sort(arr)
# print("ptivot:",pivot)
# le=len(arr)
# print(le)

def quick_sort(arr):
    if len(arr) <=1:
        return arr
    
    pivot=rand.choice(arr)
    left= [ x for x in  arr if x < pivot]
    midle= [ x for x in  arr if x == pivot]
    right= [ x for x in  arr if x > pivot]

    return quick_sort(left)+midle+right

print(*quick_sort(arr))