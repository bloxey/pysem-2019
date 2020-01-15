import numpy
from matplotlib import pyplot

x = numpy.arange(10)
y = numpy.array([5,3,4,2,7,5,4,6,3,2])

fig = pyplot.figure()
ax = fig.add_subplot(111)
ax.set_ylim(0,10)
pyplot.plot(x,y)
for i,j in zip(x,y):
    ax.annotate(str(j),xy=(i,j))

pyplot.show()



"""
ax=laikssum.plot()
plt.tight_layout()
for i in ax.patches:
    ax.text(i.get_x(), i.get_height()+200, \
        str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)

plt.show()

#print(data.head(data.Laiks))
#laikssum = data.pivot_table(index=data['Laiks'], aggfunc='size')

#grouped=data.groupby([pd.Grouper(freq='1H'),'Laiks']).count()
#laikssum = data.pivot_table(index=grouped, aggfunc='size')

#times = pd.DatetimeIndex(data.Laiks)
#time = datetime.strptime(row[8], '%d.%m.%Y %H:%M:%S')

grouper = df.groupby([pd.Grouper(freq='1H'), 'Location'])

laiks = data.pivot_table(index=['Laiks'], aggfunc='size')

ax=data.groupby('Laiks')['TMarsruts'].plot(color='dodgerblue', width=0.2)

plt.show()

times = pd.to_datetime(data.Laiks)
grouped = data.groupby([times.dt.hour, times.dt.minute]).sum() //kaut ko parada

df = pd.DataFrame({'val':values, 'times':times})
df.groupby(pd.Grouper(level='times', freq='H')).median()



"""