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


class TimeUtils(object):

    @classmethod
    def int_time_to_str_format(cls):
        """ 1343142315.35345 --> '134314231535345' """
        return str(time.time()).replace('.', '')

    @classmethod
    def time_now_to_str_format(cls):
        return datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')


class UrlUtils(object):

    @classmethod
    def unique_file_name_from_url(cls, url):
        full_name = url.split('/')[-1]
        postfix = full_name.split('.')[-1]
        unique_full_name = TimeUtils.int_time_to_str_format() + '.' + postfix
        return unique_full_name

