import matplotlib.pyplot as plt
import pandas as pd
import csv
from tkinter import *

def check(*args):
    if variable.get() == "01.05.":
        data=pd.read_csv('ValidDati01_05_18.txt')
        plt.figure(figsize=(20,10))
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
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "02.05.":
        data=pd.read_csv('ValidDati02_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 02.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "03.05.":
        data=pd.read_csv('ValidDati03_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 03.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "05.05.":
        data=pd.read_csv('ValidDati05_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 05.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "06.05.":
        data=pd.read_csv('ValidDati06_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 06.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "07.05.":
        data=pd.read_csv('ValidDati07_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 07.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "08.05.":
        data=pd.read_csv('ValidDati08_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 08.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "09.05.":
        data=pd.read_csv('ValidDati09_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 09.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "10.05.":
        data=pd.read_csv('ValidDati10_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 10.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "11.05.":
        data=pd.read_csv('ValidDati11_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 11.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "12.05.":
        data=pd.read_csv('ValidDati12_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 12.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "13.05.":
        data=pd.read_csv('ValidDati13_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 13.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "14.05.":
        data=pd.read_csv('ValidDati14_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 14.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "15.05.":
        data=pd.read_csv('ValidDati15_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 15.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "16.05.":
        data=pd.read_csv('ValidDati16_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 16.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "17.05.":
        data=pd.read_csv('ValidDati17_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 17.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "18.05.":
        data=pd.read_csv('ValidDati18_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 18.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "19.05.":
        data=pd.read_csv('ValidDati19_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 19.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "20.05.":
        data=pd.read_csv('ValidDati20_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 20.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "21.05.":
        data=pd.read_csv('ValidDati21_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 21.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "22.05.":
        data=pd.read_csv('ValidDati22_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 22.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "23.05.":
        data=pd.read_csv('ValidDati23_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 23.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "24.05.":
        data=pd.read_csv('ValidDati24_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 24.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "25.05.":
        data=pd.read_csv('ValidDati25_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 25.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "26.05.":
        data=pd.read_csv('ValidDati26_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 26.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "27.05.":
        data=pd.read_csv('ValidDati27_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 27.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "28.05.":
        data=pd.read_csv('ValidDati28_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 28.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "29.05.":
        data=pd.read_csv('ValidDati29_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 29.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "30.05.":
        data=pd.read_csv('ValidDati30_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 30.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
            ax.text(i.get_x(), i.get_height()+200, \
                str(round((i.get_height()), 2)), fontsize=11, color='dimgrey',rotation=90)
        plt.show()
    if variable.get() == "31.05.":
        data=pd.read_csv('ValidDati31_05_18.txt')
        plt.figure(figsize=(20,10))
        transp = data.groupby(['TMarsruts'])
        transp = data.pivot_table(index=['TMarsruts'], aggfunc='size')
        ax = transp.plot(kind='bar', color='dodgerblue', width=0.7)
        plt.title('Registered e-talons on 31.05.2018.')
        plt.ylabel('Count')
        plt.xlabel('Transport')
        plt.tight_layout()
        for i in ax.patches:
            # get_x pulls left or right; get_height pushes up or down
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
