
create view time_view as
select date(time), count(*) as views
from log
group by date(time)
order by date(time);

create view total_error as
select date(time), count(*) as errors
from log where status = '404 NOT FOUND'
group by date(time)
order by date(time);

create view error as
select time_view.date, (100.0*total_error.errors/time_view.views) as percentage
from time_view, total_error
where time_view.date = total_error.date
order by time_view.date;
