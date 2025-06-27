-- SQL script that computes and store the average score
-- for a student. Note: An average score can be a decimal

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE avg_score FLOAT;
	SELECT AVG(score) INTO avg_score FROM corrections AS p WHERE p.user_id = user_id;
	UPDATE users SET average_score = avg_score WHERE id = user_id;
END $$
DELIMITER ;
