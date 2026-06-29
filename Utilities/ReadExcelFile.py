from xlrd import *

m = []
def read_excel_file():
    workbook=open_workbook("C:\\Users\\Lenovo\\PycharmProjects\\AMAZON_Checkout_Workflow_Automation\\TestData\\SigninInput.xlsx")
    sheet=workbook.sheet_by_name("Username")
    totalrows=sheet.nrows
    for i in range(1, totalrows):
        l=[]
        username=(sheet.row_values(i,0,1))[0]
        if type(username)==str:
            l.append(username)
        else:
            l.append(int(username))
        l.extend((sheet.row_values(i,1,2)))
        m.append(l)

    return m