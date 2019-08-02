-- drop table if exists wordassociation_AC;
	
-- create table wordassociation_AC(
-- 	author INT,
-- 	word1 varchar,
-- 	word2 varchar,
-- 	source varchar(10)
-- );
-- select * from wordassociation_AC;

-- select * from wordassociation_AC;
-- select * from wordassociation_AC
-- 	where word1 = 'stone';
-- select * from wordassociation_AC
-- 	where author between 0 and 10;
-- select * from wordassociation_AC
-- 	where word1 = 'pie' or word2 = 'pie';

select * from wordassociation_AC;
select * from wordassociation_AC where source = 'BC' and author between 333 and 335;
