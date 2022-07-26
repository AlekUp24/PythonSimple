import pandas as pd
import tkinter as tk
from ntpath import join
from tkinter import filedialog

#wybierz scieżkę pliku 
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
new = pd.DataFrame({'Short': [x.upper()[0:3] for x in dr['States']]})
new2 = pd.DataFrame({'Score': [int(x) for x in dr['Population']]})

#połącz dwa Data Frame'y
finTable = new.join(df)
finTable = finTable.join(new2)

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
finTable.to_excel(pathT, sheet_name=ws,index = False, startrow=0, startcol=0)

#msg box 
tk.messagebox.showinfo(title="Done!", message="Procedure completed succesfully.")
