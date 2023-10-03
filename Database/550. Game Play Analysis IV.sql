# Write your MySQL query statement below
select round(count(*) / (select count(distinct player_id) from activity), 2) as fraction
from activity
where (player_id, date_sub(event_date, INTERVAL 1 DAY)) in (
    select player_id, min(event_date) as first_login
    from activity
    group by player_id
)