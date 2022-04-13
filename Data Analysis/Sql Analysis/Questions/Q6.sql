WITH t1 AS
  (SELECT a.Name,
          SUM(l.UnitPrice * l.Quantity) AS AmountSpent
   FROM Artist a
   JOIN Album m ON m.ArtistId=a.ArtistId
   JOIN Track t ON t.AlbumId=m.AlbumId
   JOIN InvoiceLine l ON t.TrackId=l.TrackId
   GROUP BY 1
   ORDER BY 2 DESC
   LIMIT 1)
SELECT a.Name,
       SUM(l.UnitPrice * l.Quantity) AS AmountSpent,
       c.CustomerId,
       c.FirstName,
       c.LastName
FROM Artist a
JOIN Album m ON m.ArtistId=a.ArtistId
JOIN Track t ON t.AlbumId=m.AlbumId
JOIN InvoiceLine l ON t.TrackId=l.TrackId
JOIN Invoice i ON i.InvoiceId=l.InvoiceId
JOIN Customer c ON c.CustomerId=i.CustomerId
WHERE a.NAME=
    (SELECT Name
     FROM t1)
GROUP BY 1,
         3,
         4,
         5
ORDER BY 2 DESC