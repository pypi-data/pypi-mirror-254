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
import sys
class bstack1l11ll1111_opy_:
    def __init__(self, handler):
        self._11ll1l11l1_opy_ = sys.stdout.write
        self._11ll11llll_opy_ = sys.stderr.write
        self.handler = handler
        self._started = False
    def start(self):
        if self._started:
            return
        self._started = True
        sys.stdout.write = self.bstack11ll1l111l_opy_
        sys.stdout.error = self.bstack11ll1l1111_opy_
    def bstack11ll1l111l_opy_(self, _str):
        self._11ll1l11l1_opy_(_str)
        if self.handler:
            self.handler({bstack111lll1_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩຝ"): bstack111lll1_opy_ (u"ࠫࡎࡔࡆࡐࠩພ"), bstack111lll1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ຟ"): _str})
    def bstack11ll1l1111_opy_(self, _str):
        self._11ll11llll_opy_(_str)
        if self.handler:
            self.handler({bstack111lll1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬຠ"): bstack111lll1_opy_ (u"ࠧࡆࡔࡕࡓࡗ࠭ມ"), bstack111lll1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩຢ"): _str})
    def reset(self):
        if not self._started:
            return
        self._started = False
        sys.stdout.write = self._11ll1l11l1_opy_
        sys.stderr.write = self._11ll11llll_opy_