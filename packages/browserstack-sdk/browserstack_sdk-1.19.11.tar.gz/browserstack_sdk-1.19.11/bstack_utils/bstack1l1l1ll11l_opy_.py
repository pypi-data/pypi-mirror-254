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
from browserstack_sdk.bstack1l111l11_opy_ import bstack11ll1l1l1_opy_
from browserstack_sdk.bstack1l11l1l1l1_opy_ import RobotHandler
def bstack111l1l1l_opy_(framework):
    if framework.lower() == bstack111lll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩᄮ"):
        return bstack11ll1l1l1_opy_.version()
    elif framework.lower() == bstack111lll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩᄯ"):
        return RobotHandler.version()
    elif framework.lower() == bstack111lll1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫᄰ"):
        import behave
        return behave.__version__
    else:
        return bstack111lll1_opy_ (u"ࠬࡻ࡮࡬ࡰࡲࡻࡳ࠭ᄱ")