print ("helloworld")
print ("line2")
print ("line3")
print ("line4")
import openpyxl
path = "C:\CommonUser\py_sheet1.xlsx"
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active
cell_obj = sheet_obj.cell(row = 1, column = 1)
print(cell_obj.value)
