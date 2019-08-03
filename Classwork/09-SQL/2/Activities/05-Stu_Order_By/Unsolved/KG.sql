--count of actors first name ordered in descending order
select first_name, count(first_name) as "Actors FN"
from actor
group by first_name
order by "Actors FN" DESC;

--average rental duration for each rating rounded to 2 places and sorted in ascending order
select rating, round(avg(rental_duration),2) as "Rental Duration"
from film
group by rating
order by "Rental Duration" ASC;

--top 10 average replace costs for movies by length
select length, avg(replacement_cost) as "Replacement Cost"
from film
group by length
order by "Replacement Cost" ASC
limit 10;

--count of countries in descending order
select country.country, count(country.country) as "Country"
from city 
join country on city.country_id = country.country_id
group by country.country
order by "Country" ASC;