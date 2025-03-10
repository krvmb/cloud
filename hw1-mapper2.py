#!/usr/bin/env python3

import sys
import csv
from csv import reader

rpt_date_index = 5
ofns_desc_index = 7

months = ['JANUARY',
          'FEBRUARY',
          'MARCH',
          'APRIL',
          'MAY',
          'JUNE',
          'JULY',
          'AUGUST',
          'SEPTEMBER',
          'OCTOBER',
          'NOVEMBER',
          'DECEMBER']

def print_dang_weap_date():
    for line in reader(sys.stdin):
        #print(line)
        if (line[ofns_desc_index].strip() == 'DANGEROUS WEAPONS'):
            #process date of dangerous weapon crime
            date = line[rpt_date_index].strip()
            month_num = int(date.split('/')[0]) -1
            #print("{} on {} in month of {}".format(line[ofns_desc_index].strip(), date, months[month_num]))
            print(months[month_num])

def get_col_name_lst():
    with open(sys.argv[1], newline='') as fp:
        reader = csv.reader(fp)
        ret = next(reader)
        fp.close()
    return ret

def find_col_index(value, col_name_lst):
    return col_name_lst.index(value)

def count_total_crime_occurences(ofns_desc, col_names):
    count = 0
    idx = find_col_index('OFNS_DESC', col_names)
    date_idx = find_col_index('RPT_DT', col_names)
    print(idx, date_idx)
    fp = open(sys.argv[1], newline='')
    for line in reader(fp):
        #print(line)
        if line[idx] == ofns_desc:
            count += 1
            #print("{}. {} occurred on {}".format(count, line[idx], line[date_idx]))
    return count
def count_monthly_crime_occurences(ofns_desc, col_names):
    ret = [0]*12
    idx = find_col_index('OFNS_DESC', col_names)
    date_idx = find_col_index('RPT_DT', col_names)
    print(idx, date_idx)
    fp = open(sys.argv[1], newline='')
    for line in reader(fp):
        #print(line)
        if line[idx] == ofns_desc:            
            month = int(line[date_idx].split('/')[0]) -1
            #print("{}. {} occurred on month{}".format(line[idx], line[date_idx], month))
            ret[month]+=1
    print(ret)
    return ret

if __name__=='__main__':
    #col_names = get_col_name_lst()
    #print(col_names)
    #print('index of OFNS_DESC is {}'.format(find_col_index('OFNS_DESC', col_names)))
    #print('index of RPT_DT is {}'.format(find_col_index('RPT_DT', col_names)))
    #print('total dangerous weapon crimes on 2016 is :{}'\
    #       .format(count_total_crime_occurences('DANGEROUS WEAPONS', col_names)))
    #lst = count_monthly_crime_occurences('DANGEROUS WEAPONS', col_names)
    #total = 0
    #for each in lst:
    #    total += each
    #print('total dangerous weapons crimes by summing month totals is {}'.format(total))
    #months = ['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    #print('DANGEROUS WEAPONS reported per month:')
    #for i in range(len(months)):
    #    print(months[i], lst[i])
    print_dang_weap_date()
