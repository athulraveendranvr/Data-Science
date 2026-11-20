create database MovieStreamDB;
use MovieStreamDB;
create table mmovies(
	Movie_ID int primary key,
    Movie_Name varchar(50),
    Genre enum("Action","Romance","Thriller"),
    Language varchar(50),
    Rating decimal(10,1),
    Duration_Min int,
    Release_Year int);
alter table mmovies rename to movies;
drop table movies;
describe movies;
insert into movies(Movie_ID,Movie_Name,Genre,Language,Rating,Duration_Min,Release_Year)values(101,"Leo","Action","Tamil",8.2,164,2023),
																					(102,"Premalu","Romance","Malayalam",8.5,156,2024),
                                                                                    (103,"KGF","Action","Kannada",8.4,168,2018),
                                                                                    (104,"Drishyam","Thriller","Malayalam",8.6,160,2013),
                                                                                    (105,"Jawan","Action","Hindi",7.4,169,2023),
                                                                                    (106,"96","Romance","Tamil",8.5,158,2018);
select * from movies;
select Movie_name,Rating from movies;
select distinct Genre from movies;
select distinct Language from movies;
select * from movies limit 3;
select * from movies order by rating desc limit 2;
select * from movies where rating>8.0;
select * from movies where Release_year > 2020;
select * from movies where Genre = "Action";
select * from movies order by Rating desc;
select * from movies order by Release_Year;
select * from movies order by rating desc limit 1;
select * from movies order by Duration_Min limit 1;
select avg(rating) from movies;
select Genre,count(*) from movies group by Genre;
select Language,avg(rating) from movies group by Language;
select Genre,count(*) from movies group by Genre having count(*)>1;
select Language,count(*) from movies group by Language having count(*)>1;







    