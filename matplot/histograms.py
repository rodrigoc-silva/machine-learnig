from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')

ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]

plt.title('Age of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total respondents')

plt.tight_layout()

plt.show()