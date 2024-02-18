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
class bstack111l1l1l1_opy_:
    def __init__(self, handler):
        self._11111l11ll_opy_ = None
        self.handler = handler
        self._11111l1ll1_opy_ = self.bstack11111l1l1l_opy_()
        self.patch()
    def patch(self):
        self._11111l11ll_opy_ = self._11111l1ll1_opy_.execute
        self._11111l1ll1_opy_.execute = self.bstack11111l1l11_opy_()
    def bstack11111l1l11_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack111lll1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࠣᏰ"), driver_command)
            response = self._11111l11ll_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack111lll1_opy_ (u"ࠤࡤࡪࡹ࡫ࡲࠣᏱ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11111l1ll1_opy_.execute = self._11111l11ll_opy_
    @staticmethod
    def bstack11111l1l1l_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver