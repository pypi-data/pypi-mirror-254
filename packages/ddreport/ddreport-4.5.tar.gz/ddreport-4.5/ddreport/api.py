from ddreport.exceptd import ExceptInfo
from jsonpath import jsonpath
import requests
import traceback
import warnings
requests.packages.urllib3.disable_warnings()


class RequestObj(object):
    __slots__ = ('__query', '__status_code', '__resp_headers', '__resp_cookies', '__response')

    def __init__(self):
        self.__query = None
        self.__status_code = None
        self.__resp_headers = None
        self.__resp_cookies = None
        self.__response = None

    @property
    def query(self):
        return self.__query

    @query.setter
    def query(self, value):
        self.__query = value

    @property
    def status_code(self):
        return self.__status_code

    @status_code.setter
    def status_code(self, value):
        self.__status_code = value

    @property
    def resp_headers(self):
        return self.__resp_headers

    @resp_headers.setter
    def resp_headers(self, value):
        self.__resp_headers = value

    @property
    def resp_cookies(self):
        return self.__resp_cookies

    @resp_cookies.setter
    def resp_cookies(self, value):
        self.__resp_cookies = value

    @property
    def response(self):
        return self.__response

    @response.setter
    def response(self, value):
        self.__response = value


class ExceptObj:
    __slots__ = ('__msg_dict', '__typed')

    def __init__(self):
        self.__msg_dict = None
        self.__typed = None

    @property
    def msg_dict(self):
        return self.__msg_dict

    @msg_dict.setter
    def msg_dict(self, value):
        self.__msg_dict = value

    @property
    def typed(self):
        return self.__typed

    @typed.setter
    def typed(self, value):
        self.__typed = value

def session():
	# 这行告警代码被识别到
    warnings.warn("some_old_function is deprecated", DeprecationWarning)
    return



