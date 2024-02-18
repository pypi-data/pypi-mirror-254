#############################################
# File Name: ddreport
# Author: duanliangcong
# Mail: 137562703@qq.com
# Created Time:  2022-11-02 15:00:00
#############################################
from _pytest.python import Function
from _pytest.runner import runtestprotocol
from jsonpath import jsonpath
from collections.abc import Iterable
from ddreport.api import CustomQuery
from ddreport.db import PytestMysql
from ddreport.func import PytestFunctions
from ddreport.handle import Process
from itertools import product
import requests
import pytest
import time
import json
import os, sys
import re
import ast
import traceback


requests.packages.urllib3.disable_warnings()

test_result = {
    "title": "",
    "desc": "",
    "tester": "",
    "start_time": "",
    "end_time": "",
    "failed": 0,
    "passed": 0,
    "skipped": 0,
    "error": 0,
    "cases": [],
}

dict_data = {
    'show_success': False
}

Result = {"nowResponse": {}}


class Gvalues(object):
    __slots__ = ('__value')

    def __init__(self):
        self.__value = dict()

    def set(self, key, value):
        self.__value.update({key: value})

    def get(self, key):
        return self.__value.get(key)

    def append(self, key, value):
        self.__value.get(key).append(value)

    def extend(self, key, value):
        self.__value.get(key).extend(value)

    def insert(self, key, index, value):
        self.__value.get(key).insert(index, value)


GG = Gvalues()

dd_paramet = dict()

exit_info = {"fail": False, "status": "passed"}


def getEnvData(env_path, env_name):
    try:
        with open(env_path, 'r', encoding='utf-8')as f:
            envs = json.loads(f.read())
        return jsonpath(envs, f'$..[?(@.env_name=="{env_name}")]')[0]
    except Exception:
        return dict()


def node_handle(node, item, call):
    d = dict()
    # 模块
    d['model'] = item.module.__name__
    # 类
    d['classed'] = '' if item.parent.obj == item.module else item.parent.obj.__name__
    # 方法
    d['method'] = item.originalname
    # 描述
    d['doc'] = item.function.__doc__
    # 响应时间
    d['duration'] = call.duration
    # 结果
    d['status'] = node.outcome
    # 详细内容
    if node.sections:
        d["print"] = ''.join(node.sections[0][1:]).replace('<', '&lt;').replace('>', '&gt;')
    # 异常信息展示
    if call.excinfo:
        excobj = node.longrepr
        try:
            if d['status'] == 'skipped':
                d["skipped"] = excobj[-1].replace('<', '&lt;').replace('>', '&gt;')
            else:
                # 错误的响应信息，如没有设置verfy
                d.update(call.excinfo.value.value.query_info)
                d.update(call.excinfo.value.value.error_info)
        except Exception:
            # 异常情况
            try:
                exc_list = ["file " + excobj.reprcrash.path + ", line " + str(excobj.reprcrash.lineno), excobj.reprcrash.message.replace('<', '&lt;').replace('>', '&gt;')]
            except Exception:
                try:
                    exc_list = excobj.tblines
                    errorstring = excobj.errorstring
                    exc_list.append(errorstring)
                except Exception:
                    exc_list = [str(call.excinfo).replace('<', '&lt;').replace('>', '&gt;')]
            d.update(dict(msg_dict="\n".join(exc_list)))
            # 失败的的类型
            failed_list = ["AssertionError", "assert"]
            # 如果不是失败类型就是错误的
            if not any([exc_list[-1].startswith(ee) for ee in failed_list]):
                d['status'] = "error"
                node.outcome = "error"

    # 打印正确请求
    if GG.get("@@ddreportQuery") and dict_data['show_success'] is True:
        queryData = GG.get("@@ddreportQuery")
        if queryData:
            Pro = Process()
            Pro.data_process(queryData, None)
            d.update(Pro.query_info)
    return d


def pytest_addoption(parser):
    """添加main的可调用参数"""
    group = parser.getgroup("testreport")
    group.addoption(
        "--ddreport",
        action="store",
        default=None,
        help="测试报告标识",
    )
    group.addoption(
        "--title",
        action="store",
        default=None,
        help="测试报告最顶部标题",
    )
    group.addoption(
        "--desc",
        action="store",
        default=None,
        help="当前测试报告的说明",
    )
    group.addoption(
        "--tester",
        action="store",
        default=None,
        help="测试人员",
    )
    group.addoption(
        "--env_path",
        action="store",
        default=None,
        help="环境配置路径",
    ),
    group.addoption(
        "--env_name",
        action="store",
        default=None,
        help="环境名称",
    ),
    group.addoption(
        "--receive",
        action="store",
        default=None,
        help="接收一个字典类型的参数",
    ),
    group.addoption(
        "--api_success",
        action="store",
        default=None,
        help="是否打印正确的api请求信息",
    ),


