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
import datetime
import json
import logging
import os
import threading
from bstack_utils.helper import bstack11ll1l1ll1_opy_, bstack1lll11l1ll_opy_, get_host_info, bstack11ll1l1l11_opy_, bstack11ll1ll1l1_opy_, bstack11l1l11l11_opy_, \
    bstack11l1lll1ll_opy_, bstack11l1ll111l_opy_, bstack1l1111111_opy_, bstack11l11l111l_opy_, bstack1lllll111l_opy_, bstack1l11ll1ll1_opy_
from bstack_utils.bstack11111lll11_opy_ import bstack1111l11111_opy_
from bstack_utils.bstack1l1111l11l_opy_ import bstack1l11lll11l_opy_
bstack1lllll1lll1_opy_ = [
    bstack111lll1_opy_ (u"ࠬࡒ࡯ࡨࡅࡵࡩࡦࡺࡥࡥࠩᑤ"), bstack111lll1_opy_ (u"࠭ࡃࡃࡖࡖࡩࡸࡹࡩࡰࡰࡆࡶࡪࡧࡴࡦࡦࠪᑥ"), bstack111lll1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩᑦ"), bstack111lll1_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩᑧ"),
    bstack111lll1_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫᑨ"), bstack111lll1_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᑩ"), bstack111lll1_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬᑪ")
]
bstack1lllllll1l1_opy_ = bstack111lll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡣࡰ࡮࡯ࡩࡨࡺ࡯ࡳ࠯ࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬᑫ")
logger = logging.getLogger(__name__)
class bstack1llll11l1_opy_:
    bstack11111lll11_opy_ = None
    bs_config = None
    @classmethod
    @bstack1l11ll1ll1_opy_(class_method=True)
    def launch(cls, bs_config, bstack1lllllll11l_opy_):
        cls.bs_config = bs_config
        if not cls.bstack1llllll11ll_opy_():
            return
        cls.bstack1lllll1l1ll_opy_()
        bstack11ll1lllll_opy_ = bstack11ll1l1l11_opy_(bs_config)
        bstack11ll1ll1ll_opy_ = bstack11ll1ll1l1_opy_(bs_config)
        data = {
            bstack111lll1_opy_ (u"࠭ࡦࡰࡴࡰࡥࡹ࠭ᑬ"): bstack111lll1_opy_ (u"ࠧ࡫ࡵࡲࡲࠬᑭ"),
            bstack111lll1_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡡࡱࡥࡲ࡫ࠧᑮ"): bs_config.get(bstack111lll1_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧᑯ"), bstack111lll1_opy_ (u"ࠪࠫᑰ")),
            bstack111lll1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᑱ"): bs_config.get(bstack111lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨᑲ"), os.path.basename(os.path.abspath(os.getcwd()))),
            bstack111lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩᑳ"): bs_config.get(bstack111lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩᑴ")),
            bstack111lll1_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭ᑵ"): bs_config.get(bstack111lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡅࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬᑶ"), bstack111lll1_opy_ (u"ࠪࠫᑷ")),
            bstack111lll1_opy_ (u"ࠫࡸࡺࡡࡳࡶࡢࡸ࡮ࡳࡥࠨᑸ"): datetime.datetime.now().isoformat(),
            bstack111lll1_opy_ (u"ࠬࡺࡡࡨࡵࠪᑹ"): bstack11l1l11l11_opy_(bs_config),
            bstack111lll1_opy_ (u"࠭ࡨࡰࡵࡷࡣ࡮ࡴࡦࡰࠩᑺ"): get_host_info(),
            bstack111lll1_opy_ (u"ࠧࡤ࡫ࡢ࡭ࡳ࡬࡯ࠨᑻ"): bstack1lll11l1ll_opy_(),
            bstack111lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡳࡷࡱࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᑼ"): os.environ.get(bstack111lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨᑽ")),
            bstack111lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࡢࡸࡪࡹࡴࡴࡡࡵࡩࡷࡻ࡮ࠨᑾ"): os.environ.get(bstack111lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࠩᑿ"), False),
            bstack111lll1_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳࡥࡣࡰࡰࡷࡶࡴࡲࠧᒀ"): bstack11ll1l1ll1_opy_(),
            bstack111lll1_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᒁ"): {
                bstack111lll1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡑࡥࡲ࡫ࠧᒂ"): bstack1lllllll11l_opy_.get(bstack111lll1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࠩᒃ"), bstack111lll1_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵࠩᒄ")),
                bstack111lll1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᒅ"): bstack1lllllll11l_opy_.get(bstack111lll1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨᒆ")),
                bstack111lll1_opy_ (u"ࠬࡹࡤ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩᒇ"): bstack1lllllll11l_opy_.get(bstack111lll1_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫᒈ"))
            }
        }
        config = {
            bstack111lll1_opy_ (u"ࠧࡢࡷࡷ࡬ࠬᒉ"): (bstack11ll1lllll_opy_, bstack11ll1ll1ll_opy_),
            bstack111lll1_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩᒊ"): cls.default_headers()
        }
        response = bstack1l1111111_opy_(bstack111lll1_opy_ (u"ࠩࡓࡓࡘ࡚ࠧᒋ"), cls.request_url(bstack111lll1_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡺ࡯࡬ࡥࡵࠪᒌ")), data, config)
        if response.status_code != 200:
            os.environ[bstack111lll1_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡄࡑࡐࡔࡑࡋࡔࡆࡆࠪᒍ")] = bstack111lll1_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫᒎ")
            os.environ[bstack111lll1_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡎ࡜࡚ࠧᒏ")] = bstack111lll1_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬᒐ")
            os.environ[bstack111lll1_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧᒑ")] = bstack111lll1_opy_ (u"ࠤࡱࡹࡱࡲࠢᒒ")
            os.environ[bstack111lll1_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡂࡎࡏࡓ࡜ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࡖࠫᒓ")] = bstack111lll1_opy_ (u"ࠦࡳࡻ࡬࡭ࠤᒔ")
            bstack1lllll1l111_opy_ = response.json()
            if bstack1lllll1l111_opy_ and bstack1lllll1l111_opy_[bstack111lll1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᒕ")]:
                error_message = bstack1lllll1l111_opy_[bstack111lll1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᒖ")]
                if bstack1lllll1l111_opy_[bstack111lll1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࡚ࡹࡱࡧࠪᒗ")] == bstack111lll1_opy_ (u"ࠨࡇࡕࡖࡔࡘ࡟ࡊࡐ࡙ࡅࡑࡏࡄࡠࡅࡕࡉࡉࡋࡎࡕࡋࡄࡐࡘ࠭ᒘ"):
                    logger.error(error_message)
                elif bstack1lllll1l111_opy_[bstack111lll1_opy_ (u"ࠩࡨࡶࡷࡵࡲࡕࡻࡳࡩࠬᒙ")] == bstack111lll1_opy_ (u"ࠪࡉࡗࡘࡏࡓࡡࡄࡇࡈࡋࡓࡔࡡࡇࡉࡓࡏࡅࡅࠩᒚ"):
                    logger.info(error_message)
                elif bstack1lllll1l111_opy_[bstack111lll1_opy_ (u"ࠫࡪࡸࡲࡰࡴࡗࡽࡵ࡫ࠧᒛ")] == bstack111lll1_opy_ (u"ࠬࡋࡒࡓࡑࡕࡣࡘࡊࡋࡠࡆࡈࡔࡗࡋࡃࡂࡖࡈࡈࠬᒜ"):
                    logger.error(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack111lll1_opy_ (u"ࠨࡄࡢࡶࡤࠤࡺࡶ࡬ࡰࡣࡧࠤࡹࡵࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡔࡦࡵࡷࠤࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡩࡻࡥࠡࡶࡲࠤࡸࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠣᒝ"))
            return [None, None, None]
        logger.debug(bstack111lll1_opy_ (u"ࠧࡕࡧࡶࡸࠥࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠥࡈࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦࡓࡶࡥࡦࡩࡸࡹࡦࡶ࡮ࠤࠫᒞ"))
        os.environ[bstack111lll1_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡈࡕࡍࡑࡎࡈࡘࡊࡊࠧᒟ")] = bstack111lll1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧᒠ")
        bstack1lllll1l111_opy_ = response.json()
        if bstack1lllll1l111_opy_.get(bstack111lll1_opy_ (u"ࠪ࡮ࡼࡺࠧᒡ")):
            os.environ[bstack111lll1_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡌ࡚ࡘࠬᒢ")] = bstack1lllll1l111_opy_[bstack111lll1_opy_ (u"ࠬࡰࡷࡵࠩᒣ")]
            os.environ[bstack111lll1_opy_ (u"࠭ࡃࡓࡇࡇࡉࡓ࡚ࡉࡂࡎࡖࡣࡋࡕࡒࡠࡅࡕࡅࡘࡎ࡟ࡓࡇࡓࡓࡗ࡚ࡉࡏࡉࠪᒤ")] = json.dumps({
                bstack111lll1_opy_ (u"ࠧࡶࡵࡨࡶࡳࡧ࡭ࡦࠩᒥ"): bstack11ll1lllll_opy_,
                bstack111lll1_opy_ (u"ࠨࡲࡤࡷࡸࡽ࡯ࡳࡦࠪᒦ"): bstack11ll1ll1ll_opy_
            })
        if bstack1lllll1l111_opy_.get(bstack111lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫᒧ")):
            os.environ[bstack111lll1_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩᒨ")] = bstack1lllll1l111_opy_[bstack111lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ᒩ")]
        if bstack1lllll1l111_opy_.get(bstack111lll1_opy_ (u"ࠬࡧ࡬࡭ࡱࡺࡣࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩᒪ")):
            os.environ[bstack111lll1_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡅࡑࡒࡏࡘࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࡙ࠧᒫ")] = str(bstack1lllll1l111_opy_[bstack111lll1_opy_ (u"ࠧࡢ࡮࡯ࡳࡼࡥࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫᒬ")])
        return [bstack1lllll1l111_opy_[bstack111lll1_opy_ (u"ࠨ࡬ࡺࡸࠬᒭ")], bstack1lllll1l111_opy_[bstack111lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫᒮ")], bstack1lllll1l111_opy_[bstack111lll1_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡡࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧᒯ")]]
    @classmethod
    @bstack1l11ll1ll1_opy_(class_method=True)
    def stop(cls):
        if not cls.on():
            return
        if os.environ[bstack111lll1_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡌ࡚ࡘࠬᒰ")] == bstack111lll1_opy_ (u"ࠧࡴࡵ࡭࡮ࠥᒱ") or os.environ[bstack111lll1_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠬᒲ")] == bstack111lll1_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧᒳ"):
            print(bstack111lll1_opy_ (u"ࠨࡇ࡛ࡇࡊࡖࡔࡊࡑࡑࠤࡎࡔࠠࡴࡶࡲࡴࡇࡻࡩ࡭ࡦࡘࡴࡸࡺࡲࡦࡣࡰࠤࡗࡋࡑࡖࡇࡖࡘ࡚ࠥࡏࠡࡖࡈࡗ࡙ࠦࡏࡃࡕࡈࡖ࡛ࡇࡂࡊࡎࡌࡘ࡞ࠦ࠺ࠡࡏ࡬ࡷࡸ࡯࡮ࡨࠢࡤࡹࡹ࡮ࡥ࡯ࡶ࡬ࡧࡦࡺࡩࡰࡰࠣࡸࡴࡱࡥ࡯ࠩᒴ"))
            return {
                bstack111lll1_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᒵ"): bstack111lll1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩᒶ"),
                bstack111lll1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᒷ"): bstack111lll1_opy_ (u"࡚ࠬ࡯࡬ࡧࡱ࠳ࡧࡻࡩ࡭ࡦࡌࡈࠥ࡯ࡳࠡࡷࡱࡨࡪ࡬ࡩ࡯ࡧࡧ࠰ࠥࡨࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦ࡭ࡪࡩ࡫ࡸࠥ࡮ࡡࡷࡧࠣࡪࡦ࡯࡬ࡦࡦࠪᒸ")
            }
        else:
            cls.bstack11111lll11_opy_.shutdown()
            data = {
                bstack111lll1_opy_ (u"࠭ࡳࡵࡱࡳࡣࡹ࡯࡭ࡦࠩᒹ"): datetime.datetime.now().isoformat()
            }
            config = {
                bstack111lll1_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨᒺ"): cls.default_headers()
            }
            bstack11l1ll11ll_opy_ = bstack111lll1_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀ࠳ࡸࡺ࡯ࡱࠩᒻ").format(os.environ[bstack111lll1_opy_ (u"ࠤࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠣᒼ")])
            bstack1lllll1llll_opy_ = cls.request_url(bstack11l1ll11ll_opy_)
            response = bstack1l1111111_opy_(bstack111lll1_opy_ (u"ࠪࡔ࡚࡚ࠧᒽ"), bstack1lllll1llll_opy_, data, config)
            if not response.ok:
                raise Exception(bstack111lll1_opy_ (u"ࠦࡘࡺ࡯ࡱࠢࡵࡩࡶࡻࡥࡴࡶࠣࡲࡴࡺࠠࡰ࡭ࠥᒾ"))
    @classmethod
    def bstack1l11ll111l_opy_(cls):
        if cls.bstack11111lll11_opy_ is None:
            return
        cls.bstack11111lll11_opy_.shutdown()
    @classmethod
    def bstack1l11l111l_opy_(cls):
        if cls.on():
            print(
                bstack111lll1_opy_ (u"ࠬ࡜ࡩࡴ࡫ࡷࠤ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀࠤࡹࡵࠠࡷ࡫ࡨࡻࠥࡨࡵࡪ࡮ࡧࠤࡷ࡫ࡰࡰࡴࡷ࠰ࠥ࡯࡮ࡴ࡫ࡪ࡬ࡹࡹࠬࠡࡣࡱࡨࠥࡳࡡ࡯ࡻࠣࡱࡴࡸࡥࠡࡦࡨࡦࡺ࡭ࡧࡪࡰࡪࠤ࡮ࡴࡦࡰࡴࡰࡥࡹ࡯࡯࡯ࠢࡤࡰࡱࠦࡡࡵࠢࡲࡲࡪࠦࡰ࡭ࡣࡦࡩࠦࡢ࡮ࠨᒿ").format(os.environ[bstack111lll1_opy_ (u"ࠨࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠧᓀ")]))
    @classmethod
    def bstack1lllll1l1ll_opy_(cls):
        if cls.bstack11111lll11_opy_ is not None:
            return
        cls.bstack11111lll11_opy_ = bstack1111l11111_opy_(cls.bstack1llllll1l1l_opy_)
        cls.bstack11111lll11_opy_.start()
    @classmethod
    def bstack1l11l1l11l_opy_(cls, bstack1l11111lll_opy_, bstack1lllll1l1l1_opy_=bstack111lll1_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡣࡷࡧ࡭࠭ᓁ")):
        if not cls.on():
            return
        bstack1ll11ll11_opy_ = bstack1l11111lll_opy_[bstack111lll1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬᓂ")]
        bstack1lllll1ll1l_opy_ = {
            bstack111lll1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪᓃ"): bstack111lll1_opy_ (u"ࠪࡘࡪࡹࡴࡠࡕࡷࡥࡷࡺ࡟ࡖࡲ࡯ࡳࡦࡪࠧᓄ"),
            bstack111lll1_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᓅ"): bstack111lll1_opy_ (u"࡚ࠬࡥࡴࡶࡢࡉࡳࡪ࡟ࡖࡲ࡯ࡳࡦࡪࠧᓆ"),
            bstack111lll1_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓ࡬࡫ࡳࡴࡪࡪࠧᓇ"): bstack111lll1_opy_ (u"ࠧࡕࡧࡶࡸࡤ࡙࡫ࡪࡲࡳࡩࡩࡥࡕࡱ࡮ࡲࡥࡩ࠭ᓈ"),
            bstack111lll1_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬᓉ"): bstack111lll1_opy_ (u"ࠩࡏࡳ࡬ࡥࡕࡱ࡮ࡲࡥࡩ࠭ᓊ"),
            bstack111lll1_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᓋ"): bstack111lll1_opy_ (u"ࠫࡍࡵ࡯࡬ࡡࡖࡸࡦࡸࡴࡠࡗࡳࡰࡴࡧࡤࠨᓌ"),
            bstack111lll1_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧᓍ"): bstack111lll1_opy_ (u"࠭ࡈࡰࡱ࡮ࡣࡊࡴࡤࡠࡗࡳࡰࡴࡧࡤࠨᓎ"),
            bstack111lll1_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫᓏ"): bstack111lll1_opy_ (u"ࠨࡅࡅࡘࡤ࡛ࡰ࡭ࡱࡤࡨࠬᓐ")
        }.get(bstack1ll11ll11_opy_)
        if bstack1lllll1l1l1_opy_ == bstack111lll1_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡥࡹࡩࡨࠨᓑ"):
            cls.bstack1lllll1l1ll_opy_()
            cls.bstack11111lll11_opy_.add(bstack1l11111lll_opy_)
        elif bstack1lllll1l1l1_opy_ == bstack111lll1_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨᓒ"):
            cls.bstack1llllll1l1l_opy_([bstack1l11111lll_opy_], bstack1lllll1l1l1_opy_)
    @classmethod
    @bstack1l11ll1ll1_opy_(class_method=True)
    def bstack1llllll1l1l_opy_(cls, bstack1l11111lll_opy_, bstack1lllll1l1l1_opy_=bstack111lll1_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪᓓ")):
        config = {
            bstack111lll1_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭ᓔ"): cls.default_headers()
        }
        response = bstack1l1111111_opy_(bstack111lll1_opy_ (u"࠭ࡐࡐࡕࡗࠫᓕ"), cls.request_url(bstack1lllll1l1l1_opy_), bstack1l11111lll_opy_, config)
        bstack11ll1lll11_opy_ = response.json()
    @classmethod
    @bstack1l11ll1ll1_opy_(class_method=True)
    def bstack1l11lll111_opy_(cls, bstack1l111l1l11_opy_):
        bstack1llllll1111_opy_ = []
        for log in bstack1l111l1l11_opy_:
            bstack1llllll1l11_opy_ = {
                bstack111lll1_opy_ (u"ࠧ࡬࡫ࡱࡨࠬᓖ"): bstack111lll1_opy_ (u"ࠨࡖࡈࡗ࡙ࡥࡌࡐࡉࠪᓗ"),
                bstack111lll1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᓘ"): log[bstack111lll1_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩᓙ")],
                bstack111lll1_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧᓚ"): log[bstack111lll1_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨᓛ")],
                bstack111lll1_opy_ (u"࠭ࡨࡵࡶࡳࡣࡷ࡫ࡳࡱࡱࡱࡷࡪ࠭ᓜ"): {},
                bstack111lll1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᓝ"): log[bstack111lll1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᓞ")],
            }
            if bstack111lll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᓟ") in log:
                bstack1llllll1l11_opy_[bstack111lll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᓠ")] = log[bstack111lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᓡ")]
            elif bstack111lll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᓢ") in log:
                bstack1llllll1l11_opy_[bstack111lll1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᓣ")] = log[bstack111lll1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᓤ")]
            bstack1llllll1111_opy_.append(bstack1llllll1l11_opy_)
        cls.bstack1l11l1l11l_opy_({
            bstack111lll1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬᓥ"): bstack111lll1_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭ᓦ"),
            bstack111lll1_opy_ (u"ࠪࡰࡴ࡭ࡳࠨᓧ"): bstack1llllll1111_opy_
        })
    @classmethod
    @bstack1l11ll1ll1_opy_(class_method=True)
    def bstack1lllllll1ll_opy_(cls, steps):
        bstack1llllll1ll1_opy_ = []
        for step in steps:
            bstack1llllll111l_opy_ = {
                bstack111lll1_opy_ (u"ࠫࡰ࡯࡮ࡥࠩᓨ"): bstack111lll1_opy_ (u"࡚ࠬࡅࡔࡖࡢࡗ࡙ࡋࡐࠨᓩ"),
                bstack111lll1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᓪ"): step[bstack111lll1_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ᓫ")],
                bstack111lll1_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫᓬ"): step[bstack111lll1_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬᓭ")],
                bstack111lll1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᓮ"): step[bstack111lll1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᓯ")],
                bstack111lll1_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧᓰ"): step[bstack111lll1_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠨᓱ")]
            }
            if bstack111lll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᓲ") in step:
                bstack1llllll111l_opy_[bstack111lll1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᓳ")] = step[bstack111lll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᓴ")]
            elif bstack111lll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᓵ") in step:
                bstack1llllll111l_opy_[bstack111lll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᓶ")] = step[bstack111lll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᓷ")]
            bstack1llllll1ll1_opy_.append(bstack1llllll111l_opy_)
        cls.bstack1l11l1l11l_opy_({
            bstack111lll1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪᓸ"): bstack111lll1_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫᓹ"),
            bstack111lll1_opy_ (u"ࠨ࡮ࡲ࡫ࡸ࠭ᓺ"): bstack1llllll1ll1_opy_
        })
    @classmethod
    @bstack1l11ll1ll1_opy_(class_method=True)
    def bstack1l1l11l111_opy_(cls, screenshot):
        cls.bstack1l11l1l11l_opy_({
            bstack111lll1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ᓻ"): bstack111lll1_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧᓼ"),
            bstack111lll1_opy_ (u"ࠫࡱࡵࡧࡴࠩᓽ"): [{
                bstack111lll1_opy_ (u"ࠬࡱࡩ࡯ࡦࠪᓾ"): bstack111lll1_opy_ (u"࠭ࡔࡆࡕࡗࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࠨᓿ"),
                bstack111lll1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪᔀ"): datetime.datetime.utcnow().isoformat() + bstack111lll1_opy_ (u"ࠨ࡜ࠪᔁ"),
                bstack111lll1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᔂ"): screenshot[bstack111lll1_opy_ (u"ࠪ࡭ࡲࡧࡧࡦࠩᔃ")],
                bstack111lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᔄ"): screenshot[bstack111lll1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᔅ")]
            }]
        }, bstack1lllll1l1l1_opy_=bstack111lll1_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫᔆ"))
    @classmethod
    @bstack1l11ll1ll1_opy_(class_method=True)
    def bstack1ll11l1ll_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1l11l1l11l_opy_({
            bstack111lll1_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫᔇ"): bstack111lll1_opy_ (u"ࠨࡅࡅࡘࡘ࡫ࡳࡴ࡫ࡲࡲࡈࡸࡥࡢࡶࡨࡨࠬᔈ"),
            bstack111lll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫᔉ"): {
                bstack111lll1_opy_ (u"ࠥࡹࡺ࡯ࡤࠣᔊ"): cls.current_test_uuid(),
                bstack111lll1_opy_ (u"ࠦ࡮ࡴࡴࡦࡩࡵࡥࡹ࡯࡯࡯ࡵࠥᔋ"): cls.bstack1l11ll1lll_opy_(driver)
            }
        })
    @classmethod
    def on(cls):
        if os.environ.get(bstack111lll1_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡍ࡛࡙࠭ᔌ"), None) is None or os.environ[bstack111lll1_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡎ࡜࡚ࠧᔍ")] == bstack111lll1_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧᔎ"):
            return False
        return True
    @classmethod
    def bstack1llllll11ll_opy_(cls):
        return bstack1lllll111l_opy_(cls.bs_config.get(bstack111lll1_opy_ (u"ࠨࡶࡨࡷࡹࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬᔏ"), False))
    @staticmethod
    def request_url(url):
        return bstack111lll1_opy_ (u"ࠩࡾࢁ࠴ࢁࡽࠨᔐ").format(bstack1lllllll1l1_opy_, url)
    @staticmethod
    def default_headers():
        headers = {
            bstack111lll1_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩᔑ"): bstack111lll1_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧᔒ"),
            bstack111lll1_opy_ (u"ࠬ࡞࠭ࡃࡕࡗࡅࡈࡑ࠭ࡕࡇࡖࡘࡔࡖࡓࠨᔓ"): bstack111lll1_opy_ (u"࠭ࡴࡳࡷࡨࠫᔔ")
        }
        if os.environ.get(bstack111lll1_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡏ࡝ࡔࠨᔕ"), None):
            headers[bstack111lll1_opy_ (u"ࠨࡃࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨᔖ")] = bstack111lll1_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬᔗ").format(os.environ[bstack111lll1_opy_ (u"ࠥࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡋ࡙ࡗࠦᔘ")])
        return headers
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack111lll1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨᔙ"), None)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack111lll1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᔚ"), None)
    @staticmethod
    def bstack1l111lllll_opy_():
        if getattr(threading.current_thread(), bstack111lll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪᔛ"), None):
            return {
                bstack111lll1_opy_ (u"ࠧࡵࡻࡳࡩࠬᔜ"): bstack111lll1_opy_ (u"ࠨࡶࡨࡷࡹ࠭ᔝ"),
                bstack111lll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᔞ"): getattr(threading.current_thread(), bstack111lll1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧᔟ"), None)
            }
        if getattr(threading.current_thread(), bstack111lll1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᔠ"), None):
            return {
                bstack111lll1_opy_ (u"ࠬࡺࡹࡱࡧࠪᔡ"): bstack111lll1_opy_ (u"࠭ࡨࡰࡱ࡮ࠫᔢ"),
                bstack111lll1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᔣ"): getattr(threading.current_thread(), bstack111lll1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬᔤ"), None)
            }
        return None
    @staticmethod
    def bstack1l11ll1lll_opy_(driver):
        return {
            bstack11l1ll111l_opy_(): bstack11l1lll1ll_opy_(driver)
        }
    @staticmethod
    def bstack1lllllll111_opy_(exception_info, report):
        return [{bstack111lll1_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬᔥ"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack11lll1l1ll_opy_(typename):
        if bstack111lll1_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࠨᔦ") in typename:
            return bstack111lll1_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࡅࡳࡴࡲࡶࠧᔧ")
        return bstack111lll1_opy_ (u"࡛ࠧ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࠨᔨ")
    @staticmethod
    def bstack1llllll1lll_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1llll11l1_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack1l11ll1l11_opy_(test, hook_name=None):
        bstack1lllll1l11l_opy_ = test.parent
        if hook_name in [bstack111lll1_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡩ࡬ࡢࡵࡶࠫᔩ"), bstack111lll1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠨᔪ"), bstack111lll1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠧᔫ"), bstack111lll1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫᔬ")]:
            bstack1lllll1l11l_opy_ = test
        scope = []
        while bstack1lllll1l11l_opy_ is not None:
            scope.append(bstack1lllll1l11l_opy_.name)
            bstack1lllll1l11l_opy_ = bstack1lllll1l11l_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack1llllll11l1_opy_(hook_type):
        if hook_type == bstack111lll1_opy_ (u"ࠥࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠣᔭ"):
            return bstack111lll1_opy_ (u"ࠦࡘ࡫ࡴࡶࡲࠣ࡬ࡴࡵ࡫ࠣᔮ")
        elif hook_type == bstack111lll1_opy_ (u"ࠧࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠤᔯ"):
            return bstack111lll1_opy_ (u"ࠨࡔࡦࡣࡵࡨࡴࡽ࡮ࠡࡪࡲࡳࡰࠨᔰ")
    @staticmethod
    def bstack1lllll1ll11_opy_(bstack1l1lllll_opy_):
        try:
            if not bstack1llll11l1_opy_.on():
                return bstack1l1lllll_opy_
            if os.environ.get(bstack111lll1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࠧᔱ"), None) == bstack111lll1_opy_ (u"ࠣࡶࡵࡹࡪࠨᔲ"):
                tests = os.environ.get(bstack111lll1_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔ࡟ࡕࡇࡖࡘࡘࠨᔳ"), None)
                if tests is None or tests == bstack111lll1_opy_ (u"ࠥࡲࡺࡲ࡬ࠣᔴ"):
                    return bstack1l1lllll_opy_
                bstack1l1lllll_opy_ = tests.split(bstack111lll1_opy_ (u"ࠫ࠱࠭ᔵ"))
                return bstack1l1lllll_opy_
        except Exception as exc:
            print(bstack111lll1_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡷ࡫ࡲࡶࡰࠣ࡬ࡦࡴࡤ࡭ࡧࡵ࠾ࠥࠨᔶ"), str(exc))
        return bstack1l1lllll_opy_
    @classmethod
    def bstack1l111l11ll_opy_(cls, event: str, bstack1l11111lll_opy_: bstack1l11lll11l_opy_):
        bstack1l11l11ll1_opy_ = {
            bstack111lll1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪᔷ"): event,
            bstack1l11111lll_opy_.bstack1l11l1ll1l_opy_(): bstack1l11111lll_opy_.bstack1l11l1l1ll_opy_(event)
        }
        bstack1llll11l1_opy_.bstack1l11l1l11l_opy_(bstack1l11l11ll1_opy_)