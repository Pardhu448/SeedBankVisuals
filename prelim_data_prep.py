#Code for preliminary analysis of seed bank data.
import pandas
from datetime import datetime
import re 

seed_data = pandas.read_csv('../csb_seed_library_survey_ver_1.csv')
index_date = seed_data['date'].str.contains(r'(\d+/\d+\d)|\d', na = False)
'''Data with clean 'date' attribute.'''
seed_date_data = seed_data[index_date]

def date_clean(date_str):
    try:
        if (len(date_str) > 10):
            year_date = re.split(r'[(]', date_str)[0]
            year_date = year_date.split(' ')[0] + '/2016'
            return datetime.strptime(year_date, '%m/%d/%Y').date().strftime('%m/%d/%Y')
        elif (len(date_str) == 4):
            date = datetime.strptime('02/15/' + date_str, '%m/%d/%Y')
            return date.date().strftime('%m/%d/%Y')
        elif ((len(date_str) == 3) | (len(date_str) == 5)):
            date = datetime.strptime(date_str + '/2016', '%m/%d/%Y')
            return date.date().strftime('%m/%d/%Y')
        else:
            if (re.match( r'\d{1,2}/\d{1,2}/\d{2}$', date_str)):
                date = date_str.split(r'/')
                date = date[0] + '/'+ date[1]+ '/20'+ date[2]        
                return datetime.strptime(date, '%d/%M/%Y').date().strftime('%m/%d/%Y')
            else: 
                return datetime.strptime(date_str, '%d/%M/%Y').date().strftime('%m/%d/%Y')
    except ValueError:
        print date_str

dates = seed_date_data.date.apply(lambda x: date_clean(str(x)))
#seed_date_data['date'] = dates

''' To plot dates variation '''
import random, matplotlib 
values = random.sample(range(len(dates)), len(dates))
date_map = matplotlib.dates.datestr2num(dates)

matplotlib.pyplot.plot_date(dates, values)

# Sample data to get the first draft of visualization
import pandas 
d = pandas.read_csv('data/stream_data.csv')

dates = d[d['key'] == 'RI']
aj = dates
dates.key  = 'DJ'
dates  = aj.append(dates)
d['key'].unique()

d.loc[d['key'] == 'DJ', 'date'] = dates.values
d.loc[d['key'] == 'MS', 'date'] = dates.values
d.loc[d['key'] == 'RC', 'date'] = dates.values
d.loc[d['key'] == 'CG', 'date'] = dates.values
d.loc[d['key'] == 'RI', 'date'] = dates.values

unemploy_data = pandas.DataFrame.from_csv('data/unemployment.tsv', sep = '/t', 
                                          header = 0) 
un_data = unemploy_data.index.values
un_data_new = pandas.DataFrame(un_data)
un_data_new.columns = ['rate']
un = un_data_new.merge(un_data_new.rate.apply(lambda s: pd.Series({'GEOID':
    s.split('\t')[0], 'urate': s.split('\t')[1]})), left_index=True,
    right_index=True)

import json 
with open('data/ohio_counties.json') as f :
    data = json.load(f)
 

data = pd.read_json('data/ohio_counties.json', orient = 'records')

    
