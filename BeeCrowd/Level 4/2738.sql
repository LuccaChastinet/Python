SELECT candidate.name,
    round((score.math*2 + score.specific*3 + score.project_plan*5) / 10.0, 2)
    AS avg FROM candidate, score
    WHERE candidate.id = score.candidate_id ORDER BY avg DESC;