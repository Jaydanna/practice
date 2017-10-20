#!usr/bin/python
#encoding:utf-8

import time

year = int(raw_input('year: '))
month = int(raw_input('month: '))
day = int(raw_input('day: '))


def __assert(body,notice):
    if body:
        return True
    else:
        print notice
    return False


def is_leap_year(year):
    if(year%4 == 0 and year%100 != 0) or year%400 == 0:
        return True
    else:
        return False

year_ok = __assert(year>0,'year must to be large than zero')
month_ok = __assert(month>0 and month<=12,'month invaild')
day_ok = __assert(day>0 and day<=31,'month invaild')
result = 0
nums_ping = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if month_ok == 1:
    print day
else:
    if month_ok:
        if is_leap_year(year):
            print'该年是闰年'
            result = sum(nums_ping[:month-1])+day_ok

        else:
            result = sum(nums_ping[:month-1])+day_ok+1
            print'该年是平年'


if __name__ == '__main__':

    print'%s年%s月%s日,是%s年第%s天' % (year, month, day, year, result)
    print'这一天是该年的第', result, '天'