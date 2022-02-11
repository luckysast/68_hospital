CREATE DATABASE IF NOT EXISTS hospital;
use hospital;
create table patients(patient_id INT AUTO_INCREMENT primary key, medical_policy VARCHAR(45) NOT NULL unique);
create table doctors(doctor_id INT AUTO_INCREMENT primary key,medical_policy VARCHAR(45) NOT NULL unique);

create table patients_doctors(
patient_id INT NOT NULL,
doctor_id INT NOT NULL,
complaint varchar(45) not null,
foreign key(patient_id) REFERENCES patients(patient_id),
foreign key(doctor_id) REFERENCES doctors(doctor_id));

CREATE USER 'root'@'%' IDENTIFIED BY 'root';
GRANT ALL ON *.* TO 'root'@'%' WITH GRANT OPTION;
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'root';
FLUSH PRIVILEGES;
