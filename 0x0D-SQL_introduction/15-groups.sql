-- this is to count similar scoreess

SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score;
