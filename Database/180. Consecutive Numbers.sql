# Write your MySQL query statement below
select distinct num as ConsecutiveNums
from Logs
where (id + 1, num) in (select * from Logs) and (id + 2, num) in (select * from Logs)

/* 
with cte as (
    select num,
    lead(num,1) over() as num1,
    lead(num,2) over() as num2
    from logs
)

select distinct num ConsecutiveNums from cte where (num=num1) and (num=num2)
*/