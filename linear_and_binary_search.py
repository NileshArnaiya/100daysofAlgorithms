#linear search

def linear_search(array, query):
    for i in range(len(array)):
        if array[i] == query:
            return i
            
#binary search

def binary_search(array,query):
    array.sort()
    start,end = 0, len(array)-1
    while start<= end:
        mid = (start + end) // 2
        value = array[mid]
        if value==query:
            return mid
        elif value < query:
            start = mid + 1
        elif value > query:
            end = mid - 1
    return None
    
    
print(binary_search([3,2,8,4,5,6,7],2))
