"""
Recently, I encountered an interview question whose description was as below:

The number 89 is the first integer with more than one digit whose digits when raised up to consecutive powers give the same 
number. For example, 89 = 8**1 + 9**2 gives the number 89. 

The next number after 89 with this property is 135 = 1**1 + 3**2 + 5**3 = 135.

Write a function that returns a list of numbers with the above property. The function will receive range as parameter.
"""

def sum_of_digits_of_pow(x,y):
    
    result = []
    
    
    for i in range(x,y + 1):
        exponential = 1
        sum = 0
        string_of_number = str(i)
        seperated_digits = list(map(int, string_of_number))
        
        for k in seperated_digits:
            sum = sum + ( k ** exponential)
            exponential += 1
            
        if sum == i:
            result.append(i)
        
    return result
print(sum_of_digits_of_pow(88,4000))
     
     
        
        
    
    
    
