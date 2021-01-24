import xlwt

'''
workbook = xlwt.Workbook(encoding="utf-8") #创建workbook对象
sheet = workbook.add_sheet(sheetname="sheet1") #创建sheet对象
sheet.write(0,0,"hello")
workbook.save("student.xls")
'''
workbook = xlwt.Workbook(encoding="utf-8") #创建workbook对象
sheet = workbook.add_sheet(sheetname="sheet1") #创建sheet对象

for i in range(0,9):
    for j in range(0,i+1):
        sheet.write(i,j,"%d * %d = %d"%(i+1,j+1,(i+1)*(j+1)))

workbook.save("student.xls")