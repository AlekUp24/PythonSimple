from ntpath import join
import pandas as pd
from csv import excel

pathT = r'C:\Users\hchmiele\OneDrive - Linklaters\Desktop\ImportExport\pythonTEST.xlsx'
pathR = r'C:\Users\hchmiele\OneDrive - Linklaters\Desktop\ImportExport\pythonRESULT.xlsx'
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