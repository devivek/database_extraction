import PyPDF2 as py

a = py.PdfReader("/Users/v/Drive/sharing_team0/resources/JEE-Main-1st-Sep-2021-Shift-2-Physics-Embibe.pdf")
str = a.getPage(0).extractText()
print(str)
