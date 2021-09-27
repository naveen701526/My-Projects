class Solution:
    def normalizeDate(self, date):
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        year, month, days = [int(part) for part in date.split('-')]
        
        if not (1971 <= year <= 2100):
            return None
        
        result = 0
        for y in range(1971, year):
            result += sum(days_in_month)
            if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
                result += 1
                
        for m in range(1, month):
            result += days_in_month[m]
            if m == 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
                result += 1
            
        result += days      # days in the considered month
        return result
        
        
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        if not date1 or not date2: 
            return -1
        
        start, end = self.normalizeDate(date1), self.normalizeDate(date2)
        
        
        if start is None or end is None:
            return -1
        
        return abs(start - end)
        
opt = Solution()
print(opt.daysBetweenDates( date1 = "2019-06-29", date2 = "2019-06-30"))
