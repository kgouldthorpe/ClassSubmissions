--#1 actor in Alter Victory
select first_name, last_name
from actor 
where actor_id in
(
	select actor_id 
	from film_actor
	where film_id in
	(
		select film_id 
		from film
		where title = 'ALTER VICTORY'
	)
);

--#2 Jon Stephens rented to customer
select title
from film 
where film_id in
(
	select film_id
	from inventory
	where inventory_id in
	(
		select inventory_id
		from rental
		where staff_id in
		(
			select staff_id
			from staff
			where first_name = 'Jon' AND last_name = 'Stephens'
		)
	)
);