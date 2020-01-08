import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('ValidDati01_05_18.txt')
#print(data.head(data.Laiks))
plt.plot(data.Laiks)
plt.show()