#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt 
# def main():
try:
    with open('user_study.json') as js:
        _df = pd.read_json(js)
        df = _df[['user_id', 'minutes']].groupby('user_id').sum()

        ax = df.plot()
        ax.set_xlabel('User ID')
        ax.set_ylabel('Study Time')
        ax.set_title('StudyData')

        plt.show()
except:
    print('error')
    pass



