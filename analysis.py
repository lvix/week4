#!/usr/bin/env python3

import json
import pandas as pd 

def analysis(file, user_id):
    times = 0;
    minutes = 0;
    try:
        with open(file) as js:
            df = pd.read_json(js)
            times = df[df['user_id'] == user_id]['minutes'].count()
            minutes = df[df['user_id'] == user_id]['minutes'].sum()
        return times, minutes
    except:
        return 0

    
