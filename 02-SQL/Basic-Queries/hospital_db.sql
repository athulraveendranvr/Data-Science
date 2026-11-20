create database hospital_db;
use hospital_db;
create table doctor(id int auto_increment primary key,
					name varchar(50),
                    specialized varchar(30),
                    experience int);
insert into doctor(name,specialized,experience)values("arun","Eye specialist",5),("sharath","heart specialist",3),("kamala","ENT",7);
select * from doctor;
create table patient(id int auto_increment primary key,
					 name varchar(50),
                     age int,
                     disease varchar(50),
                     bill_amount int,
                     doctor_id int,
                     foreign key (doctor_id) references doctor(id) on delete cascade);
insert into patient(name,age,disease,bill_amount,doctor_id)values("amal",25,"fever",5000,1),("aron",19,"cold",2500,1),("chandhu",26,"headache",1600,2),("ramya",20,"attack",7000,3),("fathima",22,"leg pain",2500,2);
select * from doctor join patient on doctor.id = patient.doctor_id;
select doctor_id,name,count(*) from patient group by doctor_id;
select doctor_id,sum(bill_amount) from patient group by doctor_id;
select doctor_id,avg(bill_amount) from patient group by doctor_id;
select doctor.name,count(patient.doctor_id) as total_patients from doctor join patients on doctor.id = patient.doctor_id group by doctor.id,doctor.name;
select disease,count(*) as total_patients from patient group by disease;
select disease,min(bill_amount) from patient group by disease;
select disease,max(bill_amount) from patient group by disease;
select disease,avg(bill_amount) from patient group by disease;
select doctor_id,disease,count(*) as total from patient group by doctor_id,disease;
                     
						