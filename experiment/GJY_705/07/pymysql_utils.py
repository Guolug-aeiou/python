import pymysql

class MySQLUtils:
    # 初始化操作,连接数据
    def __init__(self, host, user, password, database):
        self.connection = None
        self.cursor = None
        try:
            self.connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                charset='utf8'
            )
            self.cursor = self.connection.cursor()
        except pymysql.Error as e:
            print(f"数据库连接失败：{e}")
            raise
    # 执行语句
    def execute_query(self, sql, params=None):
        try:
            self.cursor.execute(sql, params)
            return self.cursor.fetchall()
        except pymysql.Error as e:
            print(f"执行查询出错：{e}")
            return None
    # 执行更新
    def execute_update(self, sql, params=None):
        try:
            self.cursor.execute(sql, params)
            self.connection.commit()
            return self.cursor.rowcount
        except pymysql.IntegrityError as e:
            self.connection.rollback()
            print(f"操作失败：数据重复或约束错误。详情：{e}")
            return 0
        except pymysql.Error as e:
            self.connection.rollback()
            print(f"数据库错误：{e}")
            return 0
    # 关闭数据连接
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()