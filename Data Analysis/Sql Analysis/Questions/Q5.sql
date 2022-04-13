SELECT a.ArtistId,
       a.Name,
       Count(*) AS Songs
FROM Artist a
JOIN Album m ON a.ArtistId =m.ArtistId
JOIN Track t ON t.AlbumId=m.AlbumId
JOIN Genre g ON t.GenreId=g.GenreId
WHERE g.Name='Rock'
GROUP BY 1,
         2
ORDER BY 3 DESC
LIMIT 10;