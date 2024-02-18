# _*_ coding:utf-8 _*_
from typing import Optional
from enum import EnumMeta
from pydantic import BaseModel


class AtMobile(BaseModel):
    atMobiles: Optional[list] = []
    isAtAll: Optional[bool] = False


class TextMsg(BaseModel):
    project_title: str
    subserver: str
    text: str


class Text(BaseModel):
    """
    文本消息结构
    """
    msgtype: Optional[str] = "text"
    text: Optional[dict] = {}
    at: Optional[dict] = AtMobile.construct()


class MarkdownMsg(BaseModel):
    title: Optional[str] = " "
    text: Optional[str] = ""


class Markdown(BaseModel):
    msgtype: Optional[str] = 'markdown'
    markdown: Optional[dict] = MarkdownMsg.construct()
    at: Optional[dict] = AtMobile.construct()


class LinkMsg(BaseModel):
    text: Optional[str] = ""
    title: Optional[str] = ""
    picUrl: Optional[str] = ""
    messageUrl: Optional[str] = ""


class Link(BaseModel):
    msgtype: Optional[str] = 'link'
    link: Optional[dict] = LinkMsg.construct()


class RedisConfig(EnumMeta):
    TASK_QUEUE = '{}:{}:queue'
    RUN_SIGN = '{}:{}:run_sign'
    MD5_HSET = '{}:{}:{}'  # 服务，子服务，日期


# ---------------------------- WEB 请求返回枚举配置 ----------------------------
class WebEnum(EnumMeta):
    STATUS_SUCCESS = [0, '启动成功']
    STATUS_RUNING = [1, '正在运行']
    STATUS_BREAK = [0, '程序退出']
    STATUS_ERROR = [1, '程序错误']
    STATUS_UNKNOWN = [1, '未知参数']
    STATUS_INIT = [0, '初始化成功']


# ------------------------------ POST接口传参声明 --------------------------------
class PostItems(BaseModel):
    """
    传参
    """
    service_name: str
    subserver: str
    operation_type: Optional[str] = 'sync'  # sync:同步，async:异步， 默认同步
    run_sign: Optional[str] = 'start'  # start:启动，stop:停止， 默认启动
    extra_params: Optional[dict] = {}  # 额外传参


class ItemEnum(EnumMeta):
    OPERATION_ASYNC = "async"  # 异步操作
    OPERATION_SYNC = "sync"  # 同步操作
    RUN_START = "start"  # 开始
    RUN_STOP = "stop"  # 停止


class UrlEnum(EnumMeta):
    Get_Url = "http://192.168.0.12:8014/api/v1/common-lingxing-sign-api/schedule"
    PAYLOAD = {
        "service_name": "common-lingxing-sign-api",
        "subserver": "get_lingxing_sign_api",
        "extra_params": {}
    }
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
                      "/107.0.0.0 Safari/537.36",
        "Content-Type": "application/json"
    }

