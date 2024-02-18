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
class RobotHandler():
    def __init__(self, args, logger, bstack11llll11ll_opy_, bstack11llllll1l_opy_):
        self.args = args
        self.logger = logger
        self.bstack11llll11ll_opy_ = bstack11llll11ll_opy_
        self.bstack11llllll1l_opy_ = bstack11llllll1l_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack1l11ll1l11_opy_(bstack11lll1lll1_opy_):
        bstack11lll1ll11_opy_ = []
        if bstack11lll1lll1_opy_:
            tokens = str(os.path.basename(bstack11lll1lll1_opy_)).split(bstack111lll1_opy_ (u"ࠣࡡࠥก"))
            camelcase_name = bstack111lll1_opy_ (u"ࠤࠣࠦข").join(t.title() for t in tokens)
            suite_name, bstack11lll1ll1l_opy_ = os.path.splitext(camelcase_name)
            bstack11lll1ll11_opy_.append(suite_name)
        return bstack11lll1ll11_opy_
    @staticmethod
    def bstack11lll1l1ll_opy_(typename):
        if bstack111lll1_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࠨฃ") in typename:
            return bstack111lll1_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࡅࡳࡴࡲࡶࠧค")
        return bstack111lll1_opy_ (u"࡛ࠧ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࠨฅ")