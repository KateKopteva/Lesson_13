"""На вход программа получает имя, фамилию, время для
фокусировки(по-умолчанию 25 минут), длину перерыва(по-умолчанию 5 минут),
количество циклов(по-умолчанию 4) и название задачи. Программа указывает
оставшееся время фокусировки, после сигнализирует о наступлении перерыва,
после сигнализирует о начале нового цикла фокусировки. Программа должна
вести файл лога о всех запусках"""
import csv
import argparse
import datetime
import time
from datetime import timedelta
parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name', required=True)
parser.add_argument('-ln', '--last-name', required=True)
parser.add_argument('-mf', '--minutes-focus', required=True)
parser.add_argument('-mb', '--minutes-break', required=True)
parser.add_argument('-c', '--cycle', required=True)
args = parser.parse_args()
with open('file2.csv', 'a') as file:
    csvwriter = csv.writer(file)
    time_start = datetime.datetime.now()
    csvwriter.writerow(['Программу запускал:', args.first_name, args.last_name, time_start])
for i in range(int(args.cycle)):
    t = (int(args.minutes_focus)) * 60
    while t:
        mins = t // 60
        sec = t % 60
        timer = '{:02d}:{:02d}'.format(mins, sec)
        print(timer)
        time.sleep(1)
        t -= 1
    print('Break Time!')
    t = (int(args.minutes_break)) * 60
    while t:
        mins = t // 60
        sec = t % 60
        timer = '{:02d}:{:02d}'.format(mins, sec)
        print(timer)
        time.sleep(1)
        t -= 1
    if i == (int(args.cycle)-1):
        print('Finish Work!')
    else:
        print('Work Time!')
        print('Start new cycle!')

