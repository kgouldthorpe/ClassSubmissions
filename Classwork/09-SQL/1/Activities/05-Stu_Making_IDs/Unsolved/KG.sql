drop table programming_language

create table programming_language(
	id serial primary key,
	language varchar(20) not null,
	rating INT
);

insert into programming_language (language, rating)
values ('HTML', 95),
		('JS', 99),
		('JQuery', 98),
		('MySQL', 70),
		('MySQL', 70);
select * from programming_language;
select * from programming_language
	where language = 'MySQL';
delete from  programming_language
	where id = 5;
select * from programming_language;
update programming_language
	set id =45, language = 'Python', rating = 85;
select * from programming_language;

alter table programming_language
add column mastered boolean default true;