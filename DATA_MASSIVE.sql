INSERT INTO users (second_name, first_name, last_name)
VALUES
  ('Orson', 'Gunner', 'Garrett'),
  ('Cash', 'Newt', 'Causer'),
  ('Clint', 'Rodolph', 'Pierce'),
  ('Romilly', 'Everette', 'Vipond'),
  ('Basil', 'Rowen', 'Murgatroyd'),
  ('Quinlan', 'Sheldon', 'Wyatt'),
  ('Cosmo', 'Jensen', 'Woolf'),
  ('Gresham', 'Barney', 'Rose'),
  ('Sanford', 'Oz', 'Clement'),
  ('Merv', 'Gerrard', 'Glass'),
  ('Scout', 'Abraham', 'Gray'),
  ('Dex', 'Zackery', 'Hammond'),
  ('Nathan', 'Gregg', 'Brittain'),
  ('Sequoia', 'Zak', 'Cokes'),
  ('Grover', 'Ashton', 'Franklyn'),
  ('Austen', 'Keefe', 'Irvine'),
  ('Madison', 'Elton', 'Dabney'),
  ('Gerald', 'Darrell', 'Lowry'),
  ('Scott', 'Legend', 'Corey'),
  ('Sterling', 'Roman', 'Clemens'),
  ('Gorden', 'Bryson', 'Jakeman'),
  ('Malakai', 'Colin', 'Warren'),
  ('Amos', 'Gift', 'Kinsley'),
  ('Wendell', 'Jake', 'Penny'),
  ('Benj', 'Cassidy', 'Holme');


INSERT INTO courses (title, price, description)
VALUES
	('Programming for Everybody', 10000, 'This course aims to teach everyone the basics of programming computers using Python. We cover the basics of how one constructs a program from a series of simple instructions in Python.  The course has no pre-requisites and avoids all but the simplest mathematics. Anyone with moderate computer experience should be able to master the materials in this course. This course will cover Chapters 1-5 of the textbook “Python for Everybody”.  Once a student completes this course, they will be ready to take more advanced programming courses. This course covers Python 3.'),
	('Foundations of Cybersecurity', 12500, 'This is the first course in the Google Cybersecurity Certificate. These courses will equip you with the skills you need to prepare for an entry-level cybersecurity job. In this course, you will be introduced to the world of cybersecurity through an interactive curriculum developed by Google. You will identify significant events that led to the development of the cybersecurity field, explain the importance of cybersecurity in today\'s business operations, and explore the job responsibilities and skills of an entry-level cybersecurity analyst.'),
	('Meta Back-End Developer', 15000, 'Ready to gain new skills and the tools developers use to create websites and web applications? This certificate, designed by the software engineering experts at  Meta—the creators of Facebook and Instagram, will prepare you for an entry-level career as a back-end developer.'),
	('Developing Applications with Google Cloud', 7000, 'In this specialization, application developers learn how to design, develop, and deploy applications that seamlessly integrate managed services from Google Cloud. Through a combination of presentations, demos, and hands-on labs, participants learn how to use Google Cloud services and pre-trained machine learning APIs to build secure, scalable, and intelligent cloud-native applications. Learners can choose to complete labs in their favorite language: Node.js, Java, or Python.'),
	('Google Cloud Fundamentals', 13500, 'Google Cloud Fundamentals: Core Infrastructure introduces important concepts and terminology for working with Google Cloud. Through videos and hands-on labs, this course presents and compares many of Google Cloud\'s computing and storage services, along with important resource and policy management tools.'),
	('Indigenous Canada', 6000, 'Indigenous Canada is a 12-lesson Massive Open Online Course (MOOC) from the Faculty of Native Studies that explores the different histories and contemporary perspectives of Indigenous peoples living in Canada. From an Indigenous perspective, this course explores complex experiences Indigenous peoples face today from a historical and critical perspective highlighting national and local Indigenous-settler relations. Topics for the 12 lessons include the fur trade and other exchange relationships, land claims and environmental impacts, legal systems and rights, political conflicts and alliances, Indigenous political activism, and contemporary Indigenous life, art and its expressions.'),
	('The Modern World', 9000, 'This is a survey of modern history from a global perspective. Part One begins with the political and economic revolutions of the late 1700s and tracks the transformation of the world during the 1800s.  Part One concludes as these bewildering changes seem to be running beyond the capacity of older institutions to handle them.  Throughout the course we try to grasp what is happening and ask:  Why?  And the answers often turn on very human choices.');


