WITH t1 AS
  (SELECT COUNT(*) AS Purchases,
          i.BillingCountry,
          g.Name,
          g.GenreId
   FROM Invoice i
   JOIN InvoiceLine l ON i.InvoiceId=l.InvoiceId
   JOIN Track t ON t.TrackId=l.TrackId
   JOIN Genre g ON g.GenreId=t.GenreId
   GROUP BY 2,
            3,
            4
   ORDER BY 2),
     t2 AS
  (SELECT MAX(Purchases) AS Purchases,
          BillingCountry
   FROM t1
   GROUP BY 2
   ORDER BY 2)
SELECT t1.*
FROM t1
JOIN t2 ON t1.Purchases=t2.Purchases
AND t1.BillingCountry=t2.BillingCountry