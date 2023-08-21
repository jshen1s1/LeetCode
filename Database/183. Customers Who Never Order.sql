# Write your MySQL query statement below
select c.name as Customers
from Customers c
left join Orders 
on c.Id = Orders.customerId
where Orders.customerId is NULL