SELECT DISTINCT c.Email,
                c.FirstName,
                c.LastName,
                g.Name AS Genre
FROM Customer c
JOIN Invoice i ON c.CustomerId=i.CustomerId
JOIN InvoiceLine l ON i.InvoiceId = l.InvoiceId
JOIN Track t ON t.TrackId=l.TrackId
JOIN Genre g ON t.GenreId=g.GenreId
WHERE g.Name='Rock'
ORDER BY 1 ;