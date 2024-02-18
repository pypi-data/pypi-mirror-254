import json
import re
import uuid
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional, Any, List, Dict

from loguru import logger
from pydantic import BaseModel


# 调用返回类型
class RespType(Enum):
    """
    调用返回类型
    """
    task_success = 1  # 任务成功执行，并有结果
    task_normal = 0  # 任务成功执行，但无结果
    task_failed = -1  # 任务失败/取消
    task_delay = -2  # 任务延迟执行
    task_stock_limit = -3  # 无库存
    session_expired = -11  # session过期
    session_invalid_token = -12  # 无效token
    session_invalid_user = -13  # 无效用户名
    session_invalid_password = -14  # 无效密码
    session_user_blocked = -15  # 用户被冻结


class ActionType(Enum):
    """
    动作类型
    """
    bill_info = 1  # 提单信息
    ctn_list = 2  # 集装箱列表
    apply_eir = 3  # 申请条码
    print_eir = 4  # 打印条码


class BillStatus(Enum):
    canceled = -1,  # 已取消
    unknown = 0,  # 未知
    booked = 1,  # 已订舱
    applied = 2,  # 已申请
    printed = 3,  # 已打印
    taken = 4  # 已提箱


async def get_f_time(action):
    if action == ActionType.bill_info:
        return 'last_bill_info_time'
    elif action == ActionType.ctn_list:
        return 'last_ctn_list_time'
    elif action == ActionType.apply_eir:
        return 'last_apply_eir_time'
    else:
        return 'last_print_eir_time'


def clear_dict(d):
    """
    清除字典中的none值
    @param d:
    @return:
    """
    if not d:
        return None
    elif isinstance(d, list):
        return list(filter(lambda x: x is not None, map(clear_dict, d)))
    elif not isinstance(d, dict):
        return d
    else:
        r = dict(filter(lambda x: x[1], map(lambda x: (x[0], clear_dict(x[1])), d.items())))
        if not bool(r):
            return None
        return r


def is_json(ss):
    """
    判断是否json
    """
    try:
        return json.loads(ss)
    except Exception as e:
        logger.error(e)
        return


def get_guid():
    return uuid.uuid4().hex


class ResponseData(BaseModel):
    """
    响应类
    """
    code: Optional[RespType] = None
    msg: Optional[str] = ''
    data: Optional[Any] = None

    def __init__(self, **data: Any):
        super().__init__(**data)
        if data.get('code') and data.get('code') != RespType.task_success:
            if data.get('msg'):
                logger.info(f"{data.get('msg')}")
            if data.get('data'):
                logger.info(f"{data.get('data')}")


class SessionData(BaseModel):
    """
    session信息
    """
    session_guid: Optional[str] = None
    carrier_id: Optional[str] = None
    account: Optional[str] = None
    sub_code: Optional[str] = None
    bookingagent_id: Optional[str] = None
    proxy_id: Optional[str] = None
    login_time: Optional[float] = None
    last_access_time: Optional[float] = None
    state: int = 1
    data: dict = {}
    lock_id: Optional[str] = None  # 锁ID

    def __init__(self, **data: Any):
        super().__init__(**data)
        if not data.get('session_guid'):
            self.session_guid = get_guid()

    @property
    def redis_session_key(self):
        return f'{self.carrier_id}:{self.account}:{self.session_guid}'


