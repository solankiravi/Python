#Import xlrd
import xlrd
#file url on which you will perform operation
locOfFile = ("C:\\Users\\Ravi\\Desktop\\TestDeocument.xlsx")

#open the file
workbook = xlrd.open_workbook(locOfFile)

#Open Sheet
sheet = workbook.sheet_by_index(0)

#Get a cell value
res = sheet.cell_value(3, 2) 
print(res)

#Print sheet rows and columns value
for row in range(sheet.nrows):
	for column in range(sheet.ncols):
		print(sheet.cell_value(row,column))
		