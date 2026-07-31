SELECT competitor.name, SUM(scores.score) AS totality, (SUM(scores.score) > 250) AS qual
FROM competitor join scores on competitor.id = scores.id
GROUP BY competitor.id