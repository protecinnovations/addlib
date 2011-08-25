-- Create the changelog table that will keep track of changes to the database

CREATE TABLE `addlib_log` (
  `id` INT  NOT NULL AUTO_INCREMENT,
  `change_name` TEXT  NOT NULL,
  `action` ENUM('DO', 'UNDO')  NOT NULL,
  `timestamp` INT  NOT NULL,
  `was_redo` INT(1)  NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
)
ENGINE = MyISAM;

