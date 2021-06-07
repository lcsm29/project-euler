# Solution of;
# Project Euler Problem 19: Counting Sundays
# https://projecteuler.net/problem=19
# 
# You are given the following information, 
# but you may prefer to do some research for yourself. 
# 
#   - 1 Jan 1900 was a Monday. 
#   - Thirty days has September, April, June and November.
#     All the rest have thirty-one, Saving February alone,
#     Which has twenty-eight, rain or shine. And on leap years, twenty-nine.
#   - A leap year occurs on any year evenly divisible by 4, 
#     but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during 
# the twentieth century (1 Jan 1901 to 31 Dec 2000)?
# 
# by lcsm29 http://github.com/lcsm29/project-euler
import timed
from datetime import date


def fn_brute(n):
    def get_days(year, month):
        days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        d = days[month - 1]
        if month == 2:
            if year % 4 == 0:
                if year % 100 != 0 or year % 400 == 0:
                    d += 1
        return d

    def get_days_in_year(year):
        return 365 if get_days(year, 2) == 28 else 366

    def set_start_day(year):
        base_year = 1_900
        num_days = 0
        step = 1 if year >= base_year else -1
        for year in range(base_year, year, step):
            num_days += get_days_in_year(year)
        return num_days % 7 if step == 1 else 6 - (num_days % 7)

    s_year = (n - 1) * 100 + 1
    base = set_start_day(s_year)
    sunday_count = 0
    for y in range(s_year, n * 100 + 1):
        for m in range(1, 13):
            base += get_days(y, m)
            if base % 7 == 6:
                sunday_count += 1
    return sunday_count


def fn_datetime(n):
    year = (n - 1) * 100 + 1
    return sum(
        1 for y in range(year, n * 100 + 1) for m in range(1, 13)
            if date(y, m, 1).weekday() == 6)


if __name__ == '__main__':
    n = 20
    i = 2_800
    prob_id = 19
    timed.caller(fn_brute, n, i, prob_id)
    timed.caller(fn_datetime, n, i, prob_id)
