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
import re
from bstack_utils.bstack111l11l11_opy_ import bstack1111l1ll1l_opy_
def bstack1111l1lll1_opy_(fixture_name):
    if fixture_name.startswith(bstack111lll1_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᎽ")):
        return bstack111lll1_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᎾ")
    elif fixture_name.startswith(bstack111lll1_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᎿ")):
        return bstack111lll1_opy_ (u"ࠩࡶࡩࡹࡻࡰ࠮࡯ࡲࡨࡺࡲࡥࠨᏀ")
    elif fixture_name.startswith(bstack111lll1_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᏁ")):
        return bstack111lll1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᏂ")
    elif fixture_name.startswith(bstack111lll1_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᏃ")):
        return bstack111lll1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮࠮࡯ࡲࡨࡺࡲࡥࠨᏄ")
def bstack1111l1l111_opy_(fixture_name):
    return bool(re.match(bstack111lll1_opy_ (u"ࠧ࡟ࡡࡻࡹࡳ࡯ࡴࡠࠪࡶࡩࡹࡻࡰࡽࡶࡨࡥࡷࡪ࡯ࡸࡰࠬࡣ࠭࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࡼ࡮ࡱࡧࡹࡱ࡫ࠩࡠࡨ࡬ࡼࡹࡻࡲࡦࡡ࠱࠮ࠬᏅ"), fixture_name))
def bstack1111l11l1l_opy_(fixture_name):
    return bool(re.match(bstack111lll1_opy_ (u"ࠨࡠࡢࡼࡺࡴࡩࡵࡡࠫࡷࡪࡺࡵࡱࡾࡷࡩࡦࡸࡤࡰࡹࡱ࠭ࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪࡥ࠮ࠫࠩᏆ"), fixture_name))
def bstack1111l1llll_opy_(fixture_name):
    return bool(re.match(bstack111lll1_opy_ (u"ࠩࡡࡣࡽࡻ࡮ࡪࡶࡢࠬࡸ࡫ࡴࡶࡲࡿࡸࡪࡧࡲࡥࡱࡺࡲ࠮ࡥࡣ࡭ࡣࡶࡷࡤ࡬ࡩࡹࡶࡸࡶࡪࡥ࠮ࠫࠩᏇ"), fixture_name))
def bstack1111ll1111_opy_(fixture_name):
    if fixture_name.startswith(bstack111lll1_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᏈ")):
        return bstack111lll1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᏉ"), bstack111lll1_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠪᏊ")
    elif fixture_name.startswith(bstack111lll1_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭Ꮛ")):
        return bstack111lll1_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠳࡭ࡰࡦࡸࡰࡪ࠭Ꮜ"), bstack111lll1_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡃࡏࡐࠬᏍ")
    elif fixture_name.startswith(bstack111lll1_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᏎ")):
        return bstack111lll1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧᏏ"), bstack111lll1_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡉࡆࡉࡈࠨᏐ")
    elif fixture_name.startswith(bstack111lll1_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᏑ")):
        return bstack111lll1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮࠮࡯ࡲࡨࡺࡲࡥࠨᏒ"), bstack111lll1_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡁࡍࡎࠪᏓ")
    return None, None
def bstack1111l111ll_opy_(hook_name):
    if hook_name in [bstack111lll1_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧᏔ"), bstack111lll1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࠫᏕ")]:
        return hook_name.capitalize()
    return hook_name
def bstack1111l1l11l_opy_(hook_name):
    if hook_name in [bstack111lll1_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࠫᏖ"), bstack111lll1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡪࡺࡨࡰࡦࠪᏗ")]:
        return bstack111lll1_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠪᏘ")
    elif hook_name in [bstack111lll1_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࠬᏙ"), bstack111lll1_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡣ࡭ࡣࡶࡷࠬᏚ")]:
        return bstack111lll1_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡃࡏࡐࠬᏛ")
    elif hook_name in [bstack111lll1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭Ꮬ"), bstack111lll1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠬᏝ")]:
        return bstack111lll1_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡉࡆࡉࡈࠨᏞ")
    elif hook_name in [bstack111lll1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠧᏟ"), bstack111lll1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡥ࡯ࡥࡸࡹࠧᏠ")]:
        return bstack111lll1_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡁࡍࡎࠪᏡ")
    return hook_name
def bstack1111l1l1l1_opy_(node, scenario):
    if hasattr(node, bstack111lll1_opy_ (u"ࠨࡥࡤࡰࡱࡹࡰࡦࡥࠪᏢ")):
        parts = node.nodeid.rsplit(bstack111lll1_opy_ (u"ࠤ࡞ࠦᏣ"))
        params = parts[-1]
        return bstack111lll1_opy_ (u"ࠥࡿࢂ࡛ࠦࡼࡿࠥᏤ").format(scenario.name, params)
    return scenario.name
def bstack1111l1l1ll_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack111lll1_opy_ (u"ࠫࡨࡧ࡬࡭ࡵࡳࡩࡨ࠭Ꮵ")):
            examples = list(node.callspec.params[bstack111lll1_opy_ (u"ࠬࡥࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡩࡽࡧ࡭ࡱ࡮ࡨࠫᏦ")].values())
        return examples
    except:
        return []
def bstack1111l11lll_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack1111l11l11_opy_(report):
    try:
        status = bstack111lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭Ꮷ")
        if report.passed or (report.failed and hasattr(report, bstack111lll1_opy_ (u"ࠢࡸࡣࡶࡼ࡫ࡧࡩ࡭ࠤᏨ"))):
            status = bstack111lll1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᏩ")
        elif report.skipped:
            status = bstack111lll1_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪᏪ")
        bstack1111l1ll1l_opy_(status)
    except:
        pass
def bstack1ll1l11111_opy_(status):
    try:
        bstack1111l1ll11_opy_ = bstack111lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᏫ")
        if status == bstack111lll1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᏬ"):
            bstack1111l1ll11_opy_ = bstack111lll1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᏭ")
        elif status == bstack111lll1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᏮ"):
            bstack1111l1ll11_opy_ = bstack111lll1_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᏯ")
        bstack1111l1ll1l_opy_(bstack1111l1ll11_opy_)
    except:
        pass
def bstack1111l11ll1_opy_(item=None, report=None, summary=None, extra=None):
    return