class EirTaskInfo(BaseModel):
    """
    创建EirOrder参数
    """
    order_guid: Optional[str] = None
    carrier_id: Optional[str] = ''  # 船公司
    bookingagent_id: Optional[str] = ''  # 一代
    account: Optional[str] = ''  # 账号
    password: Optional[str] = ''  # 密码
    bill_no: Optional[str] = ''  # 提单号
    valid_code: Optional[str] = ''  # 校验码

    apply_ctntypedigit: Optional[str] = ''  # 申请箱型箱量 todo cma？
    ctntype_id: Optional[str] = ''  # 箱型
    ctn_digit: Optional[int] = 0  # 箱量
    client_user: Optional[str] = ''  # 客户用户名
    client_user_openid: Optional[str] = ''  # 客户用户Openid用于推送

    callback_url: Optional[str] = ''  # 回调url
    notify_email: Optional[str] = ''

    begin_time: Optional[datetime] = datetime.strptime(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'),
                                                       '%Y-%m-%d %H:%M:%S')  # 刷箱开始时间
    end_time: Optional[datetime] = datetime.strptime(
        datetime.strftime(datetime.now() + timedelta(hours=4), '%Y-%m-%d %H:%M:%S'),
        '%Y-%m-%d %H:%M:%S')  # 刷箱结束时间
    plan_amount: Optional[int] = 0  # 计划数 todo
    memo: Optional[str] = None  # 备注
    account_list: Optional[List[dict]] = []


class CtnInfo(BaseModel):
    """
    集装箱信息
    """
    bill_no: Optional[str] = None  # 提单号
    ctn_id: Optional[str] = None  # 集装箱号
    ctntype_id: Optional[str] = None  # 箱型
    is_applied: Optional[bool] = None  # 是否已申请
    is_printed: Optional[bool] = None  # 是否已打印
    is_taken: Optional[bool] = None  # 是否已提箱
    order_guid: Optional[str] = None  # 完成的订单号
    ctn_data: Optional[dict] = {}  # 服务器返回的集装箱数据
    barcode_data: Optional[dict] = {}  # 条码信息
    desc: Optional[str] = ''


class CtnListData(BaseModel):
    data: Optional[List[CtnInfo]] = []


class CtnTypeDigit(BaseModel):
    """
    箱型箱量
    """
    ctntype_id: Optional[str] = None  # 箱型
    ctn_digit: Optional[int] = 0  # 箱量
    ctn_digit_applied: Optional[int] = 0  # 已申请量
    ctn_digit_printed: Optional[int] = 0  # 已打印量
    ctn_digit_for_apply: Optional[int] = 0  # 可申请量，未申请
    ctn_digit_for_print: Optional[int] = 0  # 可打印量，已申请未打印
    ctn_digit_need_apply: Optional[int] = 0  # 需申请量,订单传过来的
    is_over_apply: bool = False  # 已超出申请量，不可再申请

    # is_valid = False  #

    def __str__(self):
        return f'{self.ctn_digit}x{self.ctntype_id.upper()}'


class BillCtntypeDigit(BaseModel):
    """
    提单箱型箱量
    """
    ctntype_id: Optional[str] = None  # 箱型
    ctn_digit_total: int = 0  # 总箱量
    ctn_digit_applied: int = 0  # 已申请量
    cnt_digit_printed: int = 0  # 已打印量
    is_over_apply: bool = False  # 已超出申请量，不可再申请


def convert_ctntype_tolist(ctntype_id, ctn_digit=1):
    """
    转换箱型箱量
    @return:
    """
    ctntypedigit_list = []
    if not ctntype_id:
        return ctntypedigit_list

    ctntype_id = ctntype_id.upper()

    # 如果未输入箱量并且箱型不符合 1x20GP 这样的格式,将ctntypedigit_list清空
    if not ctn_digit and not re.search('[xX]', ctntype_id):
        return ctntypedigit_list

    if ctntype_id.find('X') != -1:
        for item in re.split(r'[;,]', ctntype_id):
            if item:
                lst = re.split(r'[xX]', item)
                ctntypedigit = CtnTypeDigit()
                if lst[0].isdigit():
                    ctntypedigit.ctntype_id = lst[1]
                    ctntypedigit.ctn_digit = int(lst[0])
                else:
                    ctntypedigit.ctntype_id = lst[0]
                    ctntypedigit.ctn_digit = int(lst[1])
                ctntypedigit_list.append(ctntypedigit)
    elif ctntype_id:
        ctntypedigit = CtnTypeDigit()
        ctntypedigit.ctntype_id = ctntype_id
        ctntypedigit.ctn_digit = ctn_digit
        ctntypedigit_list.append(ctntypedigit)
    return ctntypedigit_list


