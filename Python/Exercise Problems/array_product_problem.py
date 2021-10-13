def array_product_problem(array, length):
    output = [1]*length
    
    for index in range(1, length):
        output[index] = array[index - 1] * output[index - 1]
        
        
    right = 1
    
    for index in range(length - 1, -1, -1):
        output[index] *=  right
        right *= array[index]
        
    return output
        
        
        
        
print(array_product_problem([1,2,3,4], 4))

# time complexity: O(n)
# space complexity: O(1)
