-- only with score above or equal 10

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score  DESC;
