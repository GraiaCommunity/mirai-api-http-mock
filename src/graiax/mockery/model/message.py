from datetime import datetime
from enum import Enum
from typing import Any, List, Optional

from pydantic import BaseModel, Field


class Element(BaseModel):
    """
    指示一个消息中的元素.
    type (str): 元素类型
    """

    type: str = "Unknown"
    """元素类型"""


class Plain(Element):
    """代表消息中的文本元素"""

    type: str = "Plain"

    text: str
    """实际的文本"""


class Source(Element):
    """表示消息在一个特定聊天区域内的唯一标识"""

    type: str = "Source"

    id: int
    """消息 ID"""

    time: datetime
    """发送时间"""


class Quote(Element):
    """表示消息中回复其他消息/用户的部分, 通常包含一个完整的消息链(`origin` 属性)"""

    type: str = "Quote"

    id: int
    """引用的消息 ID"""

    groupId: int
    """引用消息所在群号 (好友消息为 0)"""

    senderId: int
    """发送者 QQ 号"""

    targetId: int
    """原消息的接收者QQ号 (或群号) """

    origin: "MessageChain"
    """原来的消息链"""


class At(Element):
    """该消息元素用于承载消息中用于提醒/呼唤特定用户的部分."""

    type: str = "At"

    target: int
    """At 的目标 QQ 号"""

    display: Optional[str]
    """显示名称"""


class AtAll(Element):
    """该消息元素用于群组中的管理员提醒群组中的所有成员"""

    type: str = "AtAll"


class Face(Element):
    """表示消息中所附带的表情, 这些表情大多都是聊天工具内置的."""

    type: str = "Face"

    faceId: Optional[int] = None
    """QQ 表情编号, 优先于 name"""

    name: Optional[str] = None
    """QQ 表情名称"""


class MarketFace(Element):
    """表示消息中的商城表情."""

    type: str = "MarketFace"

    id: int
    """QQ 表情编号"""

    name: str
    """QQ 表情名称"""


class Xml(Element):
    """表示消息中的 XML 消息元素"""

    type = "Xml"

    xml: str
    """XML文本"""


class Json(Element):
    """表示消息中的 JSON 消息元素"""

    type = "Json"

    Json: str = Field(None, alias="json")
    """JSON 文本"""


class App(Element):
    """表示消息中自带的 App 消息元素"""

    type = "App"

    content: str
    """App 内容"""


class PokeMethods(str, Enum):
    """戳一戳可用方法"""

    ChuoYiChuo = "ChuoYiChuo"
    """戳一戳"""

    BiXin = "BiXin"
    """比心"""

    DianZan = "DianZan"
    """点赞"""

    XinSui = "XinSui"
    """心碎"""

    LiuLiuLiu = "LiuLiuLiu"
    """666"""

    FangDaZhao = "FangDaZhao"
    """放大招"""

    BaoBeiQiu = "BaoBeiQiu"
    """宝贝球"""

    Rose = "Rose"
    """玫瑰花"""

    ZhaoHuanShu = "ZhaoHuanShu"
    """召唤术"""

    RangNiPi = "RangNiPi"
    """让你皮"""

    JeiYin = "JeiYin"
    """结印"""

    ShouLei = "ShouLei"
    """手雷"""

    GouYin = "GouYin"
    """勾引"""

    ZhuaYiXia = "ZhuaYiXia"
    """抓一下"""

    SuiPing = "SuiPing"
    """碎屏"""

    QiaoMen = "QiaoMen"
    """敲门"""


class Poke(Element):
    """表示消息中戳一戳消息元素"""

    type = "Poke"

    name: PokeMethods
    """戳一戳使用的方法"""


class Dice(Element):
    """表示消息中骰子消息元素"""

    type = "Dice"

    value: int
    """骰子值"""


class MusicShareKind(str, Enum):
    """音乐分享的来源。"""

    NeteaseCloudMusic = "NeteaseCloudMusic"
    """网易云音乐"""

    QQMusic = "QQMusic"
    """QQ音乐"""

    MiguMusic = "MiguMusic"
    """咪咕音乐"""

    KugouMusic = "KugouMusic"
    """酷狗音乐"""

    KuwoMusic = "KuwoMusic"
    """酷我音乐"""


class MusicShare(Element):
    """表示消息中音乐分享消息元素"""

    type = "MusicShare"

    kind: MusicShareKind
    """音乐分享的来源"""

    title: Optional[str]
    """音乐标题"""

    summary: Optional[str]
    """音乐摘要"""

    jumpUrl: Optional[str]
    """音乐跳转链接"""

    pictureUrl: Optional[str]
    """音乐图片链接"""

    musicUrl: Optional[str]
    """音乐链接"""

    brief: Optional[str]
    """音乐简介"""


class ForwardNode(BaseModel):
    """表示合并转发中的一个节点"""

    senderId: int
    """发送者 QQ 号 (决定显示头像)"""

    time: datetime
    """发送时间"""

    senderName: str
    """发送者显示名字"""

    messageChain: Optional["MessageChain"]
    """发送的消息链"""

    messageId: Optional[int]
    """缓存的消息 ID"""


class Forward(Element):
    """
    指示合并转发信息

    nodeList (List[ForwardNode]): 转发的消息节点
    """

    type = "Forward"

    nodeList: List[ForwardNode]
    """转发节点列表"""


class File(Element):
    """指示一个文件信息元素"""

    type = "File"

    id: str
    """文件 ID"""

    name: str
    """文件名"""

    size: int
    """文件大小"""


class MiraiCode(Element):
    """Mirai 码, 并不建议直接使用. Ariadne 也不会提供互转换接口."""

    type = "MiraiCode"

    code: str
    """Mirai Code"""


class MultimediaElement(Element):
    """指示多媒体消息元素."""

    id: Optional[str]
    """元素 ID"""

    url: Optional[str] = None
    """元素的下载 url"""

    path: Optional[str] = None

    base64: Optional[str] = None
    """元素的 base64"""


class Image(Element):
    """指示消息中的图片元素"""

    type = "Image"

    imageId: Optional[str] = None

    url: Optional[str] = None
    """元素的下载 url"""

    path: Optional[str] = None

    base64: Optional[str] = None
    """元素的 base64"""


class FlashImage(Element):
    """指示消息中的闪照元素"""

    type = "FlashImage"

    imageId: Optional[str] = None

    url: Optional[str] = None
    """元素的下载 url"""

    path: Optional[str] = None

    base64: Optional[str] = None
    """元素的 base64"""


class Voice(Element):
    """指示消息中的语音元素"""

    type = "Voice"

    voiceId: Optional[str] = None

    url: Optional[str] = None
    """元素的下载 url"""

    path: Optional[str] = None

    base64: Optional[str] = None
    """元素的 base64"""

    length: Optional[int]
    """语音长度"""


class MessageChain(BaseModel):
    """消息链"""

    __root__: List[Element]
    """消息元素"""

    def __init__(self, __root__: Any) -> None:
        super().__init__(__root__=__root__)


Quote.update_forward_refs(**locals())
ForwardNode.update_forward_refs(**locals())
