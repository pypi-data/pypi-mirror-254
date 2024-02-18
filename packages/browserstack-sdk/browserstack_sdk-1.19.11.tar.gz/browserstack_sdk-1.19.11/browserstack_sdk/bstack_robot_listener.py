# coding: UTF-8
import sys
bstack111l_opy_ = sys.version_info [0] == 2
bstack11l11l1_opy_ = 2048
bstack1ll1ll1_opy_ = 7
def bstack111lll1_opy_ (bstack11lll11_opy_):
    global bstack1ll11_opy_
    bstack1lllll1_opy_ = ord (bstack11lll11_opy_ [-1])
    bstack11l1ll1_opy_ = bstack11lll11_opy_ [:-1]
    bstack1l1lll1_opy_ = bstack1lllll1_opy_ % len (bstack11l1ll1_opy_)
    bstack111lll_opy_ = bstack11l1ll1_opy_ [:bstack1l1lll1_opy_] + bstack11l1ll1_opy_ [bstack1l1lll1_opy_:]
    if bstack111l_opy_:
        bstack111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11l1_opy_ - (bstack1l11l1_opy_ + bstack1lllll1_opy_) % bstack1ll1ll1_opy_) for bstack1l11l1_opy_, char in enumerate (bstack111lll_opy_)])
    else:
        bstack111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l11l1_opy_ - (bstack1l11l1_opy_ + bstack1lllll1_opy_) % bstack1ll1ll1_opy_) for bstack1l11l1_opy_, char in enumerate (bstack111lll_opy_)])
    return eval (bstack111l1l_opy_)
import os
import datetime
import threading
from uuid import uuid4
from itertools import zip_longest
from collections import OrderedDict
from robot.libraries.BuiltIn import BuiltIn
from browserstack_sdk.bstack1l11l1l1l1_opy_ import RobotHandler
from bstack_utils.capture import bstack1l11ll1111_opy_
from bstack_utils.bstack1l1111l11l_opy_ import bstack1l11lll11l_opy_, bstack1l1111ll11_opy_, bstack1l11lll1ll_opy_
from bstack_utils.bstack111l1111l_opy_ import bstack1llll11l1_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack1ll1111111_opy_, bstack1ll1l11lll_opy_, Result, \
    bstack1l11ll1ll1_opy_
