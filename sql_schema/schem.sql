CREATE TABLE IF NOT EXISTS `score_table` 
(
    'user_id': 'FLOAT NOT NULL',
    'promo2': 'INT NOT NULL',
    'customers': 'INT NOT NULL',
    'ales': 'INT DEFAULT NULL',
    PRIMARY KEY (`user_id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;