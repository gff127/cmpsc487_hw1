-- Creating the table
CREATE Table card_swipes(
	s_id int,
	swipe_time timestamp,
	constraint  primary key (s_id, swipe_time)
 );



SET GLOBAL event_scheduler = ON; 

SET SQL_SAFE_UPDATES = 0; -- needed to allow delete

-- Every day, delete any records older than 5 years
DELIMITER //
CREATE EVENT old_records
ON SCHEDULE EVERY 1 DAY
DO
 BEGIN
	DELETE FROM card_swipes WHERE swipe_time <= current_timestamp() - INTERVAL 5 YEAR;
END//
DELIMITER ;