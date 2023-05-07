-- MySQL Script generated by MySQL Workbench
-- Sun May  7 20:46:37 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema course_work
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema course_work
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `course_work` DEFAULT CHARACTER SET utf8 ;
USE `course_work` ;

-- -----------------------------------------------------
-- Table `course_work`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `course_work`.`users` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `second_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NULL,
  PRIMARY KEY (`user_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `course_work`.`courses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `course_work`.`courses` (
  `course_id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NOT NULL,
  `price` DECIMAL(8,2) NOT NULL,
  `description` VARCHAR(2048) NULL,
  PRIMARY KEY (`course_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `course_work`.`teachers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `course_work`.`teachers` (
  `teacher_id` INT NOT NULL AUTO_INCREMENT,
  `course_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `salary` DECIMAL(8,2) NULL,
  PRIMARY KEY (`teacher_id`),
  INDEX `teacher_course_fk_idx` (`course_id` ASC) VISIBLE,
  INDEX `teacher_user_fk_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `teacher_course_fk`
    FOREIGN KEY (`course_id`)
    REFERENCES `course_work`.`courses` (`course_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `teacher_user_fk`
    FOREIGN KEY (`user_id`)
    REFERENCES `course_work`.`users` (`user_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `course_work`.`students`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `course_work`.`students` (
  `student_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `course_id` INT NOT NULL,
  `has_paid` TINYINT NOT NULL,
  `progress` DECIMAL(5,2) NOT NULL DEFAULT 0,
  `certificate_date` DATE NULL,
  PRIMARY KEY (`student_id`),
  INDEX `student_user_fk_idx` (`user_id` ASC) VISIBLE,
  INDEX `student_course_fk_idx` (`course_id` ASC) VISIBLE,
  CONSTRAINT `student_user_fk`
    FOREIGN KEY (`user_id`)
    REFERENCES `course_work`.`users` (`user_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `student_course_fk`
    FOREIGN KEY (`course_id`)
    REFERENCES `course_work`.`courses` (`course_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `course_work`.`certificate`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `course_work`.`certificate` (
  `certificate_id` INT NOT NULL AUTO_INCREMENT,
  `progress_pass` DECIMAL(5,2) NOT NULL,
  `course_id` INT NOT NULL,
  `certificate_path` VARCHAR(256) NOT NULL,
  PRIMARY KEY (` certificate_id`),
  INDEX `certificate_course_fk_idx` (`course_id` ASC) VISIBLE,
  CONSTRAINT `certificate_course_fk`
    FOREIGN KEY (`course_id`)
    REFERENCES `course_work`.`courses` (`course_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;