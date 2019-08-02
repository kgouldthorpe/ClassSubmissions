create table people(
	name varchar(30) not null,
	has_pet Boolean Default false,
	pet_type varchar(10) not null,
	pet_name varchar(30),
	pet_age int
);

insert into people (name, has_pet, pet_type, pet_name, pet_age)
values ('Jacob', true,'dog', 'Misty', 10),
	('Ahmed', true, 'rock', 'Rockington', 100),
	('Peter', true, 'cat', 'Franklin', 2),
	('Dave', true, 'dog', 'Queso', 1),
	('Dave', true, 'cat', 'Catty', 1);
select * from people;
select pet_name from people;
select name, pet_name from people limit 1;
select * from people
where pet_age<5 and pet_type = 'dog';

-- Recreate people table
drop table people;

create table people(
	id serial primary key,
	name varchar(30) not null,
	has_pet Boolean Default false,
	pet_type varchar(10) not null,
	pet_name varchar(30),
	pet_age int
);

insert into people (name, has_pet, pet_type, pet_name, pet_age)
	values ('Jacob', true,'dog', 'Misty', 10),
		('Ahmed', true, 'rock', 'Rockington', 100),
		('Peter', true, 'cat', 'Franklin', 2),
		('Dave', true, 'dog', 'Queso', 1),
		('Dave', true, 'cat', 'Catty', 1);
select * from people;
delete from people
	where id = 5;
select * from people;
update people
	set has_pet = true, pet_name = 'Rocket', pet_age = 8
	where id = 2;
select * from people;