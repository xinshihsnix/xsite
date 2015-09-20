# coding: utf-8
"""
参数说明:

"""

import sys

COMPANY = 'keju'
# print sys.argv

argvs = [a.lower() for a in sys.argv]   # 忽略大小写

option = argvs[1]

title = argvs[2]

content = argvs[3]

if option == 'add':
    pass

elif option == 's':
    """ select """
    pass

elif option == 'sa':
    """ select all  """
