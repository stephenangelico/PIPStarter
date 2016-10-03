#!/usr/bin/env python3
# Simple time machine for Ted Leo and the Pharmacists
#year = int(input('What year is it?\n'))
for year in range(2001,2016):
    if (year >= 2001) and (year <= 2006) :
        print('Lookout Records')
    elif (year >= 2007) and (year <= 2009) :
        print('Touch and Go Records')
    elif (year >= 2010) :
        print('Matador Records')
