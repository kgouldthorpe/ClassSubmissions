--#1
--Count rows in city
select count(*)
from city;

--Count rows in Country
select count(*)
from country;

--Display as union with both information
select count(*)
from city

UNION

select count(*)
from country;

--#2
--Find out if data is comprable
select count(*)
from customer

UNION

select count(*)
from customer_list;

--They are the same so can join;
--Just joining
select customer_id as id
from customer

UNION

select id as id
from customer_list

order by id;

--Union all to see repeats
select customer_id as id
from customer

UNION ALL

select id as id
from customer_list

order by id;
