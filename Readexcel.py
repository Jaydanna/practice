# -*- coding:utf-8 -*-  
# author:Jaydan

import xdrlib
import xlrd,sys,xlwt
from xlutils.copy import copy

# file = r'..\\practice\DATA\Test.xlsx'


def open_file(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print e

def read_excel(file,sheetindex):
    data = open_file(file)
    table = data.sheets()[sheetindex]
    # table = data.sheet_by_name(sheetname)
    nrows = table.nrows
    ncols = table.ncols
    getdata = table.col_values(0)
    # datadic = {u'行数':nrows,u'列数':ncols,u'数据':getdata}
    return getdata

def write_excel(file,sheetindex):
    workbook = xlrd.open_workbook(file)
    workbooknew = copy(workbook)
    ws = workbooknew.get_sheet(0)
    writedata = ws.write('changed!')
    print 'data is chagne '
    return writedata



# print type(read_excel(file,u'VPG-001陈洁丹'))
# print read_excel(file,0)
# write_excel(file,0)





