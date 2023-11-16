-- Создаем базу данных.
create database if not exists lesson14;

-- Начинаем работать с конкретной базой.
use lesson14;

-- Посмотреть какие есть таблицы.
show tables;

-- Таблица поставщиков.
create table seller (
	id int unsigned primary key auto_increment,  -- Уникальный идентификатор
	company varchar(64) unique not null,  -- длина 64 символа (обязательно для заполнения)
    phone varchar(15) null
);

-- Таблица пользователей.
create table users (
	id int unsigned primary key auto_increment,  -- Уникальный идентификатор
	username varchar(64) unique not null,  -- длина 64 символа (обязательно для заполнения)
    password varchar(64) not null,
    email varchar(50) unique not null
);

-- Таблица продуктов.
create table products (
	id int unsigned primary key auto_increment,
	name varchar(64) not null,  -- длина 64 символа (обязательно для заполнения)
	cost int unsigned not null,
	count int unsigned not null,
    seller_id int unsigned not null,  -- Для уникального ключа поставщика
    -- Связываем таблицы.
    -- Создаем "внешний ключ".
    foreign key (seller_id) references seller (id)
);

-- Таблица заказов.
create table orders (
	id int unsigned primary key auto_increment,
    user_id int unsigned not null,  -- Для уникального ключа пользователя
    product_id int unsigned not null,  -- Для уникального ключа продукта
	count int unsigned not null,
    -- Связываем таблицы.
    -- Создаем "внешний ключ".
    foreign key (user_id) references users (id),
    foreign key (product_id) references products (id)
);

-- Посмотреть какие есть таблицы.
show tables;

-- Вставка данных
insert users(username, password, email) values('igor', 'password', 'pass@word.ru');
insert users(username, password, email) values('polik', 'paSSword', 'paSS@word.com');

insert seller(company, phone) values('Igor&Co', '+79785696670');
insert seller(company, phone) values('Volvo', '+375293666450');
insert seller(company, phone) values('HP', '+375333421421');

insert products(name, cost, count, seller_id) values('book', 15, 250, 1);
insert products(name, cost, count, seller_id) values('pen', 5, 50, 1);
insert products(name, cost, count, seller_id) values('S90', 5000, 10, 2);
insert products(name, cost, count, seller_id) values('V60', 8000, 5, 2);
insert products(name, cost, count, seller_id) values('XC90', 15000, 15, 2);
insert products(name, cost, count, seller_id) values('МФУ HP Laser 137fnw (4ZB84A)', 350, 66, 3);
insert products(name, cost, count, seller_id) values('ViewSonic VA2432-H', 110, 25, 3);
insert products(name, cost, count, seller_id) values('HP Victus 15-Fb0134nw (712D2EA)', 1010, 18, 3);
insert products(name, cost, count, seller_id) values('HP Pavilion X360 14-Ek0033dx (67W83UA)', 905, 22, 3);

insert orders(user_id, product_id, count) values(1, 1, 2);
insert orders(user_id, product_id, count) values(2, 5, 1);
insert orders(user_id, product_id, count) values(2, 7, 2);
insert orders(user_id, product_id, count) values(1, 4, 2);

-- Вернуть все записи из таблицы seller
select * from seller;

-- Вернуть все записи из таблицы users
select * from users;

-- Вернуть все записи из таблицы products
select * from products;

-- Вернуть все записи из таблицы orders
select * from orders;
