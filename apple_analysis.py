#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from pandas.tseries.offsets import *
from operator import itemgetter 

def quarter_volume():
	data = pd.read_csv('apple.csv', header=0)
	ser = pd.Series(data['Volume'].values, pd.to_datetime(data['Date']))

	start = pd.Timestamp('2009-1-1')
	end = start + MonthBegin() * 3 - Second()
	res_list = []
	while(start <= ser.index[-1]):
		res = ser[start:end].sum()
		res_list.append((start, res))
		start = start + MonthBegin() * 3
		end = start + MonthBegin() * 3 - Second()

	second_volume = sorted(res_list, key=itemgetter(1))[-2][1]
	# print(second_volume)
	return second_volume

if __name__ == '__main__':
	quarter_volume()