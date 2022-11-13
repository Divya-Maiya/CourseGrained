SET sql_safe_updates = FALSE;
USE defaultdb;
CREATE DATABASE IF NOT EXISTS coursegrained;

USE coursegrained;

--INSERT INTO coursereviews (coursename, professor, semester,courseload,reviews,industryroles,prereqs,difficulty)
  --VALUES ('520:Introduction to Software Engineering Practices', 'Heather Conboy', 'FALL 2022',3.5,'Amazing class, learned git','SDE','Java',4);
--INSERT INTO profreviews (profname,classtaken,semester,rating,reviews)
  --VALUES('Heather Conboy','520:Introduction to Software Engineering Practices','FALL 2022',4,'Great Prof');
--INSERT INTO coursecatalog(coursename,department,courseurl,description)
    --VALUES('520:Introduction to Software Engineering Practices','CICS','https://people.cs.umass.edu/~hconboy/class/2022Fall/CS520/','Learn software engineering practices');
--INSERT INTO professors(profname,pagelink,department)
    --VALUES('Heather Conboy','https://people.cs.umass.edu/~hconboy/class/2022Fall/CS520/','CICS');
INSERT INTO courseinterest(coursename,emailID,phone)
    VALUES('520:Introduction to Software Engineering Practices','xyz@umass.edu','1234567891');