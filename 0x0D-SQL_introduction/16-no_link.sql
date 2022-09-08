-- this displays all the record except null NAMES

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
