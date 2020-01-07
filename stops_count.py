import matplotlib.pyplot as plt
import pandas as pd
import csv

plt.figure(figsize=(20,10))
data=pd.read_csv('trips.csv')
stops_count = data.groupby(['route_id'])
stops_count = data.pivot_table(index=['route_id'], aggfunc='size')

ax = stops_count.plot(kind='bar', color='dodgerblue', width=0.7)
plt.title('Stops per transport')
plt.ylabel('Stop count')
plt.xlabel('Transport')
plt.tight_layout()
for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.text(i.get_x(), i.get_height()+10, \
            str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',
                rotation=90)

plt.show()

