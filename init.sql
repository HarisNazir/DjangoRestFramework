create user hero;
create database my_db;
alter role hero with password 'admin123';
grant all privileges on database my_db to hero;
alter database my_db owner to hero;