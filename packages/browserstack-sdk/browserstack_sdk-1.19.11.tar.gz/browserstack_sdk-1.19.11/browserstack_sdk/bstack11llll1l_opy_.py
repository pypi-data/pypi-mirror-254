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
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1lll1ll1ll_opy_ = {}
        bstack1l1l111111_opy_ = os.environ.get(bstack111lll1_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪೱ"), bstack111lll1_opy_ (u"ࠪࠫೲ"))
        if not bstack1l1l111111_opy_:
            return bstack1lll1ll1ll_opy_
        try:
            bstack1l11llllll_opy_ = json.loads(bstack1l1l111111_opy_)
            if bstack111lll1_opy_ (u"ࠦࡴࡹࠢೳ") in bstack1l11llllll_opy_:
                bstack1lll1ll1ll_opy_[bstack111lll1_opy_ (u"ࠧࡵࡳࠣ೴")] = bstack1l11llllll_opy_[bstack111lll1_opy_ (u"ࠨ࡯ࡴࠤ೵")]
            if bstack111lll1_opy_ (u"ࠢࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠦ೶") in bstack1l11llllll_opy_ or bstack111lll1_opy_ (u"ࠣࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠦ೷") in bstack1l11llllll_opy_:
                bstack1lll1ll1ll_opy_[bstack111lll1_opy_ (u"ࠤࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠧ೸")] = bstack1l11llllll_opy_.get(bstack111lll1_opy_ (u"ࠥࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠢ೹"), bstack1l11llllll_opy_.get(bstack111lll1_opy_ (u"ࠦࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠢ೺")))
            if bstack111lll1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࠨ೻") in bstack1l11llllll_opy_ or bstack111lll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠦ೼") in bstack1l11llllll_opy_:
                bstack1lll1ll1ll_opy_[bstack111lll1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠧ೽")] = bstack1l11llllll_opy_.get(bstack111lll1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࠤ೾"), bstack1l11llllll_opy_.get(bstack111lll1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠢ೿")))
            if bstack111lll1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧഀ") in bstack1l11llllll_opy_ or bstack111lll1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠧഁ") in bstack1l11llllll_opy_:
                bstack1lll1ll1ll_opy_[bstack111lll1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳࠨം")] = bstack1l11llllll_opy_.get(bstack111lll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣഃ"), bstack1l11llllll_opy_.get(bstack111lll1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠣഄ")))
            if bstack111lll1_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࠣഅ") in bstack1l11llllll_opy_ or bstack111lll1_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪࠨആ") in bstack1l11llllll_opy_:
                bstack1lll1ll1ll_opy_[bstack111lll1_opy_ (u"ࠥࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠢഇ")] = bstack1l11llllll_opy_.get(bstack111lll1_opy_ (u"ࠦࡩ࡫ࡶࡪࡥࡨࠦഈ"), bstack1l11llllll_opy_.get(bstack111lll1_opy_ (u"ࠧࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠤഉ")))
            if bstack111lll1_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠣഊ") in bstack1l11llllll_opy_ or bstack111lll1_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨഋ") in bstack1l11llllll_opy_:
                bstack1lll1ll1ll_opy_[bstack111lll1_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠢഌ")] = bstack1l11llllll_opy_.get(bstack111lll1_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࠦ഍"), bstack1l11llllll_opy_.get(bstack111lll1_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠤഎ")))
            if bstack111lll1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠢഏ") in bstack1l11llllll_opy_ or bstack111lll1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢഐ") in bstack1l11llllll_opy_:
                bstack1lll1ll1ll_opy_[bstack111lll1_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣ഑")] = bstack1l11llllll_opy_.get(bstack111lll1_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡࡹࡩࡷࡹࡩࡰࡰࠥഒ"), bstack1l11llllll_opy_.get(bstack111lll1_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥഓ")))
            if bstack111lll1_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡘࡤࡶ࡮ࡧࡢ࡭ࡧࡶࠦഔ") in bstack1l11llllll_opy_:
                bstack1lll1ll1ll_opy_[bstack111lll1_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯࡙ࡥࡷ࡯ࡡࡣ࡮ࡨࡷࠧക")] = bstack1l11llllll_opy_[bstack111lll1_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰ࡚ࡦࡸࡩࡢࡤ࡯ࡩࡸࠨഖ")]
        except Exception as error:
            logger.error(bstack111lll1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡥࡸࡶࡷ࡫࡮ࡵࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡩࡧࡴࡢ࠼ࠣࠦഗ") +  str(error))
        return bstack1lll1ll1ll_opy_