class TaskResult(BaseModel):
    order_guid: Optional[str] = None
    status: Optional[BillStatus] = None
    memo: Optional[str] = None
    vessel: Optional[str] = None  # 船名
    voyage: Optional[str] = None  # 航次
    ctns: List[CtnInfo] = []  # 申请的集装箱列表


class BillInfo(BaseModel):
    carrier_id: Optional[str] = None  # 船公司
    bookingagent_id: Optional[str] = None  # 代理
    bill_no: Optional[str] = None  # 提单
    booking_no: Optional[str] = None  # 订舱号
    is_init: Optional[int] = None  # 是否已经初始化
    vessel: Optional[str] = None  # 船名
    voyage: Optional[str] = None  # 航次
    info: dict = {}
    status: BillStatus = None  # 提单状态


class EirOrder(EirTaskInfo):
    booking_no: Optional[str] = None  # 提单号
    bill_info: Optional[BillInfo] = BillInfo()  # 提单信息
    ctns: List[CtnInfo] = []  # 集装箱列表
    apply_ctns: List[CtnInfo] = []  # 申请的集装箱列表
    print_ctns: List[CtnInfo] = []
    ctntypedigit_list: Optional[List[CtnTypeDigit]] = []  # eir订单箱型箱量
    bill_ctntypedigit_dict: Optional[Dict[str, BillCtntypeDigit]] = {}  # 提单箱型箱量

    def __init__(self, **data: Any):
        super().__init__(**data)
        self.convert_ctntypedigit()

    def __str__(self):
        return f'{self.carrier_id} {self.bill_no} {self.order_guid}'

    def check_completed(self):
        """
        @todo 看看还需要吗？
        检查是否已完成，订单量 < 已打印量
        @return:
        """
        if self.ctntypedigit_list:
            for item in self.ctntypedigit_list:
                if item.ctn_digit_need_apply > item.ctn_digit_printed or item.ctn_digit > item.ctn_digit_printed or 0:
                    return False
            return True
        else:
            ctns = list(filter(lambda x: not x.is_printed, self.ctns))
            return not ctns

    def bill_summary(self):
        """
        获得集装箱列表后，箱型箱量统计
        @return:
        """
        self.ctns.sort(key=lambda x: x.ctntype_id)
        cur = None
        for ctn in self.ctns:
            if not cur or cur.ctntype_id != ctn.ctntype_id:
                cur = self.bill_ctntypedigit_dict.get(ctn.ctntype_id)
                if not cur:
                    cur = BillCtntypeDigit()
                    cur.ctntype_id = ctn.ctntype_id
                    self.bill_ctntypedigit_dict.update({cur.ctntype_id: cur})
                else:
                    cur.ctn_digit_total = cur.ctn_digit_applied = cur.cnt_digit_printed = 0
            cur.ctn_digit_total += 1
            cur.ctn_digit_applied += 1 if ctn.is_applied else 0
            cur.cnt_digit_printed += 1 if ctn.is_printed else 0

    def convert_ctntypedigit(self):
        """
        转换箱型箱量
        @return:
        """
        self.ctntypedigit_list = convert_ctntype_tolist(self.ctntype_id, self.ctn_digit)
        # 统一申请模式
        if self.apply_ctntypedigit:
            apply_ctntypedigit_list = convert_ctntype_tolist(self.apply_ctntypedigit)
            for item in apply_ctntypedigit_list:
                lst = list(filter(lambda x: x.ctntype_id == item.ctntype_id, self.ctntypedigit_list))
                if lst:
                    ctntypedigit = lst[0]
                    ctntypedigit.ctn_digit_need_apply = item.ctn_digit

    def ctns_for_apply(self):
        """
        获得待申请集装箱清单，整单则返回所有，按箱型则返回该箱型实际需求量
        @return:
        """
        if self.ctntypedigit_list:
            ctns = []
            for ctntypedigit in self.ctntypedigit_list:
                if ctntypedigit.ctn_digit_for_apply:
                    ctn_list = list(
                        filter(lambda x: x.ctntype_id == ctntypedigit.ctntype_id and not x.is_applied,
                               self.ctns))
                    ctns += ctn_list[:ctntypedigit.ctn_digit_for_apply]
                    return ctns
        else:
            return list(filter(lambda x: not x.is_applied, self.ctns))

    def ctns_for_print(self) -> List[CtnInfo]:
        """
        获得待打印集装箱清单，整单则返回所有，按箱型则返回该箱型实际需求量
        @return:
        """
        if self.ctntypedigit_list:
            ctns = []
            for ctntypedigit in self.ctntypedigit_list:
                if ctntypedigit.ctn_digit_for_print:
                    ctn_list = list(
                        filter(lambda x: x.ctntype_id == ctntypedigit.ctntype_id and x.is_applied and not x.is_printed,
                               self.ctns))
                    ctns += ctn_list[:ctntypedigit.ctn_digit_for_print]
                    return ctns
        else:
            return list(filter(lambda x: x.is_applied and not x.is_printed, self.ctns))

    @property
    def need_apply(self):
        """
        判断本单是否需要申请
        @return:
        """
        if self.ctntypedigit_list:
            for item in self.ctntypedigit_list:
                if item.ctn_digit_for_apply > 0:
                    return True
            return False
        else:
            return bool(list(filter(lambda x: not x.is_applied, self.ctns)))

    @property
    def need_print(self):
        """
        判断本单是否需要打印,未打印的 大于 未申请的 大于 0
        @return:
        """
        self.summary()
        if self.ctntypedigit_list:
            for item in self.ctntypedigit_list:
                if item.ctn_digit_for_print > 0:
                    return True
        else:
            return bool(list(filter(lambda x: x.is_applied and not x.is_printed, self.ctns)))

    @property
    def order_ctntype_digit_describe(self):
        """
        订单箱型箱量描述
        @return:
        """
        return self.ctntypedigit

    def summary(self):
        """
        获得集装箱列表后，计算各箱型需申请、打印量
        @return:
        """
        # 除了cma,msk,hpl，需要申请后才能获得集装箱列表，其他船公司都可以获取集装箱列表
        # msk 以申请为准
        # 其他船公司，ctntypedigit_list中的值，必须在集装箱列表中，否则就清空ctntypedigit_list，整票刷
        self.bill_summary()

        if self.carrier_id.upper() not in ['CMA-EIR', 'MSK-EIR', 'HPL-EIR'] and self.ctntypedigit_list:
            order_ctntype_set = set(map(lambda x: x.ctntype_id, self.ctntypedigit_list))
            bill_ctntype_set = set(map(lambda x: x.ctntype_id, self.ctns))
            if not bill_ctntype_set >= order_ctntype_set:
                self.ctntypedigit_list = []

        for item in self.ctntypedigit_list:
            bill_ctntypedigit = self.bill_ctntypedigit_dict.get(item.ctntype_id)
            # item.is_valid = bill_ctntypedigit is not None
            # if item.is_valid:
            item.ctn_digit_applied = 0 if not bill_ctntypedigit else bill_ctntypedigit.ctn_digit_applied
            item.ctn_digit_printed = 0 if not bill_ctntypedigit else bill_ctntypedigit.cnt_digit_printed
            # 可申请量=订单量-已申请量
            # 可打印量=min（订单量，已申请量-已打印量)
            item.ctn_digit_for_print = min(item.ctn_digit_applied - item.ctn_digit_printed, item.ctn_digit)

            if item.ctn_digit_need_apply:
                item.ctn_digit_for_apply = item.ctn_digit_need_apply - item.ctn_digit_applied if item.ctn_digit_need_apply > item.ctn_digit_applied else 0
            else:
                item.ctn_digit_for_apply = item.ctn_digit - item.ctn_digit_for_print if item.ctn_digit > item.ctn_digit_for_print else 0


class AccountInfo(BaseModel):
    carrier_id: Optional[str] = None  # 船公司
    account: Optional[str] = None
    password: Optional[str] = None
    bookingagent_id: Optional[str] = None
    info: dict = {}
