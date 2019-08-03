--Find city id for each city in given list
select * from city
where city  in ('Qalyub', 'Qinhuangdao', 'Qomsheh', 'Quilmes');

--display district using subquieres
select * from address
where city_id in 
(
	select city_id from city
	where city in('Qalyub', 'Qinhuangdao', 'Qomsheh', 'Quilmes')
);

--Bonus
-- use subquiere first and last names of customers who reside in cities that start with Q
select first_name, last_name from customer
where address_id in
(
	select address_id from address
	where city_id in 
	(
		select city_id from city
		where city like 'Q%'
	)
);