#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Module Andrew Malih
# Module date 
import datetime

if __name__ == '__main__':
	main()

# date(day month year)
def date_out(symphols = '.'):
	date = datetime.datetime.now()
	date = date.strftime("%d" + str(symphols) + "%m" + str(symphols) + "%Y")
	return date

# time (hour minute second)
def time_out(symphols = ':'):
	date = datetime.datetime.now()
	date = date.strftime("%H" + str(symphols) + "%M" + str(symphols) + "%S")
	return date

# date and time (day month year hour minute second)
def datetime_out(symphols_date = '.', symphols_time = ':'):
	date = datetime.datetime.now()
	date = date.strftime("%d" + str(symphols_date) + "%m" + str(symphols_date) + "%Y " 
							+ "%H" + str(symphols_time) + "%M" + str(symphols_time) + "%S")
	return date
