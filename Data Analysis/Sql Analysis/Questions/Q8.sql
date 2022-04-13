SELECT NAME,
       Milliseconds
FROM Track
WHERE Milliseconds>
    (SELECT AVG(Milliseconds)
     FROM Track)
ORDER BY 2 DESC;