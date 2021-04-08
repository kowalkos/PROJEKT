import easygui
import pandas as pd
def odczyt_pliku():
    path = easygui.fileopenbox(filetypes=["*.xlsx",".csv"],default="*.xlsx""*.csv")
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
