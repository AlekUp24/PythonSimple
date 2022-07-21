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
capper = dr.join(new)
print(capper)

i=0
#sprawdź i dopisz wyniki
for x in capper['Score']:
    if x > 100000:
        capper['Score'][i]="Positive"
    else:
        capper['Score'][i]="Negative"
    i+=1
    
print(capper)

#zapisz w Excelu    
capper.to_excel(pathT, sheet_name= "testowa",index = False, startrow=0, startcol=0)