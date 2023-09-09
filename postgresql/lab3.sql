 TABLE levell(STUDENT_ID INTEGER PRIMARY KEY,NAME VARCHAR(100));
CREATE TABLE STUDENT(STUDENT_ID INTEGER PRIMARY KEY,NAME VARCHAR (100),EMAIL TEXT,PHONE INTEGER, LEVEL_ID INTEGER REFERENCES levell (STUDENT_ID),age integer,track text);
CREATE TABLE EXAM (STUDENT_ID INTEGER PRIMARY KEY,DATEE DATE);
CREATE TABLE SUBJECT(STUDENT_ID INTEGER PRIMARY KEY,NAME VARCHAR (100),SUB_DESC TEXT,MAX_SCORE INTEGER);
CREATE TABLE STU_SUBJECTS(STU_ID INTEGER  REFERENCES STUDENT(STUDENT_ID),SUB_ID INTEGER REFERENCES SUBJECT(STUDENT_ID),PRIMARY KEY(STU_ID,SUB_ID));
CREATE TABLE STU_GRADES(STU_ID INTEGER  REFERENCES STUDENT(STUDENT_ID),SUB_ID INTEGER REFERENCES SUBJECT(STUDENT_ID),PRIMARY KEY(STU_ID,SUB_ID),GRADE INTEGER);
insert into levell (student_id,name) values (1,'one'),
(2,'two'),(3,'three');
    alter table student
    add COLUMN gender text;
    alter table student
    add COLUMN birth_d DATE;
    INSERT INTO student (STUDENT_ID,name, email, phone, level_id,birth_d,gender,age,track)
VALUES
    (1,'John Doe', 'john@example.com', '123790', 1,'2000-12-12','MALE',13,'python'),
    (2,'Alice Adams', 'alice@example.com', '9810', 2,'1990-12-10','FEMALE',18,'IOT'),
    (3,'Bob Smith', 'bob@example.com', '55567', 3,'1980-09-08','MALE',19,'AI');
    INSERT INTO SUBJECT(STUDENT_ID,NAME,SUB_DESC,MAX_SCORE) VALUES(1,'ENGLISH','EXCELLENT',90),
    (2,'ARABIC','GOOD',70),(3,'MATH','VERY GOOD',80);
    alter table student
    add constraint fk_id
    foreign key (level_id)
    REFERENCES levell (student_id);
    select name from student
    where name like 'A%';
    SELECT * FROM STUDENT
    WHERE birth_d <'1991-10-01' AND gender='MALE';
    SELECT S.NAME FROM STUDENT S
    INNER JOIN (SELECT STUDENT_ID FROM SUBJECT 
    ORDER BY MAX_SCORE DESC 
    LIMIT 1 OFFSET 2)E ON S.STUDENT_ID=E.STUDENT_ID;
    SELECT S.NAME,L.NAME FROM STUDENT S INNER JOIN
    LEVELL L ON S.STUDENT_ID=L.STUDENT_ID;
	create view stu_data as SELECT NAME,TRACK FROM STUDENT;
	SELECT NAME,AGE FROM STUDENT;
	CREATE FUNCTION MULTIPLY(INPUTA INTEGER ,INPUTB INTEGER)
	RETURNS INT
	AS  $$
	BEGIN
	RETURN INPUTA*INPUTB;
	END;
	$$ LANGUAGE plpgsql;
	SELECT MULTIPLY(8,9) AS RESULT;
  CREATE OR REPLACE FUNCTION RETRIVE(TRACK_O TEXT)
RETURNS TABLE (STUDENT_N VARCHAR(100)) AS $$
BEGIN
    RETURN QUERY
SELECT S.NAME
    FROM STUDENT S
    INNER JOIN LEVELL L ON S.LEVEL_ID = L.STUDENT_ID
    WHERE L.NAME = TRACK_O;
END;
$$ LANGUAGE plpgsql;
SELECT RETRIVE('one')AS NAMEB;
SELECT * FROM STUDENT;
SELECT * FROM LEVELL;
create view scored as select l.name as levelname,s.name as studentname
from student s inner join levell l on s.level_id=l.student_id;
create function agec(birth_d date)
returns INTEGER
as $$
begin
 RETURN EXTRACT(YEAR FROM age(date(now()), birth_d));
end;
$$ language plpgsql;
select agec('2003-12-23') as d;
select name,agec(birth_d)from student;







 

	
	
	
	
	
	
	