import pandas
import xlrd
import xlwt
import json

from base.basic import excle_path


class ReadExcle():
    def read_excle_column_index(self,sheetname,columnName):
        workbook = xlrd.open_workbook(excle_path)  # 打开excle
        table = workbook.sheet_by_name(sheetname)
        columnIndex = None
        for i in range(table.ncols):
            if (table.cell_value(0, i) == columnName):#从表头检测属于哪一列
                columnIndex = i
                break
        return columnIndex
    def read_excle_row_index(self,sheetname,rowName,columnIndex):
        workbook = xlrd.open_workbook(excle_path)  # 打开excle
        table = workbook.sheet_by_name(sheetname)
        rowIndex = None
        for j in range(table.nrows):
            if (table.cell_value(j, columnIndex) == rowName):
                rowIndex = j
                break
        return rowIndex

    def read_excle_cell_index(self, sheetname, Name):
        workbook = xlrd.open_workbook(excle_path)  # 打开excle
        table = workbook.sheet_by_name(sheetname)
        row_Index = None
        column_Index = None
        for i in range(0,table.ncols):
            # print(i)
            for j in range(0,table.nrows):
                # print(j)

                if (table.cell_value(j,i) == Name):
                    row_Index =j
                    column_Index = i
                    # print(i, j)
                    break

        return row_Index,column_Index
    def read_excle_cell_value(self,sheetname, row, col):
        workbook = xlrd.open_workbook(excle_path)  # 打开excle
        table = workbook.sheet_by_name(sheetname)
        return table.cell_value(row,col)

