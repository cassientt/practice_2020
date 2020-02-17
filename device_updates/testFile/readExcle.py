import os
import getpathInfo
from xlrd import open_workbook
path = getpathInfo.get_Path()

class readExcel():
    def get_xls(self,xls_name,sheet_name):
        """ 
        xls_name:填写用例的excel名称
        sheet_name：该用例的sheet名称
        """
        cls = []
        # 获取文件路径
        xlsPath = os.path.join(path,'case',xls_name)# 在相同的文件夹“testFile下，即第一级文件名不加”
        file = open_workbook(xlsPath)#打开用例excel
        sheet = file.sheet_by_name(sheet_name)#获得打开Excel的sheet
        # 获取这个sheet内容行数
        nrows = sheet.nrows
        for i in range(nrows):
            if sheet.row_values(i)[0] !=u'case_name':
                cls.append(sheet.row_values(i))
        return cls
if __name__ == '__main__':
# 执行该文件看是否可以正确获取Excel中的值。
    print(readExcel().get_xls('serverapkCase.xlsx','Sheet1'))
    print(readExcel().get_xls('serverapkCase.xlsx','Sheet1')[0][1])
    print(readExcel().get_xls('serverapkCase.xlsx','Sheet1')[1][2])





