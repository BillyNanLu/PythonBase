create database pythonbase;

use pythonbase;

create table student (
    id int,
    name varchar(50),
    age int
);

insert into student
values (1, 'GeJingyi', 22),
       (2, 'LiJiawen', 23),
       (3, 'LuoShuxian', 21),
       (4, 'Tomcat', 25),
       (5, 'XieYifei', 20);

select *
from student;



create table orders(
    order_date Date,
    order_id varchar(255),
    money int,
    province varchar(10)
);

select *
from orders;