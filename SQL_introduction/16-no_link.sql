-- List all records whose name value isn't null
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
