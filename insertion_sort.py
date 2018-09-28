def insertion_sort(arr):
    
    for i in range(1,len(arr)):
        
        cursor = arr[i]
        position = i
        
        while position > 0 and arr[position-1] > cursor:
            arr[position] = arr[position-1]
            position = position - 1
            
        arr[position] = cursor
        
    return arr
    
print(insertion_sort([89,85,91,95,75,41,2,90]))

  