class CustomQuery():
    def __init__(self, gg, host=''):
        self.host = host
        self.__GG = gg
        self.headers = dict()
        self.cookies = dict()
        self.verify = None
        self.proxies = None
        self.cert = None

    def __assert(self, r, is_json, assert_list, E, Q):
        if not assert_list:
            if r.status_code != 200:
                E.typed = 20                                                                           # 状态码错误
                E.msg_dict = r.status_code
                ExceptInfo(Q, E).raised()
            else:
                return r
        if isinstance(assert_list, list) is False:
            E.typed = 11                                                                                # 断言类型错误
            E.msg_dict = assert_list
            ExceptInfo(Q, E).raised()
        for n, assert_item in enumerate(assert_list):
            if not isinstance(assert_item, dict):
                E.typed = 12                                                                            # 断言元素类型错误
                E.msg_dict = dict(eq=assert_item, row=n+1)
                ExceptInfo(Q, E).raised()
            if not all([k in assert_item.keys() for k in ["type", 'exp', 'value']]):
                E.typed = 13                                                                            # 断言元素key错误
                E.msg_dict = dict(eq=assert_item, row=n + 1)
                ExceptInfo(Q, E).raised()
            if assert_item.get("type").upper() == 'TEXT':
                if assert_item.get("value") not in r.text:
                    E.typed = 21                                                                        # TEXT匹配失败
                    E.msg_dict = dict(eq=assert_item, row=n + 1, expect_value=assert_item.get("value"))
                    ExceptInfo(Q, E).raised()
            elif assert_item.get("type").upper() in ['JSON', 'JSON_BOOL', 'JSON_IN', 'JSON_LEN']:
                if is_json is False:
                    E.typed = 14                                                                        # 响应类型不是json
                    E.msg_dict = dict(eq=assert_item, row=n + 1)
                    ExceptInfo(Q, E).raised()
                results = jsonpath(r.json(), assert_item.get('exp')) or []
                result = results[0] if len(results) == 1 else results
                if assert_item.get("type").upper() == "JSON":
                    if result != assert_item.get("value"):
                        E.typed = 22                                                                   # JSON匹配失败
                        E.msg_dict = dict(eq=assert_item, row=n + 1, expect_value=assert_item.get("value"), actual_value=result)
                        ExceptInfo(Q, E).raised()
                elif assert_item.get("type").upper() == "JSON_BOOL":
                    if bool(result) != assert_item.get("value"):
                        E.typed = 22                                                                    # JSON匹配失败
                        E.msg_dict = dict(eq=assert_item, row=n + 1, expect_value=assert_item.get("value"), actual_value=result)
                        ExceptInfo(Q, E).raised()
                elif assert_item.get("type").upper() == "JSON_IN":
                    if result not in assert_item.get("value"):
                        E.typed = 22  # JSON匹配失败
                        E.msg_dict = dict(eq=assert_item, row=n + 1, expect_value=assert_item.get("value"), actual_value=result)
                        ExceptInfo(Q, E).raised()
                else:
                    try:
                        length = len(result)
                    except Exception:
                        length = ''
                    if length != assert_item.get("value"):
                        E.typed = 22                                                                    # JSON匹配失败
                        E.msg_dict = dict(eq=assert_item, row=n + 1, expect_value=assert_item.get("value"), actual_value=length)
                        ExceptInfo(Q, E).raised()
            else:
                E.typed = 15                                                                            # 元素类型值错误
                E.msg_dict = dict(eq=assert_item, row=n + 1)
                ExceptInfo(Q, E).raised()

    def query(self, method=None, url=None, **kwargs):
        Q = RequestObj()
        E = ExceptObj()
        if self.headers is None:
            self.headers = dict()
        if self.cookies is None:
            self.cookies = dict()
        self.__info, asserts, encode = {}, None, 'utf-8'
        if "eq" in kwargs.keys():
            asserts = kwargs["eq"]
            del kwargs['eq']
        if "encode" in kwargs.keys():
            encode = kwargs["encode"]
            del kwargs['encode']
        if method:
            kwargs["method"] = method
        if url:
            kwargs["url"] = url
        if not kwargs['url'].startswith('http'):
            kwargs['url'] = self.host + kwargs['url']
        if "headers" in kwargs.keys():
            if kwargs.get("headers"):
                self.headers.update(kwargs["headers"])
            else:
                self.headers = {}
        if "cookies" in kwargs.keys():
            if kwargs.get("cookies"):
                self.cookies.update(kwargs["cookies"])
            else:
                self.cookies = {}
        if "verify" in kwargs.keys():
            self.verify = kwargs["verify"]
        if "proxies" in kwargs.keys():
            if kwargs.get("proxies"):
                self.proxies = kwargs["proxies"]
            else:
                self.proxies = None
        if "cert" in kwargs.keys():
            if kwargs.get("cert"):
                self.cert = kwargs["cert"]
            else:
                self.cert = None
        data = kwargs.copy()
        if self.headers:
            data.update({"headers": self.headers.copy()})
        if self.cookies:
            data.update({"cookies": self.cookies.copy()})
        if self.verify is not None:
            vf = {"verify": self.verify}.copy()
            data.update(vf)
        if self.proxies:
            data.update({"proxies": self.proxies.copy()})
        if self.cert:
            data.update({"cert": self.cert.copy()})
        Q.query = data
        try:
            r = requests.request(**data)
            r.encoding = encode
            status_code = r.status_code
            headers = dict(r.headers)
            cookies = r.cookies.get_dict()
            if cookies:
                self.cookies.update(cookies)
            try:
                response, is_json = r.json(), True
            except Exception:
                response, is_json = r.text, False
            Q.status_code, Q.resp_headers, Q.resp_cookies, Q.response = status_code, headers, cookies, response
            self.__GG.set("@@ddreportQuery", Q)
        except Exception:
            E.typed = 10
            E.msg_dict = traceback.format_exc()
            ExceptInfo(Q, E).raised()
        self.__assert(r, is_json, asserts, E, Q)
        return r
