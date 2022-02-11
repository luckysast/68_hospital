# coding=utf-8           # -*- coding: utf-8 -*-
from sqlalchemy import  create_engine
import pymysql
import re
pymysql.install_as_MySQLdb()

try:
    engine = create_engine('mysql://root:root@172.24.24.10:3306 /hospital')
except:
    pass

def clean_db():
    engine.execute('DELETE FROM `hospital`.`patients_doctors` WHERE `patient_id`>\'0\';')


class Patient(object):
    def __init__(self,medical_policy):
        self.medical_policy = medical_policy
        if engine.execute("select medical_policy from patients where medical_policy=\'"+ self.medical_policy +'\'').fetchone() == None:
            engine.execute("INSERT INTO `hospital`.`patients` (`medical_policy`) VALUES (\'" + self.medical_policy +"\');")

    def record(self,doctor_medical_policy,complaint):
        try:
            #hack me
            #print('\nSQL QUERY FOR DEBUG !')
            #print('INSERT INTO `hospital`.`patients_doctors` (`patient_id`, `doctor_id`, `complaint`)\n VALUES ((select patient_id from `hospital`.`patients` where medical_policy=\''+self.medical_policy+'\'),\n (select doctor_id from `hospital`.`doctors` where medical_policy=\''+doctor_medical_policy+'\'),\n \''+complaint+'\');\n')
            engine.execute('INSERT INTO `hospital`.`patients_doctors` (`patient_id`, `doctor_id`, `complaint`) VALUES ((select patient_id from `hospital`.`patients` where medical_policy=\''+self.medical_policy+'\'), (select doctor_id from `hospital`.`doctors` where medical_policy=\''+doctor_medical_policy+'\'), \''+complaint+'\');')
        except:
            print("Что-то произошло не так !")

    def history(self):
        print("История болезней:")
        result = engine.execute('select complaint from `hospital`.`patients_doctors` where patient_id=(select patient_id from `hospital`.`patients` where medical_policy=\''+self.medical_policy+'\')')
        for row in result:
            print(row[0])
        print("\n\n")

    def show(self):
        print("Доступные врачи:")
        result = engine.execute('select medical_policy from doctors')
        personal = []
        for row in result:
            personal.append(row[0])
        count = 100
        for person in personal:
            print(person)
            count-=1
            if count <= 0:
                break
        print("\n\n")

    def setDoctor(self):
        try:
            engine.execute("INSERT INTO `hospital`.`doctors` (`medical_policy`) VALUES ('"+self.medical_policy+"');")
            print("Вы врач !\n")
        except:
            print("Что-то произошло не так !")
