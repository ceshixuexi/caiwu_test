import pymssql #引入pymssql模块
import re
import pytest
import json



# @pytest.mark.parametrize('SQL',read_json())
from base.basic import sql_path


class TSql():

    def read_json(self,sheetname):
        sql_list = []
        with open(sql_path, 'r', encoding='utf-8') as f:

            elements = json.load(f).get(sheetname)
            for element in elements:
                for value in element.values():
                    sql_list.append(value)
        return sql_list
    def Conn(self,name):
        server_name = '192.168.7.216'
        username = 'sc'
        password = 'Aa123!@#'
        database_name = 'ProjectX_test2'

        connect = pymssql.connect(server_name, username, password, database_name) #服务器名,账户,密码,数据库名
        # if connect:
        #     print("连接成功!")

        cur = connect.cursor()
        # SQL ="select  sum(Total_AR_Exclude_DUTY_EXCG_Local)/1000 from baselevel_list list inner join baselevel_head head " \
        #      "on list.HeadUniqueNo = head.UniqueNo  where Accounting_Period = '201908' and Business_Type='CN export' and PXStationCode='SHANGHAI_HEADQUARTERS'"
        data_list = []
        sql_list = self.read_json(name)
        for sql in sql_list:
            cur.execute(sql)
            for ele in cur.fetchall()[0]:
                data_list.append(float(ele))



        return   data_list

