-- 1. Create a Customer table
create table customer(
	id serial primary key,
	first_name varchar(255),
	last_name varchar(255));

-- 2. Populate that table
-- 'Bob Smith', 'Jane Davidson', 'Jimmy Bell', and 'Stephanie Duke'
insert into customer(first_name, last_name)
values ('Bob','Smith'),
	('Jane', 'Davidson'),
	('Jimmy', 'Bell'),
	('Stephanie', 'Duke');


-- 3. View Table
select * from customer;


-- 4.. Create Customer Email table
create table customer_email(
id serial primary key,
customer_id int not null,
email varchar(355),
foreign key (customer_id) references customer (id));

-- 5. Populate the second table
-- 'bobsmith@email.com', 'jdavids@email.com', 'jimmyb@email.com', 'sd@email.com'
insert into customer_email(customer_id,email)
values (1,'bobsmith@email.com'),
		(2,'jdavids@email.com'),
		(3,'jimmyb@email.com'),
		(4,'sd@email.com');

-- 6. View Table
select * from customer_email;

-- 7. Creater Customer Phone Number table
create table phone(
id serial primary key,
customer_id int not null,
phone_no varchar(355),
foreign key(customer_id) references customer (id));

-- 8. Populate Third Table
-- '435-344-2245', '332-776-4678', '221-634-7753', '445-663-5799'
insert into phone (customer_id, phone_no)
values (1,'435-344-2245'),
		(2, '332-776-4678'),
		(3,'221-634-7753'),
		(4,'445-663-5799');

-- 9. View Table
select * from phone;

--10. Combine
create table combined(
primary key (customer_id))
