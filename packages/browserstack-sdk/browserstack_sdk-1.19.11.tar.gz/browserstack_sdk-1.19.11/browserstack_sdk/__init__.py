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
import atexit
import os
import signal
import sys
import yaml
import requests
import logging
import threading
import socket
import datetime
import string
import random
import json
import collections.abc
import re
import multiprocessing
import traceback
import copy
import tempfile
from packaging import version
from browserstack.local import Local
from urllib.parse import urlparse
from bstack_utils.constants import *
from bstack_utils.percy import *
from browserstack_sdk.bstack11llll1l_opy_ import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack1lll1ll11_opy_ import bstack11ll11l1_opy_
import time
import requests
def bstack1ll1l1llll_opy_():
  global CONFIG
  headers = {
        bstack111lll1_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩࡶ"): bstack111lll1_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧࡷ"),
      }
  proxies = bstack1l1l11llll_opy_(CONFIG, bstack1ll1ll11ll_opy_)
  try:
    response = requests.get(bstack1ll1ll11ll_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1111lll11_opy_ = response.json()[bstack111lll1_opy_ (u"ࠬ࡮ࡵࡣࡵࠪࡸ")]
      logger.debug(bstack1llll111l_opy_.format(response.json()))
      return bstack1111lll11_opy_
    else:
      logger.debug(bstack1ll1l11l_opy_.format(bstack111lll1_opy_ (u"ࠨࡒࡦࡵࡳࡳࡳࡹࡥࠡࡌࡖࡓࡓࠦࡰࡢࡴࡶࡩࠥ࡫ࡲࡳࡱࡵࠤࠧࡹ")))
  except Exception as e:
    logger.debug(bstack1ll1l11l_opy_.format(e))
def bstack111111111_opy_(hub_url):
  global CONFIG
  url = bstack111lll1_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤࡺ")+  hub_url + bstack111lll1_opy_ (u"ࠣ࠱ࡦ࡬ࡪࡩ࡫ࠣࡻ")
  headers = {
        bstack111lll1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨࡼ"): bstack111lll1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ࡽ"),
      }
  proxies = bstack1l1l11llll_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack11lll1111_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack11ll1llll_opy_.format(hub_url, e))
def bstack1l1l1lllll_opy_():
  try:
    global bstack1llll11lll_opy_
    bstack1111lll11_opy_ = bstack1ll1l1llll_opy_()
    bstack1lll1l1l_opy_ = []
    results = []
    for bstack11lll1l1l_opy_ in bstack1111lll11_opy_:
      bstack1lll1l1l_opy_.append(bstack1llll1ll1l_opy_(target=bstack111111111_opy_,args=(bstack11lll1l1l_opy_,)))
    for t in bstack1lll1l1l_opy_:
      t.start()
    for t in bstack1lll1l1l_opy_:
      results.append(t.join())
    bstack1l1l1l1lll_opy_ = {}
    for item in results:
      hub_url = item[bstack111lll1_opy_ (u"ࠫ࡭ࡻࡢࡠࡷࡵࡰࠬࡾ")]
      latency = item[bstack111lll1_opy_ (u"ࠬࡲࡡࡵࡧࡱࡧࡾ࠭ࡿ")]
      bstack1l1l1l1lll_opy_[hub_url] = latency
    bstack111ll1l1l_opy_ = min(bstack1l1l1l1lll_opy_, key= lambda x: bstack1l1l1l1lll_opy_[x])
    bstack1llll11lll_opy_ = bstack111ll1l1l_opy_
    logger.debug(bstack1ll1ll111_opy_.format(bstack111ll1l1l_opy_))
  except Exception as e:
    logger.debug(bstack11l11ll1_opy_.format(e))
from bstack_utils.messages import *
from bstack_utils.config import Config
from bstack_utils.helper import bstack1l1111111_opy_, bstack11ll111l_opy_, bstack1ll1111111_opy_, bstack1ll1l1l1l1_opy_, \
  Notset, bstack1llll1l1ll_opy_, \
  bstack1llll111_opy_, bstack111lllll1_opy_, bstack1l1llllll1_opy_, bstack1lll11l1ll_opy_, bstack1l1111ll1_opy_, bstack1lllllll1_opy_, \
  bstack1111lll1_opy_, \
  bstack1ll11111ll_opy_, bstack1l1l111lll_opy_, bstack1l1l1llll_opy_, bstack1l11111ll_opy_, \
  bstack1l1llllll_opy_, bstack1l1lllll1l_opy_, bstack1lllll111l_opy_
from bstack_utils.bstack1l1l1ll11l_opy_ import bstack111l1l1l_opy_
from bstack_utils.bstack11l1111ll_opy_ import bstack111l1l1l1_opy_
from bstack_utils.bstack111l11l11_opy_ import bstack1l11ll11_opy_, bstack1lll11l11_opy_
from bstack_utils.bstack111l1111l_opy_ import bstack1llll11l1_opy_
from bstack_utils.proxy import bstack1llll1l11_opy_, bstack1l1l11llll_opy_, bstack1l1lll11l_opy_, bstack11llllll_opy_
import bstack_utils.bstack1l1l1lll11_opy_ as bstack1lllll1111_opy_
from browserstack_sdk.bstack1l111l11_opy_ import *
from browserstack_sdk.bstack1lll1111_opy_ import *
from bstack_utils.bstack11l1lll11_opy_ import bstack1ll1l11111_opy_
bstack1lll11111_opy_ = bstack111lll1_opy_ (u"࠭ࠠࠡ࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࡠࡳࠦࠠࡪࡨࠫࡴࡦ࡭ࡥࠡ࠿ࡀࡁࠥࡼ࡯ࡪࡦࠣ࠴࠮ࠦࡻ࡝ࡰࠣࠤࠥࡺࡲࡺࡽ࡟ࡲࠥࡩ࡯࡯ࡵࡷࠤ࡫ࡹࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࡠࠬ࡬ࡳ࡝ࠩࠬ࠿ࡡࡴࠠࠡࠢࠣࠤ࡫ࡹ࠮ࡢࡲࡳࡩࡳࡪࡆࡪ࡮ࡨࡗࡾࡴࡣࠩࡤࡶࡸࡦࡩ࡫ࡠࡲࡤࡸ࡭࠲ࠠࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡲࡢ࡭ࡳࡪࡥࡹࠫࠣ࠯ࠥࠨ࠺ࠣࠢ࠮ࠤࡏ࡙ࡏࡏ࠰ࡶࡸࡷ࡯࡮ࡨ࡫ࡩࡽ࠭ࡐࡓࡐࡐ࠱ࡴࡦࡸࡳࡦࠪࠫࡥࡼࡧࡩࡵࠢࡱࡩࡼࡖࡡࡨࡧ࠵࠲ࡪࡼࡡ࡭ࡷࡤࡸࡪ࠮ࠢࠩࠫࠣࡁࡃࠦࡻࡾࠤ࠯ࠤࡡ࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡧࡦࡶࡖࡩࡸࡹࡩࡰࡰࡇࡩࡹࡧࡩ࡭ࡵࠥࢁࡡ࠭ࠩࠪࠫ࡞ࠦ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠢ࡞ࠫࠣ࠯ࠥࠨࠬ࡝࡞ࡱࠦ࠮ࡢ࡮ࠡࠢࠣࠤࢂࡩࡡࡵࡥ࡫ࠬࡪࡾࠩࡼ࡞ࡱࠤࠥࠦࠠࡾ࡞ࡱࠤࠥࢃ࡜࡯ࠢࠣ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴࠭ࢀ")
bstack11ll1l11_opy_ = bstack111lll1_opy_ (u"ࠧ࡝ࡰ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࡡࡴࡣࡰࡰࡶࡸࠥࡨࡳࡵࡣࡦ࡯ࡤࡶࡡࡵࡪࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠹࡝࡝ࡰࡦࡳࡳࡹࡴࠡࡤࡶࡸࡦࡩ࡫ࡠࡥࡤࡴࡸࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠳ࡠࡠࡳࡩ࡯࡯ࡵࡷࠤࡵࡥࡩ࡯ࡦࡨࡼࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠳࡟࡟ࡲࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡸࡲࡩࡤࡧࠫ࠴࠱ࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠴ࠫ࡟ࡲࡨࡵ࡮ࡴࡶࠣ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫ࠡ࠿ࠣࡶࡪࡷࡵࡪࡴࡨࠬࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤࠬ࠿ࡡࡴࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮࠲ࡨ࡮ࡲࡰ࡯࡬ࡹࡲ࠴࡬ࡢࡷࡱࡧ࡭ࠦ࠽ࠡࡣࡶࡽࡳࡩࠠࠩ࡮ࡤࡹࡳࡩࡨࡐࡲࡷ࡭ࡴࡴࡳࠪࠢࡀࡂࠥࢁ࡜࡯࡮ࡨࡸࠥࡩࡡࡱࡵ࠾ࡠࡳࡺࡲࡺࠢࡾࡠࡳࡩࡡࡱࡵࠣࡁࠥࡐࡓࡐࡐ࠱ࡴࡦࡸࡳࡦࠪࡥࡷࡹࡧࡣ࡬ࡡࡦࡥࡵࡹࠩ࡝ࡰࠣࠤࢂࠦࡣࡢࡶࡦ࡬࠭࡫ࡸࠪࠢࡾࡠࡳࠦࠠࠡࠢࢀࡠࡳࠦࠠࡳࡧࡷࡹࡷࡴࠠࡢࡹࡤ࡭ࡹࠦࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮࠲ࡨ࡮ࡲࡰ࡯࡬ࡹࡲ࠴ࡣࡰࡰࡱࡩࡨࡺࠨࡼ࡞ࡱࠤࠥࠦࠠࡸࡵࡈࡲࡩࡶ࡯ࡪࡰࡷ࠾ࠥࡦࡷࡴࡵ࠽࠳࠴ࡩࡤࡱ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࡁࡦࡥࡵࡹ࠽ࠥࡽࡨࡲࡨࡵࡤࡦࡗࡕࡍࡈࡵ࡭ࡱࡱࡱࡩࡳࡺࠨࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡥࡤࡴࡸ࠯ࠩࡾࡢ࠯ࡠࡳࠦࠠࠡࠢ࠱࠲࠳ࡲࡡࡶࡰࡦ࡬ࡔࡶࡴࡪࡱࡱࡷࡡࡴࠠࠡࡿࠬࡠࡳࢃ࡜࡯࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࡠࡳ࠭ࢁ")
from ._version import __version__
bstack111l11ll_opy_ = None
CONFIG = {}
bstack1ll111l1l1_opy_ = {}
bstack1llll1l11l_opy_ = {}
bstack1ll1111l11_opy_ = None
bstack111ll1l11_opy_ = None
bstack1l1lll1l11_opy_ = None
bstack1ll111lll1_opy_ = -1
bstack1111111l_opy_ = 0
bstack11l1ll11l_opy_ = bstack11111l1l_opy_
bstack1111l11ll_opy_ = 1
bstack11l1l11ll_opy_ = False
bstack1lll1ll11l_opy_ = False
bstack1llll11l11_opy_ = bstack111lll1_opy_ (u"ࠨࠩࢂ")
bstack1111l1l1l_opy_ = bstack111lll1_opy_ (u"ࠩࠪࢃ")
bstack1ll1l1l11l_opy_ = False
bstack1ll1ll1ll_opy_ = True
bstack111ll1ll_opy_ = bstack111lll1_opy_ (u"ࠪࠫࢄ")
bstack1lllllllll_opy_ = []
bstack1llll11lll_opy_ = bstack111lll1_opy_ (u"ࠫࠬࢅ")
bstack11lllll1l_opy_ = False
bstack1l11ll1l1_opy_ = None
bstack111lll11l_opy_ = None
bstack1l1l1l1111_opy_ = None
bstack111l11111_opy_ = -1
bstack1l1l1l11l1_opy_ = os.path.join(os.path.expanduser(bstack111lll1_opy_ (u"ࠬࢄࠧࢆ")), bstack111lll1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ࢇ"), bstack111lll1_opy_ (u"ࠧ࠯ࡴࡲࡦࡴࡺ࠭ࡳࡧࡳࡳࡷࡺ࠭ࡩࡧ࡯ࡴࡪࡸ࠮࡫ࡵࡲࡲࠬ࢈"))
bstack1lll11lll_opy_ = 0
bstack1l1ll11l_opy_ = []
bstack1llllll11l_opy_ = []
bstack11l1l1lll_opy_ = []
bstack1l11lllll_opy_ = []
bstack11l1lllll_opy_ = bstack111lll1_opy_ (u"ࠨࠩࢉ")
bstack1ll1l111ll_opy_ = bstack111lll1_opy_ (u"ࠩࠪࢊ")
bstack11l11lll_opy_ = False
bstack111llll1_opy_ = False
bstack11l1l1l1_opy_ = {}
bstack11ll1lll_opy_ = None
bstack1llll1l111_opy_ = None
bstack1l1llll11l_opy_ = None
bstack1l1ll1l1l1_opy_ = None
bstack11l111l11_opy_ = None
bstack1llll111l1_opy_ = None
bstack111l11l1l_opy_ = None
bstack1ll1lllll_opy_ = None
bstack111111l11_opy_ = None
bstack11l11111l_opy_ = None
bstack1111llll_opy_ = None
bstack1lllll11l1_opy_ = None
bstack1l11llll1_opy_ = None
bstack1lll1l1l1l_opy_ = None
bstack1ll11l1l1_opy_ = None
bstack1llllll1l1_opy_ = None
bstack11111llll_opy_ = None
bstack1l11l11l_opy_ = None
bstack1111lllll_opy_ = None
bstack11ll1ll1_opy_ = None
bstack1l1l11l1ll_opy_ = None
bstack1lll1lll_opy_ = bstack111lll1_opy_ (u"ࠥࠦࢋ")
logger = logging.getLogger(__name__)
logging.basicConfig(level=bstack11l1ll11l_opy_,
                    format=bstack111lll1_opy_ (u"ࠫࡡࡴࠥࠩࡣࡶࡧࡹ࡯࡭ࡦࠫࡶࠤࡠࠫࠨ࡯ࡣࡰࡩ࠮ࡹ࡝࡜ࠧࠫࡰࡪࡼࡥ࡭ࡰࡤࡱࡪ࠯ࡳ࡞ࠢ࠰ࠤࠪ࠮࡭ࡦࡵࡶࡥ࡬࡫ࠩࡴࠩࢌ"),
                    datefmt=bstack111lll1_opy_ (u"ࠬࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧࢍ"),
                    stream=sys.stdout)
bstack11l11l111_opy_ = Config.bstack111l1ll1_opy_()
percy = bstack1ll1l1lll1_opy_()
bstack1lll1111ll_opy_ = bstack11ll11l1_opy_()
def bstack1ll11l11l_opy_():
  global CONFIG
  global bstack11l1ll11l_opy_
  if bstack111lll1_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨࢎ") in CONFIG:
    bstack11l1ll11l_opy_ = bstack1l1ll1ll_opy_[CONFIG[bstack111lll1_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩ࢏")]]
    logging.getLogger().setLevel(bstack11l1ll11l_opy_)
def bstack1l11111l_opy_():
  global CONFIG
  global bstack11l11lll_opy_
  global bstack11l11l111_opy_
  bstack1111ll11l_opy_ = bstack111lll111_opy_(CONFIG)
  if (bstack111lll1_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ࢐") in bstack1111ll11l_opy_ and str(bstack1111ll11l_opy_[bstack111lll1_opy_ (u"ࠩࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ࢑")]).lower() == bstack111lll1_opy_ (u"ࠪࡸࡷࡻࡥࠨ࢒")):
    bstack11l11lll_opy_ = True
  bstack11l11l111_opy_.bstack111l1llll_opy_(bstack1111ll11l_opy_.get(bstack111lll1_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ࢓"), False))
def bstack1ll11l1l11_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack1lll1l11l_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1lllll1lll_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack111lll1_opy_ (u"ࠧ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡩ࡯࡯ࡨ࡬࡫࡫࡯࡬ࡦࠤ࢔") == args[i].lower() or bstack111lll1_opy_ (u"ࠨ࠭࠮ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡱࡪ࡮࡭ࠢ࢕") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack111ll1ll_opy_
      bstack111ll1ll_opy_ += bstack111lll1_opy_ (u"ࠧ࠮࠯ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡄࡱࡱࡪ࡮࡭ࡆࡪ࡮ࡨࠤࠬ࢖") + path
      return path
  return None
bstack11l1l1ll1_opy_ = re.compile(bstack111lll1_opy_ (u"ࡳࠤ࠱࠮ࡄࡢࠤࡼࠪ࠱࠮ࡄ࠯ࡽ࠯ࠬࡂࠦࢗ"))
def bstack1ll1l1ll11_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack11l1l1ll1_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack111lll1_opy_ (u"ࠤࠧࡿࠧ࢘") + group + bstack111lll1_opy_ (u"ࠥࢁ࢙ࠧ"), os.environ.get(group))
  return value
def bstack1ll111l1_opy_():
  bstack111ll11l1_opy_ = bstack1lllll1lll_opy_()
  if bstack111ll11l1_opy_ and os.path.exists(os.path.abspath(bstack111ll11l1_opy_)):
    fileName = bstack111ll11l1_opy_
  if bstack111lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࡢࡊࡎࡒࡅࠨ࢚") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack111lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࡣࡋࡏࡌࡆ࢛ࠩ")])) and not bstack111lll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡒࡦࡳࡥࠨ࢜") in locals():
    fileName = os.environ[bstack111lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌࡥࡆࡊࡎࡈࠫ࢝")]
  if bstack111lll1_opy_ (u"ࠨࡨ࡬ࡰࡪࡔࡡ࡮ࡧࠪ࢞") in locals():
    bstack11ll1ll_opy_ = os.path.abspath(fileName)
  else:
    bstack11ll1ll_opy_ = bstack111lll1_opy_ (u"ࠩࠪ࢟")
  bstack1llllll1ll_opy_ = os.getcwd()
  bstack1lll111l_opy_ = bstack111lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭ࢠ")
  bstack1l1lll111_opy_ = bstack111lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡦࡳ࡬ࠨࢡ")
  while (not os.path.exists(bstack11ll1ll_opy_)) and bstack1llllll1ll_opy_ != bstack111lll1_opy_ (u"ࠧࠨࢢ"):
    bstack11ll1ll_opy_ = os.path.join(bstack1llllll1ll_opy_, bstack1lll111l_opy_)
    if not os.path.exists(bstack11ll1ll_opy_):
      bstack11ll1ll_opy_ = os.path.join(bstack1llllll1ll_opy_, bstack1l1lll111_opy_)
    if bstack1llllll1ll_opy_ != os.path.dirname(bstack1llllll1ll_opy_):
      bstack1llllll1ll_opy_ = os.path.dirname(bstack1llllll1ll_opy_)
    else:
      bstack1llllll1ll_opy_ = bstack111lll1_opy_ (u"ࠨࠢࢣ")
  if not os.path.exists(bstack11ll1ll_opy_):
    bstack1ll1lll111_opy_(
      bstack111l1l11_opy_.format(os.getcwd()))
  try:
    with open(bstack11ll1ll_opy_, bstack111lll1_opy_ (u"ࠧࡳࠩࢤ")) as stream:
      yaml.add_implicit_resolver(bstack111lll1_opy_ (u"ࠣࠣࡳࡥࡹ࡮ࡥࡹࠤࢥ"), bstack11l1l1ll1_opy_)
      yaml.add_constructor(bstack111lll1_opy_ (u"ࠤࠤࡴࡦࡺࡨࡦࡺࠥࢦ"), bstack1ll1l1ll11_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      return config
  except:
    with open(bstack11ll1ll_opy_, bstack111lll1_opy_ (u"ࠪࡶࠬࢧ")) as stream:
      try:
        config = yaml.safe_load(stream)
        return config
      except yaml.YAMLError as exc:
        bstack1ll1lll111_opy_(bstack11l1lll1_opy_.format(str(exc)))
def bstack11l1l111l_opy_(config):
  bstack11l1l11l_opy_ = bstack1111ll11_opy_(config)
  for option in list(bstack11l1l11l_opy_):
    if option.lower() in bstack1lll1ll111_opy_ and option != bstack1lll1ll111_opy_[option.lower()]:
      bstack11l1l11l_opy_[bstack1lll1ll111_opy_[option.lower()]] = bstack11l1l11l_opy_[option]
      del bstack11l1l11l_opy_[option]
  return config
def bstack11l111ll_opy_():
  global bstack1llll1l11l_opy_
  for key, bstack1l11l11ll_opy_ in bstack111l1ll1l_opy_.items():
    if isinstance(bstack1l11l11ll_opy_, list):
      for var in bstack1l11l11ll_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack1llll1l11l_opy_[key] = os.environ[var]
          break
    elif bstack1l11l11ll_opy_ in os.environ and os.environ[bstack1l11l11ll_opy_] and str(os.environ[bstack1l11l11ll_opy_]).strip():
      bstack1llll1l11l_opy_[key] = os.environ[bstack1l11l11ll_opy_]
  if bstack111lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ࢨ") in os.environ:
    bstack1llll1l11l_opy_[bstack111lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩࢩ")] = {}
    bstack1llll1l11l_opy_[bstack111lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪࢪ")][bstack111lll1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩࢫ")] = os.environ[bstack111lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪࢬ")]
def bstack1l1ll11l1_opy_():
  global bstack1ll111l1l1_opy_
  global bstack111ll1ll_opy_
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) and bstack111lll1_opy_ (u"ࠩ࠰࠱ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬࢭ").lower() == val.lower():
      bstack1ll111l1l1_opy_[bstack111lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧࢮ")] = {}
      bstack1ll111l1l1_opy_[bstack111lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨࢯ")][bstack111lll1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࢰ")] = sys.argv[idx + 1]
      del sys.argv[idx:idx + 2]
      break
  for key, bstack1111l1l1_opy_ in bstack11l1l1l11_opy_.items():
    if isinstance(bstack1111l1l1_opy_, list):
      for idx, val in enumerate(sys.argv):
        for var in bstack1111l1l1_opy_:
          if idx < len(sys.argv) and bstack111lll1_opy_ (u"࠭࠭࠮ࠩࢱ") + var.lower() == val.lower() and not key in bstack1ll111l1l1_opy_:
            bstack1ll111l1l1_opy_[key] = sys.argv[idx + 1]
            bstack111ll1ll_opy_ += bstack111lll1_opy_ (u"ࠧࠡ࠯࠰ࠫࢲ") + var + bstack111lll1_opy_ (u"ࠨࠢࠪࢳ") + sys.argv[idx + 1]
            del sys.argv[idx:idx + 2]
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx < len(sys.argv) and bstack111lll1_opy_ (u"ࠩ࠰࠱ࠬࢴ") + bstack1111l1l1_opy_.lower() == val.lower() and not key in bstack1ll111l1l1_opy_:
          bstack1ll111l1l1_opy_[key] = sys.argv[idx + 1]
          bstack111ll1ll_opy_ += bstack111lll1_opy_ (u"ࠪࠤ࠲࠳ࠧࢵ") + bstack1111l1l1_opy_ + bstack111lll1_opy_ (u"ࠫࠥ࠭ࢶ") + sys.argv[idx + 1]
          del sys.argv[idx:idx + 2]
def bstack1lll1l1111_opy_(config):
  bstack1lll1l111_opy_ = config.keys()
  for bstack1lll111111_opy_, bstack1ll11ll111_opy_ in bstack1llll1lll_opy_.items():
    if bstack1ll11ll111_opy_ in bstack1lll1l111_opy_:
      config[bstack1lll111111_opy_] = config[bstack1ll11ll111_opy_]
      del config[bstack1ll11ll111_opy_]
  for bstack1lll111111_opy_, bstack1ll11ll111_opy_ in bstack1ll111ll1l_opy_.items():
    if isinstance(bstack1ll11ll111_opy_, list):
      for bstack1l1ll11ll_opy_ in bstack1ll11ll111_opy_:
        if bstack1l1ll11ll_opy_ in bstack1lll1l111_opy_:
          config[bstack1lll111111_opy_] = config[bstack1l1ll11ll_opy_]
          del config[bstack1l1ll11ll_opy_]
          break
    elif bstack1ll11ll111_opy_ in bstack1lll1l111_opy_:
      config[bstack1lll111111_opy_] = config[bstack1ll11ll111_opy_]
      del config[bstack1ll11ll111_opy_]
  for bstack1l1ll11ll_opy_ in list(config):
    for bstack11ll11l1l_opy_ in bstack1lll11ll1l_opy_:
      if bstack1l1ll11ll_opy_.lower() == bstack11ll11l1l_opy_.lower() and bstack1l1ll11ll_opy_ != bstack11ll11l1l_opy_:
        config[bstack11ll11l1l_opy_] = config[bstack1l1ll11ll_opy_]
        del config[bstack1l1ll11ll_opy_]
  bstack11llll1ll_opy_ = []
  if bstack111lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨࢷ") in config:
    bstack11llll1ll_opy_ = config[bstack111lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩࢸ")]
  for platform in bstack11llll1ll_opy_:
    for bstack1l1ll11ll_opy_ in list(platform):
      for bstack11ll11l1l_opy_ in bstack1lll11ll1l_opy_:
        if bstack1l1ll11ll_opy_.lower() == bstack11ll11l1l_opy_.lower() and bstack1l1ll11ll_opy_ != bstack11ll11l1l_opy_:
          platform[bstack11ll11l1l_opy_] = platform[bstack1l1ll11ll_opy_]
          del platform[bstack1l1ll11ll_opy_]
  for bstack1lll111111_opy_, bstack1ll11ll111_opy_ in bstack1ll111ll1l_opy_.items():
    for platform in bstack11llll1ll_opy_:
      if isinstance(bstack1ll11ll111_opy_, list):
        for bstack1l1ll11ll_opy_ in bstack1ll11ll111_opy_:
          if bstack1l1ll11ll_opy_ in platform:
            platform[bstack1lll111111_opy_] = platform[bstack1l1ll11ll_opy_]
            del platform[bstack1l1ll11ll_opy_]
            break
      elif bstack1ll11ll111_opy_ in platform:
        platform[bstack1lll111111_opy_] = platform[bstack1ll11ll111_opy_]
        del platform[bstack1ll11ll111_opy_]
  for bstack1111l11l1_opy_ in bstack1lll11l1_opy_:
    if bstack1111l11l1_opy_ in config:
      if not bstack1lll11l1_opy_[bstack1111l11l1_opy_] in config:
        config[bstack1lll11l1_opy_[bstack1111l11l1_opy_]] = {}
      config[bstack1lll11l1_opy_[bstack1111l11l1_opy_]].update(config[bstack1111l11l1_opy_])
      del config[bstack1111l11l1_opy_]
  for platform in bstack11llll1ll_opy_:
    for bstack1111l11l1_opy_ in bstack1lll11l1_opy_:
      if bstack1111l11l1_opy_ in list(platform):
        if not bstack1lll11l1_opy_[bstack1111l11l1_opy_] in platform:
          platform[bstack1lll11l1_opy_[bstack1111l11l1_opy_]] = {}
        platform[bstack1lll11l1_opy_[bstack1111l11l1_opy_]].update(platform[bstack1111l11l1_opy_])
        del platform[bstack1111l11l1_opy_]
  config = bstack11l1l111l_opy_(config)
  return config
def bstack1llll1111l_opy_(config):
  global bstack1111l1l1l_opy_
  if bstack111lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫࢹ") in config and str(config[bstack111lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬࢺ")]).lower() != bstack111lll1_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨࢻ"):
    if not bstack111lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧࢼ") in config:
      config[bstack111lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨࢽ")] = {}
    if not bstack111lll1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࢾ") in config[bstack111lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪࢿ")]:
      bstack1ll1l11lll_opy_ = datetime.datetime.now()
      bstack11lll1ll_opy_ = bstack1ll1l11lll_opy_.strftime(bstack111lll1_opy_ (u"ࠧࠦࡦࡢࠩࡧࡥࠥࡉࠧࡐࠫࣀ"))
      hostname = socket.gethostname()
      bstack1l1ll1111_opy_ = bstack111lll1_opy_ (u"ࠨࠩࣁ").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack111lll1_opy_ (u"ࠩࡾࢁࡤࢁࡽࡠࡽࢀࠫࣂ").format(bstack11lll1ll_opy_, hostname, bstack1l1ll1111_opy_)
      config[bstack111lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧࣃ")][bstack111lll1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ࣄ")] = identifier
    bstack1111l1l1l_opy_ = config[bstack111lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩࣅ")][bstack111lll1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨࣆ")]
  return config
