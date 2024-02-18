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
import requests
import logging
from urllib.parse import urlparse
from datetime import datetime
from bstack_utils.constants import bstack11ll1ll111_opy_ as bstack11ll1l11ll_opy_
from bstack_utils.helper import bstack1ll1l11lll_opy_, bstack1ll1l1l1l1_opy_, bstack11ll1l1l11_opy_, bstack11ll1ll1l1_opy_, bstack1lll11l1ll_opy_, get_host_info, bstack11ll1l1ll1_opy_, bstack1l1111111_opy_, bstack1l11ll1ll1_opy_
from browserstack_sdk._version import __version__
logger = logging.getLogger(__name__)
@bstack1l11ll1ll1_opy_(class_method=False)
def _11lll1l11l_opy_(driver, bstack1lll1ll1l_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack111lll1_opy_ (u"࠭࡯ࡴࡡࡱࡥࡲ࡫ࠧฆ"): caps.get(bstack111lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪ࠭ง"), None),
        bstack111lll1_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬจ"): bstack1lll1ll1l_opy_.get(bstack111lll1_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬฉ"), None),
        bstack111lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡳࡧ࡭ࡦࠩช"): caps.get(bstack111lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩซ"), None),
        bstack111lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧฌ"): caps.get(bstack111lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧญ"), None)
    }
  except Exception as error:
    logger.debug(bstack111lll1_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡦࡦࡶࡦ࡬࡮ࡴࡧࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡨࡪࡺࡡࡪ࡮ࡶࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲࠡ࠼ࠣࠫฎ") + str(error))
  return response
def bstack1111l1ll1_opy_(config):
  return config.get(bstack111lll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨฏ"), False) or any([p.get(bstack111lll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩฐ"), False) == True for p in config.get(bstack111lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ฑ"), [])])
def bstack1lll1llll_opy_(config, bstack11l1l1111_opy_):
  try:
    if not bstack1ll1l1l1l1_opy_(config):
      return False
    bstack11lll11ll1_opy_ = config.get(bstack111lll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫฒ"), False)
    bstack11ll1llll1_opy_ = config[bstack111lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨณ")][bstack11l1l1111_opy_].get(bstack111lll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ด"), None)
    if bstack11ll1llll1_opy_ != None:
      bstack11lll11ll1_opy_ = bstack11ll1llll1_opy_
    bstack11ll1lll1l_opy_ = os.getenv(bstack111lll1_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬต")) is not None and len(os.getenv(bstack111lll1_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ถ"))) > 0 and os.getenv(bstack111lll1_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧท")) != bstack111lll1_opy_ (u"ࠪࡲࡺࡲ࡬ࠨธ")
    return bstack11lll11ll1_opy_ and bstack11ll1lll1l_opy_
  except Exception as error:
    logger.debug(bstack111lll1_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡺࡪࡸࡩࡧࡻ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡷࡪࡹࡳࡪࡱࡱࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲࠡ࠼ࠣࠫน") + str(error))
  return False
def bstack1l11l1ll1_opy_(bstack11lll1l1l1_opy_, test_tags):
  bstack11lll1l1l1_opy_ = os.getenv(bstack111lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭บ"))
  if bstack11lll1l1l1_opy_ is None:
    return True
  bstack11lll1l1l1_opy_ = json.loads(bstack11lll1l1l1_opy_)
  try:
    include_tags = bstack11lll1l1l1_opy_[bstack111lll1_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫป")] if bstack111lll1_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬผ") in bstack11lll1l1l1_opy_ and isinstance(bstack11lll1l1l1_opy_[bstack111lll1_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ฝ")], list) else []
    exclude_tags = bstack11lll1l1l1_opy_[bstack111lll1_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧพ")] if bstack111lll1_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨฟ") in bstack11lll1l1l1_opy_ and isinstance(bstack11lll1l1l1_opy_[bstack111lll1_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩภ")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack111lll1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡺࡦࡲࡩࡥࡣࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡪࡴࡸࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡥࡤࡲࡳ࡯࡮ࡨ࠰ࠣࡉࡷࡸ࡯ࡳࠢ࠽ࠤࠧม") + str(error))
  return False
def bstack1lll11ll_opy_(config, bstack11lll1111l_opy_, bstack11lll11l11_opy_):
  bstack11ll1lllll_opy_ = bstack11ll1l1l11_opy_(config)
  bstack11ll1ll1ll_opy_ = bstack11ll1ll1l1_opy_(config)
  if bstack11ll1lllll_opy_ is None or bstack11ll1ll1ll_opy_ is None:
    logger.error(bstack111lll1_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡥࡵࡩࡦࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡴࡸࡲࠥ࡬࡯ࡳࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࠿ࠦࡍࡪࡵࡶ࡭ࡳ࡭ࠠࡢࡷࡷ࡬ࡪࡴࡴࡪࡥࡤࡸ࡮ࡵ࡮ࠡࡶࡲ࡯ࡪࡴࠧย"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack111lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨร"), bstack111lll1_opy_ (u"ࠨࡽࢀࠫฤ")))
    data = {
        bstack111lll1_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧล"): config[bstack111lll1_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨฦ")],
        bstack111lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧว"): config.get(bstack111lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨศ"), os.path.basename(os.getcwd())),
        bstack111lll1_opy_ (u"࠭ࡳࡵࡣࡵࡸ࡙࡯࡭ࡦࠩษ"): bstack1ll1l11lll_opy_(),
        bstack111lll1_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬส"): config.get(bstack111lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫห"), bstack111lll1_opy_ (u"ࠩࠪฬ")),
        bstack111lll1_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪอ"): {
            bstack111lll1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡎࡢ࡯ࡨࠫฮ"): bstack11lll1111l_opy_,
            bstack111lll1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨฯ"): bstack11lll11l11_opy_,
            bstack111lll1_opy_ (u"࠭ࡳࡥ࡭࡙ࡩࡷࡹࡩࡰࡰࠪะ"): __version__
        },
        bstack111lll1_opy_ (u"ࠧࡴࡧࡷࡸ࡮ࡴࡧࡴࠩั"): settings,
        bstack111lll1_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࡅࡲࡲࡹࡸ࡯࡭ࠩา"): bstack11ll1l1ll1_opy_(),
        bstack111lll1_opy_ (u"ࠩࡦ࡭ࡎࡴࡦࡰࠩำ"): bstack1lll11l1ll_opy_(),
        bstack111lll1_opy_ (u"ࠪ࡬ࡴࡹࡴࡊࡰࡩࡳࠬิ"): get_host_info(),
        bstack111lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ี"): bstack1ll1l1l1l1_opy_(config)
    }
    headers = {
        bstack111lll1_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫึ"): bstack111lll1_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩื"),
    }
    config = {
        bstack111lll1_opy_ (u"ࠧࡢࡷࡷ࡬ุࠬ"): (bstack11ll1lllll_opy_, bstack11ll1ll1ll_opy_),
        bstack111lll1_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴูࠩ"): headers
    }
    response = bstack1l1111111_opy_(bstack111lll1_opy_ (u"ࠩࡓࡓࡘฺ࡚ࠧ"), bstack11ll1l11ll_opy_ + bstack111lll1_opy_ (u"ࠪ࠳ࡹ࡫ࡳࡵࡡࡵࡹࡳࡹࠧ฻"), data, config)
    bstack11ll1lll11_opy_ = response.json()
    if bstack11ll1lll11_opy_[bstack111lll1_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬ฼")]:
      parsed = json.loads(os.getenv(bstack111lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭฽"), bstack111lll1_opy_ (u"࠭ࡻࡾࠩ฾")))
      parsed[bstack111lll1_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ฿")] = bstack11ll1lll11_opy_[bstack111lll1_opy_ (u"ࠨࡦࡤࡸࡦ࠭เ")][bstack111lll1_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪแ")]
      os.environ[bstack111lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫโ")] = json.dumps(parsed)
      return bstack11ll1lll11_opy_[bstack111lll1_opy_ (u"ࠫࡩࡧࡴࡢࠩใ")][bstack111lll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ࡙ࡵ࡫ࡦࡰࠪไ")], bstack11ll1lll11_opy_[bstack111lll1_opy_ (u"࠭ࡤࡢࡶࡤࠫๅ")][bstack111lll1_opy_ (u"ࠧࡪࡦࠪๆ")]
    else:
      logger.error(bstack111lll1_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡶࡺࡴ࡮ࡪࡰࡪࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠺ࠡࠩ็") + bstack11ll1lll11_opy_[bstack111lll1_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧ่ࠪ")])
      if bstack11ll1lll11_opy_[bstack111lll1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨ้ࠫ")] == bstack111lll1_opy_ (u"ࠫࡎࡴࡶࡢ࡮࡬ࡨࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥࡶࡡࡴࡵࡨࡨ࠳๊࠭"):
        for bstack11lll111ll_opy_ in bstack11ll1lll11_opy_[bstack111lll1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡷ๋ࠬ")]:
          logger.error(bstack11lll111ll_opy_[bstack111lll1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ์")])
      return None, None
  except Exception as error:
    logger.error(bstack111lll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡵࡹࡳࠦࡦࡰࡴࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡀࠠࠣํ") +  str(error))
    return None, None
def bstack1ll11ll1ll_opy_():
  if os.getenv(bstack111lll1_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭๎")) is None:
    return {
        bstack111lll1_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ๏"): bstack111lll1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ๐"),
        bstack111lll1_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ๑"): bstack111lll1_opy_ (u"ࠬࡈࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦࡨࡢࡦࠣࡪࡦ࡯࡬ࡦࡦ࠱ࠫ๒")
    }
  data = {bstack111lll1_opy_ (u"࠭ࡥ࡯ࡦࡗ࡭ࡲ࡫ࠧ๓"): bstack1ll1l11lll_opy_()}
  headers = {
      bstack111lll1_opy_ (u"ࠧࡂࡷࡷ࡬ࡴࡸࡩࡻࡣࡷ࡭ࡴࡴࠧ๔"): bstack111lll1_opy_ (u"ࠨࡄࡨࡥࡷ࡫ࡲࠡࠩ๕") + os.getenv(bstack111lll1_opy_ (u"ࠤࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠢ๖")),
      bstack111lll1_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩ๗"): bstack111lll1_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ๘")
  }
  response = bstack1l1111111_opy_(bstack111lll1_opy_ (u"ࠬࡖࡕࡕࠩ๙"), bstack11ll1l11ll_opy_ + bstack111lll1_opy_ (u"࠭࠯ࡵࡧࡶࡸࡤࡸࡵ࡯ࡵ࠲ࡷࡹࡵࡰࠨ๚"), data, { bstack111lll1_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨ๛"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack111lll1_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤ࡙࡫ࡳࡵࠢࡕࡹࡳࠦ࡭ࡢࡴ࡮ࡩࡩࠦࡡࡴࠢࡦࡳࡲࡶ࡬ࡦࡶࡨࡨࠥࡧࡴࠡࠤ๜") + datetime.utcnow().isoformat() + bstack111lll1_opy_ (u"ࠩ࡝ࠫ๝"))
      return {bstack111lll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ๞"): bstack111lll1_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬ๟"), bstack111lll1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭๠"): bstack111lll1_opy_ (u"࠭ࠧ๡")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack111lll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡧࡴࡳࡰ࡭ࡧࡷ࡭ࡴࡴࠠࡰࡨࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡔࡦࡵࡷࠤࡗࡻ࡮࠻ࠢࠥ๢") + str(error))
    return {
        bstack111lll1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ๣"): bstack111lll1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ๤"),
        bstack111lll1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ๥"): str(error)
    }
def bstack1l1lll111l_opy_(caps, options):
  try:
    bstack11ll1l1l1l_opy_ = caps.get(bstack111lll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ๦"), {}).get(bstack111lll1_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩ๧"), caps.get(bstack111lll1_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭๨"), bstack111lll1_opy_ (u"ࠧࠨ๩")))
    if bstack11ll1l1l1l_opy_:
      logger.warn(bstack111lll1_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡆࡨࡷࡰࡺ࡯ࡱࠢࡥࡶࡴࡽࡳࡦࡴࡶ࠲ࠧ๪"))
      return False
    browser = caps.get(bstack111lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ๫"), bstack111lll1_opy_ (u"ࠪࠫ๬")).lower()
    if browser != bstack111lll1_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫ๭"):
      logger.warn(bstack111lll1_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡉࡨࡳࡱࡰࡩࠥࡨࡲࡰࡹࡶࡩࡷࡹ࠮ࠣ๮"))
      return False
    browser_version = caps.get(bstack111lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ๯"), caps.get(bstack111lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ๰")))
    if browser_version and browser_version != bstack111lll1_opy_ (u"ࠨ࡮ࡤࡸࡪࡹࡴࠨ๱") and int(browser_version.split(bstack111lll1_opy_ (u"ࠩ࠱ࠫ๲"))[0]) <= 94:
      logger.warn(bstack111lll1_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥ࡭ࡲࡦࡣࡷࡩࡷࠦࡴࡩࡣࡱࠤ࠾࠺࠮ࠣ๳"))
      return False
    if not options is None:
      bstack11ll1l1lll_opy_ = options.to_capabilities().get(bstack111lll1_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ๴"), {})
      if bstack111lll1_opy_ (u"ࠬ࠳࠭ࡩࡧࡤࡨࡱ࡫ࡳࡴࠩ๵") in bstack11ll1l1lll_opy_.get(bstack111lll1_opy_ (u"࠭ࡡࡳࡩࡶࠫ๶"), []):
        logger.warn(bstack111lll1_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡱࡳࡹࠦࡲࡶࡰࠣࡳࡳࠦ࡬ࡦࡩࡤࡧࡾࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪ࠴ࠠࡔࡹ࡬ࡸࡨ࡮ࠠࡵࡱࠣࡲࡪࡽࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫ࠠࡰࡴࠣࡥࡻࡵࡩࡥࠢࡸࡷ࡮ࡴࡧࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠤ๷"))
        return False
    return True
  except Exception as error:
    logger.debug(bstack111lll1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡷࡣ࡯࡭ࡩࡧࡴࡦࠢࡤ࠵࠶ࡿࠠࡴࡷࡳࡴࡴࡸࡴࠡ࠼ࠥ๸") + str(error))
    return False
def set_capabilities(caps, config):
  try:
    bstack11lll1l111_opy_ = config.get(bstack111lll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ๹"), {})
    bstack11lll1l111_opy_[bstack111lll1_opy_ (u"ࠪࡥࡺࡺࡨࡕࡱ࡮ࡩࡳ࠭๺")] = os.getenv(bstack111lll1_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩ๻"))
    bstack11ll1ll11l_opy_ = json.loads(os.getenv(bstack111lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭๼"), bstack111lll1_opy_ (u"࠭ࡻࡾࠩ๽"))).get(bstack111lll1_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ๾"))
    caps[bstack111lll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ๿")] = True
    if bstack111lll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ຀") in caps:
      caps[bstack111lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫກ")][bstack111lll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫຂ")] = bstack11lll1l111_opy_
      caps[bstack111lll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭຃")][bstack111lll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ຄ")][bstack111lll1_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ຅")] = bstack11ll1ll11l_opy_
    else:
      caps[bstack111lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧຆ")] = bstack11lll1l111_opy_
      caps[bstack111lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨງ")][bstack111lll1_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫຈ")] = bstack11ll1ll11l_opy_
  except Exception as error:
    logger.debug(bstack111lll1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ࠱ࠤࡊࡸࡲࡰࡴ࠽ࠤࠧຉ") +  str(error))
def bstack1l1ll1lll_opy_(driver, bstack11lll111l1_opy_):
  try:
    session = driver.session_id
    if session:
      bstack11lll11l1l_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack11lll11l1l_opy_ = False
      bstack11lll11l1l_opy_ = url.scheme in [bstack111lll1_opy_ (u"ࠧ࡮ࡴࡵࡲࠥຊ"), bstack111lll1_opy_ (u"ࠨࡨࡵࡶࡳࡷࠧ຋")]
      if bstack11lll11l1l_opy_:
        if bstack11lll111l1_opy_:
          logger.info(bstack111lll1_opy_ (u"ࠢࡔࡧࡷࡹࡵࠦࡦࡰࡴࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡭ࡧࡳࠡࡵࡷࡥࡷࡺࡥࡥ࠰ࠣࡅࡺࡺ࡯࡮ࡣࡷࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡧࡻࡩࡨࡻࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡥࡩ࡬࡯࡮ࠡ࡯ࡲࡱࡪࡴࡴࡢࡴ࡬ࡰࡾ࠴ࠢຌ"))
          driver.execute_async_script(bstack111lll1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡨࡵ࡮ࡴࡶࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯ࠥࡃࠠࡢࡴࡪࡹࡲ࡫࡮ࡵࡵ࡞ࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠳ࡠ࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡩ࡯࡯ࡵࡷࠤ࡫ࡴࠠ࠾ࠢࠫ࠭ࠥࡃ࠾ࠡࡽࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡸ࡫ࡱࡨࡴࡽ࠮ࡢࡦࡧࡉࡻ࡫࡮ࡵࡎ࡬ࡷࡹ࡫࡮ࡦࡴࠫࠫࡆ࠷࠱࡚ࡡࡗࡅࡕࡥࡓࡕࡃࡕࡘࡊࡊࠧ࠭ࠢࡩࡲ࠷࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡩ࡯࡯ࡵࡷࠤࡪࠦ࠽ࠡࡰࡨࡻࠥࡉࡵࡴࡶࡲࡱࡊࡼࡥ࡯ࡶࠫࠫࡆ࠷࠱࡚ࡡࡉࡓࡗࡉࡅࡠࡕࡗࡅࡗ࡚ࠧࠪ࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡸ࡫ࡱࡨࡴࡽ࠮ࡥ࡫ࡶࡴࡦࡺࡣࡩࡇࡹࡩࡳࡺࠨࡦࠫ࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡤࡱࡱࡷࡹࠦࡦ࡯࠴ࠣࡁࠥ࠮ࠩࠡ࠿ࡁࠤࢀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡻ࡮ࡴࡤࡰࡹ࠱ࡶࡪࡳ࡯ࡷࡧࡈࡺࡪࡴࡴࡍ࡫ࡶࡸࡪࡴࡥࡳࠪࠪࡅ࠶࠷࡙ࡠࡖࡄࡔࡤ࡙ࡔࡂࡔࡗࡉࡉ࠭ࠬࠡࡨࡱ࠭ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯࠭࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡪࡳ࠮ࠩ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣຍ"))
          logger.info(bstack111lll1_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡦࡺࡨࡧࡺࡺࡩࡰࡰࠣ࡬ࡦࡹࠠࡴࡶࡤࡶࡹ࡫ࡤ࠯ࠤຎ"))
        else:
          driver.execute_script(bstack111lll1_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡣࡰࡰࡶࡸࠥ࡫ࠠ࠾ࠢࡱࡩࡼࠦࡃࡶࡵࡷࡳࡲࡋࡶࡦࡰࡷࠬࠬࡇ࠱࠲࡛ࡢࡊࡔࡘࡃࡆࡡࡖࡘࡔࡖࠧࠪ࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡻ࡮ࡴࡤࡰࡹ࠱ࡨ࡮ࡹࡰࡢࡶࡦ࡬ࡊࡼࡥ࡯ࡶࠫࡩ࠮ࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨຏ"))
      return bstack11lll111l1_opy_
  except Exception as e:
    logger.error(bstack111lll1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡹࡧࡲࡵ࡫ࡱ࡫ࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩ࠿ࠦࠢຐ") + str(e))
    return False
def bstack111lll11_opy_(driver, class_name, name, module_name, path, bstack1lll1ll1l_opy_):
  try:
    bstack11llll1l11_opy_ = [class_name] if not class_name is None else []
    bstack11lll11lll_opy_ = {
        bstack111lll1_opy_ (u"ࠧࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠥຑ"): True,
        bstack111lll1_opy_ (u"ࠨࡴࡦࡵࡷࡈࡪࡺࡡࡪ࡮ࡶࠦຒ"): {
            bstack111lll1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧຓ"): name,
            bstack111lll1_opy_ (u"ࠣࡶࡨࡷࡹࡘࡵ࡯ࡋࡧࠦດ"): os.environ.get(bstack111lll1_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡘࡊ࡙ࡔࡠࡔࡘࡒࡤࡏࡄࠨຕ")),
            bstack111lll1_opy_ (u"ࠥࡪ࡮ࡲࡥࡑࡣࡷ࡬ࠧຖ"): str(path),
            bstack111lll1_opy_ (u"ࠦࡸࡩ࡯ࡱࡧࡏ࡭ࡸࡺࠢທ"): [module_name, *bstack11llll1l11_opy_, name],
        },
        bstack111lll1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࠢຘ"): _11lll1l11l_opy_(driver, bstack1lll1ll1l_opy_)
    }
    driver.execute_async_script(bstack111lll1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡧࡴࡴࡳࡵࠢࡦࡥࡱࡲࡢࡢࡥ࡮ࠤࡂࠦࡡࡳࡩࡸࡱࡪࡴࡴࡴ࡝ࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠲࡟࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡺࡨࡪࡵ࠱ࡶࡪࡹࠠ࠾ࠢࡱࡹࡱࡲ࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢ࡬ࡪࠥ࠮ࡡࡳࡩࡸࡱࡪࡴࡴࡴ࡝࠳ࡡ࠳ࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠬࠤࢀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡼ࡯࡮ࡥࡱࡺ࠲ࡦࡪࡤࡆࡸࡨࡲࡹࡒࡩࡴࡶࡨࡲࡪࡸࠨࠨࡃ࠴࠵࡞ࡥࡔࡂࡒࡢࡘࡗࡇࡎࡔࡒࡒࡖ࡙ࡋࡒࠨ࠮ࠣࠬࡪࡼࡥ࡯ࡶࠬࠤࡂࡄࠠࡼࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡼ࡯࡮ࡥࡱࡺ࠲ࡹࡧࡰࡕࡴࡤࡲࡸࡶ࡯ࡳࡶࡨࡶࡉࡧࡴࡢࠢࡀࠤࡪࡼࡥ࡯ࡶ࠱ࡨࡪࡺࡡࡪ࡮࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡴࡩ࡫ࡶ࠲ࡷ࡫ࡳࠡ࠿ࠣࡻ࡮ࡴࡤࡰࡹ࠱ࡸࡦࡶࡔࡳࡣࡱࡷࡵࡵࡲࡵࡧࡵࡈࡦࡺࡡ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡨࡧ࡬࡭ࡤࡤࡧࡰ࠮ࡴࡩ࡫ࡶ࠲ࡷ࡫ࡳࠪ࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿࠬ࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡽࠋࠢࠣࠤࠥࠦࠠࠡࠢࡦࡳࡳࡹࡴࠡࡧࠣࡁࠥࡴࡥࡸࠢࡆࡹࡸࡺ࡯࡮ࡇࡹࡩࡳࡺࠨࠨࡃ࠴࠵࡞ࡥࡔࡆࡕࡗࡣࡊࡔࡄࠨ࠮ࠣࡿࠥࡪࡥࡵࡣ࡬ࡰ࠿ࠦࡡࡳࡩࡸࡱࡪࡴࡴࡴ࡝࠳ࡡࠥࢃࠩ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡻ࡮ࡴࡤࡰࡹ࠱ࡨ࡮ࡹࡰࡢࡶࡦ࡬ࡊࡼࡥ࡯ࡶࠫࡩ࠮ࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡩࠤ࠭ࠧࡡࡳࡩࡸࡱࡪࡴࡴࡴ࡝࠳ࡡ࠳ࡹࡡࡷࡧࡕࡩࡸࡻ࡬ࡵࡵࠬࠤࢀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡨࡧ࡬࡭ࡤࡤࡧࡰ࠮ࠩ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࢁࠏࠦࠠࠡࠢࠥࠦࠧນ"), bstack11lll11lll_opy_)
    logger.info(bstack111lll1_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡵࡧࡶࡸ࡮ࡴࡧࠡࡨࡲࡶࠥࡺࡨࡪࡵࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡨࡢࡵࠣࡩࡳࡪࡥࡥ࠰ࠥບ"))
  except Exception as bstack11lll11111_opy_:
    logger.error(bstack111lll1_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴࠢࡦࡳࡺࡲࡤࠡࡰࡲࡸࠥࡨࡥࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡧࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥ࠻ࠢࠥປ") + str(path) + bstack111lll1_opy_ (u"ࠤࠣࡉࡷࡸ࡯ࡳࠢ࠽ࠦຜ") + str(bstack11lll11111_opy_))