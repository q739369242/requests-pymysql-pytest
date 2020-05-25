import pymysql

from common import config


class Open_mysql(object):
    def __init__(self):
        '''
        从config文件中读取参数
        '''
        self.aa=pymysql.connect(
                host=config.database_host,
                db=config.database_name,
                user=config.database_user,
                password=config.database_password,
                port=config.database_port,
                cursorclass = pymysql.cursors.DictCursor #将输出结果使用字典形式。默认是元祖
            )
        self.cursor = self.aa.cursor()
    def err_text(self,a,sql):
        '''
        :param a: 传入list
        :param sql: 传入字符串
        :return: 
        '''
        print('数据库错误  '+'\n'+
                '错误码：%d '% a[0] +'\n'
                '错误结果：%s' % a[1]+'\n'+
                '错误语句：' + sql
              )
    def pass_text(self,sql):
        print('语句执行成功'+sql)


    def select_all(self,sql):
        '''
        用于查询，并返回
        :param sql: 
        :return: 返回一个list，里面包含一个dist
        '''
        try:
            self.cursor.execute(sql)
            result=self.cursor.fetchall()
            self.pass_text(sql)
            return result
        except pymysql.Error as e :
            self.aa.rollback()
            self.err_text(e.args,sql)

    def select_one(self,sql):
        '''
        用于查询，并返回
        :param sql: 
        :return: 返回一个dist
        '''
        try:
            self.cursor.execute(sql)
            result=self.cursor.fetchone()
            self.pass_text(sql)
            return result
        except pymysql.Error as e :
            self.aa.rollback()
            self.err_text(e.args,sql)

    def op_sql(self,sql):
        '''
        可用于insert delete updata
        :param sql:传入字符串
        :return: 返回一个list，里面包含一个dist
        '''
        try:
            self.cursor.execute(sql)
            self.aa.commit()
        except pymysql.Error as e :
            self.aa.rollback()
            self.err_text(e.args,sql)

    def __del__(self):
        self.cursor.close()
        self.aa.close()

if __name__ =='__main__':
    sql1 = 'select * from istester1'
    a=Open_mysql().select_all(sql1)
    print(a)
    #[{'id': 1, 'uname': '2', 'SEX': '3', 'birth': 2003, 'department': '3', 'address': '3', 'idoxu': '3'}]
    print(a[0]['id'])
    # 1
