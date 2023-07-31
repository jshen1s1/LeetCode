# Write your MySQL query statement below
# Using with clause to create a temporary result set that can be referred within later statements
with cte as
(
    select request_at, T.status <> 'completed' as Cancelled
    from Trips T
    join Users C on (client_id = C.users_id and C.banned = 'No')
    join Users D on (driver_id = D.users_id and D.banned = 'No')
    where request_at between '2013-10-01' and '2013-10-03'
)
select request_at as Day, 
    Round(cast(sum(Cancelled) as real) / cast(count(*) as real), 2) as 'Cancellation Rate'
from cte
group by request_at