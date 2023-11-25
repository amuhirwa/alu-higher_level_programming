-- Shows count of groups of scores
SELECT score, COUNT(score) as number FROM second_table
GROUP BY score ORDER BY COUNT(score) DESC;
