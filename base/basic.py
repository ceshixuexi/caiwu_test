import os

base_dir = os.getcwd() #获取当前目录
excle_name = '201908-科目余额表-K3.xls'     #EXCLE名称
sql_name= 'sql.json'
excle_json_name = 'excle.json'
excle_path = os.path.abspath(os.path.join(base_dir, ".."+os.sep+"data"+os.sep+excle_name)) #获取的excle的绝对路径
sql_path = os.path.abspath(os.path.join(base_dir, ".."+os.sep+"data"+os.sep+sql_name))
excle_json_path = os.path.abspath(os.path.join(base_dir, ".."+os.sep+"data"+os.sep+excle_json_name))