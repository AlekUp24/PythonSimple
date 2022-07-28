from ntpath import join
import pandas as pd
from csv import excel

import tkinter as tk
from tkinter import filedialog

#wybierz scieżkę pliku 
root = tk.Tk()
root.withdraw()
pathT = filedialog.askopenfilename()
ws = "testowa"

#utwórz i zapisz w Excelu
df = pd.DataFrame({'States':['California', 'Florida', 'Montana', 'Colorodo', 'Washington', 'Virginia'],
                   'Capitals':['Sacramento', 'Tallahassee', 'Helena', 'Denver', 'Olympia', 'Richmond'],
                   'Population':['508529', '193551', '32315', '619968', '52555', '227032']})

df.to_excel(pathT, sheet_name=ws, index = False)

#odczytaj z Excela
dr = pd.read_excel(pathT)

#utwórz DF wynik i dodaj tam int z populacji
new = pd.DataFrame({'Score': [int(x) for x in dr['Population']]})

#połącz dwa Frame'y
finTable = dr.join(new)
print(finTable)

i=0
#sprawdź i dopisz wyniki
for x in finTable['Score']:
    if x > 100000:
        finTable['Score'][i]="Positive"
    else:
        finTable['Score'][i]="Negative"
    i+=1
    
print(finTable)

#zapisz w Excelu    
finTable.to_excel(pathT, sheet_name= "testowa",index = False, startrow=0, startcol=0)

#msg box 
tk.messagebox.showinfo(title="Done!", message="Procedure completed succesfully.")