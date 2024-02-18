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
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.helper import bstack11l11lll1l_opy_, bstack1l1l1111l_opy_, bstack1ll1111111_opy_, bstack1ll11l111_opy_, \
    bstack11l1llll11_opy_
def bstack1ll11llll1_opy_(bstack11111l111l_opy_):
    for driver in bstack11111l111l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1l11ll11_opy_(driver, status, reason=bstack111lll1_opy_ (u"ࠪࠫᏲ")):
    bstack11l11l111_opy_ = Config.bstack111l1ll1_opy_()
    if bstack11l11l111_opy_.bstack11lllll1l1_opy_():
        return
    bstack1l1l1ll111_opy_ = bstack11lll111l_opy_(bstack111lll1_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧᏳ"), bstack111lll1_opy_ (u"ࠬ࠭Ᏼ"), status, reason, bstack111lll1_opy_ (u"࠭ࠧᏵ"), bstack111lll1_opy_ (u"ࠧࠨ᏶"))
    driver.execute_script(bstack1l1l1ll111_opy_)
def bstack1lll11l11_opy_(page, status, reason=bstack111lll1_opy_ (u"ࠨࠩ᏷")):
    try:
        if page is None:
            return
        bstack11l11l111_opy_ = Config.bstack111l1ll1_opy_()
        if bstack11l11l111_opy_.bstack11lllll1l1_opy_():
            return
        bstack1l1l1ll111_opy_ = bstack11lll111l_opy_(bstack111lll1_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬᏸ"), bstack111lll1_opy_ (u"ࠪࠫᏹ"), status, reason, bstack111lll1_opy_ (u"ࠫࠬᏺ"), bstack111lll1_opy_ (u"ࠬ࠭ᏻ"))
        page.evaluate(bstack111lll1_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢᏼ"), bstack1l1l1ll111_opy_)
    except Exception as e:
        print(bstack111lll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳࠡࡨࡲࡶࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡾࢁࠧᏽ"), e)
def bstack11lll111l_opy_(type, name, status, reason, bstack1ll11ll1l_opy_, bstack1l1ll1l111_opy_):
    bstack1l111l111_opy_ = {
        bstack111lll1_opy_ (u"ࠨࡣࡦࡸ࡮ࡵ࡮ࠨ᏾"): type,
        bstack111lll1_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ᏿"): {}
    }
    if type == bstack111lll1_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩࠬ᐀"):
        bstack1l111l111_opy_[bstack111lll1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᐁ")][bstack111lll1_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫᐂ")] = bstack1ll11ll1l_opy_
        bstack1l111l111_opy_[bstack111lll1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᐃ")][bstack111lll1_opy_ (u"ࠧࡥࡣࡷࡥࠬᐄ")] = json.dumps(str(bstack1l1ll1l111_opy_))
    if type == bstack111lll1_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩᐅ"):
        bstack1l111l111_opy_[bstack111lll1_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᐆ")][bstack111lll1_opy_ (u"ࠪࡲࡦࡳࡥࠨᐇ")] = name
    if type == bstack111lll1_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧᐈ"):
        bstack1l111l111_opy_[bstack111lll1_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᐉ")][bstack111lll1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ᐊ")] = status
        if status == bstack111lll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᐋ") and str(reason) != bstack111lll1_opy_ (u"ࠣࠤᐌ"):
            bstack1l111l111_opy_[bstack111lll1_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᐍ")][bstack111lll1_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪᐎ")] = json.dumps(str(reason))
    bstack1ll1l1ll1_opy_ = bstack111lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩᐏ").format(json.dumps(bstack1l111l111_opy_))
    return bstack1ll1l1ll1_opy_
def bstack11l1llll1_opy_(url, config, logger, bstack1l1ll1l11l_opy_=False):
    hostname = bstack1l1l1111l_opy_(url)
    is_private = bstack1ll11l111_opy_(hostname)
    try:
        if is_private or bstack1l1ll1l11l_opy_:
            file_path = bstack11l11lll1l_opy_(bstack111lll1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᐐ"), bstack111lll1_opy_ (u"࠭࠮ࡣࡵࡷࡥࡨࡱ࠭ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬᐑ"), logger)
            if os.environ.get(bstack111lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡔࡏࡕࡡࡖࡉ࡙ࡥࡅࡓࡔࡒࡖࠬᐒ")) and eval(
                    os.environ.get(bstack111lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ࠭ᐓ"))):
                return
            if (bstack111lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ᐔ") in config and not config[bstack111lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧᐕ")]):
                os.environ[bstack111lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡑࡓ࡙ࡥࡓࡆࡖࡢࡉࡗࡘࡏࡓࠩᐖ")] = str(True)
                bstack11111l1111_opy_ = {bstack111lll1_opy_ (u"ࠬ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠧᐗ"): hostname}
                bstack11l1llll11_opy_(bstack111lll1_opy_ (u"࠭࠮ࡣࡵࡷࡥࡨࡱ࠭ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬᐘ"), bstack111lll1_opy_ (u"ࠧ࡯ࡷࡧ࡫ࡪࡥ࡬ࡰࡥࡤࡰࠬᐙ"), bstack11111l1111_opy_, logger)
    except Exception as e:
        pass
def bstack11111l111_opy_(caps, bstack111111llll_opy_):
    if bstack111lll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᐚ") in caps:
        caps[bstack111lll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᐛ")][bstack111lll1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࠩᐜ")] = True
        if bstack111111llll_opy_:
            caps[bstack111lll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᐝ")][bstack111lll1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᐞ")] = bstack111111llll_opy_
    else:
        caps[bstack111lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࠫᐟ")] = True
        if bstack111111llll_opy_:
            caps[bstack111lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᐠ")] = bstack111111llll_opy_
def bstack1111l1ll1l_opy_(bstack1l11l111ll_opy_):
    bstack11111l11l1_opy_ = bstack1ll1111111_opy_(threading.current_thread(), bstack111lll1_opy_ (u"ࠨࡶࡨࡷࡹ࡙ࡴࡢࡶࡸࡷࠬᐡ"), bstack111lll1_opy_ (u"ࠩࠪᐢ"))
    if bstack11111l11l1_opy_ == bstack111lll1_opy_ (u"ࠪࠫᐣ") or bstack11111l11l1_opy_ == bstack111lll1_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬᐤ"):
        threading.current_thread().testStatus = bstack1l11l111ll_opy_
    else:
        if bstack1l11l111ll_opy_ == bstack111lll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᐥ"):
            threading.current_thread().testStatus = bstack1l11l111ll_opy_