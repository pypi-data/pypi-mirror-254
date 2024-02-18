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
from collections import deque
from bstack_utils.constants import *
class bstack11ll11l1_opy_:
    def __init__(self):
        self._1111lll1l1_opy_ = deque()
        self._111l111ll1_opy_ = {}
        self._111l111111_opy_ = False
    def bstack1111lll11l_opy_(self, test_name, bstack1111llll1l_opy_):
        bstack111l111l1l_opy_ = self._111l111ll1_opy_.get(test_name, {})
        return bstack111l111l1l_opy_.get(bstack1111llll1l_opy_, 0)
    def bstack1111lll111_opy_(self, test_name, bstack1111llll1l_opy_):
        bstack111l1111ll_opy_ = self.bstack1111lll11l_opy_(test_name, bstack1111llll1l_opy_)
        self.bstack111l1111l1_opy_(test_name, bstack1111llll1l_opy_)
        return bstack111l1111ll_opy_
    def bstack111l1111l1_opy_(self, test_name, bstack1111llll1l_opy_):
        if test_name not in self._111l111ll1_opy_:
            self._111l111ll1_opy_[test_name] = {}
        bstack111l111l1l_opy_ = self._111l111ll1_opy_[test_name]
        bstack111l1111ll_opy_ = bstack111l111l1l_opy_.get(bstack1111llll1l_opy_, 0)
        bstack111l111l1l_opy_[bstack1111llll1l_opy_] = bstack111l1111ll_opy_ + 1
    def bstack1l1l11ll11_opy_(self, bstack111l11111l_opy_, bstack1111lll1ll_opy_):
        bstack1111llllll_opy_ = self.bstack1111lll111_opy_(bstack111l11111l_opy_, bstack1111lll1ll_opy_)
        bstack111l111l11_opy_ = bstack11ll11l11l_opy_[bstack1111lll1ll_opy_]
        bstack1111lllll1_opy_ = bstack111lll1_opy_ (u"ࠥࡿࢂ࠳ࡻࡾ࠯ࡾࢁࠧ᎗").format(bstack111l11111l_opy_, bstack111l111l11_opy_, bstack1111llllll_opy_)
        self._1111lll1l1_opy_.append(bstack1111lllll1_opy_)
    def bstack1l1l1llll1_opy_(self):
        return len(self._1111lll1l1_opy_) == 0
    def bstack1ll11lll1l_opy_(self):
        bstack1111llll11_opy_ = self._1111lll1l1_opy_.popleft()
        return bstack1111llll11_opy_
    def capturing(self):
        return self._111l111111_opy_
    def bstack1ll11ll1l1_opy_(self):
        self._111l111111_opy_ = True
    def bstack1l1l1l11_opy_(self):
        self._111l111111_opy_ = False