SELECT competitor.name,scores.score
FROM competitor
INNER JOIN scores ON competitor.id = scores.id
WHERE scores.round = 3
ORDER BY scores.score DESC