import  csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# testing plt.bar before import data.csv
# ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
#
# x_indexes = np.arange(len(ages_x))
# width = 0.25
#
# dev_y = [38496, 42000, 46752, 49320,
#          53200, 56000, 62316, 64928, 67317, 68748, 73752]
# plt.bar(x_indexes - width, dev_y, width=width, color='#444444', label='All Devs')
#
# py_dev_y = [45372, 48876, 53850, 57287,
#             63016, 65998, 70003, 70000, 71496, 75370, 83640]
# plt.bar(x_indexes, py_dev_y, width=width, color='#5a7d9a', label='Python')
#
# js_dev_y = [37810, 43515, 46823, 49293,
#             53437, 56373, 62375, 66674, 68745, 68746, 74583]
# plt.bar(x_indexes + width, js_dev_y, width=width, color='#adad3b', label='JavaScript')
#
# plt.legend()
#
# plt.xticks(ticks=x_indexes, labels=ages_x)

# open data.csv without pandas
# with open('data.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.xlabel('Programming Languages')
plt.ylabel('Number of People Who Use')
plt.title('Most Popular Languages')

plt.tight_layout()

plt.show()