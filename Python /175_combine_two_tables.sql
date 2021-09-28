# Write your MySQL query statement below
SELECT P.FirstName, P.LastName, A.City, A.State
FROM Person P
LEFT JOIN Address A ON A.PersonId=P.PersonId
