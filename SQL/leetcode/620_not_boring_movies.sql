select * from(
select * from cinema where description not in ('boring') order by rating desc
) as s
where id%2<>0;