INSERT INTO certificate (progress_pass, course_id, certificate_path)
VALUES
	(70, 1, '/certificates/certificate1.pdf'),
	(90, 2, '/certificates/certificate2.pdf'),
	(75.5, 3, '/certificates/certificate3.pdf'),
	(85, 4, '/certificates/certificate4.pdf'),
	(70, 5, '/certificates/certificate5.pdf'),
	(80, 6, '/certificates/certificate6.pdf'),
	(75, 7, '/certificates/certificate7.pdf');


INSERT INTO teachers (user_id, course_id, salary)
VALUES
	(1, 1, 12000),
	(5, 1, 13500),
	(2, 2, 10000),
	(3, 3, 11000),
	(5, 4, 9000),
	(8, 4, 9500),
	(12, 5, 10000),
	(13, 6, 13000),
	(20, 7, 12000),
	(25, 7, 5000);


INSERT INTO students (course_id, user_id, has_paid, progress, certificate_date)
VALUES
	(1, 2, false, 0, null),
	(1, 3, true, 63.7, null),
	(1, 4, true, 15.55, null),
	(1, 11, true, 93.07, '2023-05-05'),
	(1, 12, false, 0, null),
	(1, 7, true, 73, '2023-04-21'),
	(1, 6, true, 86.58, '2023-05-01'),
	(1, 10, true, 0, null),
	(1, 15, true, 100, '2023-05-10'),
	(2, 1, true, 0, null),
	(2, 3, true, 50, null),
	(2, 25, true, 35.67, null),
	(2, 24, true, 90.05, '2023-04-28'),
	(2, 23, true, 80.85, null),
	(2, 20, false, 0, null),
	(2, 15, true, 98.15, '2023-05-01'),
	(2, 4, true, 79.96, null),
	(3, 16, true, 10.5, null),
	(3, 10, false, 0, null),
	(3, 19, true, 50.5, null),
	(3, 13, true, 77, '2023-05-29'),
	(3, 21, false, 0, null),
	(3, 22, true, 65, null),
	(3, 14, true, 90.12, '2023-05-05'),
    (4, 4, true, 14, null),
    (4, 10, false, 0, null),
    (4, 23, true, 89.93, '2023-04-16'),
    (4, 1, false, 0, null),
    (4, 17, true, 19.54, null),
    (4, 15, true, 79.6, null),
    (4, 9, true, 85, '2023-05-02'),
    (4, 12, true, 91.01, '2023-04-20'),
    (5, 1, true, 97.9, '2023-04-29'),
    (5, 2, true, 60, null),
    (5, 6, true, 71.54, '2023-05-11'),
    (5, 15, false, 0, null),
    (5, 21, true, 70.51, '2023-04-30'),
    (6, 22, true, 0, null),
    (6, 20, false, 0, null),
    (6, 18, true, 81.02, '2023-05-01'),
    (6, 1, true, 98.92, '2023-04-25'),
    (6, 7, false, 0, null),
    (6, 24, true, 31, null),
    (7, 21, true, 13.23, null),
    (7, 19, true, 91.15, '2023-05-03'),
    (7, 13, true, 1.92, null),
    (7, 7, true, 39.02, null),
    (7, 2, true, 82.37, '2023-04-23'),
    (7, 1, true, 2.02, null),
    (7, 23, false, 0, null);
    