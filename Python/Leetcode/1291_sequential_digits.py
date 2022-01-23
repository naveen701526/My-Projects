class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        seq = "123456789"
        low_str = str(low)
        high_str = str(high)
        low_length = len(low_str)
        high_length = len(high_str)
        result = []
        
        while low_length <= high_length:
            for i in range(1, 10 - low_length + 1):
                start = i-1
                end = start + low_length
                number = int(seq[start:end])
                if number <= high and number >= low:
                    result.append(number)
                elif number > high:
                    return result
            
            low_length += 1
        
        return result
