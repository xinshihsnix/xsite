# coding: utf-8
import MySQLdb


class DBService(object):
    def __init__(self, host, user, passwd, db, port=3306):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.port = port

        self.conn = self.connect()
        self.cursor = self.conn.cursor()

    def connect(self):
        conn=MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, port=3306)
        conn.select_db(self.db)

        return conn

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
