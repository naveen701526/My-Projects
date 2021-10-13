class Solution:
    def fizzBuzz(self, n: int) -> [str]:
        ans, num1, num2, bothTrue, firstTrue, secondTrue = [0]*n, 3, 5, "FizzBuzz", "Fizz", "Buzz"
        for i in range(1,n+1):
            first, second = i % num1 == 0, i % num2 == 0
			
            if first and second: ans[i-1] = bothTrue
            elif first:          ans[i-1] = firstTrue
            elif second:         ans[i-1] = secondTrue
            else:                ans[i-1] = str(i)
			
        return ans
        
opt = Solution()
print(opt.fizzBuzz(3))
