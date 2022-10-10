import datetime
import pandas as pd
from selenium import webdriver
from tkinter import filedialog
import tkinter

# set vars
sciezkaSelen = "C:/SeleniumDrivers/chromedriver.exe"
newsURL = "https://polsatnews.pl" 
teraz = datetime.datetime.now()

# set driver
driver = webdriver.Chrome(sciezkaSelen)
driver.get(newsURL)

finalTable = pd.DataFrame({ 'Date':[],
                            'Source':[],
                            'News Header':[],
                            'URL':[]})

# accept cookies window
try:
    acceptCookies = driver.find_element_by_id("onetrust-accept-btn-handler")
    if acceptCookies.is_displayed():
        print("Cookies Accepted!")
        acceptCookies.click()
except:
    print("No Cookies to accept!")

# locate news table
newsTable = driver.find_element_by_class_name("tabs__box")
if newsTable.is_displayed():
    print("News Table found!")
    newsList = newsTable.text
else:
    print("News Table not found!")
    exit()

headerList = newsList.split(chr(10)) 

# get URLs
for news in headerList:
    if news[0:6] != "Zobacz":
        urlAdress = driver.find_element_by_link_text(news).get_attribute("href")
        finalTable = finalTable.append({'Date':str(teraz), 'Source':'Polsat News','News Header':news, 'URL': urlAdress},ignore_index=True)

print(finalTable)
# save to .TXT file
txtPath = filedialog.askopenfilename(filetypes=[("Text files", ".txt")])
i=0
try:
    with open(txtPath, "a") as file_object:
        for x in finalTable['Source']:
            file_object.write(finalTable['Date'][i] + " | "  + finalTable['Source'][i] + " | " + finalTable['News Header'][i]+ " | " +finalTable['URL'][i] + "\n")
            i+=1
except:
    tkinter.messagebox.showinfo(title="Error!",message="Can't save to text!")
    exit()

tkinter.messagebox.showinfo(title="Done!",message="News saved successfuly here: " + txtPath)

'''
# WRITE TO EXCEL IF NEEDED
excelPath = filedialog.askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])
shName = "Arkusz1"
finalTable.to_excel(excelPath ,sheet_name = shName, index = False, startrow=0,startcol=0)

tkinter.messagebox.showinfo(title="Done!",message="Procedure completed!")
'''