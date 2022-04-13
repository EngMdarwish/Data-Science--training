WITH t1 AS
  (SELECT i.BillingCountry AS Country,
          SUM(i.Total)AS TotalSpent,
          c.FirstName,
          c.LastName,
          c.CustomerId
   FROM Customer c
   JOIN Invoice i ON i.CustomerId=c.CustomerId
   GROUP BY 1,
            3,
            4,
            5
   ORDER BY 1),
     t2 AS
  (SELECT Country,
          MAX(TotalSpent) TotalSpent
   FROM t1
   GROUP BY 1
   ORDER BY 2)
SELECT t1.*
FROM t1
JOIN t2 ON t1.Country=t2.Country
AND t1.TotalSpent=t2.TotalSpent
ORDER BY 1 ;