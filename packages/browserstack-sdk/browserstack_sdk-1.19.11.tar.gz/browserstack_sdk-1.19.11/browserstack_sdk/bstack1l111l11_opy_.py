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
import multiprocessing
import os
import json
from time import sleep
import bstack_utils.bstack1l1l1lll11_opy_ as bstack1lllll1111_opy_
from browserstack_sdk.bstack1lll1111_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack1l1lll1lll_opy_
class bstack11ll1l1l1_opy_:
    def __init__(self, args, logger, bstack11llll11ll_opy_, bstack11llllll1l_opy_):
        self.args = args
        self.logger = logger
        self.bstack11llll11ll_opy_ = bstack11llll11ll_opy_
        self.bstack11llllll1l_opy_ = bstack11llllll1l_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack1l1lllll_opy_ = []
        self.bstack11llll1l1l_opy_ = None
        self.bstack11l1lll1l_opy_ = []
        self.bstack11lllll1ll_opy_ = self.bstack11llll111_opy_()
        self.bstack1l1lll11l1_opy_ = -1
    def bstack1l1l11l1_opy_(self, bstack11lll1llll_opy_):
        self.parse_args()
        self.bstack11llll1lll_opy_()
        self.bstack11llll1ll1_opy_(bstack11lll1llll_opy_)
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    def bstack11lllll11l_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1l1lll11l1_opy_ = -1
        if bstack111lll1_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ෤") in self.bstack11llll11ll_opy_:
            self.bstack1l1lll11l1_opy_ = int(self.bstack11llll11ll_opy_[bstack111lll1_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ෥")])
        try:
            bstack11llllll11_opy_ = [bstack111lll1_opy_ (u"ࠩ࠰࠱ࡩࡸࡩࡷࡧࡵࠫ෦"), bstack111lll1_opy_ (u"ࠪ࠱࠲ࡶ࡬ࡶࡩ࡬ࡲࡸ࠭෧"), bstack111lll1_opy_ (u"ࠫ࠲ࡶࠧ෨")]
            if self.bstack1l1lll11l1_opy_ >= 0:
                bstack11llllll11_opy_.extend([bstack111lll1_opy_ (u"ࠬ࠳࠭࡯ࡷࡰࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭෩"), bstack111lll1_opy_ (u"࠭࠭࡯ࠩ෪")])
            for arg in bstack11llllll11_opy_:
                self.bstack11lllll11l_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack11llll1lll_opy_(self):
        bstack11llll1l1l_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack11llll1l1l_opy_ = bstack11llll1l1l_opy_
        return bstack11llll1l1l_opy_
    def bstack111ll11l_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            import importlib
            bstack11llll11l1_opy_ = importlib.find_loader(bstack111lll1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠩ෫"))
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack1l1lll1lll_opy_)
    def bstack11llll1ll1_opy_(self, bstack11lll1llll_opy_):
        bstack11l11l111_opy_ = Config.bstack111l1ll1_opy_()
        if bstack11lll1llll_opy_:
            self.bstack11llll1l1l_opy_.append(bstack111lll1_opy_ (u"ࠨ࠯࠰ࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ෬"))
            self.bstack11llll1l1l_opy_.append(bstack111lll1_opy_ (u"ࠩࡗࡶࡺ࡫ࠧ෭"))
        if bstack11l11l111_opy_.bstack11lllll1l1_opy_():
            self.bstack11llll1l1l_opy_.append(bstack111lll1_opy_ (u"ࠪ࠱࠲ࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩ෮"))
            self.bstack11llll1l1l_opy_.append(bstack111lll1_opy_ (u"࡙ࠫࡸࡵࡦࠩ෯"))
        self.bstack11llll1l1l_opy_.append(bstack111lll1_opy_ (u"ࠬ࠳ࡰࠨ෰"))
        self.bstack11llll1l1l_opy_.append(bstack111lll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡵࡲࡵࡨ࡫ࡱࠫ෱"))
        self.bstack11llll1l1l_opy_.append(bstack111lll1_opy_ (u"ࠧ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠩෲ"))
        self.bstack11llll1l1l_opy_.append(bstack111lll1_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨෳ"))
        if self.bstack1l1lll11l1_opy_ > 1:
            self.bstack11llll1l1l_opy_.append(bstack111lll1_opy_ (u"ࠩ࠰ࡲࠬ෴"))
            self.bstack11llll1l1l_opy_.append(str(self.bstack1l1lll11l1_opy_))
    def bstack11lllll111_opy_(self):
        bstack11l1lll1l_opy_ = []
        for spec in self.bstack1l1lllll_opy_:
            bstack1l1l11111_opy_ = [spec]
            bstack1l1l11111_opy_ += self.bstack11llll1l1l_opy_
            bstack11l1lll1l_opy_.append(bstack1l1l11111_opy_)
        self.bstack11l1lll1l_opy_ = bstack11l1lll1l_opy_
        return bstack11l1lll1l_opy_
    def bstack11llll111_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack11lllll1ll_opy_ = True
            return True
        except Exception as e:
            self.bstack11lllll1ll_opy_ = False
        return self.bstack11lllll1ll_opy_
    def bstack1ll1ll1111_opy_(self, bstack11llll1111_opy_, bstack1l1l11l1_opy_):
        bstack1l1l11l1_opy_[bstack111lll1_opy_ (u"ࠪࡇࡔࡔࡆࡊࡉࠪ෵")] = self.bstack11llll11ll_opy_
        multiprocessing.set_start_method(bstack111lll1_opy_ (u"ࠫࡸࡶࡡࡸࡰࠪ෶"))
        if bstack111lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ෷") in self.bstack11llll11ll_opy_:
            bstack1l1l1l11l_opy_ = []
            manager = multiprocessing.Manager()
            bstack1llll11ll1_opy_ = manager.list()
            for index, platform in enumerate(self.bstack11llll11ll_opy_[bstack111lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ෸")]):
                bstack1l1l1l11l_opy_.append(multiprocessing.Process(name=str(index),
                                                           target=bstack11llll1111_opy_,
                                                           args=(self.bstack11llll1l1l_opy_, bstack1l1l11l1_opy_, bstack1llll11ll1_opy_)))
            i = 0
            bstack11llll111l_opy_ = len(self.bstack11llll11ll_opy_[bstack111lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ෹")])
            for t in bstack1l1l1l11l_opy_:
                os.environ[bstack111lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨ෺")] = str(i)
                os.environ[bstack111lll1_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪ෻")] = json.dumps(self.bstack11llll11ll_opy_[bstack111lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭෼")][i % bstack11llll111l_opy_])
                i += 1
                t.start()
            for t in bstack1l1l1l11l_opy_:
                t.join()
            return list(bstack1llll11ll1_opy_)
    @staticmethod
    def bstack1lllll1l11_opy_(driver, bstack1lll1ll1l_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack111lll1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨ෽"), None)
        if item and getattr(item, bstack111lll1_opy_ (u"ࠬࡥࡡ࠲࠳ࡼࡣࡹ࡫ࡳࡵࡡࡦࡥࡸ࡫ࠧ෾"), None) and not getattr(item, bstack111lll1_opy_ (u"࠭࡟ࡢ࠳࠴ࡽࡤࡹࡴࡰࡲࡢࡨࡴࡴࡥࠨ෿"), False):
            logger.info(
                bstack111lll1_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠥࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡪࡵࠣࡹࡳࡪࡥࡳࡹࡤࡽ࠳ࠨ฀"))
            bstack11llll1l11_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack1lllll1111_opy_.bstack111lll11_opy_(driver, bstack11llll1l11_opy_, item.name, item.module.__name__, item.path, bstack1lll1ll1l_opy_)
            item._a11y_stop_done = True
            if wait:
                sleep(2)