# -*- coding:utf-8 -*-  
# author:Jaydan

import xdrlib
import xlrd,sys

file = r'F:\GitHub\practice\DATA\Test.xlsx'


def open_file(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print e



def read_excel(file,sheetindex,rowindex,colindex):
    data = open_file(file)
    table = data.sheets()[sheetindex]
    nrows = table.nrows
    ncols = table.ncols
    getdata = table.col_values(colindex)
    datadic = {u'行数':nrows,u'列数':ncols,u'数据':getdata}
    return datadic

print read_excel(file,0,0,0)







