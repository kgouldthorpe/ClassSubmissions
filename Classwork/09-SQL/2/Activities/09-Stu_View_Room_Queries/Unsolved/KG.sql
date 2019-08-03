select title,
select count(film_id) from inventory as "Inventory Count"
where film_id in
(
	select film_id from film
	group by title
	order by title ASC
);