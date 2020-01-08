import matplotlib.pyplot as plt
import pandas as pd
import csv

plt.figure(figsize=(20,10))
data=pd.read_csv('ValidDati01_05_18.csv')
transp = data.groupby(['TMarsruts'])
transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')


ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
plt.title('Registered e-talons on 01.05.2018.')
plt.ylabel('Count')
plt.xlabel('Transport')
plt.tight_layout()
for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.text(i.get_x(), i.get_height()+200, \
            str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',
                rotation=90)
plt.show()


"""fig1, ax1 = plt.subplots()
ax1.pie(transp, labels=transp.index, autopct='%1.1f%%',
        shadow=True, startangle=90)


plt.show()"""