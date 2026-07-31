SELECT competitor.name, ROUND(AVG(scores.score),2) AS mean
FROM competitor join scores on competitor.id = scores.id
GROUP BY competitor.id
ORDER BY competitor.name ASC