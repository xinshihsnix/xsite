# coding: utf-8
import MySQLdb
import smtplib


class DBService(object):
    def __init__(self, host, user, passwd, db, port=3306, charset='utf8'):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.port = port
        self.charset = charset

        self.conn = self.connect()
        self.cursor = self.conn.cursor()

    def connect(self):
        conn=MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, port=3306, charset=self.charset)
        conn.select_db(self.db)

        return conn

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

    @classmethod
    def get_xsite_db(cls):
        from django.conf import settings
        d = settings.DATABASES.get('default')
        host = d.get('HOST')
        user = d.get('USER')
        passwd= d.get('PASSWORD')
        name = d.get('NAME')

        dbs = cls(host, user, passwd, name)
        return dbs


class EncryptService(object):
    def __init__(self):
        # todo
        pass


class MailService(object):
    def __init__(self, servername, user, pwd):
        self.servername = servername
        self.username = user
        self.pwd = pwd
        self.smtp = smtplib.SMTP(self.user)

        self.login()

    def login(self):
        smtplib.SMTP(self.servername)
        self.smtp.login(self.user, self.pwd)

    def close(self):
        self.smtp.close()

    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText

    # python 2.3.*: email.Utils email.Encoders
    from email.utils import COMMASPACE,formatdate
    from email import encoders

    import os

    #server['name'], server['user'], server['passwd']
    def send_mail(server, fro, to, subject, text, files=[]):

        msg = MIMEMultipart()
        msg['From'] = fro
        msg['Subject'] = subject
        msg['To'] = COMMASPACE.join(to) #COMMASPACE==', '
        msg['Date'] = formatdate(localtime=True)
        msg.attach(MIMEText(text))

        for file in files:
            part = MIMEBase('application', 'octet-stream') #'octet-stream': binary data
            part.set_payload(open(file, 'rb'.read()))
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
            msg.attach(part)

        smtp = smtplib.SMTP(server['name'])
        smtp.login(server['user'], server['passwd'])
        smtp.sendmail(fro, to, msg.as_string())
        smtp.close()