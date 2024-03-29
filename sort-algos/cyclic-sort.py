'''
  @ used for arrays holding [1 to N] values
  @ N = len of unsorted array
  @ O(n) runtime
'''

def cyclic_sort(array):
  i = 0
  while i < len(array):
    val = array[i]
    if val-1 != i:
      array[i], array[val-1] = array[val-1], array[i]
    else:
      i += 1
  return array
