import matplotlib.pyplot as plt
import pandas as pd
import csv
from tkinter import *

def check(*args):
    if variable.get() == "01.05.":
        data=pd.read_csv('ValidDati01_05_18.txt')
        plt.figure(figsize=(20,10))
        laiks = data.groupby(['Laiks'])
        ax = laiks.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons at ')
        plt.ylabel('Count')
        plt.xlabel('Time')
        plt.tight_layout()
        for i in ax.patches:
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()

OPTIONS = [
"01.05.","02.05.","03.05.","05.05.","06.05.","07.05.","08.05.","09.05.","10.05.","11.05.","12.05.","13.05.","14.05.","15.05.","16.05.","17.05.","18.05.","19.05.","20.05.","21.05.","22.05.","23.05.","24.05.","25.05.","26.05.","27.05.","28.05.","29.05.","30.05.","31.05.",
] 

master = Tk()
master.geometry("100x100")

variable = StringVar(master)
variable.set(OPTIONS[0]) 

w = OptionMenu(master, variable, *OPTIONS)
w.pack()

button = Button(master, text="OK", command=check)
button.pack()



mainloop()