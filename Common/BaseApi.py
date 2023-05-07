import requests
from Common.handel_yaml import get_yaml
from Common.handel_path import Test_config_path
from Common.custom_log import info_log, error_log

TOKEN = get_yaml(Test_config_path)["US_TOKEN"]  # 请求时默认的token


class Request:  #类名修改
    @staticmethod
    def post_request(url, body, token=TOKEN):
        header = {'Authorization': token}
        try:
            res = requests.post(url=url, headers=header, json=body)
            info_log(f'接口状态码：{res.status_code}')
            info_log(res.text)
            return res
        except Exception as e:
            error_log(f'python执行的错误信息{e}')
            return e

    @staticmethod
    def get_request(url, token=TOKEN, body=None):
        header = {'Authorization': token}
        try:
            res = requests.get(url=url, headers=header, params=body)
            info_log(f'接口状态码：{res.status_code}')
            info_log(f"接口响应文本：{res.text}")
            return res
        except Exception as e:
            error_log(f'python执行的错误信息{e}')
            return e
