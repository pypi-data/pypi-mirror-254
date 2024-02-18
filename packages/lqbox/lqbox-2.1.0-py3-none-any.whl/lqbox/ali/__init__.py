# -*- coding: utf-8 -*-

"""
@Project : lqbox 
@File    : __init__.py.py
@Date    : 2024/2/4 10:03:54
@Author  : zhchen
@Desc    : 
"""
import requests

from lqbox.base import BaseBox


class AliBox(BaseBox):
    pass


class AliLogBox(AliBox):
    base_url = "aHR0cHM6Ly9zbHM0c2VydmljZS5jb25zb2xlLmFsaXl1bi5jb20="

    @classmethod
    def login_from_mc(cls, url):
        session = requests.Session()
        response = session.get(url)
        cookies = dict(session.cookies)
        print(cookies)
        return cls(cookies)

    def __ali_log_request(self, path, data):
        return self.request(url=f"{self.base_url}{path}", method="POST", data=data)

    def get_logs(self, data):
        """获取日志"""
        # data = {
        #     'ProjectName': '123',
        #     'LogStoreName': '123',
        #     'from': '1706976000',
        #     'query': 'exp | with_pack_meta',
        #     'to': '1707014768',
        #     'Page': '1',
        #     'Size': '20',
        #     'Reverse': 'true',
        #     'pSql': 'false',
        #     'schemaFree': 'false',
        #     'needHighlight': 'true',
        # }
        return self.__ali_log_request(path="/console/logs/getLogs.json", data=data)
