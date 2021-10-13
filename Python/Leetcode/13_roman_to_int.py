# https://leetcode.com/problems/roman-to-integer/
def romanToInt( s: str) -> int:
    symbols_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    integer_value = 0
    current = 0
    previous = 0
    for i in range(len(s)):
        current = symbols_values[s[i]]
        if current > previous:
            integer_value += current - 2*previous
        else:
            integer_value += current
        previous = current
    return integer_value
    
    
print(romanToInt('III'))
        
