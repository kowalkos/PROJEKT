import easygui
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from itertools import product, combinations
"""
def odczyt_pliku():
    path = easygui.fileopenbox(filetypes=["*.xlsx",".csv"])
    print(path)
    dane=None
    a=path.split('.')
    if a[1]=="xlsx":
        read_file = pd.read_excel(path)
        read_file.to_csv (r'{}.csv'.format(a[0]), index = None, header=True)
        dane=pd.read_csv(r'{}.csv'.format(a[0]))
    else:
        dane=pd.read_csv(path)
    i=1
    while True:
        print(dane.iloc[i,0])
        if dane.iloc[i,0].isalnum():
            i+=1
        else:
            return dane[i:]
dane=odczyt_pliku()
print(dane)

for index,row in dane.iterrows():
    print(row[0],row[1])


    
    


"""
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x=10*np.arange(0,1,0.01)
y=10*np.arange(0,1,0.01)
z = 10*np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x,y,z,color='b')
plt.show()

