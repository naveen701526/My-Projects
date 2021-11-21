# Write your MySQL query statement below
SELECT w1.Id
FROM Weather w1, Weather w2
WHERE DATE_ADD(w2.RecordDate, INTERVAL 1 DAY) = w1.RecordDate
    AND w1.Temperature > w2.Temperature ;