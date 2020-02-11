#科目余额表解析
import os

from base.basic import excle_json_path
from method.read_excle import ReadExcle
from method.read_serversql import TSql
import pytest
import json


number= 0
def excle_json():
    sql_lists = []
    with open(excle_json_path, 'r', encoding='utf-8') as f:

        elements = json.load(f)
        for element in elements:
                sql_list =[(s) for s in element.values()]
                sql_lists.append(tuple(sql_list))
    return sql_lists


@pytest.mark.parametrize('sheetname,rowname,colname',excle_json())
class TestCheck():



    def excle_cell_value(self,sheetname,rowname,colname):
        row,col =ReadExcle().read_excle_cell_index(sheetname,rowname)
        ncol  = ReadExcle().read_excle_column_index(sheetname,colname)
        value =ReadExcle().read_excle_cell_value(sheetname,row,ncol)
        return value
    # def num_def(self):
    #     global num
    #     num = 0
    #     return num


    def test_01(self,sheetname,rowname,colname):
        try:
            global number
            sqls_list = TSql().Conn('JD_KeMuYuE_List')
            sar =sqls_list[number]
            evar = self.excle_cell_value(sheetname,rowname,colname)
            print('sql:%s,excle:%s rowname:%s,colname:%s' %(sar,evar,rowname,colname))
            assert sqls_list[number] == self.excle_cell_value(sheetname,rowname,colname)
            number += 1
        except Exception as e:
            print(e)
            with open ('../log/log.txt','w',encoding='utf-8') as f:
                f.write(str(e))

# if __name__=="__main__":
#     pytest.main(['-s','-q','--alluredir','./report','test_kemuyue.py'])
#     os.system("E:/软件包/allure-2.7.0/allure-2.7.0/bin/allure.bat "
#               "generate "
#               "C:/Users/wellwin/Desktop/工作资料/ProjectX/pythonX自动化代码/PycharmProjects/caiwu/report"
#               "-o "
#               "C:/Users/wellwin/Desktop/工作资料/ProjectX/pythonX自动化代码/PycharmProjects/caiwu/report/html")
