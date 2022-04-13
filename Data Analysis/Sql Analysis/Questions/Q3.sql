SELECT c.CustomerId,
       SUM(i.total)
FROM Customer c
JOIN Invoice i ON c.CustomerId=i.CustomerId
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;