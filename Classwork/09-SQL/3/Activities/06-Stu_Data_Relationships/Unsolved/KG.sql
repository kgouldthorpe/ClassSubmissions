create table students(
id serial primary key,
first_name varchar(355),
last_name varchar(355));

insert into students (first_name, last_name)
values ('Kendall', 'Gouldthorpe');

select * from students;

create table courses(
id serial primary key,
course_name varchar(355));

insert into courses (course_name)
values ('Biology 101');

select * from courses;

create table junction_table(
student_id int not null,
foreign key (student_id) references students (id),
course_id int not null,
foreign key (course_id) references courses (id),
course_term varchar (355),
primary key (student_id, course_id));

insert into junction_table (student_id, course_id, course_term)
values (1,1,'Spring');

select * from junction_table;

--Many to many is appropriate

--Bonus Join tables
select students.id, students.first_name, students.last_name, courses.id, courses.course_name, junction_table.student_id, junction_table.course_id, junction_table.course_term
from junction_table
join students on students.id = junction_table.student_id 
join courses on courses.id = junction_table.course_id;


