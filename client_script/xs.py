#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
from db_service import xsite_dbs
import pyperclip

# print sys.argv

argvs = [a.lower() for a in sys.argv]   # 忽略大小写

option = argvs[1]


def handle_add():
    pass


def handle_s():
    pass


def handle_sa():
    _sql = 'select * from reminder_reminder'
    xsite_dbs.cursor.execute(_sql)
    rows = xsite_dbs.cursor.fetchall()

    for r in rows:
        print r[0], ' ------ ', r[2], ' ------ ', r[3]

    xsite_dbs.close()


def handle_cp():
    id = argvs[2]
    _sql = 'select content from reminder_reminder where id=%s'%id

    xsite_dbs.cursor.execute(_sql)
    content = xsite_dbs.cursor.fetchone()[0]

    print 'copy ok:', content
    pyperclip.copy(content)

options = [
    {
        'option': 'add',
        'help_text': '',
        'function': handle_add,
    },
    {
        'option': 's',
        'help_text': 'select',
        'function': handle_s,
    },
    {
        'option': 'sa',
        'help_text': 'select all',
        'function': handle_sa,
    },
    {
        'option': 'cp',
        'help_text': 'copy',
        'function': handle_cp,
    }
]


if __name__ == '__main__':
    for op in options:
        if option == op.get('option'):
            op.get('function')()
