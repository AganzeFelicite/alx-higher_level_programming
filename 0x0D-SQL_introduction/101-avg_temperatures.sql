-- this is to get the average temperatures of the states
SELECT city,  AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
