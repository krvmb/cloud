#!/usr/bin/env python3
# Group 3
# Dylan Markovic (gqb105)


import sys

month_totals = {'JANUARY':0,
                'FEBRUARY':0,
                'MARCH':0,
                'APRIL':0,
                'MAY':0,
                'JUNE':0,
                'JULY':0,
                'AUGUST':0,
                'SEPTEMBER':0,
                'OCTOBER':0,
                'NOVEMBER':0,
                'DECEMBER':0
                }

def tally_monthly_dang_weapons():
    for line in sys.stdin:
        month_key = line.strip()
        month_totals[month_key] += 1

def generate_output():
    print('DANGEROUS WEAPONS reported per month:')
    for key in month_totals.keys():
        print('{} {}'.format(key, month_totals[key]))

if __name__=='__main__':
    tally_monthly_dang_weapons()
    generate_output()