--Average Cost to rent a movie
select avg(rental_rate)as "Avg Rate"
from film;

--Average cost to rent a movie by rating group
select rating, avg(rental_rate) as "Avg Rate"
from film
group by rating;

--Cost to replace all films
select sum (replacement_cost) as "Replacement Cost"
from film;

--Cost to replace all films in each rating group
select rating, sum(replacement_cost) as "Replacement Cost"
from film
group by rating;

--Length of longest movie
select max(length) as "Longest Movie"
from film;

--Length of shortest movie
select min(length) as "Shortest Movie"
from film;