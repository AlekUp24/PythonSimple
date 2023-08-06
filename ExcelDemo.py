import pandas as pd
import tkinter as tk
from ntpath import join
from tkinter import filedialog

#select folder path 
pathT = filedialog.askopenfilename()
ws = "testowa"

#create table and save in Excel
df = pd.DataFrame({'States':['California', 'Florida', 'Montana', 'Colorodo', 'Washington', 'Virginia'],
                   'Capitals':['Sacramento', 'Tallahassee', 'Helena', 'Denver', 'Olympia', 'Richmond'],
                   'Population':['508529', '193551', '32315', '619968', '52555', '227032']})

df.to_excel(pathT, sheet_name=ws, index = False)

#read from Excel
dr = pd.read_excel(pathT)

#create new DF and add population score
new = pd.DataFrame({'Short': [x.upper()[0:3] for x in dr['States']]})
new2 = pd.DataFrame({'Score': [int(x) for x in dr['Population']]})

#combine two Data Frames
finTable = new.join(df)
finTable = finTable.join(new2)

i=0
#write results
for x in finTable['Score']:
    if x > 100000:
        finTable['Score'][i]="Positive"
    else:
        finTable['Score'][i]="Negative"
    i+=1
    
print(finTable)

#save in Excel 
finTable.to_excel(pathT, sheet_name=ws,index = False, startrow=0, startcol=0)

#msg box 
tk.messagebox.showinfo(title="Done!", message="Procedure completed succesfully.")