class bstack_robot_listener:
    ROBOT_LISTENER_API_VERSION = 2
    store = {
        bstack111lll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪഘ"): [],
        bstack111lll1_opy_ (u"ࠧࡨ࡮ࡲࡦࡦࡲ࡟ࡩࡱࡲ࡯ࡸ࠭ങ"): [],
        bstack111lll1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡷࠬച"): []
    }
    bstack1l111ll111_opy_ = []
    bstack1l11l111l1_opy_ = []
    @staticmethod
    def bstack1l1111l111_opy_(log):
        if not (log[bstack111lll1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪഛ")] and log[bstack111lll1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫജ")].strip()):
            return
        active = bstack1llll11l1_opy_.bstack1l111lllll_opy_()
        log = {
            bstack111lll1_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪഝ"): log[bstack111lll1_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫഞ")],
            bstack111lll1_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩട"): datetime.datetime.utcnow().isoformat() + bstack111lll1_opy_ (u"࡛ࠧࠩഠ"),
            bstack111lll1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩഡ"): log[bstack111lll1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪഢ")],
        }
        if active:
            if active[bstack111lll1_opy_ (u"ࠪࡸࡾࡶࡥࠨണ")] == bstack111lll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩത"):
                log[bstack111lll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬഥ")] = active[bstack111lll1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ദ")]
            elif active[bstack111lll1_opy_ (u"ࠧࡵࡻࡳࡩࠬധ")] == bstack111lll1_opy_ (u"ࠨࡶࡨࡷࡹ࠭ന"):
                log[bstack111lll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩഩ")] = active[bstack111lll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪപ")]
        bstack1llll11l1_opy_.bstack1l11lll111_opy_([log])
    def __init__(self):
        self.messages = Messages()
        self._1l11l11111_opy_ = None
        self._1l1111ll1l_opy_ = None
        self._1l11lllll1_opy_ = OrderedDict()
        self.bstack1l11l11lll_opy_ = bstack1l11ll1111_opy_(self.bstack1l1111l111_opy_)
    @bstack1l11ll1ll1_opy_(class_method=True)
    def start_suite(self, name, attrs):
        self.messages.bstack1l111l11l1_opy_()
        if not self._1l11lllll1_opy_.get(attrs.get(bstack111lll1_opy_ (u"ࠫ࡮ࡪࠧഫ")), None):
            self._1l11lllll1_opy_[attrs.get(bstack111lll1_opy_ (u"ࠬ࡯ࡤࠨബ"))] = {}
        bstack1l111ll1l1_opy_ = bstack1l11lll1ll_opy_(
                bstack1l11l11l11_opy_=attrs.get(bstack111lll1_opy_ (u"࠭ࡩࡥࠩഭ")),
                name=name,
                bstack1l111l1l1l_opy_=bstack1ll1l11lll_opy_(),
                file_path=os.path.relpath(attrs[bstack111lll1_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧമ")], start=os.getcwd()) if attrs.get(bstack111lll1_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨയ")) != bstack111lll1_opy_ (u"ࠩࠪര") else bstack111lll1_opy_ (u"ࠪࠫറ"),
                framework=bstack111lll1_opy_ (u"ࠫࡗࡵࡢࡰࡶࠪല")
            )
        threading.current_thread().current_suite_id = attrs.get(bstack111lll1_opy_ (u"ࠬ࡯ࡤࠨള"), None)
        self._1l11lllll1_opy_[attrs.get(bstack111lll1_opy_ (u"࠭ࡩࡥࠩഴ"))][bstack111lll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪവ")] = bstack1l111ll1l1_opy_
    @bstack1l11ll1ll1_opy_(class_method=True)
    def end_suite(self, name, attrs):
        messages = self.messages.bstack1l11l1lll1_opy_()
        self._11llllllll_opy_(messages)
        for bstack1l1111111l_opy_ in self.bstack1l111ll111_opy_:
            bstack1l1111111l_opy_[bstack111lll1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪശ")][bstack111lll1_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨഷ")].extend(self.store[bstack111lll1_opy_ (u"ࠪ࡫ࡱࡵࡢࡢ࡮ࡢ࡬ࡴࡵ࡫ࡴࠩസ")])
            bstack1llll11l1_opy_.bstack1l11l1l11l_opy_(bstack1l1111111l_opy_)
        self.bstack1l111ll111_opy_ = []
        self.store[bstack111lll1_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯ࡣ࡭ࡵ࡯࡬ࡵࠪഹ")] = []
    @bstack1l11ll1ll1_opy_(class_method=True)
    def start_test(self, name, attrs):
        self.bstack1l11l11lll_opy_.start()
        if not self._1l11lllll1_opy_.get(attrs.get(bstack111lll1_opy_ (u"ࠬ࡯ࡤࠨഺ")), None):
            self._1l11lllll1_opy_[attrs.get(bstack111lll1_opy_ (u"࠭ࡩࡥ഻ࠩ"))] = {}
        driver = bstack1ll1111111_opy_(threading.current_thread(), bstack111lll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ഼࠭"), None)
        bstack1l1111l11l_opy_ = bstack1l11lll1ll_opy_(
            bstack1l11l11l11_opy_=attrs.get(bstack111lll1_opy_ (u"ࠨ࡫ࡧࠫഽ")),
            name=name,
            bstack1l111l1l1l_opy_=bstack1ll1l11lll_opy_(),
            file_path=os.path.relpath(attrs[bstack111lll1_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩാ")], start=os.getcwd()),
            scope=RobotHandler.bstack1l11ll1l11_opy_(attrs.get(bstack111lll1_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪി"), None)),
            framework=bstack111lll1_opy_ (u"ࠫࡗࡵࡢࡰࡶࠪീ"),
            tags=attrs[bstack111lll1_opy_ (u"ࠬࡺࡡࡨࡵࠪു")],
            hooks=self.store[bstack111lll1_opy_ (u"࠭ࡧ࡭ࡱࡥࡥࡱࡥࡨࡰࡱ࡮ࡷࠬൂ")],
            bstack1l111ll1ll_opy_=bstack1llll11l1_opy_.bstack1l11ll1lll_opy_(driver) if driver and driver.session_id else {},
            meta={},
            code=bstack111lll1_opy_ (u"ࠢࡼࡿࠣࡠࡳࠦࡻࡾࠤൃ").format(bstack111lll1_opy_ (u"ࠣࠢࠥൄ").join(attrs[bstack111lll1_opy_ (u"ࠩࡷࡥ࡬ࡹࠧ൅")]), name) if attrs[bstack111lll1_opy_ (u"ࠪࡸࡦ࡭ࡳࠨെ")] else name
        )
        self._1l11lllll1_opy_[attrs.get(bstack111lll1_opy_ (u"ࠫ࡮ࡪࠧേ"))][bstack111lll1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨൈ")] = bstack1l1111l11l_opy_
        threading.current_thread().current_test_uuid = bstack1l1111l11l_opy_.bstack1l111l1111_opy_()
        threading.current_thread().current_test_id = attrs.get(bstack111lll1_opy_ (u"࠭ࡩࡥࠩ൉"), None)
        self.bstack1l111l11ll_opy_(bstack111lll1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨൊ"), bstack1l1111l11l_opy_)
    @bstack1l11ll1ll1_opy_(class_method=True)
    def end_test(self, name, attrs):
        self.bstack1l11l11lll_opy_.reset()
        bstack1l11l111ll_opy_ = bstack11lllllll1_opy_.get(attrs.get(bstack111lll1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨോ")), bstack111lll1_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪൌ"))
        self._1l11lllll1_opy_[attrs.get(bstack111lll1_opy_ (u"ࠪ࡭ࡩ്࠭"))][bstack111lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧൎ")].stop(time=bstack1ll1l11lll_opy_(), duration=int(attrs.get(bstack111lll1_opy_ (u"ࠬ࡫࡬ࡢࡲࡶࡩࡩࡺࡩ࡮ࡧࠪ൏"), bstack111lll1_opy_ (u"࠭࠰ࠨ൐"))), result=Result(result=bstack1l11l111ll_opy_, exception=attrs.get(bstack111lll1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ൑")), bstack1l11ll1l1l_opy_=[attrs.get(bstack111lll1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ൒"))]))
        self.bstack1l111l11ll_opy_(bstack111lll1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ൓"), self._1l11lllll1_opy_[attrs.get(bstack111lll1_opy_ (u"ࠪ࡭ࡩ࠭ൔ"))][bstack111lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧൕ")], True)
        self.store[bstack111lll1_opy_ (u"ࠬࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࠩൖ")] = []
        threading.current_thread().current_test_uuid = None
        threading.current_thread().current_test_id = None
    @bstack1l11ll1ll1_opy_(class_method=True)
    def start_keyword(self, name, attrs):
        self.messages.bstack1l111l11l1_opy_()
        current_test_id = bstack1ll1111111_opy_(threading.current_thread(), bstack111lll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡤࠨൗ"), None)
        bstack1l11l1llll_opy_ = current_test_id if bstack1ll1111111_opy_(threading.current_thread(), bstack111lll1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡥࠩ൘"), None) else bstack1ll1111111_opy_(threading.current_thread(), bstack111lll1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡶࡹ࡮ࡺࡥࡠ࡫ࡧࠫ൙"), None)
        if attrs.get(bstack111lll1_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ൚"), bstack111lll1_opy_ (u"ࠪࠫ൛")).lower() in [bstack111lll1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪ൜"), bstack111lll1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧ൝")]:
            hook_type = bstack1l11111ll1_opy_(attrs.get(bstack111lll1_opy_ (u"࠭ࡴࡺࡲࡨࠫ൞")), bstack1ll1111111_opy_(threading.current_thread(), bstack111lll1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫൟ"), None))
            hook_name = bstack111lll1_opy_ (u"ࠨࡽࢀࠫൠ").format(attrs.get(bstack111lll1_opy_ (u"ࠩ࡮ࡻࡳࡧ࡭ࡦࠩൡ"), bstack111lll1_opy_ (u"ࠪࠫൢ")))
            if hook_type in [bstack111lll1_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡆࡒࡌࠨൣ"), bstack111lll1_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡆࡒࡌࠨ൤")]:
                hook_name = bstack111lll1_opy_ (u"࡛࠭ࡼࡿࡠࠤࢀࢃࠧ൥").format(bstack1l11111l1l_opy_.get(hook_type), attrs.get(bstack111lll1_opy_ (u"ࠧ࡬ࡹࡱࡥࡲ࡫ࠧ൦"), bstack111lll1_opy_ (u"ࠨࠩ൧")))
            bstack1l11l1ll11_opy_ = bstack1l1111ll11_opy_(
                bstack1l11l11l11_opy_=bstack1l11l1llll_opy_ + bstack111lll1_opy_ (u"ࠩ࠰ࠫ൨") + attrs.get(bstack111lll1_opy_ (u"ࠪࡸࡾࡶࡥࠨ൩"), bstack111lll1_opy_ (u"ࠫࠬ൪")).lower(),
                name=hook_name,
                bstack1l111l1l1l_opy_=bstack1ll1l11lll_opy_(),
                file_path=os.path.relpath(attrs.get(bstack111lll1_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ൫")), start=os.getcwd()),
                framework=bstack111lll1_opy_ (u"࠭ࡒࡰࡤࡲࡸࠬ൬"),
                tags=attrs[bstack111lll1_opy_ (u"ࠧࡵࡣࡪࡷࠬ൭")],
                scope=RobotHandler.bstack1l11ll1l11_opy_(attrs.get(bstack111lll1_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ൮"), None)),
                hook_type=hook_type,
                meta={}
            )
            threading.current_thread().current_hook_uuid = bstack1l11l1ll11_opy_.bstack1l111l1111_opy_()
            threading.current_thread().current_hook_id = bstack1l11l1llll_opy_ + bstack111lll1_opy_ (u"ࠩ࠰ࠫ൯") + attrs.get(bstack111lll1_opy_ (u"ࠪࡸࡾࡶࡥࠨ൰"), bstack111lll1_opy_ (u"ࠫࠬ൱")).lower()
            self.store[bstack111lll1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ൲")] = [bstack1l11l1ll11_opy_.bstack1l111l1111_opy_()]
            if bstack1ll1111111_opy_(threading.current_thread(), bstack111lll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪ൳"), None):
                self.store[bstack111lll1_opy_ (u"ࠧࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࠫ൴")].append(bstack1l11l1ll11_opy_.bstack1l111l1111_opy_())
            else:
                self.store[bstack111lll1_opy_ (u"ࠨࡩ࡯ࡳࡧࡧ࡬ࡠࡪࡲࡳࡰࡹࠧ൵")].append(bstack1l11l1ll11_opy_.bstack1l111l1111_opy_())
            if bstack1l11l1llll_opy_:
                self._1l11lllll1_opy_[bstack1l11l1llll_opy_ + bstack111lll1_opy_ (u"ࠩ࠰ࠫ൶") + attrs.get(bstack111lll1_opy_ (u"ࠪࡸࡾࡶࡥࠨ൷"), bstack111lll1_opy_ (u"ࠫࠬ൸")).lower()] = { bstack111lll1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ൹"): bstack1l11l1ll11_opy_ }
            bstack1llll11l1_opy_.bstack1l111l11ll_opy_(bstack111lll1_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧൺ"), bstack1l11l1ll11_opy_)
        else:
            bstack1l11llll1l_opy_ = {
                bstack111lll1_opy_ (u"ࠧࡪࡦࠪൻ"): uuid4().__str__(),
                bstack111lll1_opy_ (u"ࠨࡶࡨࡼࡹ࠭ർ"): bstack111lll1_opy_ (u"ࠩࡾࢁࠥࢁࡽࠨൽ").format(attrs.get(bstack111lll1_opy_ (u"ࠪ࡯ࡼࡴࡡ࡮ࡧࠪൾ")), attrs.get(bstack111lll1_opy_ (u"ࠫࡦࡸࡧࡴࠩൿ"), bstack111lll1_opy_ (u"ࠬ࠭඀"))) if attrs.get(bstack111lll1_opy_ (u"࠭ࡡࡳࡩࡶࠫඁ"), []) else attrs.get(bstack111lll1_opy_ (u"ࠧ࡬ࡹࡱࡥࡲ࡫ࠧං")),
                bstack111lll1_opy_ (u"ࠨࡵࡷࡩࡵࡥࡡࡳࡩࡸࡱࡪࡴࡴࠨඃ"): attrs.get(bstack111lll1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ඄"), []),
                bstack111lll1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧඅ"): bstack1ll1l11lll_opy_(),
                bstack111lll1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫආ"): bstack111lll1_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭ඇ"),
                bstack111lll1_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫඈ"): attrs.get(bstack111lll1_opy_ (u"ࠧࡥࡱࡦࠫඉ"), bstack111lll1_opy_ (u"ࠨࠩඊ"))
            }
            if attrs.get(bstack111lll1_opy_ (u"ࠩ࡯࡭ࡧࡴࡡ࡮ࡧࠪඋ"), bstack111lll1_opy_ (u"ࠪࠫඌ")) != bstack111lll1_opy_ (u"ࠫࠬඍ"):
                bstack1l11llll1l_opy_[bstack111lll1_opy_ (u"ࠬࡱࡥࡺࡹࡲࡶࡩ࠭ඎ")] = attrs.get(bstack111lll1_opy_ (u"࠭࡬ࡪࡤࡱࡥࡲ࡫ࠧඏ"))
            if not self.bstack1l11l111l1_opy_:
                self._1l11lllll1_opy_[self._1l111ll11l_opy_()][bstack111lll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪඐ")].add_step(bstack1l11llll1l_opy_)
                threading.current_thread().current_step_uuid = bstack1l11llll1l_opy_[bstack111lll1_opy_ (u"ࠨ࡫ࡧࠫඑ")]
            self.bstack1l11l111l1_opy_.append(bstack1l11llll1l_opy_)
    @bstack1l11ll1ll1_opy_(class_method=True)
    def end_keyword(self, name, attrs):
        messages = self.messages.bstack1l11l1lll1_opy_()
        self._11llllllll_opy_(messages)
        current_test_id = bstack1ll1111111_opy_(threading.current_thread(), bstack111lll1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡧࠫඒ"), None)
        bstack1l11l1llll_opy_ = current_test_id if current_test_id else bstack1ll1111111_opy_(threading.current_thread(), bstack111lll1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡸࡻࡩࡵࡧࡢ࡭ࡩ࠭ඓ"), None)
        bstack1l111111l1_opy_ = bstack11lllllll1_opy_.get(attrs.get(bstack111lll1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫඔ")), bstack111lll1_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ඕ"))
        bstack1l111l1lll_opy_ = attrs.get(bstack111lll1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧඖ"))
        if bstack1l111111l1_opy_ != bstack111lll1_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨ඗") and not attrs.get(bstack111lll1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ඘")) and self._1l11l11111_opy_:
            bstack1l111l1lll_opy_ = self._1l11l11111_opy_
        bstack1l11l1111l_opy_ = Result(result=bstack1l111111l1_opy_, exception=bstack1l111l1lll_opy_, bstack1l11ll1l1l_opy_=[bstack1l111l1lll_opy_])
        if attrs.get(bstack111lll1_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ඙"), bstack111lll1_opy_ (u"ࠪࠫක")).lower() in [bstack111lll1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪඛ"), bstack111lll1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧග")]:
            bstack1l11l1llll_opy_ = current_test_id if current_test_id else bstack1ll1111111_opy_(threading.current_thread(), bstack111lll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡴࡷ࡬ࡸࡪࡥࡩࡥࠩඝ"), None)
            if bstack1l11l1llll_opy_:
                bstack1l11l11l1l_opy_ = bstack1l11l1llll_opy_ + bstack111lll1_opy_ (u"ࠢ࠮ࠤඞ") + attrs.get(bstack111lll1_opy_ (u"ࠨࡶࡼࡴࡪ࠭ඟ"), bstack111lll1_opy_ (u"ࠩࠪච")).lower()
                self._1l11lllll1_opy_[bstack1l11l11l1l_opy_][bstack111lll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ඡ")].stop(time=bstack1ll1l11lll_opy_(), duration=int(attrs.get(bstack111lll1_opy_ (u"ࠫࡪࡲࡡࡱࡵࡨࡨࡹ࡯࡭ࡦࠩජ"), bstack111lll1_opy_ (u"ࠬ࠶ࠧඣ"))), result=bstack1l11l1111l_opy_)
                bstack1llll11l1_opy_.bstack1l111l11ll_opy_(bstack111lll1_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨඤ"), self._1l11lllll1_opy_[bstack1l11l11l1l_opy_][bstack111lll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪඥ")])
        else:
            bstack1l11l1llll_opy_ = current_test_id if current_test_id else bstack1ll1111111_opy_(threading.current_thread(), bstack111lll1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡪࡦࠪඦ"), None)
            if bstack1l11l1llll_opy_ and len(self.bstack1l11l111l1_opy_) == 1:
                current_step_uuid = bstack1ll1111111_opy_(threading.current_thread(), bstack111lll1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡷࡹ࡫ࡰࡠࡷࡸ࡭ࡩ࠭ට"), None)
                self._1l11lllll1_opy_[bstack1l11l1llll_opy_][bstack111lll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ඨ")].bstack1l1111llll_opy_(current_step_uuid, duration=int(attrs.get(bstack111lll1_opy_ (u"ࠫࡪࡲࡡࡱࡵࡨࡨࡹ࡯࡭ࡦࠩඩ"), bstack111lll1_opy_ (u"ࠬ࠶ࠧඪ"))), result=bstack1l11l1111l_opy_)
            else:
                self.bstack1l111l111l_opy_(attrs)
            self.bstack1l11l111l1_opy_.pop()
    def log_message(self, message):
        try:
            if message.get(bstack111lll1_opy_ (u"࠭ࡨࡵ࡯࡯ࠫණ"), bstack111lll1_opy_ (u"ࠧ࡯ࡱࠪඬ")) == bstack111lll1_opy_ (u"ࠨࡻࡨࡷࠬත"):
                return
            self.messages.push(message)
            bstack1l111l1l11_opy_ = []
            if bstack1llll11l1_opy_.bstack1l111lllll_opy_():
                bstack1l111l1l11_opy_.append({
                    bstack111lll1_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬථ"): bstack1ll1l11lll_opy_(),
                    bstack111lll1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫද"): message.get(bstack111lll1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬධ")),
                    bstack111lll1_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫන"): message.get(bstack111lll1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ඲")),
                    **bstack1llll11l1_opy_.bstack1l111lllll_opy_()
                })
                if len(bstack1l111l1l11_opy_) > 0:
                    bstack1llll11l1_opy_.bstack1l11lll111_opy_(bstack1l111l1l11_opy_)
        except Exception as err:
            pass
    def close(self):
        bstack1llll11l1_opy_.bstack1l11ll111l_opy_()
    def bstack1l111l111l_opy_(self, bstack1l111llll1_opy_):
        if not bstack1llll11l1_opy_.bstack1l111lllll_opy_():
            return
        kwname = bstack111lll1_opy_ (u"ࠧࡼࡿࠣࡿࢂ࠭ඳ").format(bstack1l111llll1_opy_.get(bstack111lll1_opy_ (u"ࠨ࡭ࡺࡲࡦࡳࡥࠨප")), bstack1l111llll1_opy_.get(bstack111lll1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧඵ"), bstack111lll1_opy_ (u"ࠪࠫබ"))) if bstack1l111llll1_opy_.get(bstack111lll1_opy_ (u"ࠫࡦࡸࡧࡴࠩභ"), []) else bstack1l111llll1_opy_.get(bstack111lll1_opy_ (u"ࠬࡱࡷ࡯ࡣࡰࡩࠬම"))
        error_message = bstack111lll1_opy_ (u"ࠨ࡫ࡸࡰࡤࡱࡪࡀࠠ࡝ࠤࡾ࠴ࢂࡢࠢࠡࡾࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࡡࠨࡻ࠲ࡿ࡟ࠦࠥࢂࠠࡦࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࡡࠨࡻ࠳ࡿ࡟ࠦࠧඹ").format(kwname, bstack1l111llll1_opy_.get(bstack111lll1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧය")), str(bstack1l111llll1_opy_.get(bstack111lll1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩර"))))
        bstack1l111111ll_opy_ = bstack111lll1_opy_ (u"ࠤ࡮ࡻࡳࡧ࡭ࡦ࠼ࠣࡠࠧࢁ࠰ࡾ࡞ࠥࠤࢁࠦࡳࡵࡣࡷࡹࡸࡀࠠ࡝ࠤࡾ࠵ࢂࡢࠢࠣ඼").format(kwname, bstack1l111llll1_opy_.get(bstack111lll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪල")))
        bstack1l1111l1l1_opy_ = error_message if bstack1l111llll1_opy_.get(bstack111lll1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ඾")) else bstack1l111111ll_opy_
        bstack1l11llll11_opy_ = {
            bstack111lll1_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ඿"): self.bstack1l11l111l1_opy_[-1].get(bstack111lll1_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪව"), bstack1ll1l11lll_opy_()),
            bstack111lll1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨශ"): bstack1l1111l1l1_opy_,
            bstack111lll1_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧෂ"): bstack111lll1_opy_ (u"ࠩࡈࡖࡗࡕࡒࠨස") if bstack1l111llll1_opy_.get(bstack111lll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪහ")) == bstack111lll1_opy_ (u"ࠫࡋࡇࡉࡍࠩළ") else bstack111lll1_opy_ (u"ࠬࡏࡎࡇࡑࠪෆ"),
            **bstack1llll11l1_opy_.bstack1l111lllll_opy_()
        }
        bstack1llll11l1_opy_.bstack1l11lll111_opy_([bstack1l11llll11_opy_])
    def _1l111ll11l_opy_(self):
        for bstack1l11l11l11_opy_ in reversed(self._1l11lllll1_opy_):
            bstack1l11ll11l1_opy_ = bstack1l11l11l11_opy_
            data = self._1l11lllll1_opy_[bstack1l11l11l11_opy_][bstack111lll1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩ෇")]
            if isinstance(data, bstack1l1111ll11_opy_):
                if not bstack111lll1_opy_ (u"ࠧࡆࡃࡆࡌࠬ෈") in data.bstack1l11111111_opy_():
                    return bstack1l11ll11l1_opy_
            else:
                return bstack1l11ll11l1_opy_
    def _11llllllll_opy_(self, messages):
        try:
            bstack1l1111lll1_opy_ = BuiltIn().get_variable_value(bstack111lll1_opy_ (u"ࠣࠦࡾࡐࡔࡍࠠࡍࡇ࡙ࡉࡑࢃࠢ෉")) in (bstack1l111lll11_opy_.DEBUG, bstack1l111lll11_opy_.TRACE)
            for message, bstack1l11l1l111_opy_ in zip_longest(messages, messages[1:]):
                name = message.get(bstack111lll1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧ්ࠪ"))
                level = message.get(bstack111lll1_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ෋"))
                if level == bstack1l111lll11_opy_.FAIL:
                    self._1l11l11111_opy_ = name or self._1l11l11111_opy_
                    self._1l1111ll1l_opy_ = bstack1l11l1l111_opy_.get(bstack111lll1_opy_ (u"ࠦࡲ࡫ࡳࡴࡣࡪࡩࠧ෌")) if bstack1l1111lll1_opy_ and bstack1l11l1l111_opy_ else self._1l1111ll1l_opy_
        except:
            pass
    @classmethod
    def bstack1l111l11ll_opy_(self, event: str, bstack1l11111lll_opy_: bstack1l11lll11l_opy_, bstack1l11111l11_opy_=False):
        if event == bstack111lll1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ෍"):
            bstack1l11111lll_opy_.set(hooks=self.store[bstack111lll1_opy_ (u"࠭ࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࠪ෎")])
        if event == bstack111lll1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔ࡭࡬ࡴࡵ࡫ࡤࠨා"):
            event = bstack111lll1_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪැ")
        if bstack1l11111l11_opy_:
            bstack1l11l11ll1_opy_ = {
                bstack111lll1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ෑ"): event,
                bstack1l11111lll_opy_.bstack1l11l1ll1l_opy_(): bstack1l11111lll_opy_.bstack1l11l1l1ll_opy_(event)
            }
            self.bstack1l111ll111_opy_.append(bstack1l11l11ll1_opy_)
        else:
            bstack1llll11l1_opy_.bstack1l111l11ll_opy_(event, bstack1l11111lll_opy_)
class Messages:
    def __init__(self):
        self._1l11lll1l1_opy_ = []
    def bstack1l111l11l1_opy_(self):
        self._1l11lll1l1_opy_.append([])
    def bstack1l11l1lll1_opy_(self):
        return self._1l11lll1l1_opy_.pop() if self._1l11lll1l1_opy_ else list()
    def push(self, message):
        self._1l11lll1l1_opy_[-1].append(message) if self._1l11lll1l1_opy_ else self._1l11lll1l1_opy_.append([message])
class bstack1l111lll11_opy_:
    FAIL = bstack111lll1_opy_ (u"ࠪࡊࡆࡏࡌࠨි")
    ERROR = bstack111lll1_opy_ (u"ࠫࡊࡘࡒࡐࡔࠪී")
    WARNING = bstack111lll1_opy_ (u"ࠬ࡝ࡁࡓࡐࠪු")
    bstack1l111lll1l_opy_ = bstack111lll1_opy_ (u"࠭ࡉࡏࡈࡒࠫ෕")
    DEBUG = bstack111lll1_opy_ (u"ࠧࡅࡇࡅ࡙ࡌ࠭ූ")
    TRACE = bstack111lll1_opy_ (u"ࠨࡖࡕࡅࡈࡋࠧ෗")
    bstack1l1111l1ll_opy_ = [FAIL, ERROR]
def bstack1l111l1ll1_opy_(bstack1l11ll11ll_opy_):
    if not bstack1l11ll11ll_opy_:
        return None
    if bstack1l11ll11ll_opy_.get(bstack111lll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬෘ"), None):
        return getattr(bstack1l11ll11ll_opy_[bstack111lll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ෙ")], bstack111lll1_opy_ (u"ࠫࡺࡻࡩࡥࠩේ"), None)
    return bstack1l11ll11ll_opy_.get(bstack111lll1_opy_ (u"ࠬࡻࡵࡪࡦࠪෛ"), None)
def bstack1l11111ll1_opy_(hook_type, current_test_uuid):
    if hook_type.lower() not in [bstack111lll1_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬො"), bstack111lll1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩෝ")]:
        return
    if hook_type.lower() == bstack111lll1_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧෞ"):
        if current_test_uuid is None:
            return bstack111lll1_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ෟ")
        else:
            return bstack111lll1_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠨ෠")
    elif hook_type.lower() == bstack111lll1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭෡"):
        if current_test_uuid is None:
            return bstack111lll1_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡆࡒࡌࠨ෢")
        else:
            return bstack111lll1_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠪ෣")