import xlrd

#path = input("the path:")
path = "system.xlsx"
workbook = xlrd.open_workbook(path)
sheet = workbook.sheet_by_index(0)
for row in range(sheet.nrows):
    print()
    for col in  range(sheet.ncols):
        print("%7s"%sheet.row(row)[col].value, '\t', end='')
