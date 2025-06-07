import pymysql

class MySQLUtils:
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
    def connect(self):
        return pymysql.connect(host=self.host,
                               user=self.user,
                               password=self.password,
                               db=self.db,
                               cursorclass=pymysql.cursors.DictCursor)
    def select_one(self, sql, params=()):
        try:
            conn = self.connect()
            cur = conn.cursor()
            cur.execute(sql, params)
            return cur.fetchone()
        finally:
            cur.close()
            conn.close()

    def select_list(self, sql, params=()):
        try:
            conn = self.connect()
            cur = conn.cursor()
            cur.execute(sql, params)
            return cur.fetchall()
        finally:
            cur.close()
            conn.close()

    def update(self, sql , params=()):
        try:
            conn = self.connect()
            cur = conn.cursor()
            result = cur.execute(sql, params)
            conn.commit()
            return result
        except:
            conn.rollback()
            raise
        finally:
            cur.close()
            conn.close()
    def insert(self, sql: str, params: tuple = None) -> int:
        """插入一条数据，并返回自增主键"""
        with self.conn.cursor() as cursor:
            cursor.execute(sql, params)
            self.conn.commit()
            return cursor.lastrowid

if __name__ == '__main__':
    db_utils = MySQLUtils('localhost','root','root', 'mini_blog')
    db_utils.update("INSERT INTO users(`username`,`password`,`nickname`,`email`) VALUES(%s,%s,%s,%s)",('11234','1234','l12izhi','12314@qq.com'))
    # db_utils.insert('INSERT INTO users(`username`,`password`,`nickname`,`email`) VALUES(%s,%s,%s,%s)',("1234","1234","lizhi","1234@qq.com"))
