#!/usr/bin/python3
"""Написать программу таймер. Программа при запуске принимает имя,
фамилию, часы, минуты и секунды. После программа начинает обратный
отсчет выводя оставшееся время. Программа должна хранить файл
логирования с информацией о том кто запускал программу и когда.
Пример:00:00:03 00:00:02 00:00:01 ALARM!!!"""
import csv
import argparse
import datetime
import time
from datetime import timedelta
parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name', required=True)
parser.add_argument('-ln', '--last-name', required=True)
parser.add_argument('-ho', '--hours', required=True)
parser.add_argument('-min', '--minutes', required=True)
parser.add_argument('-se', '--seconds', required=True)
args = parser.parse_args()
with open('file.csv', 'a') as file:
    csvwriter = csv.writer(file)
    time_start = datetime.datetime.now()
    csvwriter.writerow(['Программу запукал:', args.first_name, args.last_name, time_start])
time_delta = timedelta(hours=int(args.hours), minutes=int(args.minutes), seconds=int(args.seconds))
second_total = time_delta.total_seconds()
for i in range(int(second_total), -1, -1):
    ty_res = time.gmtime(i)
    res = time.strftime('%H:%M:%S', ty_res)
    time.sleep(1)
    print(res)
print('ALLARM!!!')