def pytest_sessionstart(session):
    test_result['start_time'] = time.strftime("%Y-%m-%d %H:%M:%S")
    test_result['title'] = session.config.getoption('--title') or ''
    test_result['tester'] = session.config.getoption('--tester') or ''
    test_result['desc'] = session.config.getoption('--desc') or ''
    # 是否展示正确的请求及响应信息
    success_show = session.config.getoption('--api_success')
    try:
        if success_show.upper() == "TRUE" or int(success_show) == 1:
            dict_data['show_success'] = True
        else:
            dict_data['show_success'] = False
    except Exception:
        dict_data['show_success'] = False
    # 记录命令传过来的参数
    receive_dict = session.config.getoption("--receive")
    if receive_dict:
        try:
            receive_dict = json.loads(receive_dict)
        except Exception:
            try:
                receive_dict = ast.literal_eval(receive_dict)
            except Exception:
                receive_dict = {}
        for k, v in receive_dict.items():
            GG.set(k, v)


def pytest_sessionfinish(session, exitstatus):
    def set_default(obj):
        if isinstance(obj, (list, dict)):
            return str(obj).replace('<', '&lt;').replace('>', '&gt;')
    test_result['end_time'] = time.strftime("%Y-%m-%d %H:%M:%S")
    ddreport = session.config.getoption('--ddreport')
    if ddreport:
        report_dirOrFile = ddreport.replace('\\', '/').strip()
        if not report_dirOrFile.endswith('.html'):
            report_dir, report_name = report_dirOrFile, f'testReport {time.strftime("%Y-%m-%d_%H%M%S")}.html'
        else:
            report_dir, report_name = '/'.join(report_dirOrFile.split('/')[:-1]), report_dirOrFile.split('/')[-1]
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)
        report_save_path = os.path.join(report_dir, report_name)
        # 读取测试报告文件
        template_path = os.path.join(os.path.dirname(__file__), './template')
        with open(f'{template_path}/index.html', 'r', encoding='utf-8')as f:
            template = f.read()
        report_template = template.replace('templateData', json.dumps(test_result))
        with open(report_save_path, 'w', encoding='utf-8') as f:
            f.write(report_template)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    call.duration = '%.2f' % call.duration          # 科学计数转普通格式
    info = {}
    if report.when == 'call':
        # 过滤不需要的funcargs
        dd_paramet.clear()
        params_keys = [om.args[0] for om in item.own_markers if om.args]
        for k in item.fixturenames:
            if k in ["_session_faker", "request"]:
                continue
            elif params_keys and k in params_keys:
                continue
            else:
                dd_paramet[k] = item.funcargs[k]
        info = node_handle(report, item, call)
        test_result[report.outcome] += 1
        # 失败结束标签
        if item.funcargs.get("ddreport") and item.funcargs["ddreport"].pyexit is True:
            exit_info["fail"] = True
            exit_info["status"] = report.outcome
            if report.outcome != "passed":
                info["fail_tag"] = "用例标记为: 非成功用例，程序结束"
    elif report.outcome == 'failed':
        report.outcome = 'error'
        info = node_handle(report, item, call)
        test_result['error'] += 1
    elif report.outcome == 'skipped':
        info = node_handle(report, item, call)
        test_result[report.outcome] += 1
    if report.when == 'teardown':
        # 是否有图片信息
        if GG.get("@ddImage"):
            Result["nowResponse"].update(dict(img=GG.get("@ddImage")))
        test_result["cases"].append(Result["nowResponse"])
        GG.set("@@ddreportQuery", None)
        GG.set("@ddImage", None)
        if exit_info["fail"]:
            if exit_info["status"] != "passed":
                pytest.exit()
            else:
                item.funcargs["ddreport"].pyexit = False
                exit_info.update({"fail": False, "status": "passed"})
    Result["nowResponse"] = info