def bstack111l11ll1_opy_():
  bstack1ll1lllll1_opy_ =  bstack1lll11l1ll_opy_()[bstack111lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷ࠭ࣇ")]
  return bstack1ll1lllll1_opy_ if bstack1ll1lllll1_opy_ else -1
def bstack1l1ll1ll1l_opy_(bstack1ll1lllll1_opy_):
  global CONFIG
  if not bstack111lll1_opy_ (u"ࠨࠦࡾࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࡿࠪࣈ") in CONFIG[bstack111lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫࣉ")]:
    return
  CONFIG[bstack111lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ࣊")] = CONFIG[bstack111lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭࣋")].replace(
    bstack111lll1_opy_ (u"ࠬࠪࡻࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࢃࠧ࣌"),
    str(bstack1ll1lllll1_opy_)
  )
def bstack11111lll_opy_():
  global CONFIG
  if not bstack111lll1_opy_ (u"࠭ࠤࡼࡆࡄࡘࡊࡥࡔࡊࡏࡈࢁࠬ࣍") in CONFIG[bstack111lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ࣎")]:
    return
  bstack1ll1l11lll_opy_ = datetime.datetime.now()
  bstack11lll1ll_opy_ = bstack1ll1l11lll_opy_.strftime(bstack111lll1_opy_ (u"ࠨࠧࡧ࠱ࠪࡨ࠭ࠦࡊ࠽ࠩࡒ࣏࠭"))
  CONFIG[bstack111lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵ࣐ࠫ")] = CONFIG[bstack111lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶ࣑ࠬ")].replace(
    bstack111lll1_opy_ (u"ࠫࠩࢁࡄࡂࡖࡈࡣ࡙ࡏࡍࡆࡿ࣒ࠪ"),
    bstack11lll1ll_opy_
  )
def bstack1lllll111_opy_():
  global CONFIG
  if bstack111lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸ࣓ࠧ") in CONFIG and not bool(CONFIG[bstack111lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨࣔ")]):
    del CONFIG[bstack111lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩࣕ")]
    return
  if not bstack111lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࣖ") in CONFIG:
    CONFIG[bstack111lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫࣗ")] = bstack111lll1_opy_ (u"ࠪࠧࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭ࣘ")
  if bstack111lll1_opy_ (u"ࠫࠩࢁࡄࡂࡖࡈࡣ࡙ࡏࡍࡆࡿࠪࣙ") in CONFIG[bstack111lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࣚ")]:
    bstack11111lll_opy_()
    os.environ[bstack111lll1_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡥࡃࡐࡏࡅࡍࡓࡋࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪࣛ")] = CONFIG[bstack111lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩࣜ")]
  if not bstack111lll1_opy_ (u"ࠨࠦࡾࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࡿࠪࣝ") in CONFIG[bstack111lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫࣞ")]:
    return
  bstack1ll1lllll1_opy_ = bstack111lll1_opy_ (u"ࠪࠫࣟ")
  bstack11lll111_opy_ = bstack111l11ll1_opy_()
  if bstack11lll111_opy_ != -1:
    bstack1ll1lllll1_opy_ = bstack111lll1_opy_ (u"ࠫࡈࡏࠠࠨ࣠") + str(bstack11lll111_opy_)
  if bstack1ll1lllll1_opy_ == bstack111lll1_opy_ (u"ࠬ࠭࣡"):
    bstack1l11ll111_opy_ = bstack1l1ll111l1_opy_(CONFIG[bstack111lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ࣢")])
    if bstack1l11ll111_opy_ != -1:
      bstack1ll1lllll1_opy_ = str(bstack1l11ll111_opy_)
  if bstack1ll1lllll1_opy_:
    bstack1l1ll1ll1l_opy_(bstack1ll1lllll1_opy_)
    os.environ[bstack111lll1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑ࡟ࡄࡑࡐࡆࡎࡔࡅࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࣣࠫ")] = CONFIG[bstack111lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࣤ")]
def bstack11l11l11_opy_(bstack1l1ll1l11_opy_, bstack111l111ll_opy_, path):
  bstack1l1llll1l_opy_ = {
    bstack111lll1_opy_ (u"ࠩ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ࣥ"): bstack111l111ll_opy_
  }
  if os.path.exists(path):
    bstack111llllll_opy_ = json.load(open(path, bstack111lll1_opy_ (u"ࠪࡶࡧࣦ࠭")))
  else:
    bstack111llllll_opy_ = {}
  bstack111llllll_opy_[bstack1l1ll1l11_opy_] = bstack1l1llll1l_opy_
  with open(path, bstack111lll1_opy_ (u"ࠦࡼ࠱ࠢࣧ")) as outfile:
    json.dump(bstack111llllll_opy_, outfile)
def bstack1l1ll111l1_opy_(bstack1l1ll1l11_opy_):
  bstack1l1ll1l11_opy_ = str(bstack1l1ll1l11_opy_)
  bstack1ll11llll_opy_ = os.path.join(os.path.expanduser(bstack111lll1_opy_ (u"ࠬࢄࠧࣨ")), bstack111lll1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࣩ࠭"))
  try:
    if not os.path.exists(bstack1ll11llll_opy_):
      os.makedirs(bstack1ll11llll_opy_)
    file_path = os.path.join(os.path.expanduser(bstack111lll1_opy_ (u"ࠧࡿࠩ࣪")), bstack111lll1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ࣫"), bstack111lll1_opy_ (u"ࠩ࠱ࡦࡺ࡯࡬ࡥ࠯ࡱࡥࡲ࡫࠭ࡤࡣࡦ࡬ࡪ࠴ࡪࡴࡱࡱࠫ࣬"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack111lll1_opy_ (u"ࠪࡻ࣭ࠬ")):
        pass
      with open(file_path, bstack111lll1_opy_ (u"ࠦࡼ࠱࣮ࠢ")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack111lll1_opy_ (u"ࠬࡸ࣯ࠧ")) as bstack1l1lllllll_opy_:
      bstack11111l11l_opy_ = json.load(bstack1l1lllllll_opy_)
    if bstack1l1ll1l11_opy_ in bstack11111l11l_opy_:
      bstack11lll1ll1_opy_ = bstack11111l11l_opy_[bstack1l1ll1l11_opy_][bstack111lll1_opy_ (u"࠭ࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࣰࠪ")]
      bstack1l1ll1l1ll_opy_ = int(bstack11lll1ll1_opy_) + 1
      bstack11l11l11_opy_(bstack1l1ll1l11_opy_, bstack1l1ll1l1ll_opy_, file_path)
      return bstack1l1ll1l1ll_opy_
    else:
      bstack11l11l11_opy_(bstack1l1ll1l11_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack1111l111l_opy_.format(str(e)))
    return -1
def bstack1ll11l1l_opy_(config):
  if not config[bstack111lll1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࣱࠩ")] or not config[bstack111lll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࣲࠫ")]:
    return True
  else:
    return False
def bstack1lll111l1_opy_(config, index=0):
  global bstack1ll1l1l11l_opy_
  bstack1ll1111l1_opy_ = {}
  caps = bstack1ll1llllll_opy_ + bstack1l1l11lll1_opy_
  if bstack1ll1l1l11l_opy_:
    caps += bstack111llll11_opy_
  for key in config:
    if key in caps + [bstack111lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬࣳ")]:
      continue
    bstack1ll1111l1_opy_[key] = config[key]
  if bstack111lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ࣴ") in config:
    for bstack1lllll1l1l_opy_ in config[bstack111lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧࣵ")][index]:
      if bstack1lllll1l1l_opy_ in caps + [bstack111lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࣶࠪ"), bstack111lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧࣷ")]:
        continue
      bstack1ll1111l1_opy_[bstack1lllll1l1l_opy_] = config[bstack111lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪࣸ")][index][bstack1lllll1l1l_opy_]
  bstack1ll1111l1_opy_[bstack111lll1_opy_ (u"ࠨࡪࡲࡷࡹࡔࡡ࡮ࡧࣹࠪ")] = socket.gethostname()
  if bstack111lll1_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࣺࠪ") in bstack1ll1111l1_opy_:
    del (bstack1ll1111l1_opy_[bstack111lll1_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫࣻ")])
  return bstack1ll1111l1_opy_
def bstack1l111l11l_opy_(config):
  global bstack1ll1l1l11l_opy_
  bstack11lll11ll_opy_ = {}
  caps = bstack1l1l11lll1_opy_
  if bstack1ll1l1l11l_opy_:
    caps += bstack111llll11_opy_
  for key in caps:
    if key in config:
      bstack11lll11ll_opy_[key] = config[key]
  return bstack11lll11ll_opy_
def bstack1l1l111l1_opy_(bstack1ll1111l1_opy_, bstack11lll11ll_opy_):
  bstack1l11lll1_opy_ = {}
  for key in bstack1ll1111l1_opy_.keys():
    if key in bstack1llll1lll_opy_:
      bstack1l11lll1_opy_[bstack1llll1lll_opy_[key]] = bstack1ll1111l1_opy_[key]
    else:
      bstack1l11lll1_opy_[key] = bstack1ll1111l1_opy_[key]
  for key in bstack11lll11ll_opy_:
    if key in bstack1llll1lll_opy_:
      bstack1l11lll1_opy_[bstack1llll1lll_opy_[key]] = bstack11lll11ll_opy_[key]
    else:
      bstack1l11lll1_opy_[key] = bstack11lll11ll_opy_[key]
  return bstack1l11lll1_opy_
def bstack11l11l1l1_opy_(config, index=0):
  global bstack1ll1l1l11l_opy_
  config = copy.deepcopy(config)
  caps = {}
  bstack11lll11ll_opy_ = bstack1l111l11l_opy_(config)
  bstack1l1llll1ll_opy_ = bstack1l1l11lll1_opy_
  bstack1l1llll1ll_opy_ += bstack1l1ll11l1l_opy_
  if bstack1ll1l1l11l_opy_:
    bstack1l1llll1ll_opy_ += bstack111llll11_opy_
  if bstack111lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧࣼ") in config:
    if bstack111lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪࣽ") in config[bstack111lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩࣾ")][index]:
      caps[bstack111lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬࣿ")] = config[bstack111lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫऀ")][index][bstack111lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧँ")]
    if bstack111lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫं") in config[bstack111lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧः")][index]:
      caps[bstack111lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ऄ")] = str(config[bstack111lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩअ")][index][bstack111lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨआ")])
    bstack11ll1ll1l_opy_ = {}
    for bstack1l1l1l111_opy_ in bstack1l1llll1ll_opy_:
      if bstack1l1l1l111_opy_ in config[bstack111lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫइ")][index]:
        if bstack1l1l1l111_opy_ == bstack111lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫई"):
          try:
            bstack11ll1ll1l_opy_[bstack1l1l1l111_opy_] = str(config[bstack111lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭उ")][index][bstack1l1l1l111_opy_] * 1.0)
          except:
            bstack11ll1ll1l_opy_[bstack1l1l1l111_opy_] = str(config[bstack111lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧऊ")][index][bstack1l1l1l111_opy_])
        else:
          bstack11ll1ll1l_opy_[bstack1l1l1l111_opy_] = config[bstack111lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨऋ")][index][bstack1l1l1l111_opy_]
        del (config[bstack111lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩऌ")][index][bstack1l1l1l111_opy_])
    bstack11lll11ll_opy_ = update(bstack11lll11ll_opy_, bstack11ll1ll1l_opy_)
  bstack1ll1111l1_opy_ = bstack1lll111l1_opy_(config, index)
  for bstack1l1ll11ll_opy_ in bstack1l1l11lll1_opy_ + [bstack111lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬऍ"), bstack111lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩऎ")]:
    if bstack1l1ll11ll_opy_ in bstack1ll1111l1_opy_:
      bstack11lll11ll_opy_[bstack1l1ll11ll_opy_] = bstack1ll1111l1_opy_[bstack1l1ll11ll_opy_]
      del (bstack1ll1111l1_opy_[bstack1l1ll11ll_opy_])
  if bstack1llll1l1ll_opy_(config):
    bstack1ll1111l1_opy_[bstack111lll1_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩए")] = True
    caps.update(bstack11lll11ll_opy_)
    caps[bstack111lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫऐ")] = bstack1ll1111l1_opy_
  else:
    bstack1ll1111l1_opy_[bstack111lll1_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫऑ")] = False
    caps.update(bstack1l1l111l1_opy_(bstack1ll1111l1_opy_, bstack11lll11ll_opy_))
    if bstack111lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪऒ") in caps:
      caps[bstack111lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧओ")] = caps[bstack111lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬऔ")]
      del (caps[bstack111lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭क")])
    if bstack111lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪख") in caps:
      caps[bstack111lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬग")] = caps[bstack111lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬघ")]
      del (caps[bstack111lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ङ")])
  return caps
def bstack11111lll1_opy_():
  global bstack1llll11lll_opy_
  if bstack1lll1l11l_opy_() <= version.parse(bstack111lll1_opy_ (u"࠭࠳࠯࠳࠶࠲࠵࠭च")):
    if bstack1llll11lll_opy_ != bstack111lll1_opy_ (u"ࠧࠨछ"):
      return bstack111lll1_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤज") + bstack1llll11lll_opy_ + bstack111lll1_opy_ (u"ࠤ࠽࠼࠵࠵ࡷࡥ࠱࡫ࡹࡧࠨझ")
    return bstack1ll11111l1_opy_
  if bstack1llll11lll_opy_ != bstack111lll1_opy_ (u"ࠪࠫञ"):
    return bstack111lll1_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨट") + bstack1llll11lll_opy_ + bstack111lll1_opy_ (u"ࠧ࠵ࡷࡥ࠱࡫ࡹࡧࠨठ")
  return bstack111llll1l_opy_
def bstack1llll1l1l_opy_(options):
  return hasattr(options, bstack111lll1_opy_ (u"࠭ࡳࡦࡶࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹࡿࠧड"))
def update(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = update(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack1llll1ll11_opy_(options, bstack11111ll1l_opy_):
  for bstack1ll111ll1_opy_ in bstack11111ll1l_opy_:
    if bstack1ll111ll1_opy_ in [bstack111lll1_opy_ (u"ࠧࡢࡴࡪࡷࠬढ"), bstack111lll1_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬण")]:
      continue
    if bstack1ll111ll1_opy_ in options._experimental_options:
      options._experimental_options[bstack1ll111ll1_opy_] = update(options._experimental_options[bstack1ll111ll1_opy_],
                                                         bstack11111ll1l_opy_[bstack1ll111ll1_opy_])
    else:
      options.add_experimental_option(bstack1ll111ll1_opy_, bstack11111ll1l_opy_[bstack1ll111ll1_opy_])
  if bstack111lll1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧत") in bstack11111ll1l_opy_:
    for arg in bstack11111ll1l_opy_[bstack111lll1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨथ")]:
      options.add_argument(arg)
    del (bstack11111ll1l_opy_[bstack111lll1_opy_ (u"ࠫࡦࡸࡧࡴࠩद")])
  if bstack111lll1_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩध") in bstack11111ll1l_opy_:
    for ext in bstack11111ll1l_opy_[bstack111lll1_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪन")]:
      options.add_extension(ext)
    del (bstack11111ll1l_opy_[bstack111lll1_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫऩ")])
def bstack11llll1l1_opy_(options, bstack1l1ll111l_opy_):
  if bstack111lll1_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧप") in bstack1l1ll111l_opy_:
    for bstack1l1lll1l1l_opy_ in bstack1l1ll111l_opy_[bstack111lll1_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨफ")]:
      if bstack1l1lll1l1l_opy_ in options._preferences:
        options._preferences[bstack1l1lll1l1l_opy_] = update(options._preferences[bstack1l1lll1l1l_opy_], bstack1l1ll111l_opy_[bstack111lll1_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩब")][bstack1l1lll1l1l_opy_])
      else:
        options.set_preference(bstack1l1lll1l1l_opy_, bstack1l1ll111l_opy_[bstack111lll1_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪभ")][bstack1l1lll1l1l_opy_])
  if bstack111lll1_opy_ (u"ࠬࡧࡲࡨࡵࠪम") in bstack1l1ll111l_opy_:
    for arg in bstack1l1ll111l_opy_[bstack111lll1_opy_ (u"࠭ࡡࡳࡩࡶࠫय")]:
      options.add_argument(arg)
def bstack1ll1ll11l1_opy_(options, bstack1l1ll11ll1_opy_):
  if bstack111lll1_opy_ (u"ࠧࡸࡧࡥࡺ࡮࡫ࡷࠨर") in bstack1l1ll11ll1_opy_:
    options.use_webview(bool(bstack1l1ll11ll1_opy_[bstack111lll1_opy_ (u"ࠨࡹࡨࡦࡻ࡯ࡥࡸࠩऱ")]))
  bstack1llll1ll11_opy_(options, bstack1l1ll11ll1_opy_)
def bstack11lllll11_opy_(options, bstack11lllll1_opy_):
  for bstack1lll1l1l1_opy_ in bstack11lllll1_opy_:
    if bstack1lll1l1l1_opy_ in [bstack111lll1_opy_ (u"ࠩࡷࡩࡨ࡮࡮ࡰ࡮ࡲ࡫ࡾࡖࡲࡦࡸ࡬ࡩࡼ࠭ल"), bstack111lll1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨळ")]:
      continue
    options.set_capability(bstack1lll1l1l1_opy_, bstack11lllll1_opy_[bstack1lll1l1l1_opy_])
  if bstack111lll1_opy_ (u"ࠫࡦࡸࡧࡴࠩऴ") in bstack11lllll1_opy_:
    for arg in bstack11lllll1_opy_[bstack111lll1_opy_ (u"ࠬࡧࡲࡨࡵࠪव")]:
      options.add_argument(arg)
  if bstack111lll1_opy_ (u"࠭ࡴࡦࡥ࡫ࡲࡴࡲ࡯ࡨࡻࡓࡶࡪࡼࡩࡦࡹࠪश") in bstack11lllll1_opy_:
    options.bstack1llll1l1_opy_(bool(bstack11lllll1_opy_[bstack111lll1_opy_ (u"ࠧࡵࡧࡦ࡬ࡳࡵ࡬ࡰࡩࡼࡔࡷ࡫ࡶࡪࡧࡺࠫष")]))
def bstack11ll1l11l_opy_(options, bstack1l1lll11_opy_):
  for bstack111l11l1_opy_ in bstack1l1lll11_opy_:
    if bstack111l11l1_opy_ in [bstack111lll1_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬस"), bstack111lll1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧह")]:
      continue
    options._options[bstack111l11l1_opy_] = bstack1l1lll11_opy_[bstack111l11l1_opy_]
  if bstack111lll1_opy_ (u"ࠪࡥࡩࡪࡩࡵ࡫ࡲࡲࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧऺ") in bstack1l1lll11_opy_:
    for bstack1ll1ll1l11_opy_ in bstack1l1lll11_opy_[bstack111lll1_opy_ (u"ࠫࡦࡪࡤࡪࡶ࡬ࡳࡳࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨऻ")]:
      options.bstack111l1l1ll_opy_(
        bstack1ll1ll1l11_opy_, bstack1l1lll11_opy_[bstack111lll1_opy_ (u"ࠬࡧࡤࡥ࡫ࡷ࡭ࡴࡴࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴ़ࠩ")][bstack1ll1ll1l11_opy_])
  if bstack111lll1_opy_ (u"࠭ࡡࡳࡩࡶࠫऽ") in bstack1l1lll11_opy_:
    for arg in bstack1l1lll11_opy_[bstack111lll1_opy_ (u"ࠧࡢࡴࡪࡷࠬा")]:
      options.add_argument(arg)
def bstack1ll111l1l_opy_(options, caps):
  if not hasattr(options, bstack111lll1_opy_ (u"ࠨࡍࡈ࡝ࠬि")):
    return
  if options.KEY == bstack111lll1_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧी") and options.KEY in caps:
    bstack1llll1ll11_opy_(options, caps[bstack111lll1_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨु")])
  elif options.KEY == bstack111lll1_opy_ (u"ࠫࡲࡵࡺ࠻ࡨ࡬ࡶࡪ࡬࡯ࡹࡑࡳࡸ࡮ࡵ࡮ࡴࠩू") and options.KEY in caps:
    bstack11llll1l1_opy_(options, caps[bstack111lll1_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡩ࡭ࡷ࡫ࡦࡰࡺࡒࡴࡹ࡯࡯࡯ࡵࠪृ")])
  elif options.KEY == bstack111lll1_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠴࡯ࡱࡶ࡬ࡳࡳࡹࠧॄ") and options.KEY in caps:
    bstack11lllll11_opy_(options, caps[bstack111lll1_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯࠮ࡰࡲࡷ࡭ࡴࡴࡳࠨॅ")])
  elif options.KEY == bstack111lll1_opy_ (u"ࠨ࡯ࡶ࠾ࡪࡪࡧࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩॆ") and options.KEY in caps:
    bstack1ll1ll11l1_opy_(options, caps[bstack111lll1_opy_ (u"ࠩࡰࡷ࠿࡫ࡤࡨࡧࡒࡴࡹ࡯࡯࡯ࡵࠪे")])
  elif options.KEY == bstack111lll1_opy_ (u"ࠪࡷࡪࡀࡩࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩै") and options.KEY in caps:
    bstack11ll1l11l_opy_(options, caps[bstack111lll1_opy_ (u"ࠫࡸ࡫࠺ࡪࡧࡒࡴࡹ࡯࡯࡯ࡵࠪॉ")])
def bstack1l1ll1llll_opy_(caps):
  global bstack1ll1l1l11l_opy_
  if isinstance(os.environ.get(bstack111lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ॊ")), str):
    bstack1ll1l1l11l_opy_ = eval(os.getenv(bstack111lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧो")))
  if bstack1ll1l1l11l_opy_:
    if bstack1ll11l1l11_opy_() < version.parse(bstack111lll1_opy_ (u"ࠧ࠳࠰࠶࠲࠵࠭ौ")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack111lll1_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨ्")
    if bstack111lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧॎ") in caps:
      browser = caps[bstack111lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨॏ")]
    elif bstack111lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬॐ") in caps:
      browser = caps[bstack111lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭॑")]
    browser = str(browser).lower()
    if browser == bstack111lll1_opy_ (u"࠭ࡩࡱࡪࡲࡲࡪ॒࠭") or browser == bstack111lll1_opy_ (u"ࠧࡪࡲࡤࡨࠬ॓"):
      browser = bstack111lll1_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࠨ॔")
    if browser == bstack111lll1_opy_ (u"ࠩࡶࡥࡲࡹࡵ࡯ࡩࠪॕ"):
      browser = bstack111lll1_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪॖ")
    if browser not in [bstack111lll1_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫॗ"), bstack111lll1_opy_ (u"ࠬ࡫ࡤࡨࡧࠪक़"), bstack111lll1_opy_ (u"࠭ࡩࡦࠩख़"), bstack111lll1_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࠧग़"), bstack111lll1_opy_ (u"ࠨࡨ࡬ࡶࡪ࡬࡯ࡹࠩज़")]:
      return None
    try:
      package = bstack111lll1_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰ࠲ࡼ࡫ࡢࡥࡴ࡬ࡺࡪࡸ࠮ࡼࡿ࠱ࡳࡵࡺࡩࡰࡰࡶࠫड़").format(browser)
      name = bstack111lll1_opy_ (u"ࠪࡓࡵࡺࡩࡰࡰࡶࠫढ़")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack1llll1l1l_opy_(options):
        return None
      for bstack1l1ll11ll_opy_ in caps.keys():
        options.set_capability(bstack1l1ll11ll_opy_, caps[bstack1l1ll11ll_opy_])
      bstack1ll111l1l_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack1lll11l11l_opy_(options, bstack1lll1l11ll_opy_):
  if not bstack1llll1l1l_opy_(options):
    return
  for bstack1l1ll11ll_opy_ in bstack1lll1l11ll_opy_.keys():
    if bstack1l1ll11ll_opy_ in bstack1l1ll11l1l_opy_:
      continue
    if bstack1l1ll11ll_opy_ in options._caps and type(options._caps[bstack1l1ll11ll_opy_]) in [dict, list]:
      options._caps[bstack1l1ll11ll_opy_] = update(options._caps[bstack1l1ll11ll_opy_], bstack1lll1l11ll_opy_[bstack1l1ll11ll_opy_])
    else:
      options.set_capability(bstack1l1ll11ll_opy_, bstack1lll1l11ll_opy_[bstack1l1ll11ll_opy_])
  bstack1ll111l1l_opy_(options, bstack1lll1l11ll_opy_)
  if bstack111lll1_opy_ (u"ࠫࡲࡵࡺ࠻ࡦࡨࡦࡺ࡭ࡧࡦࡴࡄࡨࡩࡸࡥࡴࡵࠪफ़") in options._caps:
    if options._caps[bstack111lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪय़")] and options._caps[bstack111lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫॠ")].lower() != bstack111lll1_opy_ (u"ࠧࡧ࡫ࡵࡩ࡫ࡵࡸࠨॡ"):
      del options._caps[bstack111lll1_opy_ (u"ࠨ࡯ࡲࡾ࠿ࡪࡥࡣࡷࡪ࡫ࡪࡸࡁࡥࡦࡵࡩࡸࡹࠧॢ")]
def bstack1l1lllll1_opy_(proxy_config):
  if bstack111lll1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ॣ") in proxy_config:
    proxy_config[bstack111lll1_opy_ (u"ࠪࡷࡸࡲࡐࡳࡱࡻࡽࠬ।")] = proxy_config[bstack111lll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨ॥")]
    del (proxy_config[bstack111lll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩ०")])
  if bstack111lll1_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡙ࡿࡰࡦࠩ१") in proxy_config and proxy_config[bstack111lll1_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡚ࡹࡱࡧࠪ२")].lower() != bstack111lll1_opy_ (u"ࠨࡦ࡬ࡶࡪࡩࡴࠨ३"):
    proxy_config[bstack111lll1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬ४")] = bstack111lll1_opy_ (u"ࠪࡱࡦࡴࡵࡢ࡮ࠪ५")
  if bstack111lll1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡄࡹࡹࡵࡣࡰࡰࡩ࡭࡬࡛ࡲ࡭ࠩ६") in proxy_config:
    proxy_config[bstack111lll1_opy_ (u"ࠬࡶࡲࡰࡺࡼࡘࡾࡶࡥࠨ७")] = bstack111lll1_opy_ (u"࠭ࡰࡢࡥࠪ८")
  return proxy_config
def bstack1lll111ll_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack111lll1_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭९") in config:
    return proxy
  config[bstack111lll1_opy_ (u"ࠨࡲࡵࡳࡽࡿࠧ॰")] = bstack1l1lllll1_opy_(config[bstack111lll1_opy_ (u"ࠩࡳࡶࡴࡾࡹࠨॱ")])
  if proxy == None:
    proxy = Proxy(config[bstack111lll1_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩॲ")])
  return proxy
def bstack1l1111l1_opy_(self):
  global CONFIG
  global bstack1lllll11l1_opy_
  try:
    proxy = bstack1l1lll11l_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack111lll1_opy_ (u"ࠫ࠳ࡶࡡࡤࠩॳ")):
        proxies = bstack1llll1l11_opy_(proxy, bstack11111lll1_opy_())
        if len(proxies) > 0:
          protocol, bstack1l1l111l11_opy_ = proxies.popitem()
          if bstack111lll1_opy_ (u"ࠧࡀ࠯࠰ࠤॴ") in bstack1l1l111l11_opy_:
            return bstack1l1l111l11_opy_
          else:
            return bstack111lll1_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢॵ") + bstack1l1l111l11_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack111lll1_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡴࡷࡵࡸࡺࠢࡸࡶࡱࠦ࠺ࠡࡽࢀࠦॶ").format(str(e)))
  return bstack1lllll11l1_opy_(self)
def bstack1l111ll1l_opy_():
  global CONFIG
  return bstack11llllll_opy_(CONFIG) and bstack1lllllll1_opy_() and bstack1lll1l11l_opy_() >= version.parse(bstack11llll11l_opy_)
def bstack11lll1l1_opy_():
  global CONFIG
  return (bstack111lll1_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫॷ") in CONFIG or bstack111lll1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ॸ") in CONFIG) and bstack1111lll1_opy_()
def bstack1111ll11_opy_(config):
  bstack11l1l11l_opy_ = {}
  if bstack111lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧॹ") in config:
    bstack11l1l11l_opy_ = config[bstack111lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨॺ")]
  if bstack111lll1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫॻ") in config:
    bstack11l1l11l_opy_ = config[bstack111lll1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬॼ")]
  proxy = bstack1l1lll11l_opy_(config)
  if proxy:
    if proxy.endswith(bstack111lll1_opy_ (u"ࠧ࠯ࡲࡤࡧࠬॽ")) and os.path.isfile(proxy):
      bstack11l1l11l_opy_[bstack111lll1_opy_ (u"ࠨ࠯ࡳࡥࡨ࠳ࡦࡪ࡮ࡨࠫॾ")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack111lll1_opy_ (u"ࠩ࠱ࡴࡦࡩࠧॿ")):
        proxies = bstack1l1l11llll_opy_(config, bstack11111lll1_opy_())
        if len(proxies) > 0:
          protocol, bstack1l1l111l11_opy_ = proxies.popitem()
          if bstack111lll1_opy_ (u"ࠥ࠾࠴࠵ࠢঀ") in bstack1l1l111l11_opy_:
            parsed_url = urlparse(bstack1l1l111l11_opy_)
          else:
            parsed_url = urlparse(protocol + bstack111lll1_opy_ (u"ࠦ࠿࠵࠯ࠣঁ") + bstack1l1l111l11_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack11l1l11l_opy_[bstack111lll1_opy_ (u"ࠬࡶࡲࡰࡺࡼࡌࡴࡹࡴࠨং")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack11l1l11l_opy_[bstack111lll1_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡵࡲࡵࠩঃ")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack11l1l11l_opy_[bstack111lll1_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡛ࡳࡦࡴࠪ঄")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack11l1l11l_opy_[bstack111lll1_opy_ (u"ࠨࡲࡵࡳࡽࡿࡐࡢࡵࡶࠫঅ")] = str(parsed_url.password)
  return bstack11l1l11l_opy_
def bstack111lll111_opy_(config):
  if bstack111lll1_opy_ (u"ࠩࡷࡩࡸࡺࡃࡰࡰࡷࡩࡽࡺࡏࡱࡶ࡬ࡳࡳࡹࠧআ") in config:
    return config[bstack111lll1_opy_ (u"ࠪࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠨই")]
  return {}
def bstack11111l111_opy_(caps):
  global bstack1111l1l1l_opy_
  if bstack111lll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬঈ") in caps:
    caps[bstack111lll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭উ")][bstack111lll1_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬঊ")] = True
    if bstack1111l1l1l_opy_:
      caps[bstack111lll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨঋ")][bstack111lll1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪঌ")] = bstack1111l1l1l_opy_
  else:
    caps[bstack111lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࠧ঍")] = True
    if bstack1111l1l1l_opy_:
      caps[bstack111lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ঎")] = bstack1111l1l1l_opy_
def bstack1l1lllll11_opy_():
  global CONFIG
  if bstack111lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨএ") in CONFIG and bstack1lllll111l_opy_(CONFIG[bstack111lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩঐ")]):
    bstack11l1l11l_opy_ = bstack1111ll11_opy_(CONFIG)
    bstack1llllllll_opy_(CONFIG[bstack111lll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ঑")], bstack11l1l11l_opy_)
def bstack1llllllll_opy_(key, bstack11l1l11l_opy_):
  global bstack111l11ll_opy_
  logger.info(bstack1ll1111l_opy_)
  try:
    bstack111l11ll_opy_ = Local()
    bstack1ll1ll1l_opy_ = {bstack111lll1_opy_ (u"ࠧ࡬ࡧࡼࠫ঒"): key}
    bstack1ll1ll1l_opy_.update(bstack11l1l11l_opy_)
    logger.debug(bstack1l1lll1l_opy_.format(str(bstack1ll1ll1l_opy_)))
    bstack111l11ll_opy_.start(**bstack1ll1ll1l_opy_)
    if bstack111l11ll_opy_.isRunning():
      logger.info(bstack1l1l1l11ll_opy_)
  except Exception as e:
    bstack1ll1lll111_opy_(bstack11l1ll1ll_opy_.format(str(e)))
def bstack1l11lll1l_opy_():
  global bstack111l11ll_opy_
  if bstack111l11ll_opy_.isRunning():
    logger.info(bstack1l111l1l1_opy_)
    bstack111l11ll_opy_.stop()
  bstack111l11ll_opy_ = None
def bstack11l11l11l_opy_(bstack1ll111111_opy_=[]):
  global CONFIG
  bstack1l1l1ll1l_opy_ = []
  bstack1ll1ll11l_opy_ = [bstack111lll1_opy_ (u"ࠨࡱࡶࠫও"), bstack111lll1_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬঔ"), bstack111lll1_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧক"), bstack111lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭খ"), bstack111lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪগ"), bstack111lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧঘ")]
  try:
    for err in bstack1ll111111_opy_:
      bstack1llllll1l_opy_ = {}
      for k in bstack1ll1ll11l_opy_:
        val = CONFIG[bstack111lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪঙ")][int(err[bstack111lll1_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧচ")])].get(k)
        if val:
          bstack1llllll1l_opy_[k] = val
      if(err[bstack111lll1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨছ")] != bstack111lll1_opy_ (u"ࠪࠫজ")):
        bstack1llllll1l_opy_[bstack111lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡵࠪঝ")] = {
          err[bstack111lll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪঞ")]: err[bstack111lll1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬট")]
        }
        bstack1l1l1ll1l_opy_.append(bstack1llllll1l_opy_)
  except Exception as e:
    logger.debug(bstack111lll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩࡳࡷࡳࡡࡵࡶ࡬ࡲ࡬ࠦࡤࡢࡶࡤࠤ࡫ࡵࡲࠡࡧࡹࡩࡳࡺ࠺ࠡࠩঠ") + str(e))
  finally:
    return bstack1l1l1ll1l_opy_
def bstack1lll1lll11_opy_(file_name):
  bstack1ll11l1lll_opy_ = []
  try:
    bstack111l111l_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack111l111l_opy_):
      with open(bstack111l111l_opy_) as f:
        bstack1ll1111ll_opy_ = json.load(f)
        bstack1ll11l1lll_opy_ = bstack1ll1111ll_opy_
      os.remove(bstack111l111l_opy_)
    return bstack1ll11l1lll_opy_
  except Exception as e:
    logger.debug(bstack111lll1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡪ࡮ࡴࡤࡪࡰࡪࠤࡪࡸࡲࡰࡴࠣࡰ࡮ࡹࡴ࠻ࠢࠪড") + str(e))
def bstack1ll11llll1_opy_():
  global bstack1lll1lll_opy_
  global bstack1lllllllll_opy_
  global bstack1l1ll11l_opy_
  global bstack1llllll11l_opy_
  global bstack11l1l1lll_opy_
  global bstack1ll1l111ll_opy_
  percy.shutdown()
  bstack1llll111ll_opy_ = os.environ.get(bstack111lll1_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪঢ"))
  if bstack1llll111ll_opy_ in [bstack111lll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩণ"), bstack111lll1_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪত")]:
    bstack11111l1l1_opy_()
  if bstack1lll1lll_opy_:
    logger.warning(bstack1ll1l11l1l_opy_.format(str(bstack1lll1lll_opy_)))
  else:
    try:
      bstack111llllll_opy_ = bstack1llll111_opy_(bstack111lll1_opy_ (u"ࠬ࠴ࡢࡴࡶࡤࡧࡰ࠳ࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫথ"), logger)
      if bstack111llllll_opy_.get(bstack111lll1_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫদ")) and bstack111llllll_opy_.get(bstack111lll1_opy_ (u"ࠧ࡯ࡷࡧ࡫ࡪࡥ࡬ࡰࡥࡤࡰࠬধ")).get(bstack111lll1_opy_ (u"ࠨࡪࡲࡷࡹࡴࡡ࡮ࡧࠪন")):
        logger.warning(bstack1ll1l11l1l_opy_.format(str(bstack111llllll_opy_[bstack111lll1_opy_ (u"ࠩࡱࡹࡩ࡭ࡥࡠ࡮ࡲࡧࡦࡲࠧ঩")][bstack111lll1_opy_ (u"ࠪ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠬপ")])))
    except Exception as e:
      logger.error(e)
  logger.info(bstack1l1lll1ll_opy_)
  global bstack111l11ll_opy_
  if bstack111l11ll_opy_:
    bstack1l11lll1l_opy_()
  try:
    for driver in bstack1lllllllll_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack11l11lll1_opy_)
  if bstack1ll1l111ll_opy_ == bstack111lll1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪফ"):
    bstack11l1l1lll_opy_ = bstack1lll1lll11_opy_(bstack111lll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭ব"))
  if bstack1ll1l111ll_opy_ == bstack111lll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ভ") and len(bstack1llllll11l_opy_) == 0:
    bstack1llllll11l_opy_ = bstack1lll1lll11_opy_(bstack111lll1_opy_ (u"ࠧࡱࡹࡢࡴࡾࡺࡥࡴࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬম"))
    if len(bstack1llllll11l_opy_) == 0:
      bstack1llllll11l_opy_ = bstack1lll1lll11_opy_(bstack111lll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡲࡳࡴࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧয"))
  bstack1l1l11ll1l_opy_ = bstack111lll1_opy_ (u"ࠩࠪর")
  if len(bstack1l1ll11l_opy_) > 0:
    bstack1l1l11ll1l_opy_ = bstack11l11l11l_opy_(bstack1l1ll11l_opy_)
  elif len(bstack1llllll11l_opy_) > 0:
    bstack1l1l11ll1l_opy_ = bstack11l11l11l_opy_(bstack1llllll11l_opy_)
  elif len(bstack11l1l1lll_opy_) > 0:
    bstack1l1l11ll1l_opy_ = bstack11l11l11l_opy_(bstack11l1l1lll_opy_)
  elif len(bstack1l11lllll_opy_) > 0:
    bstack1l1l11ll1l_opy_ = bstack11l11l11l_opy_(bstack1l11lllll_opy_)
  if bool(bstack1l1l11ll1l_opy_):
    bstack1l111ll1_opy_(bstack1l1l11ll1l_opy_)
  else:
    bstack1l111ll1_opy_()
  bstack111lllll1_opy_(bstack1l1lll11ll_opy_, logger)
def bstack1lllll1l1_opy_(self, *args):
  logger.error(bstack1ll1l1l111_opy_)
  bstack1ll11llll1_opy_()
  sys.exit(1)
def bstack1ll1lll111_opy_(err):
  logger.critical(bstack1l11l1111_opy_.format(str(err)))
  bstack1l111ll1_opy_(bstack1l11l1111_opy_.format(str(err)), True)
  atexit.unregister(bstack1ll11llll1_opy_)
  bstack11111l1l1_opy_()
  sys.exit(1)
def bstack1l11ll11l_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1l111ll1_opy_(message, True)
  atexit.unregister(bstack1ll11llll1_opy_)
  bstack11111l1l1_opy_()
  sys.exit(1)
def bstack11ll11ll_opy_():
  global CONFIG
  global bstack1ll111l1l1_opy_
  global bstack1llll1l11l_opy_
  global bstack1ll1ll1ll_opy_
  CONFIG = bstack1ll111l1_opy_()
  bstack11l111ll_opy_()
  bstack1l1ll11l1_opy_()
  CONFIG = bstack1lll1l1111_opy_(CONFIG)
  update(CONFIG, bstack1llll1l11l_opy_)
  update(CONFIG, bstack1ll111l1l1_opy_)
  CONFIG = bstack1llll1111l_opy_(CONFIG)
  bstack1ll1ll1ll_opy_ = bstack1ll1l1l1l1_opy_(CONFIG)
  bstack11l11l111_opy_.bstack1ll1ll11_opy_(bstack111lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫ঱"), bstack1ll1ll1ll_opy_)
  if (bstack111lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧল") in CONFIG and bstack111lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ঳") in bstack1ll111l1l1_opy_) or (
          bstack111lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ঴") in CONFIG and bstack111lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ঵") not in bstack1llll1l11l_opy_):
    if os.getenv(bstack111lll1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬশ")):
      CONFIG[bstack111lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫষ")] = os.getenv(bstack111lll1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡢࡇࡔࡓࡂࡊࡐࡈࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧস"))
    else:
      bstack1lllll111_opy_()
  elif (bstack111lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧহ") not in CONFIG and bstack111lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ঺") in CONFIG) or (
          bstack111lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ঻") in bstack1llll1l11l_opy_ and bstack111lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧ়ࠪ") not in bstack1ll111l1l1_opy_):
    del (CONFIG[bstack111lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪঽ")])
  if bstack1ll11l1l_opy_(CONFIG):
    bstack1ll1lll111_opy_(bstack11l111111_opy_)
  bstack1l1l111ll_opy_()
  bstack1l1ll1ll1_opy_()
  if bstack1ll1l1l11l_opy_:
    CONFIG[bstack111lll1_opy_ (u"ࠩࡤࡴࡵ࠭া")] = bstack1ll1l111_opy_(CONFIG)
    logger.info(bstack1l11l1l1_opy_.format(CONFIG[bstack111lll1_opy_ (u"ࠪࡥࡵࡶࠧি")]))
  if not bstack1ll1ll1ll_opy_:
    CONFIG[bstack111lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧী")] = [{}]
def bstack1ll1111l1l_opy_(config, bstack1ll1l1l1l_opy_):
  global CONFIG
  global bstack1ll1l1l11l_opy_
  CONFIG = config
  bstack1ll1l1l11l_opy_ = bstack1ll1l1l1l_opy_
def bstack1l1ll1ll1_opy_():
  global CONFIG
  global bstack1ll1l1l11l_opy_
  if bstack111lll1_opy_ (u"ࠬࡧࡰࡱࠩু") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1l11ll11l_opy_(e, bstack11111ll11_opy_)
    bstack1ll1l1l11l_opy_ = True
    bstack11l11l111_opy_.bstack1ll1ll11_opy_(bstack111lll1_opy_ (u"࠭ࡡࡱࡲࡢࡥࡺࡺ࡯࡮ࡣࡷࡩࠬূ"), True)
def bstack1ll1l111_opy_(config):
  bstack1lll111l1l_opy_ = bstack111lll1_opy_ (u"ࠧࠨৃ")
  app = config[bstack111lll1_opy_ (u"ࠨࡣࡳࡴࠬৄ")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack111111l1_opy_:
      if os.path.exists(app):
        bstack1lll111l1l_opy_ = bstack1l1l111ll1_opy_(config, app)
      elif bstack1ll1l1l1_opy_(app):
        bstack1lll111l1l_opy_ = app
      else:
        bstack1ll1lll111_opy_(bstack1ll11l1l1l_opy_.format(app))
    else:
      if bstack1ll1l1l1_opy_(app):
        bstack1lll111l1l_opy_ = app
      elif os.path.exists(app):
        bstack1lll111l1l_opy_ = bstack1l1l111ll1_opy_(app)
      else:
        bstack1ll1lll111_opy_(bstack111111ll1_opy_)
  else:
    if len(app) > 2:
      bstack1ll1lll111_opy_(bstack111l1lll1_opy_)
    elif len(app) == 2:
      if bstack111lll1_opy_ (u"ࠩࡳࡥࡹ࡮ࠧ৅") in app and bstack111lll1_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭৆") in app:
        if os.path.exists(app[bstack111lll1_opy_ (u"ࠫࡵࡧࡴࡩࠩে")]):
          bstack1lll111l1l_opy_ = bstack1l1l111ll1_opy_(config, app[bstack111lll1_opy_ (u"ࠬࡶࡡࡵࡪࠪৈ")], app[bstack111lll1_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡥࡩࡥࠩ৉")])
        else:
          bstack1ll1lll111_opy_(bstack1ll11l1l1l_opy_.format(app))
      else:
        bstack1ll1lll111_opy_(bstack111l1lll1_opy_)
    else:
      for key in app:
        if key in bstack1ll1ll1l1l_opy_:
          if key == bstack111lll1_opy_ (u"ࠧࡱࡣࡷ࡬ࠬ৊"):
            if os.path.exists(app[key]):
              bstack1lll111l1l_opy_ = bstack1l1l111ll1_opy_(config, app[key])
            else:
              bstack1ll1lll111_opy_(bstack1ll11l1l1l_opy_.format(app))
          else:
            bstack1lll111l1l_opy_ = app[key]
        else:
          bstack1ll1lll111_opy_(bstack11l1l111_opy_)
  return bstack1lll111l1l_opy_
def bstack1ll1l1l1_opy_(bstack1lll111l1l_opy_):
  import re
  bstack1l1ll111_opy_ = re.compile(bstack111lll1_opy_ (u"ࡳࠤࡡ࡟ࡦ࠳ࡺࡂ࠯࡝࠴࠲࠿࡜ࡠ࠰࡟࠱ࡢ࠰ࠤࠣো"))
  bstack1ll1111ll1_opy_ = re.compile(bstack111lll1_opy_ (u"ࡴࠥࡢࡠࡧ࠭ࡻࡃ࠰࡞࠵࠳࠹࡝ࡡ࠱ࡠ࠲ࡣࠪ࠰࡝ࡤ࠱ࡿࡇ࡛࠭࠲࠰࠽ࡡࡥ࠮࡝࠯ࡠ࠮ࠩࠨৌ"))
  if bstack111lll1_opy_ (u"ࠪࡦࡸࡀ࠯࠰্ࠩ") in bstack1lll111l1l_opy_ or re.fullmatch(bstack1l1ll111_opy_, bstack1lll111l1l_opy_) or re.fullmatch(bstack1ll1111ll1_opy_, bstack1lll111l1l_opy_):
    return True
  else:
    return False
def bstack1l1l111ll1_opy_(config, path, bstack111ll1lll_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack111lll1_opy_ (u"ࠫࡷࡨࠧৎ")).read()).hexdigest()
  bstack1l1ll1111l_opy_ = bstack111lll1l_opy_(md5_hash)
  bstack1lll111l1l_opy_ = None
  if bstack1l1ll1111l_opy_:
    logger.info(bstack11l111l1_opy_.format(bstack1l1ll1111l_opy_, md5_hash))
    return bstack1l1ll1111l_opy_
  bstack1ll1llll_opy_ = MultipartEncoder(
    fields={
      bstack111lll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࠪ৏"): (os.path.basename(path), open(os.path.abspath(path), bstack111lll1_opy_ (u"࠭ࡲࡣࠩ৐")), bstack111lll1_opy_ (u"ࠧࡵࡧࡻࡸ࠴ࡶ࡬ࡢ࡫ࡱࠫ৑")),
      bstack111lll1_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡠ࡫ࡧࠫ৒"): bstack111ll1lll_opy_
    }
  )
  response = requests.post(bstack1lll111l11_opy_, data=bstack1ll1llll_opy_,
                           headers={bstack111lll1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨ৓"): bstack1ll1llll_opy_.content_type},
                           auth=(config[bstack111lll1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬ৔")], config[bstack111lll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ৕")]))
  try:
    res = json.loads(response.text)
    bstack1lll111l1l_opy_ = res[bstack111lll1_opy_ (u"ࠬࡧࡰࡱࡡࡸࡶࡱ࠭৖")]
    logger.info(bstack1ll1ll1l1_opy_.format(bstack1lll111l1l_opy_))
    bstack1l1111ll_opy_(md5_hash, bstack1lll111l1l_opy_)
  except ValueError as err:
    bstack1ll1lll111_opy_(bstack11llll11_opy_.format(str(err)))
  return bstack1lll111l1l_opy_
def bstack1l1l111ll_opy_():
  global CONFIG
  global bstack1111l11ll_opy_
  bstack1lll1ll1ll_opy_ = 0
  bstack1lll1ll1_opy_ = 1
  if bstack111lll1_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭ৗ") in CONFIG:
    bstack1lll1ll1_opy_ = CONFIG[bstack111lll1_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ৘")]
  if bstack111lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ৙") in CONFIG:
    bstack1lll1ll1ll_opy_ = len(CONFIG[bstack111lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ৚")])
  bstack1111l11ll_opy_ = int(bstack1lll1ll1_opy_) * int(bstack1lll1ll1ll_opy_)
def bstack111lll1l_opy_(md5_hash):
  bstack11l1111l1_opy_ = os.path.join(os.path.expanduser(bstack111lll1_opy_ (u"ࠪࢂࠬ৛")), bstack111lll1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫড়"), bstack111lll1_opy_ (u"ࠬࡧࡰࡱࡗࡳࡰࡴࡧࡤࡎࡆ࠸ࡌࡦࡹࡨ࠯࡬ࡶࡳࡳ࠭ঢ়"))
  if os.path.exists(bstack11l1111l1_opy_):
    bstack1l1l1111ll_opy_ = json.load(open(bstack11l1111l1_opy_, bstack111lll1_opy_ (u"࠭ࡲࡣࠩ৞")))
    if md5_hash in bstack1l1l1111ll_opy_:
      bstack11lll11l_opy_ = bstack1l1l1111ll_opy_[md5_hash]
      bstack1ll1l1lll_opy_ = datetime.datetime.now()
      bstack11l11llll_opy_ = datetime.datetime.strptime(bstack11lll11l_opy_[bstack111lll1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪয়")], bstack111lll1_opy_ (u"ࠨࠧࡧ࠳ࠪࡳ࠯࡛ࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠬৠ"))
      if (bstack1ll1l1lll_opy_ - bstack11l11llll_opy_).days > 30:
        return None
      elif version.parse(str(__version__)) > version.parse(bstack11lll11l_opy_[bstack111lll1_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧৡ")]):
        return None
      return bstack11lll11l_opy_[bstack111lll1_opy_ (u"ࠪ࡭ࡩ࠭ৢ")]
  else:
    return None
def bstack1l1111ll_opy_(md5_hash, bstack1lll111l1l_opy_):
  bstack1ll11llll_opy_ = os.path.join(os.path.expanduser(bstack111lll1_opy_ (u"ࠫࢃ࠭ৣ")), bstack111lll1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ৤"))
  if not os.path.exists(bstack1ll11llll_opy_):
    os.makedirs(bstack1ll11llll_opy_)
  bstack11l1111l1_opy_ = os.path.join(os.path.expanduser(bstack111lll1_opy_ (u"࠭ࡾࠨ৥")), bstack111lll1_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ০"), bstack111lll1_opy_ (u"ࠨࡣࡳࡴ࡚ࡶ࡬ࡰࡣࡧࡑࡉ࠻ࡈࡢࡵ࡫࠲࡯ࡹ࡯࡯ࠩ১"))
  bstack1ll11111l_opy_ = {
    bstack111lll1_opy_ (u"ࠩ࡬ࡨࠬ২"): bstack1lll111l1l_opy_,
    bstack111lll1_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭৩"): datetime.datetime.strftime(datetime.datetime.now(), bstack111lll1_opy_ (u"ࠫࠪࡪ࠯ࠦ࡯࠲ࠩ࡞ࠦࠥࡉ࠼ࠨࡑ࠿ࠫࡓࠨ৪")),
    bstack111lll1_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪ৫"): str(__version__)
  }
  if os.path.exists(bstack11l1111l1_opy_):
    bstack1l1l1111ll_opy_ = json.load(open(bstack11l1111l1_opy_, bstack111lll1_opy_ (u"࠭ࡲࡣࠩ৬")))
  else:
    bstack1l1l1111ll_opy_ = {}
  bstack1l1l1111ll_opy_[md5_hash] = bstack1ll11111l_opy_
  with open(bstack11l1111l1_opy_, bstack111lll1_opy_ (u"ࠢࡸ࠭ࠥ৭")) as outfile:
    json.dump(bstack1l1l1111ll_opy_, outfile)
def bstack1l1ll11lll_opy_(self):
  return
def bstack1l1l111l_opy_(self):
  return
def bstack11llllll1_opy_(self):
  global bstack1l11llll1_opy_
  bstack1l11llll1_opy_(self)
def bstack11ll1111l_opy_():
  global bstack1l1l1l1111_opy_
  bstack1l1l1l1111_opy_ = True
def bstack1111ll111_opy_(self):
  global bstack1llll11l11_opy_
  global bstack1ll1111l11_opy_
  global bstack1llll1l111_opy_
  try:
    if bstack111lll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ৮") in bstack1llll11l11_opy_ and self.session_id != None and bstack1ll1111111_opy_(threading.current_thread(), bstack111lll1_opy_ (u"ࠩࡷࡩࡸࡺࡓࡵࡣࡷࡹࡸ࠭৯"), bstack111lll1_opy_ (u"ࠪࠫৰ")) != bstack111lll1_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬৱ"):
      bstack111lllll_opy_ = bstack111lll1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ৲") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack111lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭৳")
      if bstack111lllll_opy_ == bstack111lll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ৴"):
        bstack1l1llllll_opy_(logger)
      if self != None:
        bstack1l11ll11_opy_(self, bstack111lllll_opy_, bstack111lll1_opy_ (u"ࠨ࠮ࠣࠫ৵").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack111lll1_opy_ (u"ࠩࠪ৶")
    if bstack111lll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ৷") in bstack1llll11l11_opy_ and getattr(threading.current_thread(), bstack111lll1_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ৸"), None):
      bstack11ll1l1l1_opy_.bstack1lllll1l11_opy_(self, bstack11l1l1l1_opy_, logger, wait=True)
  except Exception as e:
    logger.debug(bstack111lll1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࠨ৹") + str(e))
  bstack1llll1l111_opy_(self)
  self.session_id = None
def bstack11lllllll_opy_(self, command_executor=bstack111lll1_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵࠱࠳࠹࠱࠴࠳࠶࠮࠲࠼࠷࠸࠹࠺ࠢ৺"), *args, **kwargs):
  bstack1lll1lll1_opy_ = bstack11ll1lll_opy_(self, command_executor, *args, **kwargs)
  try:
    logger.debug(bstack111lll1_opy_ (u"ࠧࡄࡱࡰࡱࡦࡴࡤࠡࡇࡻࡩࡨࡻࡴࡰࡴࠣࡻ࡭࡫࡮ࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤ࡮ࡹࠠࡧࡣ࡯ࡷࡪࠦ࠭ࠡࡽࢀࠫ৻").format(str(command_executor)))
    logger.debug(bstack111lll1_opy_ (u"ࠨࡊࡸࡦ࡛ࠥࡒࡍࠢ࡬ࡷࠥ࠳ࠠࡼࡿࠪৼ").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack111lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬ৽") in command_executor._url:
      bstack11l11l111_opy_.bstack1ll1ll11_opy_(bstack111lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫ৾"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack111lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧ৿") in command_executor):
    bstack11l11l111_opy_.bstack1ll1ll11_opy_(bstack111lll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭਀"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack1llll11l1_opy_.bstack1ll11l1ll_opy_(self)
  return bstack1lll1lll1_opy_
def bstack1l111lll1_opy_(self, driver_command, *args, **kwargs):
  global bstack11ll1ll1_opy_
  response = bstack11ll1ll1_opy_(self, driver_command, *args, **kwargs)
  try:
    if driver_command == bstack111lll1_opy_ (u"࠭ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠪਁ"):
      bstack1llll11l1_opy_.bstack1l1l11l111_opy_({
          bstack111lll1_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪ࠭ਂ"): response[bstack111lll1_opy_ (u"ࠨࡸࡤࡰࡺ࡫ࠧਃ")],
          bstack111lll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ਄"): bstack1llll11l1_opy_.current_test_uuid() if bstack1llll11l1_opy_.current_test_uuid() else bstack1llll11l1_opy_.current_hook_uuid()
      })
  except:
    pass
  return response
def bstack1lll11l1l_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
  global CONFIG
  global bstack1ll1111l11_opy_
  global bstack1ll111lll1_opy_
  global bstack1l1lll1l11_opy_
  global bstack11l1l11ll_opy_
  global bstack1lll1ll11l_opy_
  global bstack1llll11l11_opy_
  global bstack11ll1lll_opy_
  global bstack1lllllllll_opy_
  global bstack111l11111_opy_
  global bstack11l1l1l1_opy_
  CONFIG[bstack111lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬਅ")] = str(bstack1llll11l11_opy_) + str(__version__)
  command_executor = bstack11111lll1_opy_()
  logger.debug(bstack1ll1ll1ll1_opy_.format(command_executor))
  proxy = bstack1lll111ll_opy_(CONFIG, proxy)
  bstack11l1l1111_opy_ = 0 if bstack1ll111lll1_opy_ < 0 else bstack1ll111lll1_opy_
  try:
    if bstack11l1l11ll_opy_ is True:
      bstack11l1l1111_opy_ = int(multiprocessing.current_process().name)
    elif bstack1lll1ll11l_opy_ is True:
      bstack11l1l1111_opy_ = int(threading.current_thread().name)
  except:
    bstack11l1l1111_opy_ = 0
  bstack1lll1l11ll_opy_ = bstack11l11l1l1_opy_(CONFIG, bstack11l1l1111_opy_)
  logger.debug(bstack1l1l11lll_opy_.format(str(bstack1lll1l11ll_opy_)))
  if bstack111lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨਆ") in CONFIG and bstack1lllll111l_opy_(CONFIG[bstack111lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩਇ")]):
    bstack11111l111_opy_(bstack1lll1l11ll_opy_)
  if desired_capabilities:
    bstack11l11ll11_opy_ = bstack1lll1l1111_opy_(desired_capabilities)
    bstack11l11ll11_opy_[bstack111lll1_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ਈ")] = bstack1llll1l1ll_opy_(CONFIG)
    bstack1lll111lll_opy_ = bstack11l11l1l1_opy_(bstack11l11ll11_opy_)
    if bstack1lll111lll_opy_:
      bstack1lll1l11ll_opy_ = update(bstack1lll111lll_opy_, bstack1lll1l11ll_opy_)
    desired_capabilities = None
  if options:
    bstack1lll11l11l_opy_(options, bstack1lll1l11ll_opy_)
  if not options:
    options = bstack1l1ll1llll_opy_(bstack1lll1l11ll_opy_)
  bstack11l1l1l1_opy_ = CONFIG.get(bstack111lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪਉ"))[bstack11l1l1111_opy_]
  if bstack1lllll1111_opy_.bstack1lll1llll_opy_(CONFIG, bstack11l1l1111_opy_) and bstack1lllll1111_opy_.bstack1l1lll111l_opy_(bstack1lll1l11ll_opy_, options):
    threading.current_thread().a11yPlatform = True
    bstack1lllll1111_opy_.set_capabilities(bstack1lll1l11ll_opy_, CONFIG)
  if proxy and bstack1lll1l11l_opy_() >= version.parse(bstack111lll1_opy_ (u"ࠨ࠶࠱࠵࠵࠴࠰ࠨਊ")):
    options.proxy(proxy)
  if options and bstack1lll1l11l_opy_() >= version.parse(bstack111lll1_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨ਋")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack1lll1l11l_opy_() < version.parse(bstack111lll1_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩ਌")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1lll1l11ll_opy_)
  logger.info(bstack1l1lll1ll1_opy_)
  if bstack1lll1l11l_opy_() >= version.parse(bstack111lll1_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫ਍")):
    bstack11ll1lll_opy_(self, command_executor=command_executor,
              options=options, keep_alive=keep_alive, file_detector=file_detector)
  elif bstack1lll1l11l_opy_() >= version.parse(bstack111lll1_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫ਎")):
    bstack11ll1lll_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities, options=options,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  elif bstack1lll1l11l_opy_() >= version.parse(bstack111lll1_opy_ (u"࠭࠲࠯࠷࠶࠲࠵࠭ਏ")):
    bstack11ll1lll_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  else:
    bstack11ll1lll_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive)
  try:
    bstack1l1l11ll1_opy_ = bstack111lll1_opy_ (u"ࠧࠨਐ")
    if bstack1lll1l11l_opy_() >= version.parse(bstack111lll1_opy_ (u"ࠨ࠶࠱࠴࠳࠶ࡢ࠲ࠩ਑")):
      bstack1l1l11ll1_opy_ = self.caps.get(bstack111lll1_opy_ (u"ࠤࡲࡴࡹ࡯࡭ࡢ࡮ࡋࡹࡧ࡛ࡲ࡭ࠤ਒"))
    else:
      bstack1l1l11ll1_opy_ = self.capabilities.get(bstack111lll1_opy_ (u"ࠥࡳࡵࡺࡩ࡮ࡣ࡯ࡌࡺࡨࡕࡳ࡮ࠥਓ"))
    if bstack1l1l11ll1_opy_:
      bstack1l1l1llll_opy_(bstack1l1l11ll1_opy_)
      if bstack1lll1l11l_opy_() <= version.parse(bstack111lll1_opy_ (u"ࠫ࠸࠴࠱࠴࠰࠳ࠫਔ")):
        self.command_executor._url = bstack111lll1_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨਕ") + bstack1llll11lll_opy_ + bstack111lll1_opy_ (u"ࠨ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤࠥਖ")
      else:
        self.command_executor._url = bstack111lll1_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤਗ") + bstack1l1l11ll1_opy_ + bstack111lll1_opy_ (u"ࠣ࠱ࡺࡨ࠴࡮ࡵࡣࠤਘ")
      logger.debug(bstack1l111111l_opy_.format(bstack1l1l11ll1_opy_))
    else:
      logger.debug(bstack1ll1l1ll1l_opy_.format(bstack111lll1_opy_ (u"ࠤࡒࡴࡹ࡯࡭ࡢ࡮ࠣࡌࡺࡨࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦࠥਙ")))
  except Exception as e:
    logger.debug(bstack1ll1l1ll1l_opy_.format(e))
  if bstack111lll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩਚ") in bstack1llll11l11_opy_:
    bstack1l1l11111l_opy_(bstack1ll111lll1_opy_, bstack111l11111_opy_)
  bstack1ll1111l11_opy_ = self.session_id
  if bstack111lll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫਛ") in bstack1llll11l11_opy_ or bstack111lll1_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬਜ") in bstack1llll11l11_opy_ or bstack111lll1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬਝ") in bstack1llll11l11_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
    bstack1llll11l1_opy_.bstack1ll11l1ll_opy_(self)
  bstack1lllllllll_opy_.append(self)
  if bstack111lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪਞ") in CONFIG and bstack111lll1_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ਟ") in CONFIG[bstack111lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬਠ")][bstack11l1l1111_opy_]:
    bstack1l1lll1l11_opy_ = CONFIG[bstack111lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ਡ")][bstack11l1l1111_opy_][bstack111lll1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩਢ")]
  logger.debug(bstack11ll11ll1_opy_.format(bstack1ll1111l11_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    def bstack1l11ll1ll_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack11lllll1l_opy_
      if(bstack111lll1_opy_ (u"ࠧ࡯࡮ࡥࡧࡻ࠲࡯ࡹࠢਣ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack111lll1_opy_ (u"࠭ࡾࠨਤ")), bstack111lll1_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧਥ"), bstack111lll1_opy_ (u"ࠨ࠰ࡶࡩࡸࡹࡩࡰࡰ࡬ࡨࡸ࠴ࡴࡹࡶࠪਦ")), bstack111lll1_opy_ (u"ࠩࡺࠫਧ")) as fp:
          fp.write(bstack111lll1_opy_ (u"ࠥࠦਨ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack111lll1_opy_ (u"ࠦ࡮ࡴࡤࡦࡺࡢࡦࡸࡺࡡࡤ࡭࠱࡮ࡸࠨ਩")))):
          with open(args[1], bstack111lll1_opy_ (u"ࠬࡸࠧਪ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack111lll1_opy_ (u"࠭ࡡࡴࡻࡱࡧࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡠࡰࡨࡻࡕࡧࡧࡦࠪࡦࡳࡳࡺࡥࡹࡶ࠯ࠤࡵࡧࡧࡦࠢࡀࠤࡻࡵࡩࡥࠢ࠳࠭ࠬਫ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1lll11111_opy_)
            lines.insert(1, bstack11ll1l11_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack111lll1_opy_ (u"ࠢࡪࡰࡧࡩࡽࡥࡢࡴࡶࡤࡧࡰ࠴ࡪࡴࠤਬ")), bstack111lll1_opy_ (u"ࠨࡹࠪਭ")) as bstack11lll1lll_opy_:
              bstack11lll1lll_opy_.writelines(lines)
        CONFIG[bstack111lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫਮ")] = str(bstack1llll11l11_opy_) + str(__version__)
        bstack11l1l1111_opy_ = 0 if bstack1ll111lll1_opy_ < 0 else bstack1ll111lll1_opy_
        try:
          if bstack11l1l11ll_opy_ is True:
            bstack11l1l1111_opy_ = int(multiprocessing.current_process().name)
          elif bstack1lll1ll11l_opy_ is True:
            bstack11l1l1111_opy_ = int(threading.current_thread().name)
        except:
          bstack11l1l1111_opy_ = 0
        CONFIG[bstack111lll1_opy_ (u"ࠥࡹࡸ࡫ࡗ࠴ࡅࠥਯ")] = False
        CONFIG[bstack111lll1_opy_ (u"ࠦ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥਰ")] = True
        bstack1lll1l11ll_opy_ = bstack11l11l1l1_opy_(CONFIG, bstack11l1l1111_opy_)
        logger.debug(bstack1l1l11lll_opy_.format(str(bstack1lll1l11ll_opy_)))
        if CONFIG.get(bstack111lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ਱")):
          bstack11111l111_opy_(bstack1lll1l11ll_opy_)
        if bstack111lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩਲ") in CONFIG and bstack111lll1_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬਲ਼") in CONFIG[bstack111lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ਴")][bstack11l1l1111_opy_]:
          bstack1l1lll1l11_opy_ = CONFIG[bstack111lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬਵ")][bstack11l1l1111_opy_][bstack111lll1_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨਸ਼")]
        args.append(os.path.join(os.path.expanduser(bstack111lll1_opy_ (u"ࠫࢃ࠭਷")), bstack111lll1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬਸ"), bstack111lll1_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨਹ")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack1lll1l11ll_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack111lll1_opy_ (u"ࠢࡪࡰࡧࡩࡽࡥࡢࡴࡶࡤࡧࡰ࠴ࡪࡴࠤ਺"))
      bstack11lllll1l_opy_ = True
      return bstack1ll11l1l1_opy_(self, args, bufsize=bufsize, executable=executable,
                    stdin=stdin, stdout=stdout, stderr=stderr,
                    preexec_fn=preexec_fn, close_fds=close_fds,
                    shell=shell, cwd=cwd, env=env, universal_newlines=universal_newlines,
                    startupinfo=startupinfo, creationflags=creationflags,
                    restore_signals=restore_signals, start_new_session=start_new_session,
                    pass_fds=pass_fds, user=user, group=group, extra_groups=extra_groups,
                    encoding=encoding, errors=errors, text=text, umask=umask, pipesize=pipesize)
  except Exception as e:
    pass
  import playwright._impl._api_structures
  import playwright._impl._helper
  def bstack1llll11l1l_opy_(self,
        executablePath = None,
        channel = None,
        args = None,
        ignoreDefaultArgs = None,
        handleSIGINT = None,
        handleSIGTERM = None,
        handleSIGHUP = None,
        timeout = None,
        env = None,
        headless = None,
        devtools = None,
        proxy = None,
        downloadsPath = None,
        slowMo = None,
        tracesDir = None,
        chromiumSandbox = None,
        firefoxUserPrefs = None
        ):
    global CONFIG
    global bstack1ll111lll1_opy_
    global bstack1l1lll1l11_opy_
    global bstack11l1l11ll_opy_
    global bstack1lll1ll11l_opy_
    global bstack1llll11l11_opy_
    CONFIG[bstack111lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪ਻")] = str(bstack1llll11l11_opy_) + str(__version__)
    bstack11l1l1111_opy_ = 0 if bstack1ll111lll1_opy_ < 0 else bstack1ll111lll1_opy_
    try:
      if bstack11l1l11ll_opy_ is True:
        bstack11l1l1111_opy_ = int(multiprocessing.current_process().name)
      elif bstack1lll1ll11l_opy_ is True:
        bstack11l1l1111_opy_ = int(threading.current_thread().name)
    except:
      bstack11l1l1111_opy_ = 0
    CONFIG[bstack111lll1_opy_ (u"ࠤ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ਼ࠣ")] = True
    bstack1lll1l11ll_opy_ = bstack11l11l1l1_opy_(CONFIG, bstack11l1l1111_opy_)
    logger.debug(bstack1l1l11lll_opy_.format(str(bstack1lll1l11ll_opy_)))
    if CONFIG.get(bstack111lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ਽")):
      bstack11111l111_opy_(bstack1lll1l11ll_opy_)
    if bstack111lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧਾ") in CONFIG and bstack111lll1_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪਿ") in CONFIG[bstack111lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩੀ")][bstack11l1l1111_opy_]:
      bstack1l1lll1l11_opy_ = CONFIG[bstack111lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪੁ")][bstack11l1l1111_opy_][bstack111lll1_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ੂ")]
    import urllib
    import json
    bstack11l111lll_opy_ = bstack111lll1_opy_ (u"ࠩࡺࡷࡸࡀ࠯࠰ࡥࡧࡴ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࡄࡩࡡࡱࡵࡀࠫ੃") + urllib.parse.quote(json.dumps(bstack1lll1l11ll_opy_))
    browser = self.connect(bstack11l111lll_opy_)
    return browser
except Exception as e:
    pass
def bstack11l111ll1_opy_():
    global bstack11lllll1l_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        BrowserType.launch = bstack1llll11l1l_opy_
        bstack11lllll1l_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack1l11ll1ll_opy_
      bstack11lllll1l_opy_ = True
    except Exception as e:
      pass
def bstack1l1l1l1l_opy_(context, bstack11ll1l1ll_opy_):
  try:
    context.page.evaluate(bstack111lll1_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦ੄"), bstack111lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠨ੅")+ json.dumps(bstack11ll1l1ll_opy_) + bstack111lll1_opy_ (u"ࠧࢃࡽࠣ੆"))
  except Exception as e:
    logger.debug(bstack111lll1_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠡࡽࢀࠦੇ"), e)
def bstack1ll1lll1l_opy_(context, message, level):
  try:
    context.page.evaluate(bstack111lll1_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣੈ"), bstack111lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭੉") + json.dumps(message) + bstack111lll1_opy_ (u"ࠩ࠯ࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠬ੊") + json.dumps(level) + bstack111lll1_opy_ (u"ࠪࢁࢂ࠭ੋ"))
  except Exception as e:
    logger.debug(bstack111lll1_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡢࡰࡱࡳࡹࡧࡴࡪࡱࡱࠤࢀࢃࠢੌ"), e)
def bstack11111l1ll_opy_(self, url):
  global bstack1lll1l1l1l_opy_
  try:
    bstack11l1llll1_opy_(url)
  except Exception as err:
    logger.debug(bstack1lll1l111l_opy_.format(str(err)))
  try:
    bstack1lll1l1l1l_opy_(self, url)
  except Exception as e:
    try:
      bstack111l1l111_opy_ = str(e)
      if any(err_msg in bstack111l1l111_opy_ for err_msg in bstack11111ll1_opy_):
        bstack11l1llll1_opy_(url, True)
    except Exception as err:
      logger.debug(bstack1lll1l111l_opy_.format(str(err)))
    raise e
def bstack111111ll_opy_(self):
  global bstack111lll11l_opy_
  bstack111lll11l_opy_ = self
  return
def bstack1111l1lll_opy_(self):
  global bstack1l11ll1l1_opy_
  bstack1l11ll1l1_opy_ = self
  return
def bstack1ll111lll_opy_(test_name, bstack1l1l1ll1_opy_):
  global CONFIG
  if CONFIG.get(bstack111lll1_opy_ (u"ࠬࡶࡥࡳࡥࡼ੍ࠫ"), False):
    bstack1ll1lll11_opy_ = os.path.relpath(bstack1l1l1ll1_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack1ll1lll11_opy_)
    bstack1lll1lll1l_opy_ = suite_name + bstack111lll1_opy_ (u"ࠨ࠭ࠣ੎") + test_name
    threading.current_thread().percySessionName = bstack1lll1lll1l_opy_
def bstack111ll111l_opy_(self, test, *args, **kwargs):
  global bstack1l1llll11l_opy_
  test_name = None
  bstack1l1l1ll1_opy_ = None
  if test:
    test_name = str(test.name)
    bstack1l1l1ll1_opy_ = str(test.source)
  bstack1ll111lll_opy_(test_name, bstack1l1l1ll1_opy_)
  bstack1l1llll11l_opy_(self, test, *args, **kwargs)
def bstack1ll1llll11_opy_(driver, bstack1lll1lll1l_opy_):
  if not bstack11l11lll_opy_ and bstack1lll1lll1l_opy_:
      bstack1l111l111_opy_ = {
          bstack111lll1_opy_ (u"ࠧࡢࡥࡷ࡭ࡴࡴࠧ੏"): bstack111lll1_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ੐"),
          bstack111lll1_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬੑ"): {
              bstack111lll1_opy_ (u"ࠪࡲࡦࡳࡥࠨ੒"): bstack1lll1lll1l_opy_
          }
      }
      bstack1ll1l1ll1_opy_ = bstack111lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩ੓").format(json.dumps(bstack1l111l111_opy_))
      driver.execute_script(bstack1ll1l1ll1_opy_)
  if bstack111ll1l11_opy_:
      bstack1ll1l1ll_opy_ = {
          bstack111lll1_opy_ (u"ࠬࡧࡣࡵ࡫ࡲࡲࠬ੔"): bstack111lll1_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨ੕"),
          bstack111lll1_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ੖"): {
              bstack111lll1_opy_ (u"ࠨࡦࡤࡸࡦ࠭੗"): bstack1lll1lll1l_opy_ + bstack111lll1_opy_ (u"ࠩࠣࡴࡦࡹࡳࡦࡦࠤࠫ੘"),
              bstack111lll1_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩਖ਼"): bstack111lll1_opy_ (u"ࠫ࡮ࡴࡦࡰࠩਗ਼")
          }
      }
      if bstack111ll1l11_opy_.status == bstack111lll1_opy_ (u"ࠬࡖࡁࡔࡕࠪਜ਼"):
          bstack1lllllll1l_opy_ = bstack111lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫੜ").format(json.dumps(bstack1ll1l1ll_opy_))
          driver.execute_script(bstack1lllllll1l_opy_)
          bstack1l11ll11_opy_(driver, bstack111lll1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ੝"))
      elif bstack111ll1l11_opy_.status == bstack111lll1_opy_ (u"ࠨࡈࡄࡍࡑ࠭ਫ਼"):
          reason = bstack111lll1_opy_ (u"ࠤࠥ੟")
          bstack1111llll1_opy_ = bstack1lll1lll1l_opy_ + bstack111lll1_opy_ (u"ࠪࠤ࡫ࡧࡩ࡭ࡧࡧࠫ੠")
          if bstack111ll1l11_opy_.message:
              reason = str(bstack111ll1l11_opy_.message)
              bstack1111llll1_opy_ = bstack1111llll1_opy_ + bstack111lll1_opy_ (u"ࠫࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳ࠼ࠣࠫ੡") + reason
          bstack1ll1l1ll_opy_[bstack111lll1_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ੢")] = {
              bstack111lll1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ੣"): bstack111lll1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭੤"),
              bstack111lll1_opy_ (u"ࠨࡦࡤࡸࡦ࠭੥"): bstack1111llll1_opy_
          }
          bstack1lllllll1l_opy_ = bstack111lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠧ੦").format(json.dumps(bstack1ll1l1ll_opy_))
          driver.execute_script(bstack1lllllll1l_opy_)
          bstack1l11ll11_opy_(driver, bstack111lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ੧"), reason)
          bstack1l1lllll1l_opy_(reason, str(bstack111ll1l11_opy_), str(bstack1ll111lll1_opy_), logger)
def bstack11ll11111_opy_(driver, test):
  if CONFIG.get(bstack111lll1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪ੨"), False) and CONFIG.get(bstack111lll1_opy_ (u"ࠬࡶࡥࡳࡥࡼࡇࡦࡶࡴࡶࡴࡨࡑࡴࡪࡥࠨ੩"), bstack111lll1_opy_ (u"ࠨࡡࡶࡶࡲࠦ੪")) == bstack111lll1_opy_ (u"ࠢࡵࡧࡶࡸࡨࡧࡳࡦࠤ੫"):
      bstack1l1111lll_opy_ = bstack1ll1111111_opy_(threading.current_thread(), bstack111lll1_opy_ (u"ࠨࡲࡨࡶࡨࡿࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ੬"), None)
      bstack11lll1l11_opy_(driver, bstack1l1111lll_opy_)
  if bstack1ll1111111_opy_(threading.current_thread(), bstack111lll1_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭੭"), None) and bstack1ll1111111_opy_(
          threading.current_thread(), bstack111lll1_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ੮"), None):
      logger.info(bstack111lll1_opy_ (u"ࠦࡆࡻࡴࡰ࡯ࡤࡸࡪࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡨࡼࡪࡩࡵࡵ࡫ࡲࡲࠥ࡮ࡡࡴࠢࡨࡲࡩ࡫ࡤ࠯ࠢࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡦࡰࡴࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡮ࡹࠠࡶࡰࡧࡩࡷࡽࡡࡺ࠰ࠣࠦ੯"))
      bstack1lllll1111_opy_.bstack111lll11_opy_(driver, class_name=test.parent.name, name=test.name, module_name=None,
                              path=test.source, bstack1lll1ll1l_opy_=bstack11l1l1l1_opy_)
def bstack1ll1l1111l_opy_(test, bstack1lll1lll1l_opy_):
    try:
      data = {}
      if test:
        data[bstack111lll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪੰ")] = bstack1lll1lll1l_opy_
      if bstack111ll1l11_opy_:
        if bstack111ll1l11_opy_.status == bstack111lll1_opy_ (u"࠭ࡐࡂࡕࡖࠫੱ"):
          data[bstack111lll1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧੲ")] = bstack111lll1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨੳ")
        elif bstack111ll1l11_opy_.status == bstack111lll1_opy_ (u"ࠩࡉࡅࡎࡒࠧੴ"):
          data[bstack111lll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪੵ")] = bstack111lll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ੶")
          if bstack111ll1l11_opy_.message:
            data[bstack111lll1_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬ੷")] = str(bstack111ll1l11_opy_.message)
      user = CONFIG[bstack111lll1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ੸")]
      key = CONFIG[bstack111lll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ੹")]
      url = bstack111lll1_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡾࢁ࠿ࢁࡽࡁࡣࡳ࡭࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡣࡸࡸࡴࡳࡡࡵࡧ࠲ࡷࡪࡹࡳࡪࡱࡱࡷ࠴ࢁࡽ࠯࡬ࡶࡳࡳ࠭੺").format(user, key, bstack1ll1111l11_opy_)
      headers = {
        bstack111lll1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨ੻"): bstack111lll1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭੼"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers)
    except Exception as e:
      logger.error(bstack1ll1l11ll_opy_.format(str(e)))
def bstack1ll11l111l_opy_(test, bstack1lll1lll1l_opy_):
  global CONFIG
  global bstack1l11ll1l1_opy_
  global bstack111lll11l_opy_
  global bstack1ll1111l11_opy_
  global bstack111ll1l11_opy_
  global bstack1l1lll1l11_opy_
  global bstack1l1ll1l1l1_opy_
  global bstack11l111l11_opy_
  global bstack1llll111l1_opy_
  global bstack1l1l11l1ll_opy_
  global bstack1lllllllll_opy_
  global bstack11l1l1l1_opy_
  try:
    if not bstack1ll1111l11_opy_:
      with open(os.path.join(os.path.expanduser(bstack111lll1_opy_ (u"ࠫࢃ࠭੽")), bstack111lll1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ੾"), bstack111lll1_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨ੿"))) as f:
        bstack1ll11111_opy_ = json.loads(bstack111lll1_opy_ (u"ࠢࡼࠤ઀") + f.read().strip() + bstack111lll1_opy_ (u"ࠨࠤࡻࠦ࠿ࠦࠢࡺࠤࠪઁ") + bstack111lll1_opy_ (u"ࠤࢀࠦં"))
        bstack1ll1111l11_opy_ = bstack1ll11111_opy_[str(threading.get_ident())]
  except:
    pass
  if bstack1lllllllll_opy_:
    for driver in bstack1lllllllll_opy_:
      if bstack1ll1111l11_opy_ == driver.session_id:
        if test:
          bstack11ll11111_opy_(driver, test)
        bstack1ll1llll11_opy_(driver, bstack1lll1lll1l_opy_)
  elif bstack1ll1111l11_opy_:
    bstack1ll1l1111l_opy_(test, bstack1lll1lll1l_opy_)
  if bstack1l11ll1l1_opy_:
    bstack11l111l11_opy_(bstack1l11ll1l1_opy_)
  if bstack111lll11l_opy_:
    bstack1llll111l1_opy_(bstack111lll11l_opy_)
  if bstack1l1l1l1111_opy_:
    bstack1l1l11l1ll_opy_()
def bstack1lllllll11_opy_(self, test, *args, **kwargs):
  bstack1lll1lll1l_opy_ = None
  if test:
    bstack1lll1lll1l_opy_ = str(test.name)
  bstack1ll11l111l_opy_(test, bstack1lll1lll1l_opy_)
  bstack1l1ll1l1l1_opy_(self, test, *args, **kwargs)
def bstack1111l1l11_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack111l11l1l_opy_
  global CONFIG
  global bstack1lllllllll_opy_
  global bstack1ll1111l11_opy_
  bstack1l1l1ll11_opy_ = None
  try:
    if bstack1ll1111111_opy_(threading.current_thread(), bstack111lll1_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩઃ"), None):
      try:
        if not bstack1ll1111l11_opy_:
          with open(os.path.join(os.path.expanduser(bstack111lll1_opy_ (u"ࠫࢃ࠭઄")), bstack111lll1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬઅ"), bstack111lll1_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨઆ"))) as f:
            bstack1ll11111_opy_ = json.loads(bstack111lll1_opy_ (u"ࠢࡼࠤઇ") + f.read().strip() + bstack111lll1_opy_ (u"ࠨࠤࡻࠦ࠿ࠦࠢࡺࠤࠪઈ") + bstack111lll1_opy_ (u"ࠤࢀࠦઉ"))
            bstack1ll1111l11_opy_ = bstack1ll11111_opy_[str(threading.get_ident())]
      except:
        pass
      if bstack1lllllllll_opy_:
        for driver in bstack1lllllllll_opy_:
          if bstack1ll1111l11_opy_ == driver.session_id:
            bstack1l1l1ll11_opy_ = driver
    bstack11l1ll111_opy_ = bstack1lllll1111_opy_.bstack1l11l1ll1_opy_(CONFIG, test.tags)
    if bstack1l1l1ll11_opy_:
      threading.current_thread().isA11yTest = bstack1lllll1111_opy_.bstack1l1ll1lll_opy_(bstack1l1l1ll11_opy_, bstack11l1ll111_opy_)
    else:
      threading.current_thread().isA11yTest = bstack11l1ll111_opy_
  except:
    pass
  bstack111l11l1l_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack111ll1l11_opy_
  bstack111ll1l11_opy_ = self._test
def bstack1lllll11_opy_():
  global bstack1l1l1l11l1_opy_
  try:
    if os.path.exists(bstack1l1l1l11l1_opy_):
      os.remove(bstack1l1l1l11l1_opy_)
  except Exception as e:
    logger.debug(bstack111lll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡪࡥ࡭ࡧࡷ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ઊ") + str(e))
def bstack1l1lll1l1_opy_():
  global bstack1l1l1l11l1_opy_
  bstack111llllll_opy_ = {}
  try:
    if not os.path.isfile(bstack1l1l1l11l1_opy_):
      with open(bstack1l1l1l11l1_opy_, bstack111lll1_opy_ (u"ࠫࡼ࠭ઋ")):
        pass
      with open(bstack1l1l1l11l1_opy_, bstack111lll1_opy_ (u"ࠧࡽࠫࠣઌ")) as outfile:
        json.dump({}, outfile)
    if os.path.exists(bstack1l1l1l11l1_opy_):
      bstack111llllll_opy_ = json.load(open(bstack1l1l1l11l1_opy_, bstack111lll1_opy_ (u"࠭ࡲࡣࠩઍ")))
  except Exception as e:
    logger.debug(bstack111lll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡵࡩࡦࡪࡩ࡯ࡩࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺ࠡࠩ઎") + str(e))
  finally:
    return bstack111llllll_opy_
def bstack1l1l11111l_opy_(platform_index, item_index):
  global bstack1l1l1l11l1_opy_
  try:
    bstack111llllll_opy_ = bstack1l1lll1l1_opy_()
    bstack111llllll_opy_[item_index] = platform_index
    with open(bstack1l1l1l11l1_opy_, bstack111lll1_opy_ (u"ࠣࡹ࠮ࠦએ")) as outfile:
      json.dump(bstack111llllll_opy_, outfile)
  except Exception as e:
    logger.debug(bstack111lll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡼࡸࡩࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠠࡧ࡫࡯ࡩ࠿ࠦࠧઐ") + str(e))
def bstack1llllll11_opy_(bstack1llll1llll_opy_):
  global CONFIG
  bstack1lll1l1ll_opy_ = bstack111lll1_opy_ (u"ࠪࠫઑ")
  if not bstack111lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ઒") in CONFIG:
    logger.info(bstack111lll1_opy_ (u"ࠬࡔ࡯ࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠤࡵࡧࡳࡴࡧࡧࠤࡺࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡨࡧࡱࡩࡷࡧࡴࡦࠢࡵࡩࡵࡵࡲࡵࠢࡩࡳࡷࠦࡒࡰࡤࡲࡸࠥࡸࡵ࡯ࠩઓ"))
  try:
    platform = CONFIG[bstack111lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩઔ")][bstack1llll1llll_opy_]
    if bstack111lll1_opy_ (u"ࠧࡰࡵࠪક") in platform:
      bstack1lll1l1ll_opy_ += str(platform[bstack111lll1_opy_ (u"ࠨࡱࡶࠫખ")]) + bstack111lll1_opy_ (u"ࠩ࠯ࠤࠬગ")
    if bstack111lll1_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ઘ") in platform:
      bstack1lll1l1ll_opy_ += str(platform[bstack111lll1_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧઙ")]) + bstack111lll1_opy_ (u"ࠬ࠲ࠠࠨચ")
    if bstack111lll1_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪછ") in platform:
      bstack1lll1l1ll_opy_ += str(platform[bstack111lll1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫજ")]) + bstack111lll1_opy_ (u"ࠨ࠮ࠣࠫઝ")
    if bstack111lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫઞ") in platform:
      bstack1lll1l1ll_opy_ += str(platform[bstack111lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬટ")]) + bstack111lll1_opy_ (u"ࠫ࠱ࠦࠧઠ")
    if bstack111lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪડ") in platform:
      bstack1lll1l1ll_opy_ += str(platform[bstack111lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫઢ")]) + bstack111lll1_opy_ (u"ࠧ࠭ࠢࠪણ")
    if bstack111lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩત") in platform:
      bstack1lll1l1ll_opy_ += str(platform[bstack111lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪથ")]) + bstack111lll1_opy_ (u"ࠪ࠰ࠥ࠭દ")
  except Exception as e:
    logger.debug(bstack111lll1_opy_ (u"ࠫࡘࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫࡮ࡦࡴࡤࡸ࡮ࡴࡧࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡷࡹࡸࡩ࡯ࡩࠣࡪࡴࡸࠠࡳࡧࡳࡳࡷࡺࠠࡨࡧࡱࡩࡷࡧࡴࡪࡱࡱࠫધ") + str(e))
  finally:
    if bstack1lll1l1ll_opy_[len(bstack1lll1l1ll_opy_) - 2:] == bstack111lll1_opy_ (u"ࠬ࠲ࠠࠨન"):
      bstack1lll1l1ll_opy_ = bstack1lll1l1ll_opy_[:-2]
    return bstack1lll1l1ll_opy_
def bstack1l11l111_opy_(path, bstack1lll1l1ll_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack1ll11l11l1_opy_ = ET.parse(path)
    bstack1l1l1l111l_opy_ = bstack1ll11l11l1_opy_.getroot()
    bstack1ll1l1l1ll_opy_ = None
    for suite in bstack1l1l1l111l_opy_.iter(bstack111lll1_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬ઩")):
      if bstack111lll1_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧપ") in suite.attrib:
        suite.attrib[bstack111lll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ફ")] += bstack111lll1_opy_ (u"ࠩࠣࠫબ") + bstack1lll1l1ll_opy_
        bstack1ll1l1l1ll_opy_ = suite
    bstack1lll1l1ll1_opy_ = None
    for robot in bstack1l1l1l111l_opy_.iter(bstack111lll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩભ")):
      bstack1lll1l1ll1_opy_ = robot
    bstack1l1l111l1l_opy_ = len(bstack1lll1l1ll1_opy_.findall(bstack111lll1_opy_ (u"ࠫࡸࡻࡩࡵࡧࠪમ")))
    if bstack1l1l111l1l_opy_ == 1:
      bstack1lll1l1ll1_opy_.remove(bstack1lll1l1ll1_opy_.findall(bstack111lll1_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫય"))[0])
      bstack1lllll11l_opy_ = ET.Element(bstack111lll1_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬર"), attrib={bstack111lll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ઱"): bstack111lll1_opy_ (u"ࠨࡕࡸ࡭ࡹ࡫ࡳࠨલ"), bstack111lll1_opy_ (u"ࠩ࡬ࡨࠬળ"): bstack111lll1_opy_ (u"ࠪࡷ࠵࠭઴")})
      bstack1lll1l1ll1_opy_.insert(1, bstack1lllll11l_opy_)
      bstack1ll1lll1_opy_ = None
      for suite in bstack1lll1l1ll1_opy_.iter(bstack111lll1_opy_ (u"ࠫࡸࡻࡩࡵࡧࠪવ")):
        bstack1ll1lll1_opy_ = suite
      bstack1ll1lll1_opy_.append(bstack1ll1l1l1ll_opy_)
      bstack1lllll1ll_opy_ = None
      for status in bstack1ll1l1l1ll_opy_.iter(bstack111lll1_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬશ")):
        bstack1lllll1ll_opy_ = status
      bstack1ll1lll1_opy_.append(bstack1lllll1ll_opy_)
    bstack1ll11l11l1_opy_.write(path)
  except Exception as e:
    logger.debug(bstack111lll1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡶࡸ࡯࡮ࡨࠢࡺ࡬࡮ࡲࡥࠡࡩࡨࡲࡪࡸࡡࡵ࡫ࡱ࡫ࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠫષ") + str(e))
def bstack1l11l11l1_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack1l11l11l_opy_
  global CONFIG
  if bstack111lll1_opy_ (u"ࠢࡱࡻࡷ࡬ࡴࡴࡰࡢࡶ࡫ࠦસ") in options:
    del options[bstack111lll1_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࡱࡣࡷ࡬ࠧહ")]
  bstack1l1llll1l_opy_ = bstack1l1lll1l1_opy_()
  for bstack1l11l1ll_opy_ in bstack1l1llll1l_opy_.keys():
    path = os.path.join(os.getcwd(), bstack111lll1_opy_ (u"ࠩࡳࡥࡧࡵࡴࡠࡴࡨࡷࡺࡲࡴࡴࠩ઺"), str(bstack1l11l1ll_opy_), bstack111lll1_opy_ (u"ࠪࡳࡺࡺࡰࡶࡶ࠱ࡼࡲࡲࠧ઻"))
    bstack1l11l111_opy_(path, bstack1llllll11_opy_(bstack1l1llll1l_opy_[bstack1l11l1ll_opy_]))
  bstack1lllll11_opy_()
  return bstack1l11l11l_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack1ll11l1111_opy_(self, ff_profile_dir):
  global bstack1ll1lllll_opy_
  if not ff_profile_dir:
    return None
  return bstack1ll1lllll_opy_(self, ff_profile_dir)
def bstack1l1111l11_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1111l1l1l_opy_
  bstack1llll1l1l1_opy_ = []
  if bstack111lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹ઼ࠧ") in CONFIG:
    bstack1llll1l1l1_opy_ = CONFIG[bstack111lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨઽ")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack111lll1_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪࠢા")],
      pabot_args[bstack111lll1_opy_ (u"ࠢࡷࡧࡵࡦࡴࡹࡥࠣિ")],
      argfile,
      pabot_args.get(bstack111lll1_opy_ (u"ࠣࡪ࡬ࡺࡪࠨી")),
      pabot_args[bstack111lll1_opy_ (u"ࠤࡳࡶࡴࡩࡥࡴࡵࡨࡷࠧુ")],
      platform[0],
      bstack1111l1l1l_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack111lll1_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸ࡫࡯࡬ࡦࡵࠥૂ")] or [(bstack111lll1_opy_ (u"ࠦࠧૃ"), None)]
    for platform in enumerate(bstack1llll1l1l1_opy_)
  ]
def bstack1lll1111l_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack1l111l1l_opy_=bstack111lll1_opy_ (u"ࠬ࠭ૄ")):
  global bstack11l11111l_opy_
  self.platform_index = platform_index
  self.bstack1l11ll1l_opy_ = bstack1l111l1l_opy_
  bstack11l11111l_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack1ll111llll_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1111llll_opy_
  global bstack111ll1ll_opy_
  if not bstack111lll1_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨૅ") in item.options:
    item.options[bstack111lll1_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩ૆")] = []
  for v in item.options[bstack111lll1_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪે")]:
    if bstack111lll1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡒࡏࡅ࡙ࡌࡏࡓࡏࡌࡒࡉࡋࡘࠨૈ") in v:
      item.options[bstack111lll1_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬૉ")].remove(v)
    if bstack111lll1_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡇࡑࡏࡁࡓࡉࡖࠫ૊") in v:
      item.options[bstack111lll1_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧો")].remove(v)
  item.options[bstack111lll1_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨૌ")].insert(0, bstack111lll1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡐࡍࡃࡗࡊࡔࡘࡍࡊࡐࡇࡉ࡝ࡀࡻࡾ્ࠩ").format(item.platform_index))
  item.options[bstack111lll1_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪ૎")].insert(0, bstack111lll1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡆࡈࡊࡑࡕࡃࡂࡎࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗࡀࡻࡾࠩ૏").format(item.bstack1l11ll1l_opy_))
  if bstack111ll1ll_opy_:
    item.options[bstack111lll1_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬૐ")].insert(0, bstack111lll1_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡇࡑࡏࡁࡓࡉࡖ࠾ࢀࢃࠧ૑").format(bstack111ll1ll_opy_))
  return bstack1111llll_opy_(caller_id, datasources, is_last, item, outs_dir)
def bstack1l111lll_opy_(command, item_index):
  if bstack11l11l111_opy_.get_property(bstack111lll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭૒")):
    os.environ[bstack111lll1_opy_ (u"࠭ࡃࡖࡔࡕࡉࡓ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡇࡅ࡙ࡇࠧ૓")] = json.dumps(CONFIG[bstack111lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ૔")][item_index % bstack1111111l_opy_])
  global bstack111ll1ll_opy_
  if bstack111ll1ll_opy_:
    command[0] = command[0].replace(bstack111lll1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ૕"), bstack111lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠮ࡵࡧ࡯ࠥࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱࠦ࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠ࡫ࡷࡩࡲࡥࡩ࡯ࡦࡨࡼࠥ࠭૖") + str(
      item_index) + bstack111lll1_opy_ (u"ࠪࠤࠬ૗") + bstack111ll1ll_opy_, 1)
  else:
    command[0] = command[0].replace(bstack111lll1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ૘"),
                                    bstack111lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠱ࡸࡪ࡫ࠡࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠢ࠰࠱ࡧࡹࡴࡢࡥ࡮ࡣ࡮ࡺࡥ࡮ࡡ࡬ࡲࡩ࡫ࡸࠡࠩ૙") + str(item_index), 1)
def bstack1lll11111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack111111l11_opy_
  bstack1l111lll_opy_(command, item_index)
  return bstack111111l11_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
def bstack11l1llll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack111111l11_opy_
  bstack1l111lll_opy_(command, item_index)
  return bstack111111l11_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
def bstack11111111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack111111l11_opy_
  bstack1l111lll_opy_(command, item_index)
  return bstack111111l11_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
def bstack1111l11l_opy_(self, runner, quiet=False, capture=True):
  global bstack1lll111ll1_opy_
  bstack1l1llll11_opy_ = bstack1lll111ll1_opy_(self, runner, quiet=False, capture=True)
  if self.exception:
    if not hasattr(runner, bstack111lll1_opy_ (u"࠭ࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࡡࡤࡶࡷ࠭૚")):
      runner.exception_arr = []
    if not hasattr(runner, bstack111lll1_opy_ (u"ࠧࡦࡺࡦࡣࡹࡸࡡࡤࡧࡥࡥࡨࡱ࡟ࡢࡴࡵࠫ૛")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1l1llll11_opy_
def bstack1ll11ll1_opy_(self, name, context, *args):
  os.environ[bstack111lll1_opy_ (u"ࠨࡅࡘࡖࡗࡋࡎࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡉࡇࡔࡂࠩ૜")] = json.dumps(CONFIG[bstack111lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૝")][int(threading.current_thread()._name) % bstack1111111l_opy_])
  global bstack11ll1l111_opy_
  if name == bstack111lll1_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡪࡪࡧࡴࡶࡴࡨࠫ૞"):
    bstack11ll1l111_opy_(self, name, context, *args)
    try:
      if not bstack11l11lll_opy_:
        bstack1l1l1ll11_opy_ = threading.current_thread().bstackSessionDriver if bstack11l111l1l_opy_(bstack111lll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪ૟")) else context.browser
        bstack11ll1l1ll_opy_ = str(self.feature.name)
        bstack1l1l1l1l_opy_(context, bstack11ll1l1ll_opy_)
        bstack1l1l1ll11_opy_.execute_script(bstack111lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠪૠ") + json.dumps(bstack11ll1l1ll_opy_) + bstack111lll1_opy_ (u"࠭ࡽࡾࠩૡ"))
      self.driver_before_scenario = False
    except Exception as e:
      logger.debug(bstack111lll1_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡩ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡩࡩࡦࡺࡵࡳࡧ࠽ࠤࢀࢃࠧૢ").format(str(e)))
  elif name == bstack111lll1_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪૣ"):
    bstack11ll1l111_opy_(self, name, context, *args)
    try:
      if not hasattr(self, bstack111lll1_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࡡࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫ૤")):
        self.driver_before_scenario = True
      if (not bstack11l11lll_opy_):
        scenario_name = args[0].name
        feature_name = bstack11ll1l1ll_opy_ = str(self.feature.name)
        bstack11ll1l1ll_opy_ = feature_name + bstack111lll1_opy_ (u"ࠪࠤ࠲ࠦࠧ૥") + scenario_name
        bstack1l1l1ll11_opy_ = threading.current_thread().bstackSessionDriver if bstack11l111l1l_opy_(bstack111lll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪ૦")) else context.browser
        if self.driver_before_scenario:
          bstack1l1l1l1l_opy_(context, bstack11ll1l1ll_opy_)
          bstack1l1l1ll11_opy_.execute_script(bstack111lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠪ૧") + json.dumps(bstack11ll1l1ll_opy_) + bstack111lll1_opy_ (u"࠭ࡽࡾࠩ૨"))
    except Exception as e:
      logger.debug(bstack111lll1_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡩ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡧࡪࡴࡡࡳ࡫ࡲ࠾ࠥࢁࡽࠨ૩").format(str(e)))
  elif name == bstack111lll1_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠩ૪"):
    try:
      bstack11111111l_opy_ = args[0].status.name
      bstack1l1l1ll11_opy_ = threading.current_thread().bstackSessionDriver if bstack111lll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨ૫") in threading.current_thread().__dict__.keys() else context.browser
      if str(bstack11111111l_opy_).lower() == bstack111lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ૬"):
        bstack1l1ll1lll1_opy_ = bstack111lll1_opy_ (u"ࠫࠬ૭")
        bstack111l111l1_opy_ = bstack111lll1_opy_ (u"ࠬ࠭૮")
        bstack1l1llll111_opy_ = bstack111lll1_opy_ (u"࠭ࠧ૯")
        try:
          import traceback
          bstack1l1ll1lll1_opy_ = self.exception.__class__.__name__
          bstack1l1ll111ll_opy_ = traceback.format_tb(self.exc_traceback)
          bstack111l111l1_opy_ = bstack111lll1_opy_ (u"ࠧࠡࠩ૰").join(bstack1l1ll111ll_opy_)
          bstack1l1llll111_opy_ = bstack1l1ll111ll_opy_[-1]
        except Exception as e:
          logger.debug(bstack1lll1l11_opy_.format(str(e)))
        bstack1l1ll1lll1_opy_ += bstack1l1llll111_opy_
        bstack1ll1lll1l_opy_(context, json.dumps(str(args[0].name) + bstack111lll1_opy_ (u"ࠣࠢ࠰ࠤࡋࡧࡩ࡭ࡧࡧࠥࡡࡴࠢ૱") + str(bstack111l111l1_opy_)),
                            bstack111lll1_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣ૲"))
        if self.driver_before_scenario:
          bstack1lll11l11_opy_(getattr(context, bstack111lll1_opy_ (u"ࠪࡴࡦ࡭ࡥࠨ૳"), None), bstack111lll1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦ૴"), bstack1l1ll1lll1_opy_)
          bstack1l1l1ll11_opy_.execute_script(bstack111lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪ૵") + json.dumps(str(args[0].name) + bstack111lll1_opy_ (u"ࠨࠠ࠮ࠢࡉࡥ࡮ࡲࡥࡥࠣ࡟ࡲࠧ૶") + str(bstack111l111l1_opy_)) + bstack111lll1_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡫ࡲࡳࡱࡵࠦࢂࢃࠧ૷"))
        if self.driver_before_scenario:
          bstack1l11ll11_opy_(bstack1l1l1ll11_opy_, bstack111lll1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ૸"), bstack111lll1_opy_ (u"ࠤࡖࡧࡪࡴࡡࡳ࡫ࡲࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡼ࡯ࡴࡩ࠼ࠣࡠࡳࠨૹ") + str(bstack1l1ll1lll1_opy_))
      else:
        bstack1ll1lll1l_opy_(context, bstack111lll1_opy_ (u"ࠥࡔࡦࡹࡳࡦࡦࠤࠦૺ"), bstack111lll1_opy_ (u"ࠦ࡮ࡴࡦࡰࠤૻ"))
        if self.driver_before_scenario:
          bstack1lll11l11_opy_(getattr(context, bstack111lll1_opy_ (u"ࠬࡶࡡࡨࡧࠪૼ"), None), bstack111lll1_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨ૽"))
        bstack1l1l1ll11_opy_.execute_script(bstack111lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬ૾") + json.dumps(str(args[0].name) + bstack111lll1_opy_ (u"ࠣࠢ࠰ࠤࡕࡧࡳࡴࡧࡧࠥࠧ૿")) + bstack111lll1_opy_ (u"ࠩ࠯ࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡪࡰࡩࡳࠧࢃࡽࠨ଀"))
        if self.driver_before_scenario:
          bstack1l11ll11_opy_(bstack1l1l1ll11_opy_, bstack111lll1_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥଁ"))
    except Exception as e:
      logger.debug(bstack111lll1_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠ࡮ࡣࡵ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡷࡹࡸࠦࡩ࡯ࠢࡤࡪࡹ࡫ࡲࠡࡨࡨࡥࡹࡻࡲࡦ࠼ࠣࡿࢂ࠭ଂ").format(str(e)))
  elif name == bstack111lll1_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣ࡫࡫ࡡࡵࡷࡵࡩࠬଃ"):
    try:
      bstack1l1l1ll11_opy_ = threading.current_thread().bstackSessionDriver if bstack11l111l1l_opy_(bstack111lll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬ଄")) else context.browser
      if context.failed is True:
        bstack1l1l1l1l1l_opy_ = []
        bstack1ll111l1ll_opy_ = []
        bstack11ll111ll_opy_ = []
        bstack1l1l1111_opy_ = bstack111lll1_opy_ (u"ࠧࠨଅ")
        try:
          import traceback
          for exc in self.exception_arr:
            bstack1l1l1l1l1l_opy_.append(exc.__class__.__name__)
          for exc_tb in self.exc_traceback_arr:
            bstack1l1ll111ll_opy_ = traceback.format_tb(exc_tb)
            bstack1ll11lllll_opy_ = bstack111lll1_opy_ (u"ࠨࠢࠪଆ").join(bstack1l1ll111ll_opy_)
            bstack1ll111l1ll_opy_.append(bstack1ll11lllll_opy_)
            bstack11ll111ll_opy_.append(bstack1l1ll111ll_opy_[-1])
        except Exception as e:
          logger.debug(bstack1lll1l11_opy_.format(str(e)))
        bstack1l1ll1lll1_opy_ = bstack111lll1_opy_ (u"ࠩࠪଇ")
        for i in range(len(bstack1l1l1l1l1l_opy_)):
          bstack1l1ll1lll1_opy_ += bstack1l1l1l1l1l_opy_[i] + bstack11ll111ll_opy_[i] + bstack111lll1_opy_ (u"ࠪࡠࡳ࠭ଈ")
        bstack1l1l1111_opy_ = bstack111lll1_opy_ (u"ࠫࠥ࠭ଉ").join(bstack1ll111l1ll_opy_)
        if not self.driver_before_scenario:
          bstack1ll1lll1l_opy_(context, bstack1l1l1111_opy_, bstack111lll1_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦଊ"))
          bstack1lll11l11_opy_(getattr(context, bstack111lll1_opy_ (u"࠭ࡰࡢࡩࡨࠫଋ"), None), bstack111lll1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢଌ"), bstack1l1ll1lll1_opy_)
          bstack1l1l1ll11_opy_.execute_script(bstack111lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭଍") + json.dumps(bstack1l1l1111_opy_) + bstack111lll1_opy_ (u"ࠩ࠯ࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡦࡴࡵࡳࡷࠨࡽࡾࠩ଎"))
          bstack1l11ll11_opy_(bstack1l1l1ll11_opy_, bstack111lll1_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥଏ"), bstack111lll1_opy_ (u"ࠦࡘࡵ࡭ࡦࠢࡶࡧࡪࡴࡡࡳ࡫ࡲࡷࠥ࡬ࡡࡪ࡮ࡨࡨ࠿ࠦ࡜࡯ࠤଐ") + str(bstack1l1ll1lll1_opy_))
          bstack1llll1lll1_opy_ = bstack1l11111ll_opy_(bstack1l1l1111_opy_, self.feature.name, logger)
          if (bstack1llll1lll1_opy_ != None):
            bstack1l11lllll_opy_.append(bstack1llll1lll1_opy_)
      else:
        if not self.driver_before_scenario:
          bstack1ll1lll1l_opy_(context, bstack111lll1_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࡀࠠࠣ଑") + str(self.feature.name) + bstack111lll1_opy_ (u"ࠨࠠࡱࡣࡶࡷࡪࡪࠡࠣ଒"), bstack111lll1_opy_ (u"ࠢࡪࡰࡩࡳࠧଓ"))
          bstack1lll11l11_opy_(getattr(context, bstack111lll1_opy_ (u"ࠨࡲࡤ࡫ࡪ࠭ଔ"), None), bstack111lll1_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤକ"))
          bstack1l1l1ll11_opy_.execute_script(bstack111lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨଖ") + json.dumps(bstack111lll1_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩ࠿ࠦࠢଗ") + str(self.feature.name) + bstack111lll1_opy_ (u"ࠧࠦࡰࡢࡵࡶࡩࡩࠧࠢଘ")) + bstack111lll1_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤࢀࢁࠬଙ"))
          bstack1l11ll11_opy_(bstack1l1l1ll11_opy_, bstack111lll1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧଚ"))
          bstack1llll1lll1_opy_ = bstack1l11111ll_opy_(bstack1l1l1111_opy_, self.feature.name, logger)
          if (bstack1llll1lll1_opy_ != None):
            bstack1l11lllll_opy_.append(bstack1llll1lll1_opy_)
    except Exception as e:
      logger.debug(bstack111lll1_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡲࡧࡲ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣ࡭ࡳࠦࡡࡧࡶࡨࡶࠥ࡬ࡥࡢࡶࡸࡶࡪࡀࠠࡼࡿࠪଛ").format(str(e)))
  else:
    bstack11ll1l111_opy_(self, name, context, *args)
  if name in [bstack111lll1_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡨࡨࡥࡹࡻࡲࡦࠩଜ"), bstack111lll1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫଝ")]:
    bstack11ll1l111_opy_(self, name, context, *args)
    if (name == bstack111lll1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬଞ") and self.driver_before_scenario) or (
            name == bstack111lll1_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣ࡫࡫ࡡࡵࡷࡵࡩࠬଟ") and not self.driver_before_scenario):
      try:
        bstack1l1l1ll11_opy_ = threading.current_thread().bstackSessionDriver if bstack11l111l1l_opy_(bstack111lll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬଠ")) else context.browser
        bstack1l1l1ll11_opy_.quit()
      except Exception:
        pass
def bstack1l1lll1111_opy_(config, startdir):
  return bstack111lll1_opy_ (u"ࠢࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡽ࠳ࢁࠧଡ").format(bstack111lll1_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠢଢ"))
notset = Notset()
def bstack1llll11ll_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack1llllll1l1_opy_
  if str(name).lower() == bstack111lll1_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࠩଣ"):
    return bstack111lll1_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠤତ")
  else:
    return bstack1llllll1l1_opy_(self, name, default, skip)
def bstack1l1l11l1l1_opy_(item, when):
  global bstack11111llll_opy_
  try:
    bstack11111llll_opy_(item, when)
  except Exception as e:
    pass
def bstack1ll111l11_opy_():
  return
def bstack11lll111l_opy_(type, name, status, reason, bstack1ll11ll1l_opy_, bstack1l1ll1l111_opy_):
  bstack1l111l111_opy_ = {
    bstack111lll1_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱࠫଥ"): type,
    bstack111lll1_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨଦ"): {}
  }
  if type == bstack111lll1_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨଧ"):
    bstack1l111l111_opy_[bstack111lll1_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪନ")][bstack111lll1_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ଩")] = bstack1ll11ll1l_opy_
    bstack1l111l111_opy_[bstack111lll1_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬପ")][bstack111lll1_opy_ (u"ࠪࡨࡦࡺࡡࠨଫ")] = json.dumps(str(bstack1l1ll1l111_opy_))
  if type == bstack111lll1_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬବ"):
    bstack1l111l111_opy_[bstack111lll1_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨଭ")][bstack111lll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫମ")] = name
  if type == bstack111lll1_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪଯ"):
    bstack1l111l111_opy_[bstack111lll1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫର")][bstack111lll1_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ଱")] = status
    if status == bstack111lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪଲ"):
      bstack1l111l111_opy_[bstack111lll1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧଳ")][bstack111lll1_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬ଴")] = json.dumps(str(reason))
  bstack1ll1l1ll1_opy_ = bstack111lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫଵ").format(json.dumps(bstack1l111l111_opy_))
  return bstack1ll1l1ll1_opy_
def bstack1ll1lll1l1_opy_(driver_command, response):
    if driver_command == bstack111lll1_opy_ (u"ࠧࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠫଶ"):
        bstack1llll11l1_opy_.bstack1l1l11l111_opy_({
            bstack111lll1_opy_ (u"ࠨ࡫ࡰࡥ࡬࡫ࠧଷ"): response[bstack111lll1_opy_ (u"ࠩࡹࡥࡱࡻࡥࠨସ")],
            bstack111lll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪହ"): bstack1llll11l1_opy_.current_test_uuid()
        })
def bstack11l1ll1l_opy_(item, call, rep):
  global bstack1111lllll_opy_
  global bstack1lllllllll_opy_
  global bstack11l11lll_opy_
  name = bstack111lll1_opy_ (u"ࠫࠬ଺")
  try:
    if rep.when == bstack111lll1_opy_ (u"ࠬࡩࡡ࡭࡮ࠪ଻"):
      bstack1ll1111l11_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack11l11lll_opy_:
          name = str(rep.nodeid)
          bstack1l1l1ll111_opy_ = bstack11lll111l_opy_(bstack111lll1_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫଼ࠧ"), name, bstack111lll1_opy_ (u"ࠧࠨଽ"), bstack111lll1_opy_ (u"ࠨࠩା"), bstack111lll1_opy_ (u"ࠩࠪି"), bstack111lll1_opy_ (u"ࠪࠫୀ"))
          threading.current_thread().bstack1l111llll_opy_ = name
          for driver in bstack1lllllllll_opy_:
            if bstack1ll1111l11_opy_ == driver.session_id:
              driver.execute_script(bstack1l1l1ll111_opy_)
      except Exception as e:
        logger.debug(bstack111lll1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫୁ").format(str(e)))
      try:
        bstack1ll1l11111_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack111lll1_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ୂ"):
          status = bstack111lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ୃ") if rep.outcome.lower() == bstack111lll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧୄ") else bstack111lll1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ୅")
          reason = bstack111lll1_opy_ (u"ࠩࠪ୆")
          if status == bstack111lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪେ"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack111lll1_opy_ (u"ࠫ࡮ࡴࡦࡰࠩୈ") if status == bstack111lll1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ୉") else bstack111lll1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ୊")
          data = name + bstack111lll1_opy_ (u"ࠧࠡࡲࡤࡷࡸ࡫ࡤࠢࠩୋ") if status == bstack111lll1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨୌ") else name + bstack111lll1_opy_ (u"ࠩࠣࡪࡦ࡯࡬ࡦࡦࠤࠤ୍ࠬ") + reason
          bstack1l1ll11111_opy_ = bstack11lll111l_opy_(bstack111lll1_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩࠬ୎"), bstack111lll1_opy_ (u"ࠫࠬ୏"), bstack111lll1_opy_ (u"ࠬ࠭୐"), bstack111lll1_opy_ (u"࠭ࠧ୑"), level, data)
          for driver in bstack1lllllllll_opy_:
            if bstack1ll1111l11_opy_ == driver.session_id:
              driver.execute_script(bstack1l1ll11111_opy_)
      except Exception as e:
        logger.debug(bstack111lll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡨࡵ࡮ࡵࡧࡻࡸࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫ୒").format(str(e)))
  except Exception as e:
    logger.debug(bstack111lll1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡸࡺࡡࡵࡧࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࠡࡵࡷࡥࡹࡻࡳ࠻ࠢࡾࢁࠬ୓").format(str(e)))
  bstack1111lllll_opy_(item, call, rep)
def bstack11lll1l11_opy_(driver, bstack111ll1l1_opy_):
  PercySDK.screenshot(driver, bstack111ll1l1_opy_)
def bstack1lll1llll1_opy_(driver):
  if bstack1lll1111ll_opy_.bstack1l1l1llll1_opy_() is True or bstack1lll1111ll_opy_.capturing() is True:
    return
  bstack1lll1111ll_opy_.bstack1ll11ll1l1_opy_()
  while not bstack1lll1111ll_opy_.bstack1l1l1llll1_opy_():
    bstack1ll11ll11l_opy_ = bstack1lll1111ll_opy_.bstack1ll11lll1l_opy_()
    bstack11lll1l11_opy_(driver, bstack1ll11ll11l_opy_)
  bstack1lll1111ll_opy_.bstack1l1l1l11_opy_()
def bstack111ll1ll1_opy_(sequence, driver_command, response = None):
    try:
      if sequence != bstack111lll1_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩ୔"):
        return
      if not CONFIG.get(bstack111lll1_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩ୕"), False):
        return
      bstack1ll11ll11l_opy_ = bstack1ll1111111_opy_(threading.current_thread(), bstack111lll1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧୖ"), None)
      for command in bstack1llllll111_opy_:
        if command == driver_command:
          for driver in bstack1lllllllll_opy_:
            bstack1lll1llll1_opy_(driver)
      bstack11l11l1l_opy_ = CONFIG.get(bstack111lll1_opy_ (u"ࠬࡶࡥࡳࡥࡼࡇࡦࡶࡴࡶࡴࡨࡑࡴࡪࡥࠨୗ"), bstack111lll1_opy_ (u"ࠨࡡࡶࡶࡲࠦ୘"))
      if driver_command in bstack1l1llll1l1_opy_[bstack11l11l1l_opy_]:
        bstack1lll1111ll_opy_.bstack1l1l11ll11_opy_(bstack1ll11ll11l_opy_, driver_command)
    except Exception as e:
      pass
def bstack111111lll_opy_(framework_name):
  global bstack1llll11l11_opy_
  global bstack11lllll1l_opy_
  global bstack111llll1_opy_
  bstack1llll11l11_opy_ = framework_name
  logger.info(bstack1llllllll1_opy_.format(bstack1llll11l11_opy_.split(bstack111lll1_opy_ (u"ࠧ࠮ࠩ୙"))[0]))
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack1ll1ll1ll_opy_:
      Service.start = bstack1l1ll11lll_opy_
      Service.stop = bstack1l1l111l_opy_
      webdriver.Remote.get = bstack11111l1ll_opy_
      WebDriver.close = bstack11llllll1_opy_
      WebDriver.quit = bstack1111ll111_opy_
      webdriver.Remote.__init__ = bstack1lll11l1l_opy_
      WebDriver.getAccessibilityResults = getAccessibilityResults
      WebDriver.bstack1ll11lll11_opy_ = getAccessibilityResults
      WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
      WebDriver.bstack1l1l1l1ll1_opy_ = getAccessibilityResultsSummary
    if not bstack1ll1ll1ll_opy_ and bstack1llll11l1_opy_.on():
      webdriver.Remote.__init__ = bstack11lllllll_opy_
    if bstack111lll1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ୚") in str(framework_name).lower() and bstack1llll11l1_opy_.on():
      WebDriver.execute = bstack1l111lll1_opy_
    bstack11lllll1l_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack1ll1ll1ll_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack11ll1111l_opy_
  except Exception as e:
    pass
  bstack11l111ll1_opy_()
  if not bstack11lllll1l_opy_:
    bstack1l11ll11l_opy_(bstack111lll1_opy_ (u"ࠤࡓࡥࡨࡱࡡࡨࡧࡶࠤࡳࡵࡴࠡ࡫ࡱࡷࡹࡧ࡬࡭ࡧࡧࠦ୛"), bstack1111111l1_opy_)
  if bstack1l111ll1l_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      RemoteConnection._get_proxy_url = bstack1l1111l1_opy_
    except Exception as e:
      logger.error(bstack11l1l1ll_opy_.format(str(e)))
  if bstack11lll1l1_opy_():
    bstack1ll11111ll_opy_(CONFIG, logger)
  if (bstack111lll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩଡ଼") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if CONFIG.get(bstack111lll1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪଢ଼"), False):
          bstack111l1l1l1_opy_(bstack111ll1ll1_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack1ll11l1111_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1111l1lll_opy_
      except Exception as e:
        logger.warn(bstack1ll1llll1_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack111111ll_opy_
      except Exception as e:
        logger.debug(bstack1ll1l1l11_opy_ + str(e))
    except Exception as e:
      bstack1l11ll11l_opy_(e, bstack1ll1llll1_opy_)
    Output.start_test = bstack111ll111l_opy_
    Output.end_test = bstack1lllllll11_opy_
    TestStatus.__init__ = bstack1111l1l11_opy_
    QueueItem.__init__ = bstack1lll1111l_opy_
    pabot._create_items = bstack1l1111l11_opy_
    try:
      from pabot import __version__ as bstack1ll111111l_opy_
      if version.parse(bstack1ll111111l_opy_) >= version.parse(bstack111lll1_opy_ (u"ࠬ࠸࠮࠲࠷࠱࠴ࠬ୞")):
        pabot._run = bstack11111111_opy_
      elif version.parse(bstack1ll111111l_opy_) >= version.parse(bstack111lll1_opy_ (u"࠭࠲࠯࠳࠶࠲࠵࠭ୟ")):
        pabot._run = bstack11l1llll_opy_
      else:
        pabot._run = bstack1lll11111l_opy_
    except Exception as e:
      pabot._run = bstack1lll11111l_opy_
    pabot._create_command_for_execution = bstack1ll111llll_opy_
    pabot._report_results = bstack1l11l11l1_opy_
  if bstack111lll1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧୠ") in str(framework_name).lower():
    if not bstack1ll1ll1ll_opy_:
      return
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l11ll11l_opy_(e, bstack11ll11lll_opy_)
    Runner.run_hook = bstack1ll11ll1_opy_
    Step.run = bstack1111l11l_opy_
  if bstack111lll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨୡ") in str(framework_name).lower():
    if not bstack1ll1ll1ll_opy_:
      return
    try:
      if CONFIG.get(bstack111lll1_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨୢ"), False):
          bstack111l1l1l1_opy_(bstack111ll1ll1_opy_)
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack1l1lll1111_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack1ll111l11_opy_
      Config.getoption = bstack1llll11ll_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack11l1ll1l_opy_
    except Exception as e:
      pass
def bstack11l11111_opy_():
  global CONFIG
  if bstack111lll1_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪୣ") in CONFIG and int(CONFIG[bstack111lll1_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫ୤")]) > 1:
    logger.warn(bstack1llll1ll_opy_)
def bstack1ll111l11l_opy_(arg, bstack1l1l11l1_opy_, bstack1ll11l1lll_opy_=None):
  global CONFIG
  global bstack1llll11lll_opy_
  global bstack1ll1l1l11l_opy_
  global bstack1ll1ll1ll_opy_
  global bstack11l11l111_opy_
  bstack1llll111ll_opy_ = bstack111lll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ୥")
  if bstack1l1l11l1_opy_ and isinstance(bstack1l1l11l1_opy_, str):
    bstack1l1l11l1_opy_ = eval(bstack1l1l11l1_opy_)
  CONFIG = bstack1l1l11l1_opy_[bstack111lll1_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭୦")]
  bstack1llll11lll_opy_ = bstack1l1l11l1_opy_[bstack111lll1_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨ୧")]
  bstack1ll1l1l11l_opy_ = bstack1l1l11l1_opy_[bstack111lll1_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ୨")]
  bstack1ll1ll1ll_opy_ = bstack1l1l11l1_opy_[bstack111lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬ୩")]
  bstack11l11l111_opy_.bstack1ll1ll11_opy_(bstack111lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫ୪"), bstack1ll1ll1ll_opy_)
  os.environ[bstack111lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭୫")] = bstack1llll111ll_opy_
  os.environ[bstack111lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࠫ୬")] = json.dumps(CONFIG)
  os.environ[bstack111lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡎࡕࡃࡡࡘࡖࡑ࠭୭")] = bstack1llll11lll_opy_
  os.environ[bstack111lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨ୮")] = str(bstack1ll1l1l11l_opy_)
  os.environ[bstack111lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑ࡛ࡗࡉࡘ࡚࡟ࡑࡎࡘࡋࡎࡔࠧ୯")] = str(True)
  if bstack1l1llllll1_opy_(arg, [bstack111lll1_opy_ (u"ࠩ࠰ࡲࠬ୰"), bstack111lll1_opy_ (u"ࠪ࠱࠲ࡴࡵ࡮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫୱ")]) != -1:
    os.environ[bstack111lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔ࡞࡚ࡅࡔࡖࡢࡔࡆࡘࡁࡍࡎࡈࡐࠬ୲")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack11l1ll11_opy_)
    return
  bstack1ll111ll11_opy_()
  global bstack1111l11ll_opy_
  global bstack1ll111lll1_opy_
  global bstack1111l1l1l_opy_
  global bstack111ll1ll_opy_
  global bstack1llllll11l_opy_
  global bstack111llll1_opy_
  global bstack11l1l11ll_opy_
  arg.append(bstack111lll1_opy_ (u"ࠧ࠳ࡗࠣ୳"))
  arg.append(bstack111lll1_opy_ (u"ࠨࡩࡨࡰࡲࡶࡪࡀࡍࡰࡦࡸࡰࡪࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡪ࡯ࡳࡳࡷࡺࡥࡥ࠼ࡳࡽࡹ࡫ࡳࡵ࠰ࡓࡽࡹ࡫ࡳࡵ࡙ࡤࡶࡳ࡯࡮ࡨࠤ୴"))
  arg.append(bstack111lll1_opy_ (u"ࠢ࠮࡙ࠥ୵"))
  arg.append(bstack111lll1_opy_ (u"ࠣ࡫ࡪࡲࡴࡸࡥ࠻ࡖ࡫ࡩࠥ࡮࡯ࡰ࡭࡬ࡱࡵࡲࠢ୶"))
  global bstack11ll1lll_opy_
  global bstack1llll1l111_opy_
  global bstack111l11l1l_opy_
  global bstack1ll1lllll_opy_
  global bstack11l11111l_opy_
  global bstack1111llll_opy_
  global bstack1l11llll1_opy_
  global bstack1lll1l1l1l_opy_
  global bstack1lllll11l1_opy_
  global bstack1llllll1l1_opy_
  global bstack11111llll_opy_
  global bstack1111lllll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack11ll1lll_opy_ = webdriver.Remote.__init__
    bstack1llll1l111_opy_ = WebDriver.quit
    bstack1l11llll1_opy_ = WebDriver.close
    bstack1lll1l1l1l_opy_ = WebDriver.get
  except Exception as e:
    pass
  if bstack11llllll_opy_(CONFIG) and bstack1lllllll1_opy_():
    if bstack1lll1l11l_opy_() < version.parse(bstack11llll11l_opy_):
      logger.error(bstack111lll1ll_opy_.format(bstack1lll1l11l_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack1lllll11l1_opy_ = RemoteConnection._get_proxy_url
      except Exception as e:
        logger.error(bstack11l1l1ll_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack1llllll1l1_opy_ = Config.getoption
    from _pytest import runner
    bstack11111llll_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack1l1lll1lll_opy_)
  try:
    from pytest_bdd import reporting
    bstack1111lllll_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack111lll1_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡱࠣࡶࡺࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࡵࠪ୷"))
  bstack1111l1l1l_opy_ = CONFIG.get(bstack111lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ୸"), {}).get(bstack111lll1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭୹"))
  bstack11l1l11ll_opy_ = True
  bstack111111lll_opy_(bstack1ll1111lll_opy_)
  os.environ[bstack111lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡚࡙ࡅࡓࡐࡄࡑࡊ࠭୺")] = CONFIG[bstack111lll1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ୻")]
  os.environ[bstack111lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡄࡅࡈࡗࡘࡥࡋࡆ࡛ࠪ୼")] = CONFIG[bstack111lll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ୽")]
  os.environ[bstack111lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬ୾")] = bstack1ll1ll1ll_opy_.__str__()
  from _pytest.config import main as bstack11111l11_opy_
  bstack11111l11_opy_(arg)
  if bstack111lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺࠧ୿") in multiprocessing.current_process().__dict__.keys():
    for bstack1lll11lll1_opy_ in multiprocessing.current_process().bstack_error_list:
      bstack1ll11l1lll_opy_.append(bstack1lll11lll1_opy_)
def bstack1ll11lll1_opy_(arg):
  bstack111111lll_opy_(bstack1ll1l11l1_opy_)
  os.environ[bstack111lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ஀")] = str(bstack1ll1l1l11l_opy_)
  from behave.__main__ import main as bstack1111l1111_opy_
  bstack1111l1111_opy_(arg)
def bstack111l11lll_opy_():
  logger.info(bstack1llll1111_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack111lll1_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ஁"), help=bstack111lll1_opy_ (u"࠭ࡇࡦࡰࡨࡶࡦࡺࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡤࡱࡱࡪ࡮࡭ࠧஂ"))
  parser.add_argument(bstack111lll1_opy_ (u"ࠧ࠮ࡷࠪஃ"), bstack111lll1_opy_ (u"ࠨ࠯࠰ࡹࡸ࡫ࡲ࡯ࡣࡰࡩࠬ஄"), help=bstack111lll1_opy_ (u"ࠩ࡜ࡳࡺࡸࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡵࡴࡧࡵࡲࡦࡳࡥࠨஅ"))
  parser.add_argument(bstack111lll1_opy_ (u"ࠪ࠱ࡰ࠭ஆ"), bstack111lll1_opy_ (u"ࠫ࠲࠳࡫ࡦࡻࠪஇ"), help=bstack111lll1_opy_ (u"ࠬ࡟࡯ࡶࡴࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡤࡧࡨ࡫ࡳࡴࠢ࡮ࡩࡾ࠭ஈ"))
  parser.add_argument(bstack111lll1_opy_ (u"࠭࠭ࡧࠩஉ"), bstack111lll1_opy_ (u"ࠧ࠮࠯ࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬஊ"), help=bstack111lll1_opy_ (u"ࠨ࡛ࡲࡹࡷࠦࡴࡦࡵࡷࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ஋"))
  bstack1ll1l11ll1_opy_ = parser.parse_args()
  try:
    bstack1ll1lll11l_opy_ = bstack111lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡩࡨࡲࡪࡸࡩࡤ࠰ࡼࡱࡱ࠴ࡳࡢ࡯ࡳࡰࡪ࠭஌")
    if bstack1ll1l11ll1_opy_.framework and bstack1ll1l11ll1_opy_.framework not in (bstack111lll1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ஍"), bstack111lll1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠷ࠬஎ")):
      bstack1ll1lll11l_opy_ = bstack111lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࠮ࡺ࡯࡯࠲ࡸࡧ࡭ࡱ࡮ࡨࠫஏ")
    bstack1ll1l1111_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1ll1lll11l_opy_)
    bstack1l1l1lll1l_opy_ = open(bstack1ll1l1111_opy_, bstack111lll1_opy_ (u"࠭ࡲࠨஐ"))
    bstack1l1l1lll_opy_ = bstack1l1l1lll1l_opy_.read()
    bstack1l1l1lll1l_opy_.close()
    if bstack1ll1l11ll1_opy_.username:
      bstack1l1l1lll_opy_ = bstack1l1l1lll_opy_.replace(bstack111lll1_opy_ (u"࡚ࠧࡑࡘࡖࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠧ஑"), bstack1ll1l11ll1_opy_.username)
    if bstack1ll1l11ll1_opy_.key:
      bstack1l1l1lll_opy_ = bstack1l1l1lll_opy_.replace(bstack111lll1_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡁࡄࡅࡈࡗࡘࡥࡋࡆ࡛ࠪஒ"), bstack1ll1l11ll1_opy_.key)
    if bstack1ll1l11ll1_opy_.framework:
      bstack1l1l1lll_opy_ = bstack1l1l1lll_opy_.replace(bstack111lll1_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪஓ"), bstack1ll1l11ll1_opy_.framework)
    file_name = bstack111lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭ஔ")
    file_path = os.path.abspath(file_name)
    bstack1l11l1lll_opy_ = open(file_path, bstack111lll1_opy_ (u"ࠫࡼ࠭க"))
    bstack1l11l1lll_opy_.write(bstack1l1l1lll_opy_)
    bstack1l11l1lll_opy_.close()
    logger.info(bstack1l1ll11l11_opy_)
    try:
      os.environ[bstack111lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧ஖")] = bstack1ll1l11ll1_opy_.framework if bstack1ll1l11ll1_opy_.framework != None else bstack111lll1_opy_ (u"ࠨࠢ஗")
      config = yaml.safe_load(bstack1l1l1lll_opy_)
      config[bstack111lll1_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧ஘")] = bstack111lll1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠮ࡵࡨࡸࡺࡶࠧங")
      bstack1l1l11l11_opy_(bstack1l11lll11_opy_, config)
    except Exception as e:
      logger.debug(bstack11l1111l_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1ll1lll1ll_opy_.format(str(e)))
def bstack1l1l11l11_opy_(bstack1ll11ll11_opy_, config, bstack1l1l11ll_opy_={}):
  global bstack1ll1ll1ll_opy_
  global bstack1ll1l111ll_opy_
  if not config:
    return
  bstack1ll1l111l1_opy_ = bstack11l1l1l1l_opy_ if not bstack1ll1ll1ll_opy_ else (
    bstack1l1ll1l1l_opy_ if bstack111lll1_opy_ (u"ࠩࡤࡴࡵ࠭ச") in config else bstack1l1l1l1ll_opy_)
  data = {
    bstack111lll1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬ஛"): config[bstack111lll1_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ஜ")],
    bstack111lll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ஝"): config[bstack111lll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩஞ")],
    bstack111lll1_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫட"): bstack1ll11ll11_opy_,
    bstack111lll1_opy_ (u"ࠨࡦࡨࡸࡪࡩࡴࡦࡦࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ஠"): os.environ.get(bstack111lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫ஡"), bstack1ll1l111ll_opy_),
    bstack111lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ஢"): bstack11l1lllll_opy_,
    bstack111lll1_opy_ (u"ࠫࡴࡶࡴࡪ࡯ࡤࡰࡤ࡮ࡵࡣࡡࡸࡶࡱ࠭ண"): bstack1l1l111lll_opy_(),
    bstack111lll1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨத"): {
      bstack111lll1_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ஥"): str(config[bstack111lll1_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧ஦")]) if bstack111lll1_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ஧") in config else bstack111lll1_opy_ (u"ࠤࡸࡲࡰࡴ࡯ࡸࡰࠥந"),
      bstack111lll1_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩ࡛࡫ࡲࡴ࡫ࡲࡲࠬன"): sys.version,
      bstack111lll1_opy_ (u"ࠫࡷ࡫ࡦࡦࡴࡵࡩࡷ࠭ப"): bstack1ll1l11l11_opy_(os.getenv(bstack111lll1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠢ஫"), bstack111lll1_opy_ (u"ࠨࠢ஬"))),
      bstack111lll1_opy_ (u"ࠧ࡭ࡣࡱ࡫ࡺࡧࡧࡦࠩ஭"): bstack111lll1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨம"),
      bstack111lll1_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࠪய"): bstack1ll1l111l1_opy_,
      bstack111lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ர"): config[bstack111lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧற")] if config[bstack111lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨல")] else bstack111lll1_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴࠢள"),
      bstack111lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩழ"): str(config[bstack111lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪவ")]) if bstack111lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫஶ") in config else bstack111lll1_opy_ (u"ࠥࡹࡳࡱ࡮ࡰࡹࡱࠦஷ"),
      bstack111lll1_opy_ (u"ࠫࡴࡹࠧஸ"): sys.platform,
      bstack111lll1_opy_ (u"ࠬ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠧஹ"): socket.gethostname()
    }
  }
  update(data[bstack111lll1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡶࡲࡰࡲࡨࡶࡹ࡯ࡥࡴࠩ஺")], bstack1l1l11ll_opy_)
  try:
    response = bstack1l1111111_opy_(bstack111lll1_opy_ (u"ࠧࡑࡑࡖࡘࠬ஻"), bstack11ll111l_opy_(bstack1l1l1l1l1_opy_), data, {
      bstack111lll1_opy_ (u"ࠨࡣࡸࡸ࡭࠭஼"): (config[bstack111lll1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ஽")], config[bstack111lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ா")])
    })
    if response:
      logger.debug(bstack1l1l1lll1_opy_.format(bstack1ll11ll11_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack111111l1l_opy_.format(str(e)))
def bstack1ll1l11l11_opy_(framework):
  return bstack111lll1_opy_ (u"ࠦࢀࢃ࠭ࡱࡻࡷ࡬ࡴࡴࡡࡨࡧࡱࡸ࠴ࢁࡽࠣி").format(str(framework), __version__) if framework else bstack111lll1_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࡦ࡭ࡥ࡯ࡶ࠲ࡿࢂࠨீ").format(
    __version__)
def bstack1ll111ll11_opy_():
  global CONFIG
  if bool(CONFIG):
    return
  try:
    bstack11ll11ll_opy_()
    logger.debug(bstack111l1111_opy_.format(str(CONFIG)))
    bstack1ll11l11l_opy_()
    bstack1l11111l_opy_()
  except Exception as e:
    logger.error(bstack111lll1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࡻࡰ࠭ࠢࡨࡶࡷࡵࡲ࠻ࠢࠥு") + str(e))
    sys.exit(1)
  sys.excepthook = bstack1l1l1111l1_opy_
  atexit.register(bstack1ll11llll1_opy_)
  signal.signal(signal.SIGINT, bstack1lllll1l1_opy_)
  signal.signal(signal.SIGTERM, bstack1lllll1l1_opy_)
def bstack1l1l1111l1_opy_(exctype, value, traceback):
  global bstack1lllllllll_opy_
  try:
    for driver in bstack1lllllllll_opy_:
      bstack1l11ll11_opy_(driver, bstack111lll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧூ"), bstack111lll1_opy_ (u"ࠣࡕࡨࡷࡸ࡯࡯࡯ࠢࡩࡥ࡮ࡲࡥࡥࠢࡺ࡭ࡹ࡮࠺ࠡ࡞ࡱࠦ௃") + str(value))
  except Exception:
    pass
  bstack1l111ll1_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1l111ll1_opy_(message=bstack111lll1_opy_ (u"ࠩࠪ௄"), bstack1llll11111_opy_ = False):
  global CONFIG
  bstack1ll1llll1l_opy_ = bstack111lll1_opy_ (u"ࠪ࡫ࡱࡵࡢࡢ࡮ࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠬ௅") if bstack1llll11111_opy_ else bstack111lll1_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪெ")
  try:
    if message:
      bstack1l1l11ll_opy_ = {
        bstack1ll1llll1l_opy_ : str(message)
      }
      bstack1l1l11l11_opy_(bstack1l11l1l1l_opy_, CONFIG, bstack1l1l11ll_opy_)
    else:
      bstack1l1l11l11_opy_(bstack1l11l1l1l_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1lll11l1l1_opy_.format(str(e)))
def bstack1llll1ll1_opy_(bstack1l1llll1_opy_, size):
  bstack1lll1l11l1_opy_ = []
  while len(bstack1l1llll1_opy_) > size:
    bstack11lll11l1_opy_ = bstack1l1llll1_opy_[:size]
    bstack1lll1l11l1_opy_.append(bstack11lll11l1_opy_)
    bstack1l1llll1_opy_ = bstack1l1llll1_opy_[size:]
  bstack1lll1l11l1_opy_.append(bstack1l1llll1_opy_)
  return bstack1lll1l11l1_opy_
def bstack11ll11l11_opy_(args):
  if bstack111lll1_opy_ (u"ࠬ࠳࡭ࠨே") in args and bstack111lll1_opy_ (u"࠭ࡰࡥࡤࠪை") in args:
    return True
  return False
def run_on_browserstack(bstack11l1l11l1_opy_=None, bstack1ll11l1lll_opy_=None, bstack1lll1l1l11_opy_=False):
  global CONFIG
  global bstack1llll11lll_opy_
  global bstack1ll1l1l11l_opy_
  global bstack1ll1l111ll_opy_
  bstack1llll111ll_opy_ = bstack111lll1_opy_ (u"ࠧࠨ௉")
  bstack111lllll1_opy_(bstack1l1lll11ll_opy_, logger)
  if bstack11l1l11l1_opy_ and isinstance(bstack11l1l11l1_opy_, str):
    bstack11l1l11l1_opy_ = eval(bstack11l1l11l1_opy_)
  if bstack11l1l11l1_opy_:
    CONFIG = bstack11l1l11l1_opy_[bstack111lll1_opy_ (u"ࠨࡅࡒࡒࡋࡏࡇࠨொ")]
    bstack1llll11lll_opy_ = bstack11l1l11l1_opy_[bstack111lll1_opy_ (u"ࠩࡋ࡙ࡇࡥࡕࡓࡎࠪோ")]
    bstack1ll1l1l11l_opy_ = bstack11l1l11l1_opy_[bstack111lll1_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬௌ")]
    bstack11l11l111_opy_.bstack1ll1ll11_opy_(bstack111lll1_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ்࠭"), bstack1ll1l1l11l_opy_)
    bstack1llll111ll_opy_ = bstack111lll1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ௎")
  if not bstack1lll1l1l11_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack11l1ll11_opy_)
      return
    if sys.argv[1] == bstack111lll1_opy_ (u"࠭࠭࠮ࡸࡨࡶࡸ࡯࡯࡯ࠩ௏") or sys.argv[1] == bstack111lll1_opy_ (u"ࠧ࠮ࡸࠪௐ"):
      logger.info(bstack111lll1_opy_ (u"ࠨࡄࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡑࡻࡷ࡬ࡴࡴࠠࡔࡆࡎࠤࡻࢁࡽࠨ௑").format(__version__))
      return
    if sys.argv[1] == bstack111lll1_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨ௒"):
      bstack111l11lll_opy_()
      return
  args = sys.argv
  bstack1ll111ll11_opy_()
  global bstack1111l11ll_opy_
  global bstack1111111l_opy_
  global bstack11l1l11ll_opy_
  global bstack1lll1ll11l_opy_
  global bstack1ll111lll1_opy_
  global bstack1111l1l1l_opy_
  global bstack111ll1ll_opy_
  global bstack1l1ll11l_opy_
  global bstack1llllll11l_opy_
  global bstack111llll1_opy_
  global bstack1lll11lll_opy_
  bstack1111111l_opy_ = len(CONFIG.get(bstack111lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭௓"), []))
  if not bstack1llll111ll_opy_:
    if args[1] == bstack111lll1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ௔") or args[1] == bstack111lll1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ࠸࠭௕"):
      bstack1llll111ll_opy_ = bstack111lll1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭௖")
      args = args[2:]
    elif args[1] == bstack111lll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ௗ"):
      bstack1llll111ll_opy_ = bstack111lll1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ௘")
      args = args[2:]
    elif args[1] == bstack111lll1_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨ௙"):
      bstack1llll111ll_opy_ = bstack111lll1_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ௚")
      args = args[2:]
    elif args[1] == bstack111lll1_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬ௛"):
      bstack1llll111ll_opy_ = bstack111lll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭௜")
      args = args[2:]
    elif args[1] == bstack111lll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭௝"):
      bstack1llll111ll_opy_ = bstack111lll1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ௞")
      args = args[2:]
    elif args[1] == bstack111lll1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ௟"):
      bstack1llll111ll_opy_ = bstack111lll1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ௠")
      args = args[2:]
    else:
      if not bstack111lll1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭௡") in CONFIG or str(CONFIG[bstack111lll1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ௢")]).lower() in [bstack111lll1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ௣"), bstack111lll1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠹ࠧ௤")]:
        bstack1llll111ll_opy_ = bstack111lll1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ௥")
        args = args[1:]
      elif str(CONFIG[bstack111lll1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ௦")]).lower() == bstack111lll1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ௧"):
        bstack1llll111ll_opy_ = bstack111lll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ௨")
        args = args[1:]
      elif str(CONFIG[bstack111lll1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ௩")]).lower() == bstack111lll1_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫ௪"):
        bstack1llll111ll_opy_ = bstack111lll1_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬ௫")
        args = args[1:]
      elif str(CONFIG[bstack111lll1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ௬")]).lower() == bstack111lll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ௭"):
        bstack1llll111ll_opy_ = bstack111lll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ௮")
        args = args[1:]
      elif str(CONFIG[bstack111lll1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭௯")]).lower() == bstack111lll1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ௰"):
        bstack1llll111ll_opy_ = bstack111lll1_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ௱")
        args = args[1:]
      else:
        os.environ[bstack111lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨ௲")] = bstack1llll111ll_opy_
        bstack1ll1lll111_opy_(bstack1l111ll11_opy_)
  os.environ[bstack111lll1_opy_ (u"ࠧࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࡢ࡙ࡘࡋࡄࠨ௳")] = bstack1llll111ll_opy_
  bstack1ll1l111ll_opy_ = bstack1llll111ll_opy_
  global bstack1ll11l1l1_opy_
  if bstack11l1l11l1_opy_:
    try:
      os.environ[bstack111lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪ௴")] = bstack1llll111ll_opy_
      bstack1l1l11l11_opy_(bstack11l1ll1l1_opy_, CONFIG)
    except Exception as e:
      logger.debug(bstack1lll11l1l1_opy_.format(str(e)))
  global bstack11ll1lll_opy_
  global bstack1llll1l111_opy_
  global bstack1l1llll11l_opy_
  global bstack1l1ll1l1l1_opy_
  global bstack1llll111l1_opy_
  global bstack11l111l11_opy_
  global bstack111l11l1l_opy_
  global bstack1ll1lllll_opy_
  global bstack111111l11_opy_
  global bstack11l11111l_opy_
  global bstack1111llll_opy_
  global bstack1l11llll1_opy_
  global bstack11ll1l111_opy_
  global bstack1lll111ll1_opy_
  global bstack1lll1l1l1l_opy_
  global bstack1lllll11l1_opy_
  global bstack1llllll1l1_opy_
  global bstack11111llll_opy_
  global bstack1l11l11l_opy_
  global bstack1111lllll_opy_
  global bstack11ll1ll1_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack11ll1lll_opy_ = webdriver.Remote.__init__
    bstack1llll1l111_opy_ = WebDriver.quit
    bstack1l11llll1_opy_ = WebDriver.close
    bstack1lll1l1l1l_opy_ = WebDriver.get
    bstack11ll1ll1_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack1ll11l1l1_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    global bstack1l1l11l1ll_opy_
    from QWeb.keywords import browser
    bstack1l1l11l1ll_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack11llllll_opy_(CONFIG) and bstack1lllllll1_opy_():
    if bstack1lll1l11l_opy_() < version.parse(bstack11llll11l_opy_):
      logger.error(bstack111lll1ll_opy_.format(bstack1lll1l11l_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        bstack1lllll11l1_opy_ = RemoteConnection._get_proxy_url
      except Exception as e:
        logger.error(bstack11l1l1ll_opy_.format(str(e)))
  if bstack1llll111ll_opy_ != bstack111lll1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ௵") or (bstack1llll111ll_opy_ == bstack111lll1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ௶") and not bstack11l1l11l1_opy_):
    bstack1l1l1lllll_opy_()
  if (bstack1llll111ll_opy_ in [bstack111lll1_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪ௷"), bstack111lll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ௸"), bstack111lll1_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧ௹")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack1ll11l1111_opy_
        bstack11l111l11_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack1ll1llll1_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack1llll111l1_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack1ll1l1l11_opy_ + str(e))
    except Exception as e:
      bstack1l11ll11l_opy_(e, bstack1ll1llll1_opy_)
    if bstack1llll111ll_opy_ != bstack111lll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨ௺"):
      bstack1lllll11_opy_()
    bstack1l1llll11l_opy_ = Output.start_test
    bstack1l1ll1l1l1_opy_ = Output.end_test
    bstack111l11l1l_opy_ = TestStatus.__init__
    bstack111111l11_opy_ = pabot._run
    bstack11l11111l_opy_ = QueueItem.__init__
    bstack1111llll_opy_ = pabot._create_command_for_execution
    bstack1l11l11l_opy_ = pabot._report_results
  if bstack1llll111ll_opy_ == bstack111lll1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ௻"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l11ll11l_opy_(e, bstack11ll11lll_opy_)
    bstack11ll1l111_opy_ = Runner.run_hook
    bstack1lll111ll1_opy_ = Step.run
  if bstack1llll111ll_opy_ == bstack111lll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ௼"):
    try:
      from _pytest.config import Config
      bstack1llllll1l1_opy_ = Config.getoption
      from _pytest import runner
      bstack11111llll_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack1l1lll1lll_opy_)
    try:
      from pytest_bdd import reporting
      bstack1111lllll_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack111lll1_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡲࠤࡷࡻ࡮ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺࡥࡴࡶࡶࠫ௽"))
  if bstack1llll111ll_opy_ in bstack111ll1111_opy_:
    try:
      framework_name = bstack111lll1_opy_ (u"ࠫࡗࡵࡢࡰࡶࠪ௾") if bstack1llll111ll_opy_ in [bstack111lll1_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫ௿"), bstack111lll1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬఀ"), bstack111lll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨఁ")] else bstack11ll1lll1_opy_(bstack1llll111ll_opy_)
      bstack1llll11l1_opy_.launch(CONFIG, {
        bstack111lll1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࠩం"): bstack111lll1_opy_ (u"ࠩࡾ࠴ࢂ࠳ࡣࡶࡥࡸࡱࡧ࡫ࡲࠨః").format(framework_name) if bstack1llll111ll_opy_ == bstack111lll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪఄ") and bstack1l1111ll1_opy_() else framework_name,
        bstack111lll1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨఅ"): bstack111l1l1l_opy_(framework_name),
        bstack111lll1_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪఆ"): __version__
      })
    except Exception as e:
      logger.debug(bstack1ll11l1ll1_opy_.format(bstack111lll1_opy_ (u"࠭ࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ఇ"), str(e)))
  if bstack1llll111ll_opy_ in bstack1l11l1l11_opy_:
    try:
      framework_name = bstack111lll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ఈ") if bstack1llll111ll_opy_ in [bstack111lll1_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧఉ"), bstack111lll1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨఊ")] else bstack1llll111ll_opy_
      if bstack1ll1ll1ll_opy_ and bstack111lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪఋ") in CONFIG and CONFIG[bstack111lll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫఌ")] == True:
        if bstack111lll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ఍") in CONFIG:
          os.environ[bstack111lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧఎ")] = os.getenv(bstack111lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨఏ"), json.dumps(CONFIG[bstack111lll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨఐ")]))
          CONFIG[bstack111lll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ఑")].pop(bstack111lll1_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨఒ"), None)
          CONFIG[bstack111lll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫఓ")].pop(bstack111lll1_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪఔ"), None)
        bstack1lllll1ll1_opy_, bstack1111lll1l_opy_ = bstack1lllll1111_opy_.bstack1lll11ll_opy_(CONFIG, bstack1llll111ll_opy_, bstack111l1l1l_opy_(framework_name))
        if not bstack1lllll1ll1_opy_ is None:
          os.environ[bstack111lll1_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫక")] = bstack1lllll1ll1_opy_
          os.environ[bstack111lll1_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡖࡈࡗ࡙ࡥࡒࡖࡐࡢࡍࡉ࠭ఖ")] = str(bstack1111lll1l_opy_)
    except Exception as e:
      logger.debug(bstack1ll11l1ll1_opy_.format(bstack111lll1_opy_ (u"ࠨࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨగ"), str(e)))
  if bstack1llll111ll_opy_ == bstack111lll1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩఘ"):
    bstack11l1l11ll_opy_ = True
    if bstack11l1l11l1_opy_ and bstack1lll1l1l11_opy_:
      bstack1111l1l1l_opy_ = CONFIG.get(bstack111lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧఙ"), {}).get(bstack111lll1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭చ"))
      bstack111111lll_opy_(bstack1lll1111l1_opy_)
    elif bstack11l1l11l1_opy_:
      bstack1111l1l1l_opy_ = CONFIG.get(bstack111lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩఛ"), {}).get(bstack111lll1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨజ"))
      global bstack1lllllllll_opy_
      try:
        if bstack11ll11l11_opy_(bstack11l1l11l1_opy_[bstack111lll1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪఝ")]) and multiprocessing.current_process().name == bstack111lll1_opy_ (u"ࠨ࠲ࠪఞ"):
          bstack11l1l11l1_opy_[bstack111lll1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬట")].remove(bstack111lll1_opy_ (u"ࠪ࠱ࡲ࠭ఠ"))
          bstack11l1l11l1_opy_[bstack111lll1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧడ")].remove(bstack111lll1_opy_ (u"ࠬࡶࡤࡣࠩఢ"))
          bstack11l1l11l1_opy_[bstack111lll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩణ")] = bstack11l1l11l1_opy_[bstack111lll1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪత")][0]
          with open(bstack11l1l11l1_opy_[bstack111lll1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫథ")], bstack111lll1_opy_ (u"ࠩࡵࠫద")) as f:
            bstack111ll111_opy_ = f.read()
          bstack1ll11lll_opy_ = bstack111lll1_opy_ (u"ࠥࠦࠧ࡬ࡲࡰ࡯ࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡶࡨࡰࠦࡩ࡮ࡲࡲࡶࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡺࡦ࠽ࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪ࠮ࡻࡾࠫ࠾ࠤ࡫ࡸ࡯࡮ࠢࡳࡨࡧࠦࡩ࡮ࡲࡲࡶࡹࠦࡐࡥࡤ࠾ࠤࡴ࡭࡟ࡥࡤࠣࡁࠥࡖࡤࡣ࠰ࡧࡳࡤࡨࡲࡦࡣ࡮࠿ࠏࡪࡥࡧࠢࡰࡳࡩࡥࡢࡳࡧࡤ࡯࠭ࡹࡥ࡭ࡨ࠯ࠤࡦࡸࡧ࠭ࠢࡷࡩࡲࡶ࡯ࡳࡣࡵࡽࠥࡃࠠ࠱ࠫ࠽ࠎࠥࠦࡴࡳࡻ࠽ࠎࠥࠦࠠࠡࡣࡵ࡫ࠥࡃࠠࡴࡶࡵࠬ࡮ࡴࡴࠩࡣࡵ࡫࠮࠱࠱࠱ࠫࠍࠤࠥ࡫ࡸࡤࡧࡳࡸࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡣࡶࠤࡪࡀࠊࠡࠢࠣࠤࡵࡧࡳࡴࠌࠣࠤࡴ࡭࡟ࡥࡤࠫࡷࡪࡲࡦ࠭ࡣࡵ࡫࠱ࡺࡥ࡮ࡲࡲࡶࡦࡸࡹࠪࠌࡓࡨࡧ࠴ࡤࡰࡡࡥࠤࡂࠦ࡭ࡰࡦࡢࡦࡷ࡫ࡡ࡬ࠌࡓࡨࡧ࠴ࡤࡰࡡࡥࡶࡪࡧ࡫ࠡ࠿ࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰࠐࡐࡥࡤࠫ࠭࠳ࡹࡥࡵࡡࡷࡶࡦࡩࡥࠩࠫ࡟ࡲࠧࠨࠢధ").format(str(bstack11l1l11l1_opy_))
          bstack1l1l1ll1l1_opy_ = bstack1ll11lll_opy_ + bstack111ll111_opy_
          bstack1l1ll1l1_opy_ = bstack11l1l11l1_opy_[bstack111lll1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧన")] + bstack111lll1_opy_ (u"ࠬࡥࡢࡴࡶࡤࡧࡰࡥࡴࡦ࡯ࡳ࠲ࡵࡿࠧ఩")
          with open(bstack1l1ll1l1_opy_, bstack111lll1_opy_ (u"࠭ࡷࠨప")):
            pass
          with open(bstack1l1ll1l1_opy_, bstack111lll1_opy_ (u"ࠢࡸ࠭ࠥఫ")) as f:
            f.write(bstack1l1l1ll1l1_opy_)
          import subprocess
          bstack1l111111_opy_ = subprocess.run([bstack111lll1_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࠣబ"), bstack1l1ll1l1_opy_])
          if os.path.exists(bstack1l1ll1l1_opy_):
            os.unlink(bstack1l1ll1l1_opy_)
          os._exit(bstack1l111111_opy_.returncode)
        else:
          if bstack11ll11l11_opy_(bstack11l1l11l1_opy_[bstack111lll1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬభ")]):
            bstack11l1l11l1_opy_[bstack111lll1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭మ")].remove(bstack111lll1_opy_ (u"ࠫ࠲ࡳࠧయ"))
            bstack11l1l11l1_opy_[bstack111lll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨర")].remove(bstack111lll1_opy_ (u"࠭ࡰࡥࡤࠪఱ"))
            bstack11l1l11l1_opy_[bstack111lll1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪల")] = bstack11l1l11l1_opy_[bstack111lll1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫళ")][0]
          bstack111111lll_opy_(bstack1lll1111l1_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack11l1l11l1_opy_[bstack111lll1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬఴ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack111lll1_opy_ (u"ࠪࡣࡤࡴࡡ࡮ࡧࡢࡣࠬవ")] = bstack111lll1_opy_ (u"ࠫࡤࡥ࡭ࡢ࡫ࡱࡣࡤ࠭శ")
          mod_globals[bstack111lll1_opy_ (u"ࠬࡥ࡟ࡧ࡫࡯ࡩࡤࡥࠧష")] = os.path.abspath(bstack11l1l11l1_opy_[bstack111lll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩస")])
          exec(open(bstack11l1l11l1_opy_[bstack111lll1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪహ")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack111lll1_opy_ (u"ࠨࡅࡤࡹ࡬࡮ࡴࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱ࠾ࠥࢁࡽࠨ఺").format(str(e)))
          for driver in bstack1lllllllll_opy_:
            bstack1ll11l1lll_opy_.append({
              bstack111lll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ఻"): bstack11l1l11l1_opy_[bstack111lll1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ఼࠭")],
              bstack111lll1_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪఽ"): str(e),
              bstack111lll1_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫా"): multiprocessing.current_process().name
            })
            bstack1l11ll11_opy_(driver, bstack111lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ి"), bstack111lll1_opy_ (u"ࠢࡔࡧࡶࡷ࡮ࡵ࡮ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰࠥీ") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1lllllllll_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack1ll1l1l11l_opy_, CONFIG, logger)
      bstack1l1lllll11_opy_()
      bstack11l11111_opy_()
      bstack1l1l11l1_opy_ = {
        bstack111lll1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫు"): args[0],
        bstack111lll1_opy_ (u"ࠩࡆࡓࡓࡌࡉࡈࠩూ"): CONFIG,
        bstack111lll1_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏࠫృ"): bstack1llll11lll_opy_,
        bstack111lll1_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ౄ"): bstack1ll1l1l11l_opy_
      }
      percy.bstack1l111l1ll_opy_()
      if bstack111lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ౅") in CONFIG:
        bstack1l1l1l11l_opy_ = []
        manager = multiprocessing.Manager()
        bstack1llll11ll1_opy_ = manager.list()
        if bstack11ll11l11_opy_(args):
          for index, platform in enumerate(CONFIG[bstack111lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩె")]):
            if index == 0:
              bstack1l1l11l1_opy_[bstack111lll1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪే")] = args
            bstack1l1l1l11l_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack1l1l11l1_opy_, bstack1llll11ll1_opy_)))
        else:
          for index, platform in enumerate(CONFIG[bstack111lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫై")]):
            bstack1l1l1l11l_opy_.append(multiprocessing.Process(name=str(index),
                                                       target=run_on_browserstack,
                                                       args=(bstack1l1l11l1_opy_, bstack1llll11ll1_opy_)))
        for t in bstack1l1l1l11l_opy_:
          t.start()
        for t in bstack1l1l1l11l_opy_:
          t.join()
        bstack1l1ll11l_opy_ = list(bstack1llll11ll1_opy_)
      else:
        if bstack11ll11l11_opy_(args):
          bstack1l1l11l1_opy_[bstack111lll1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ౉")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack1l1l11l1_opy_,))
          test.start()
          test.join()
        else:
          bstack111111lll_opy_(bstack1lll1111l1_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack111lll1_opy_ (u"ࠪࡣࡤࡴࡡ࡮ࡧࡢࡣࠬొ")] = bstack111lll1_opy_ (u"ࠫࡤࡥ࡭ࡢ࡫ࡱࡣࡤ࠭ో")
          mod_globals[bstack111lll1_opy_ (u"ࠬࡥ࡟ࡧ࡫࡯ࡩࡤࡥࠧౌ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack1llll111ll_opy_ == bstack111lll1_opy_ (u"࠭ࡰࡢࡤࡲࡸ్ࠬ") or bstack1llll111ll_opy_ == bstack111lll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭౎"):
    percy.init(bstack1ll1l1l11l_opy_, CONFIG, logger)
    percy.bstack1l111l1ll_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack1l11ll11l_opy_(e, bstack1ll1llll1_opy_)
    bstack1l1lllll11_opy_()
    bstack111111lll_opy_(bstack1l1111l1l_opy_)
    if bstack1ll1ll1ll_opy_ and bstack111lll1_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭౏") in args:
      i = args.index(bstack111lll1_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧ౐"))
      args.pop(i)
      args.pop(i)
    if bstack1ll1ll1ll_opy_:
      args.insert(0, str(bstack1111l11ll_opy_))
      args.insert(0, str(bstack111lll1_opy_ (u"ࠪ࠱࠲ࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨ౑")))
    if bstack1llll11l1_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack1111111ll_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack1lll11l111_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack111lll1_opy_ (u"ࠦࡗࡕࡂࡐࡖࡢࡓࡕ࡚ࡉࡐࡐࡖࠦ౒"),
        ).parse_args(bstack1111111ll_opy_)
        args.insert(args.index(bstack1lll11l111_opy_[0]), str(bstack111lll1_opy_ (u"ࠬ࠳࠭࡭࡫ࡶࡸࡪࡴࡥࡳࠩ౓")))
        args.insert(args.index(bstack1lll11l111_opy_[0]), str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack111lll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡲࡰࡤࡲࡸࡤࡲࡩࡴࡶࡨࡲࡪࡸ࠮ࡱࡻࠪ౔"))))
        if bstack1lllll111l_opy_(os.environ.get(bstack111lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒౕࠬ"))) and str(os.environ.get(bstack111lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓࡥࡔࡆࡕࡗࡗౖࠬ"), bstack111lll1_opy_ (u"ࠩࡱࡹࡱࡲࠧ౗"))) != bstack111lll1_opy_ (u"ࠪࡲࡺࡲ࡬ࠨౘ"):
          for bstack1lll11ll11_opy_ in bstack1lll11l111_opy_:
            args.remove(bstack1lll11ll11_opy_)
          bstack1ll1ll111l_opy_ = os.environ.get(bstack111lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࡡࡗࡉࡘ࡚ࡓࠨౙ")).split(bstack111lll1_opy_ (u"ࠬ࠲ࠧౚ"))
          for bstack11l11l1ll_opy_ in bstack1ll1ll111l_opy_:
            args.append(bstack11l11l1ll_opy_)
      except Exception as e:
        logger.error(bstack111lll1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡦࡺࡴࡢࡥ࡫࡭ࡳ࡭ࠠ࡭࡫ࡶࡸࡪࡴࡥࡳࠢࡩࡳࡷࠦࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠴ࠠࡆࡴࡵࡳࡷࠦ࠭ࠡࠤ౛").format(e))
    pabot.main(args)
  elif bstack1llll111ll_opy_ == bstack111lll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨ౜"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1l11ll11l_opy_(e, bstack1ll1llll1_opy_)
    for a in args:
      if bstack111lll1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡑࡎࡄࡘࡋࡕࡒࡎࡋࡑࡈࡊ࡞ࠧౝ") in a:
        bstack1ll111lll1_opy_ = int(a.split(bstack111lll1_opy_ (u"ࠩ࠽ࠫ౞"))[1])
      if bstack111lll1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡇࡉࡋࡒࡏࡄࡃࡏࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧ౟") in a:
        bstack1111l1l1l_opy_ = str(a.split(bstack111lll1_opy_ (u"ࠫ࠿࠭ౠ"))[1])
      if bstack111lll1_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡈࡒࡉࡂࡔࡊࡗࠬౡ") in a:
        bstack111ll1ll_opy_ = str(a.split(bstack111lll1_opy_ (u"࠭࠺ࠨౢ"))[1])
    bstack1l1l11l1l_opy_ = None
    if bstack111lll1_opy_ (u"ࠧ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽ࠭ౣ") in args:
      i = args.index(bstack111lll1_opy_ (u"ࠨ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢ࡭ࡹ࡫࡭ࡠ࡫ࡱࡨࡪࡾࠧ౤"))
      args.pop(i)
      bstack1l1l11l1l_opy_ = args.pop(i)
    if bstack1l1l11l1l_opy_ is not None:
      global bstack111l11111_opy_
      bstack111l11111_opy_ = bstack1l1l11l1l_opy_
    bstack111111lll_opy_(bstack1l1111l1l_opy_)
    run_cli(args)
    if bstack111lll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠭౥") in multiprocessing.current_process().__dict__.keys():
      for bstack1lll11lll1_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1ll11l1lll_opy_.append(bstack1lll11lll1_opy_)
  elif bstack1llll111ll_opy_ == bstack111lll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ౦"):
    percy.init(bstack1ll1l1l11l_opy_, CONFIG, logger)
    percy.bstack1l111l1ll_opy_()
    bstack1l1ll1ll11_opy_ = bstack11ll1l1l1_opy_(args, logger, CONFIG, bstack1ll1ll1ll_opy_)
    bstack1l1ll1ll11_opy_.bstack111ll11l_opy_()
    bstack1l1lllll11_opy_()
    bstack1lll1ll11l_opy_ = True
    bstack111llll1_opy_ = bstack1l1ll1ll11_opy_.bstack11llll111_opy_()
    bstack1l1ll1ll11_opy_.bstack1l1l11l1_opy_(bstack11l11lll_opy_)
    bstack1llllll11l_opy_ = bstack1l1ll1ll11_opy_.bstack1ll1ll1111_opy_(bstack1ll111l11l_opy_, {
      bstack111lll1_opy_ (u"ࠫࡍ࡛ࡂࡠࡗࡕࡐࠬ౧"): bstack1llll11lll_opy_,
      bstack111lll1_opy_ (u"ࠬࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ౨"): bstack1ll1l1l11l_opy_,
      bstack111lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩ౩"): bstack1ll1ll1ll_opy_
    })
    bstack1lll11lll_opy_ = 1 if len(bstack1llllll11l_opy_) > 0 else 0
  elif bstack1llll111ll_opy_ == bstack111lll1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ౪"):
    try:
      from behave.__main__ import main as bstack1111l1111_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1l11ll11l_opy_(e, bstack11ll11lll_opy_)
    bstack1l1lllll11_opy_()
    bstack1lll1ll11l_opy_ = True
    bstack1l1lll11l1_opy_ = 1
    if bstack111lll1_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ౫") in CONFIG:
      bstack1l1lll11l1_opy_ = CONFIG[bstack111lll1_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ౬")]
    bstack1l11llll_opy_ = int(bstack1l1lll11l1_opy_) * int(len(CONFIG[bstack111lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭౭")]))
    config = Configuration(args)
    bstack1llll11l_opy_ = config.paths
    if len(bstack1llll11l_opy_) == 0:
      import glob
      pattern = bstack111lll1_opy_ (u"ࠫ࠯࠰࠯ࠫ࠰ࡩࡩࡦࡺࡵࡳࡧࠪ౮")
      bstack111ll11ll_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack111ll11ll_opy_)
      config = Configuration(args)
      bstack1llll11l_opy_ = config.paths
    bstack1l1lllll_opy_ = [os.path.normpath(item) for item in bstack1llll11l_opy_]
    bstack1111ll1l1_opy_ = [os.path.normpath(item) for item in args]
    bstack1111ll1l_opy_ = [item for item in bstack1111ll1l1_opy_ if item not in bstack1l1lllll_opy_]
    import platform as pf
    if pf.system().lower() == bstack111lll1_opy_ (u"ࠬࡽࡩ࡯ࡦࡲࡻࡸ࠭౯"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack1l1lllll_opy_ = [str(PurePosixPath(PureWindowsPath(bstack1lll11ll1_opy_)))
                    for bstack1lll11ll1_opy_ in bstack1l1lllll_opy_]
    bstack11l1lll1l_opy_ = []
    for spec in bstack1l1lllll_opy_:
      bstack1l1l11111_opy_ = []
      bstack1l1l11111_opy_ += bstack1111ll1l_opy_
      bstack1l1l11111_opy_.append(spec)
      bstack11l1lll1l_opy_.append(bstack1l1l11111_opy_)
    execution_items = []
    for bstack1l1l11111_opy_ in bstack11l1lll1l_opy_:
      for index, _ in enumerate(CONFIG[bstack111lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ౰")]):
        item = {}
        item[bstack111lll1_opy_ (u"ࠧࡢࡴࡪࠫ౱")] = bstack111lll1_opy_ (u"ࠨࠢࠪ౲").join(bstack1l1l11111_opy_)
        item[bstack111lll1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ౳")] = index
        execution_items.append(item)
    bstack1lll1ll1l1_opy_ = bstack1llll1ll1_opy_(execution_items, bstack1l11llll_opy_)
    for execution_item in bstack1lll1ll1l1_opy_:
      bstack1l1l1l11l_opy_ = []
      for item in execution_item:
        bstack1l1l1l11l_opy_.append(bstack1llll1ll1l_opy_(name=str(item[bstack111lll1_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩ౴")]),
                                             target=bstack1ll11lll1_opy_,
                                             args=(item[bstack111lll1_opy_ (u"ࠫࡦࡸࡧࠨ౵")],)))
      for t in bstack1l1l1l11l_opy_:
        t.start()
      for t in bstack1l1l1l11l_opy_:
        t.join()
  else:
    bstack1ll1lll111_opy_(bstack1l111ll11_opy_)
  if not bstack11l1l11l1_opy_:
    bstack11111l1l1_opy_()
def browserstack_initialize(bstack1ll1ll1lll_opy_=None):
  run_on_browserstack(bstack1ll1ll1lll_opy_, None, True)
def bstack11111l1l1_opy_():
  global CONFIG
  global bstack1ll1l111ll_opy_
  global bstack1lll11lll_opy_
  bstack1llll11l1_opy_.stop()
  bstack1llll11l1_opy_.bstack1l11l111l_opy_()
  if bstack1lllll1111_opy_.bstack1111l1ll1_opy_(CONFIG):
    bstack1lllll1111_opy_.bstack1ll11ll1ll_opy_()
  [bstack11ll111l1_opy_, bstack1lll1l1lll_opy_] = bstack1lllll11ll_opy_()
  if bstack11ll111l1_opy_ is not None and bstack111l11ll1_opy_() != -1:
    sessions = bstack111l1ll11_opy_(bstack11ll111l1_opy_)
    bstack111l1l11l_opy_(sessions, bstack1lll1l1lll_opy_)
  if bstack1ll1l111ll_opy_ == bstack111lll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ౶") and bstack1lll11lll_opy_ != 0:
    sys.exit(bstack1lll11lll_opy_)
def bstack11ll1lll1_opy_(bstack1lll1lllll_opy_):
  if bstack1lll1lllll_opy_:
    return bstack1lll1lllll_opy_.capitalize()
  else:
    return bstack111lll1_opy_ (u"࠭ࠧ౷")
def bstack1111l1ll_opy_(bstack11ll1l1l_opy_):
  if bstack111lll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ౸") in bstack11ll1l1l_opy_ and bstack11ll1l1l_opy_[bstack111lll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭౹")] != bstack111lll1_opy_ (u"ࠩࠪ౺"):
    return bstack11ll1l1l_opy_[bstack111lll1_opy_ (u"ࠪࡲࡦࡳࡥࠨ౻")]
  else:
    bstack1lll1lll1l_opy_ = bstack111lll1_opy_ (u"ࠦࠧ౼")
    if bstack111lll1_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬ౽") in bstack11ll1l1l_opy_ and bstack11ll1l1l_opy_[bstack111lll1_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭౾")] != None:
      bstack1lll1lll1l_opy_ += bstack11ll1l1l_opy_[bstack111lll1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧ౿")] + bstack111lll1_opy_ (u"ࠣ࠮ࠣࠦಀ")
      if bstack11ll1l1l_opy_[bstack111lll1_opy_ (u"ࠩࡲࡷࠬಁ")] == bstack111lll1_opy_ (u"ࠥ࡭ࡴࡹࠢಂ"):
        bstack1lll1lll1l_opy_ += bstack111lll1_opy_ (u"ࠦ࡮ࡕࡓࠡࠤಃ")
      bstack1lll1lll1l_opy_ += (bstack11ll1l1l_opy_[bstack111lll1_opy_ (u"ࠬࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ಄")] or bstack111lll1_opy_ (u"࠭ࠧಅ"))
      return bstack1lll1lll1l_opy_
    else:
      bstack1lll1lll1l_opy_ += bstack11ll1lll1_opy_(bstack11ll1l1l_opy_[bstack111lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨಆ")]) + bstack111lll1_opy_ (u"ࠣࠢࠥಇ") + (
              bstack11ll1l1l_opy_[bstack111lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫಈ")] or bstack111lll1_opy_ (u"ࠪࠫಉ")) + bstack111lll1_opy_ (u"ࠦ࠱ࠦࠢಊ")
      if bstack11ll1l1l_opy_[bstack111lll1_opy_ (u"ࠬࡵࡳࠨಋ")] == bstack111lll1_opy_ (u"ࠨࡗࡪࡰࡧࡳࡼࡹࠢಌ"):
        bstack1lll1lll1l_opy_ += bstack111lll1_opy_ (u"ࠢࡘ࡫ࡱࠤࠧ಍")
      bstack1lll1lll1l_opy_ += bstack11ll1l1l_opy_[bstack111lll1_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬಎ")] or bstack111lll1_opy_ (u"ࠩࠪಏ")
      return bstack1lll1lll1l_opy_
def bstack1ll1l111l_opy_(bstack11ll1ll11_opy_):
  if bstack11ll1ll11_opy_ == bstack111lll1_opy_ (u"ࠥࡨࡴࡴࡥࠣಐ"):
    return bstack111lll1_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡧࡳࡧࡨࡲࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡧࡳࡧࡨࡲࠧࡄࡃࡰ࡯ࡳࡰࡪࡺࡥࡥ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧ಑")
  elif bstack11ll1ll11_opy_ == bstack111lll1_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧಒ"):
    return bstack111lll1_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡴࡨࡨࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡲࡦࡦࠥࡂࡋࡧࡩ࡭ࡧࡧࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩಓ")
  elif bstack11ll1ll11_opy_ == bstack111lll1_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢಔ"):
    return bstack111lll1_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽࡫ࡷ࡫ࡥ࡯࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥ࡫ࡷ࡫ࡥ࡯ࠤࡁࡔࡦࡹࡳࡦࡦ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨಕ")
  elif bstack11ll1ll11_opy_ == bstack111lll1_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣಖ"):
    return bstack111lll1_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࡸࡥࡥ࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࡶࡪࡪࠢ࠿ࡇࡵࡶࡴࡸ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬಗ")
  elif bstack11ll1ll11_opy_ == bstack111lll1_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࠧಘ"):
    return bstack111lll1_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࠤࡧࡨࡥ࠸࠸࠶࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࠦࡩࡪࡧ࠳࠳࠸ࠥࡂ࡙࡯࡭ࡦࡱࡸࡸࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪಙ")
  elif bstack11ll1ll11_opy_ == bstack111lll1_opy_ (u"ࠨࡲࡶࡰࡱ࡭ࡳ࡭ࠢಚ"):
    return bstack111lll1_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡥࡰࡦࡩ࡫࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡥࡰࡦࡩ࡫ࠣࡀࡕࡹࡳࡴࡩ࡯ࡩ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨಛ")
  else:
    return bstack111lll1_opy_ (u"ࠨ࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾ࡧࡲࡡࡤ࡭࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡧࡲࡡࡤ࡭ࠥࡂࠬಜ") + bstack11ll1lll1_opy_(
      bstack11ll1ll11_opy_) + bstack111lll1_opy_ (u"ࠩ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨಝ")
def bstack1l1l1l1l11_opy_(session):
  return bstack111lll1_opy_ (u"ࠪࡀࡹࡸࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡳࡱࡺࠦࡃࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠠࡴࡧࡶࡷ࡮ࡵ࡮࠮ࡰࡤࡱࡪࠨ࠾࠽ࡣࠣ࡬ࡷ࡫ࡦ࠾ࠤࡾࢁࠧࠦࡴࡢࡴࡪࡩࡹࡃࠢࡠࡤ࡯ࡥࡳࡱࠢ࠿ࡽࢀࡀ࠴ࡧ࠾࠽࠱ࡷࡨࡃࢁࡽࡼࡿ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࡄࡻࡾ࠾࠲ࡸࡩࡄ࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࡁࡿࢂࡂ࠯ࡵࡦࡁࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨ࠾ࡼࡿ࠿࠳ࡹࡪ࠾࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁ࠵ࡴࡳࡀࠪಞ").format(
    session[bstack111lll1_opy_ (u"ࠫࡵࡻࡢ࡭࡫ࡦࡣࡺࡸ࡬ࠨಟ")], bstack1111l1ll_opy_(session), bstack1ll1l111l_opy_(session[bstack111lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡸࡺࡡࡵࡷࡶࠫಠ")]),
    bstack1ll1l111l_opy_(session[bstack111lll1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ಡ")]),
    bstack11ll1lll1_opy_(session[bstack111lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨಢ")] or session[bstack111lll1_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨಣ")] or bstack111lll1_opy_ (u"ࠩࠪತ")) + bstack111lll1_opy_ (u"ࠥࠤࠧಥ") + (session[bstack111lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ದ")] or bstack111lll1_opy_ (u"ࠬ࠭ಧ")),
    session[bstack111lll1_opy_ (u"࠭࡯ࡴࠩನ")] + bstack111lll1_opy_ (u"ࠢࠡࠤ಩") + session[bstack111lll1_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬಪ")], session[bstack111lll1_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࠫಫ")] or bstack111lll1_opy_ (u"ࠪࠫಬ"),
    session[bstack111lll1_opy_ (u"ࠫࡨࡸࡥࡢࡶࡨࡨࡤࡧࡴࠨಭ")] if session[bstack111lll1_opy_ (u"ࠬࡩࡲࡦࡣࡷࡩࡩࡥࡡࡵࠩಮ")] else bstack111lll1_opy_ (u"࠭ࠧಯ"))
def bstack111l1l11l_opy_(sessions, bstack1lll1l1lll_opy_):
  try:
    bstack1l1l11l11l_opy_ = bstack111lll1_opy_ (u"ࠢࠣರ")
    if not os.path.exists(bstack1lll11llll_opy_):
      os.mkdir(bstack1lll11llll_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack111lll1_opy_ (u"ࠨࡣࡶࡷࡪࡺࡳ࠰ࡴࡨࡴࡴࡸࡴ࠯ࡪࡷࡱࡱ࠭ಱ")), bstack111lll1_opy_ (u"ࠩࡵࠫಲ")) as f:
      bstack1l1l11l11l_opy_ = f.read()
    bstack1l1l11l11l_opy_ = bstack1l1l11l11l_opy_.replace(bstack111lll1_opy_ (u"ࠪࡿࠪࡘࡅࡔࡗࡏࡘࡘࡥࡃࡐࡗࡑࡘࠪࢃࠧಳ"), str(len(sessions)))
    bstack1l1l11l11l_opy_ = bstack1l1l11l11l_opy_.replace(bstack111lll1_opy_ (u"ࠫࢀࠫࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠧࢀࠫ಴"), bstack1lll1l1lll_opy_)
    bstack1l1l11l11l_opy_ = bstack1l1l11l11l_opy_.replace(bstack111lll1_opy_ (u"ࠬࢁࠥࡃࡗࡌࡐࡉࡥࡎࡂࡏࡈࠩࢂ࠭ವ"),
                                              sessions[0].get(bstack111lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤࡴࡡ࡮ࡧࠪಶ")) if sessions[0] else bstack111lll1_opy_ (u"ࠧࠨಷ"))
    with open(os.path.join(bstack1lll11llll_opy_, bstack111lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠭ࡳࡧࡳࡳࡷࡺ࠮ࡩࡶࡰࡰࠬಸ")), bstack111lll1_opy_ (u"ࠩࡺࠫಹ")) as stream:
      stream.write(bstack1l1l11l11l_opy_.split(bstack111lll1_opy_ (u"ࠪࡿ࡙ࠪࡅࡔࡕࡌࡓࡓ࡙࡟ࡅࡃࡗࡅࠪࢃࠧ಺"))[0])
      for session in sessions:
        stream.write(bstack1l1l1l1l11_opy_(session))
      stream.write(bstack1l1l11l11l_opy_.split(bstack111lll1_opy_ (u"ࠫࢀࠫࡓࡆࡕࡖࡍࡔࡔࡓࡠࡆࡄࡘࡆࠫࡽࠨ಻"))[1])
    logger.info(bstack111lll1_opy_ (u"ࠬࡍࡥ࡯ࡧࡵࡥࡹ࡫ࡤࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡣࡷ࡬ࡰࡩࠦࡡࡳࡶ࡬ࡪࡦࡩࡴࡴࠢࡤࡸࠥࢁࡽࠨ಼").format(bstack1lll11llll_opy_));
  except Exception as e:
    logger.debug(bstack1111l111_opy_.format(str(e)))
def bstack111l1ll11_opy_(bstack11ll111l1_opy_):
  global CONFIG
  try:
    host = bstack111lll1_opy_ (u"࠭ࡡࡱ࡫࠰ࡧࡱࡵࡵࡥࠩಽ") if bstack111lll1_opy_ (u"ࠧࡢࡲࡳࠫಾ") in CONFIG else bstack111lll1_opy_ (u"ࠨࡣࡳ࡭ࠬಿ")
    user = CONFIG[bstack111lll1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫೀ")]
    key = CONFIG[bstack111lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ು")]
    bstack1ll11l11ll_opy_ = bstack111lll1_opy_ (u"ࠫࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧࠪೂ") if bstack111lll1_opy_ (u"ࠬࡧࡰࡱࠩೃ") in CONFIG else bstack111lll1_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨೄ")
    url = bstack111lll1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡽࢀ࠾ࢀࢃࡀࡼࡿ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡻࡾ࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁ࠴ࡹࡥࡴࡵ࡬ࡳࡳࡹ࠮࡫ࡵࡲࡲࠬ೅").format(user, key, host, bstack1ll11l11ll_opy_,
                                                                                bstack11ll111l1_opy_)
    headers = {
      bstack111lll1_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧೆ"): bstack111lll1_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬೇ"),
    }
    proxies = bstack1l1l11llll_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies)
    if response.json():
      return list(map(lambda session: session[bstack111lll1_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨೈ")], response.json()))
  except Exception as e:
    logger.debug(bstack1l11111l1_opy_.format(str(e)))
def bstack1lllll11ll_opy_():
  global CONFIG
  global bstack11l1lllll_opy_
  try:
    if bstack111lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ೉") in CONFIG:
      host = bstack111lll1_opy_ (u"ࠬࡧࡰࡪ࠯ࡦࡰࡴࡻࡤࠨೊ") if bstack111lll1_opy_ (u"࠭ࡡࡱࡲࠪೋ") in CONFIG else bstack111lll1_opy_ (u"ࠧࡢࡲ࡬ࠫೌ")
      user = CONFIG[bstack111lll1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧ್ࠪ")]
      key = CONFIG[bstack111lll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ೎")]
      bstack1ll11l11ll_opy_ = bstack111lll1_opy_ (u"ࠪࡥࡵࡶ࠭ࡢࡷࡷࡳࡲࡧࡴࡦࠩ೏") if bstack111lll1_opy_ (u"ࠫࡦࡶࡰࠨ೐") in CONFIG else bstack111lll1_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ೑")
      url = bstack111lll1_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡼࡿ࠽ࡿࢂࡆࡻࡾ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࢁࡽ࠰ࡤࡸ࡭ࡱࡪࡳ࠯࡬ࡶࡳࡳ࠭೒").format(user, key, host, bstack1ll11l11ll_opy_)
      headers = {
        bstack111lll1_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡶࡼࡴࡪ࠭೓"): bstack111lll1_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫ೔"),
      }
      if bstack111lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫೕ") in CONFIG:
        params = {bstack111lll1_opy_ (u"ࠪࡲࡦࡳࡥࠨೖ"): CONFIG[bstack111lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ೗")], bstack111lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ೘"): CONFIG[bstack111lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ೙")]}
      else:
        params = {bstack111lll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ೚"): CONFIG[bstack111lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ೛")]}
      proxies = bstack1l1l11llll_opy_(CONFIG, url)
      response = requests.get(url, params=params, headers=headers, proxies=proxies)
      if response.json():
        bstack1ll111l111_opy_ = response.json()[0][bstack111lll1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡢࡶ࡫࡯ࡨࠬ೜")]
        if bstack1ll111l111_opy_:
          bstack1lll1l1lll_opy_ = bstack1ll111l111_opy_[bstack111lll1_opy_ (u"ࠪࡴࡺࡨ࡬ࡪࡥࡢࡹࡷࡲࠧೝ")].split(bstack111lll1_opy_ (u"ࠫࡵࡻࡢ࡭࡫ࡦ࠱ࡧࡻࡩ࡭ࡦࠪೞ"))[0] + bstack111lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡷ࠴࠭೟") + bstack1ll111l111_opy_[
            bstack111lll1_opy_ (u"࠭ࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩೠ")]
          logger.info(bstack1l1l1ll1ll_opy_.format(bstack1lll1l1lll_opy_))
          bstack11l1lllll_opy_ = bstack1ll111l111_opy_[bstack111lll1_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪೡ")]
          bstack11ll1111_opy_ = CONFIG[bstack111lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫೢ")]
          if bstack111lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫೣ") in CONFIG:
            bstack11ll1111_opy_ += bstack111lll1_opy_ (u"ࠪࠤࠬ೤") + CONFIG[bstack111lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭೥")]
          if bstack11ll1111_opy_ != bstack1ll111l111_opy_[bstack111lll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ೦")]:
            logger.debug(bstack111lll1l1_opy_.format(bstack1ll111l111_opy_[bstack111lll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ೧")], bstack11ll1111_opy_))
          return [bstack1ll111l111_opy_[bstack111lll1_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ೨")], bstack1lll1l1lll_opy_]
    else:
      logger.warn(bstack1ll11l11_opy_)
  except Exception as e:
    logger.debug(bstack1111ll1ll_opy_.format(str(e)))
  return [None, None]
def bstack11l1llll1_opy_(url, bstack1l1ll1l11l_opy_=False):
  global CONFIG
  global bstack1lll1lll_opy_
  if not bstack1lll1lll_opy_:
    hostname = bstack1l1l1111l_opy_(url)
    is_private = bstack1ll11l111_opy_(hostname)
    if (bstack111lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ೩") in CONFIG and not bstack1lllll111l_opy_(CONFIG[bstack111lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭೪")])) and (is_private or bstack1l1ll1l11l_opy_):
      bstack1lll1lll_opy_ = hostname
def bstack1l1l1111l_opy_(url):
  return urlparse(url).hostname
def bstack1ll11l111_opy_(hostname):
  for bstack111l1lll_opy_ in bstack11l11ll1l_opy_:
    regex = re.compile(bstack111l1lll_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack11l111l1l_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def getAccessibilityResults(driver):
  global CONFIG
  global bstack1ll111lll1_opy_
  if not bstack1lllll1111_opy_.bstack1lll1llll_opy_(CONFIG, bstack1ll111lll1_opy_):
    logger.warning(bstack111lll1_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢࡦࡥࡳࡴ࡯ࡵࠢࡵࡩࡹࡸࡩࡦࡸࡨࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷ࠳ࠨ೫"))
    return {}
  try:
    results = driver.execute_script(bstack111lll1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡴࡨࡸࡺࡸ࡮ࠡࡰࡨࡻࠥࡖࡲࡰ࡯࡬ࡷࡪ࠮ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࠪࡵࡩࡸࡵ࡬ࡷࡧ࠯ࠤࡷ࡫ࡪࡦࡥࡷ࠭ࠥࢁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡺࡲࡺࠢࡾࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡣࡰࡰࡶࡸࠥ࡫ࡶࡦࡰࡷࠤࡂࠦ࡮ࡦࡹࠣࡇࡺࡹࡴࡰ࡯ࡈࡺࡪࡴࡴࠩࠩࡄ࠵࠶࡟࡟ࡕࡃࡓࡣࡌࡋࡔࡠࡔࡈࡗ࡚ࡒࡔࡔࠩࠬ࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡤࡱࡱࡷࡹࠦࡦ࡯ࠢࡀࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࠨࡦࡸࡨࡲࡹ࠯ࠠࡼࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡹ࡬ࡲࡩࡵࡷ࠯ࡴࡨࡱࡴࡼࡥࡆࡸࡨࡲࡹࡒࡩࡴࡶࡨࡲࡪࡸࠨࠨࡃ࠴࠵࡞ࡥࡒࡆࡕࡘࡐ࡙࡙࡟ࡓࡇࡖࡔࡔࡔࡓࡆࠩ࠯ࠤ࡫ࡴࠩ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡴࡨࡷࡴࡲࡶࡦࠪࡨࡺࡪࡴࡴ࠯ࡦࡨࡸࡦ࡯࡬࠯ࡦࡤࡸࡦ࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡹ࡬ࡲࡩࡵࡷ࠯ࡣࡧࡨࡊࡼࡥ࡯ࡶࡏ࡭ࡸࡺࡥ࡯ࡧࡵࠬࠬࡇ࠱࠲࡛ࡢࡖࡊ࡙ࡕࡍࡖࡖࡣࡗࡋࡓࡑࡑࡑࡗࡊ࠭ࠬࠡࡨࡱ࠭ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡹ࡬ࡲࡩࡵࡷ࠯ࡦ࡬ࡷࡵࡧࡴࡤࡪࡈࡺࡪࡴࡴࠩࡧࡹࡩࡳࡺࠩ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾࠢࡦࡥࡹࡩࡨࠡࡽࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡸࡥ࡫ࡧࡦࡸ࠭࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽࠋࠢࠣࠤࠥࠦࠠࠡࠢࢀ࠭ࡀࠐࠠࠡࠢࠣࠦࠧࠨ೬"))
    return results
  except Exception:
    logger.error(bstack111lll1_opy_ (u"ࠧࡔ࡯ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴࠢࡺࡩࡷ࡫ࠠࡧࡱࡸࡲࡩ࠴ࠢ೭"))
    return {}
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack1ll111lll1_opy_
  if not bstack1lllll1111_opy_.bstack1lll1llll_opy_(CONFIG, bstack1ll111lll1_opy_):
    logger.warning(bstack111lll1_opy_ (u"ࠨࡎࡰࡶࠣࡥࡳࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳࠡࡵࡸࡱࡲࡧࡲࡺ࠰ࠥ೮"))
    return {}
  try:
    bstack1ll111ll_opy_ = driver.execute_script(bstack111lll1_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡷ࡫ࡴࡶࡴࡱࠤࡳ࡫ࡷࠡࡒࡵࡳࡲ࡯ࡳࡦࠪࡩࡹࡳࡩࡴࡪࡱࡱࠤ࠭ࡸࡥࡴࡱ࡯ࡺࡪ࠲ࠠࡳࡧ࡭ࡩࡨࡺࠩࠡࡽࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡶࡵࡽࠥࢁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡦࡳࡳࡹࡴࠡࡧࡹࡩࡳࡺࠠ࠾ࠢࡱࡩࡼࠦࡃࡶࡵࡷࡳࡲࡋࡶࡦࡰࡷࠬࠬࡇ࠱࠲࡛ࡢࡘࡆࡖ࡟ࡈࡇࡗࡣࡗࡋࡓࡖࡎࡗࡗࡤ࡙ࡕࡎࡏࡄࡖ࡞࠭ࠩ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡨࡵ࡮ࡴࡶࠣࡪࡳࠦ࠽ࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࠬࡪࡼࡥ࡯ࡶࠬࠤࢀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡽࡩ࡯ࡦࡲࡻ࠳ࡸࡥ࡮ࡱࡹࡩࡊࡼࡥ࡯ࡶࡏ࡭ࡸࡺࡥ࡯ࡧࡵࠬࠬࡇ࠱࠲࡛ࡢࡖࡊ࡙ࡕࡍࡖࡖࡣࡘ࡛ࡍࡎࡃࡕ࡝ࡤࡘࡅࡔࡒࡒࡒࡘࡋࠧ࠭ࠢࡩࡲ࠮ࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡲࡦࡵࡲࡰࡻ࡫ࠨࡦࡸࡨࡲࡹ࠴ࡤࡦࡶࡤ࡭ࡱ࠴ࡳࡶ࡯ࡰࡥࡷࡿࠩ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡺ࡭ࡳࡪ࡯ࡸ࠰ࡤࡨࡩࡋࡶࡦࡰࡷࡐ࡮ࡹࡴࡦࡰࡨࡶ࠭࠭ࡁ࠲࠳࡜ࡣࡗࡋࡓࡖࡎࡗࡗࡤ࡙ࡕࡎࡏࡄࡖ࡞ࡥࡒࡆࡕࡓࡓࡓ࡙ࡅࠨ࠮ࠣࡪࡳ࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡻ࡮ࡴࡤࡰࡹ࠱ࡨ࡮ࡹࡰࡢࡶࡦ࡬ࡊࡼࡥ࡯ࡶࠫࡩࡻ࡫࡮ࡵࠫ࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࢀࠤࡨࡧࡴࡤࡪࠣࡿࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡳࡧ࡭ࡩࡨࡺࠨࠪ࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿࠍࠤࠥࠦࠠࠡࠢࠣࠤࢂ࠯࠻ࠋࠢࠣࠤࠥࠨࠢࠣ೯"))
    return bstack1ll111ll_opy_
  except Exception:
    logger.error(bstack111lll1_opy_ (u"ࠣࡐࡲࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡸࡻ࡭࡮ࡣࡵࡽࠥࡽࡡࡴࠢࡩࡳࡺࡴࡤ࠯ࠤ೰"))
    return {}