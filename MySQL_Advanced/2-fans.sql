-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT origin, nb_fans FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
