# coding: utf-8
import datetime
import time

def section_list(list, rows):
    """
    [1,2,3,4,5,6,7,8]  -->  [[1,2,3],[4,5,6],[7,8]]
    """
    section = []
    step = 0
    steps = (len(list)/rows) + 1

    for s in xrange(steps):
        section.append(list[s*rows: (s+1)*rows])
    return section


def unique_time_str():
    """ 1343142315.35345 --> '134314231535345' """
    return str(time.time()).replace('.', '')


def time_now_str():
    return datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')