"""
阔景版权服务平台

网址：https://ds.kuojingyueyi.cn/app/index

注：上传文件需要 requests-toolbelt
"""

import os
import json
import time
import hashlib
import random
from pathlib import Path
from pprint import pprint as pp

import requests

from requests import Response
from requests_toolbelt import MultipartEncoder
from urllib.parse import urlparse

from .utils import need_login, BaseClient
from .exception import LoginError, NeedAccessTokenException

HEADERS_JSON = {
    'authorization': '',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'accept-language': 'zh-CN,zh;q=0.9'
}


class KuoJingYueYi(BaseClient):

    def __init__(self, base_url='https://ds.kuojingyueyi.cn', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_url = base_url
        self.set_headers(HEADERS_JSON)
        self.data = {}
        self._access_token = None

    def set_access_token(self, access_token):
        """
        设置用户授权
        """
        HEADERS_JSON['authorization'] = access_token
        self.set_headers(HEADERS_JSON)
        # 我们获取消息数量，检查是否已经登录成功

        self._access_token = access_token

    def need_access_token(self):
        """
        检查是否已登录，我们还是只简单检查有没有 access_token
        """
        # self.get_count_message()
        if self._access_token is None:
            raise NeedAccessTokenException()

    def get_response_data(self, resp):
        """
        解析接口返回的数据
        """
        try:
            self.data = resp.json()
        except Exception as e:
            return {
                "data": {
                    "description": f"转换json数据失败：{e}",
                    "error_code": 88888888,
                }
            }

        # 我们不检查信息是否错误，在获取信息的时候在检查
        # if self.data['code'] != 200:
        #     raise ValueError(f'{self.data}')

        return self.data

    def personal_center_my_detail(self):
        """
        用户信息（当前登录账户）

        个人中心/我的信息
        网址: https://ds.kuojingyueyi.cn/app/center/info
        """
        url = f"{self.base_url}/api/admin/personal-center/detail"
        r = self._session.get(url)
        return self.get_response_data(r)

    def contract_manage_cp_list(self, page=1, page_size=20, **kwargs):
        """
        采购合约列表

        合约管理/采购合约
        网址: https://ds.kuojingyueyi.cn/app/contract-manage/cp-list/?current=1&pageSize=20&offlineCode=SZQY-CGDL-20180401-200--051

        # 支持的参数
        "pageNo": 2,  # 可不用
        "current": 1,  # 可不用
        "pageSize": 20,  # 可不用
        # 内部合约编号
        "offlineCode": "SZQY-CGDL-20180401-200--051"
        """
        # print(kwargs)
        url = f"{self.base_url}/api/admin/cp-contract/list?pageNo={page}&pageSize={page_size}"
        r = self._session.post(url, json=kwargs)
        return self.get_response_data(r)

    def search_contract_song(self, contract_id, copyright_type=3, page=1, page_size=20):
        """
        采购合约关联歌曲

        合约管理/采购合约
        网址: https://ds.kuojingyueyi.cn/app/contract-manage/cp-list/?current=1&pageSize=20&offlineCode=SZQY-CGDL-20180401-200--051
        """
        data = {
            "contractId": contract_id,  # 合同ID
            "copyrightType": copyright_type  # 版权类型 1 词版权 2 曲版权 3 录音版权
        }
        url = f"{self.base_url}/api/admin/song/search-contract-song?pageNo={page}&pageSize={page_size}"
        r = self._session.post(url, json=data)
        return self.get_response_data(r)

    def settlement_supplier_document(self, page=1, page_size=20, **kwargs):
        """
        供应商结算单

        结算管理/供应商结算单
        网址: https://ds.kuojingyueyi.cn/app/settle-manage/supplier-bill-manage?current=1&pageSize=20&contractIdOrName=QHKJ-WTZZ

        # 支持的参数
        "pageNo": 2,  # 可不用
        "current": 1,  # 可不用
        "pageSize": 20,  # 可不用
        # 合同ID/编号/名称
        contractIdOrName: "QHKJ-WTZZ"
        """
        # print(kwargs)
        # https://ds.kuojingyueyi.cn/api/admin/settlement-supplier-document/list?pageNo=1&pageSize=20
        url = f"{self.base_url}/api/admin/settlement-supplier-document/list?pageNo={page}&pageSize={page_size}"
        r = self._session.post(url, json=kwargs)
        return self.get_response_data(r)

    def supplier_bill_detail(self, settle_id):
        """
        供应商结算单-详情

        结算管理/供应商结算单
        网址: https://ds.kuojingyueyi.cn/app/settle-manage/supplier-bill-detail/196
        """
        url = f"{self.base_url}/api/admin/settlement-supplier-document/detail/{settle_id}"
        r = self._session.get(url)
        return self.get_response_data(r)

    def supplier_bill_audit_approve(self, ids, status=0, approve='通过', msg=None):
        """
        供应商结算单-审核

        合约管理/供应商结算单
        网址: https://ds.kuojingyueyi.cn/app/app/settle-manage/supplier-bill-audit/196
        # status: 5 是当前审核状态 statusStr: "审核完成" 是状态描述
        # 可以通过 isCanApprove 来判断是否可以审核，"审核完成"和"驳回"的就算可以审核 再审核也没有意义
        # frozenStatus: 0 有审核权限的时候他也会影响审核按钮的状态 0 可以审核 1 禁止审核
        """
        # http://bq-test.karakal.com.cn:18100/api/admin/
        data = {
            "batchAudit": False,  # 批量审核
            "currentStatus": status,  # 0 初审 1 业务审核 2 复核 3 财务审核 > 流程结束
            "result": 1,  # 1 通过 0 不通过
            "supplierDocIds": ids,
            'msg': msg
        }

        if approve == '通过':
            data['result'] = 1
        else:
            data['result'] = 0
            if not msg:
                raise ValueError('请输入审批描述')

        if len(ids) > 1:
            data['batchAudit'] = True
        else:
            data['batchAudit'] = False

        url = f"{self.base_url}/api/admin/settlement-supplier-document/approve"
        r = self._session.post(url, json=data)
        return self.get_response_data(r)

    def get_cp_contract_detail(self, contract_id):
        """
        采购合约详情

        网址: https://ds.kuojingyueyi.cn/app/contract-manage/cp-view/17594?status=1
        """
        url = f"{self.base_url}/api/admin/cp-contract/detail/{contract_id}"
        r = self._session.get(url)
        return self.get_response_data(r)

    def get_cp_contract_detail_copyright(self, contract_id):
        """
        采购合约-版权信息

        网址:
        """
        url = f"{self.base_url}/api/admin/cp-contract/detail-copyright/{contract_id}"
        r = self._session.get(url)
        return self.get_response_data(r)

    def get_cp_contract_detail_settlement(self, contract_id):
        """
        采购合约-结算信息

        网址:
        """
        url = f"{self.base_url}/api/admin/cp-contract/detail-settlement/list/{contract_id}"
        r = self._session.get(url)
        return self.get_response_data(r)

    def song_list(self, page=1, page_size=20, **kwargs):
        """
        歌曲列表

        内容管理/歌曲管理
        网址: https://ds-test.kuojingyueyi.cn/app/content-manage/song-manage?current=1&pageSize=20

        # 支持的参数
        'queryType': 1,  # 可不用
        'pageNo': 1,   # 可不用
        "current": 1,  # 可不用
        "pageSize": 20,  # 可不用
        """
        # print(kwargs)
        url = f"{self.base_url}/api/admin/song/list?pageNo={page}&pageSize={page_size}"
        r = self._session.post(url, json=kwargs)
        return self.get_response_data(r)

    def song_detail(self, song_id):
        """
        歌曲详情

        歌曲管理/查看详情
        网址: https://ds-test.kuojingyueyi.cn/app/content-manage/song/detail/233616?status=1&albumId=73812
        """
        url = f"{self.base_url}/api/admin/song/detail/{song_id}"
        r = self._session.get(url)
        return self.get_response_data(r)
