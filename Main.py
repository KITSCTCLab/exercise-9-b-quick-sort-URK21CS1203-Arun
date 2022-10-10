from typing import List

def partition(data, low, high) -> List[int]:
    pivot = data[high]
    i = low-1 
    for j in range(low, high):
        if (data[j]<=pivot) :
            i+=1
            (data[i], data[j]) = (data[j], data[i])
    (data[i+1], data[high]) = (data[high], data[i+1])
    return i+1
    
def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)
    return array

input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(quick_sort(data, 0, len(data)-1))