@pytest.fixture(scope='session')
def ddreport(request):
    # 环境获取
    env_path = request.config.getoption("--env_path")
    env_name = request.config.getoption("--env_name")
    get_env = getEnvData(env_path, env_name)
    host = get_env.get('host') or ''
    mysqlConfig = get_env.get('mysql')
    return DDreport(host, mysqlConfig)


class DDreport:
    def __init__(self, host, mysqlConfig):
        self.gval = GG
        self.api = CustomQuery(GG, host)
        self.fc = PytestFunctions()
        self.mysql = None
        if mysqlConfig:
            from ddreport.db import PytestMysql
            self.mysql = PytestMysql(mysqlConfig)
        self.pyexit = False      # 失败后结束程序
        super().__init__()


def pytest_runtest_protocol(item, nextitem):

    # 笛卡尔乘积索引
    def cartesian_product_index(input_list):
        if len(input_list) == 0:
            return [[]]
        result = []
        for i, element in enumerate(input_list[0]):
            for sub_index in cartesian_product_index(input_list[1:]):
                result.append([(i, element)] + sub_index)
        return result

    # copy-item-function
    def copy_item(curitem):
        newitem = Function.from_parent(name=curitem.originalname, parent=curitem.parent, callspec=curitem.callspec,
                                       fixtureinfo=curitem._fixtureinfo, originalname=curitem.originalname)
        return newitem

    # 是否使用ddreport的动态参数化
    is_cus_loop = False
    data_list = list()
    for i in item.own_markers:
        if i.name == "parametrize":
            args_key = i.args[0]
            args_str = i.args[-1]
            if isinstance(args_str, str) and args_str.endswith("}") and any([args_str.startswith(k) for k in ["{self.", "{cls.", "{dd."]]):
                is_cus_loop = True
                args_name = args_str[1:-1]
                if args_name.startswith("self.") or args_name.startswith("cls."):
                    obj_names = args_name.replace("self.", "").replace("cls.", "").split("[")
                    obj_name, obj_item = obj_names[0], obj_names[-1][1:-2]
                    if obj_item:
                        data = item.parent._obj.__dict__.get(obj_name, {}).get(obj_item)
                    else:
                        data = item.parent._obj.__dict__.get(obj_name)
                elif args_name.startswith("dd."):
                    obj_name = args_name.replace("dd.", "")
                    data = GG.get(obj_name) or None
            else:
                data = args_str
            if not isinstance(data,Iterable):
                data = [data]
            data_list.append({args_key: data})

    if is_cus_loop:
        ks = list(map(lambda x: list(x.keys())[0], data_list))
        vals = list(map(lambda x: list(x.values())[0], data_list))
        index_list = cartesian_product_index(vals)
        for loop_data in index_list:
            new_item = copy_item(item)
            params_d = dict()
            indices_d = dict()
            for n, it in enumerate(loop_data):
                indices_val = it[0]
                params_val = it[1]
                indices_d.update({ks[n]: indices_val})
                params_d.update({ks[n]: params_val})
            new_item.callspec.params.update(params_d)
            new_item.callspec.indices.update(indices_d)
            for k, v in dd_paramet.items():
                new_item.funcargs[k] = dd_paramet[k]
            runtestprotocol(new_item, nextitem=None)
        return True
    else:
        for k, v in dd_paramet.items():
            item.funcargs[k] = dd_paramet[k]


def pytest_report_teststatus(config, report):
    # 更新终端打印（.  s   F  E）
    if report.outcome == 'error':
        return report.outcome, 'E', None


def pytest_collection_modifyitems(session, config, items):
    # 处理用例收集函数
    new_items = list()
    parame_name = list()
    for i in items:
        if not i.own_markers:
            new_items.append(i)
        else:
            for p in i.own_markers:
                if p.name == "parametrize":
                    if isinstance(p.args[-1], str) and p.args[-1].startswith("{") and p.args[-1].endswith("}"):
                        args_name = p.args[-1][1:-1]
                        if args_name.startswith("self.") or args_name.startswith("dd."):
                            item_name = i.module.__name__ + "&" + i.originalname
                            if item_name not in parame_name:
                                parame_name.append(item_name)
                                new_items.append(i)
                            break
                    new_items.append(i)
                else:
                    new_items.append(i)

    session.items = new_items
    items = new_items
    config.pluginmanager.get_plugin("terminalreporter")._numcollected = len(session.items)
