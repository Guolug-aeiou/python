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

if __name__ == '__main__':
    db_utils = MySQLUtils('localhost','root','root', 'mini_blog')
    users = db_utils.select_list('select * from categories')
    for user in users:
        print(user)

