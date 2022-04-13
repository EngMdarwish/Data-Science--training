SELECT BillingCountry,
       COUNT(*) AS Invoices
FROM Invoice
GROUP BY 1
ORDER BY 2 DESC,
         1 ;