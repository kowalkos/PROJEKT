import easygui
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
def pokazanie_wykresu(dane):
    n_theta = 36 # number of values for theta
    n_phi = 73  # number of values for phi
    r = 2        #radius of sphere

    theta, phi = np.mgrid[0.0:0.5*np.pi:n_theta*1j, 0.0:2.0*np.pi:n_phi*1j]

    x = r*np.sin(theta)*np.cos(phi)
    y = r*np.sin(theta)*np.sin(phi)
    z = r*np.cos(theta)

    # mimic the input array
    # array columns phi, theta, value
    # first n_theta entries: phi=0, second n_theta entries: phi=0.0315..
    inp = []
    for j in phi[0,:]:
        for i in theta[:,0]:
            val = 0.7+np.cos(j)*np.sin(i+np.pi/4.)
            inp.append([j, i, val])
    inp = np.array(inp)
    print (inp.shape)
    print (inp[49:60, :])
    c = inp[:,2].reshape((n_phi,n_theta)).T
    print (z.shape)
    print (c.shape)
    my_color=[]
    for index,row in dane.iterrows():
        e=[100-float(row[1])]*73
        my_color.append(e)
    my_color=np.array(my_color)
    print(my_color)
    my_col = cm.gist_heat(my_color/np.amax(my_color))
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    a=ax.plot_surface(
        x,y,z,  rstride=1, cstride=1, facecolors=my_col, alpha=0.9, linewidth=1) 
    ax.set_xlim([-2.2,2.2])
    ax.set_ylim([-2.2,2.2])
    ax.set_zlim([0,4.4])
    ax.set_aspect("auto")
    #ax.plot_wireframe(x, y, z, color="k") #not needed?!
    plt.colorbar(cm.ScalarMappable(cmap=plt.cm.gist_heat))

    plt.savefig(__file__+".png")
    plt.show()
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
pokazanie_wykresu(dane)



