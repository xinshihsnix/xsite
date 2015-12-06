# coding: utf-8
import requests
import re
import json


def get_address_from_ip(ip):
    """
    sina api return result:
    var remote_ip_info = {"ret":1,"start":-1,"end":-1,"country":"\u4e2d\u56fd","province":"\u5317\u4eac","city":"\u5317\u4eac","district":"","isp":"","type":"","desc":""};
    """
    try:
        sina_api = "http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=js&ip=%s"%ip
        r = requests.get(sina_api)
        text = re.search('{.*}', r.text)
        result_json = json.loads(text)

        return result_json.get('city', u'人间')
    except:
        return u'人间'