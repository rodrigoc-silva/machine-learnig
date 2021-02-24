from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')

# ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]

data = pd.read_csv('dataAge.csv')
ids = data['Responder_id']
ages = data['Age']

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins=bins, edgecolor='black', log=True)

median_age = 29
color = '#fc4f30'

plt.axvline(median_age, color=color, label='Age Median', linewidth=2)

plt.legend()

plt.title('Age of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total respondents')

plt.tight_layout()

plt.show()