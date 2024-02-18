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
import re
import sys
import json
import time
import shutil
import tempfile
import requests
import subprocess
from threading import Thread
from os.path import expanduser
from bstack_utils.constants import *
from requests.auth import HTTPBasicAuth
from bstack_utils.helper import bstack11ll111l_opy_, bstack1l1111111_opy_
class bstack1ll1l1lll1_opy_:
  working_dir = os.getcwd()
  bstack1ll1l1l1l_opy_ = False
  config = {}
  binary_path = bstack111lll1_opy_ (u"ࠨࠩጳ")
  bstack111ll1111l_opy_ = bstack111lll1_opy_ (u"ࠩࠪጴ")
  bstack1lll1111ll_opy_ = False
  bstack111lll1ll1_opy_ = None
  bstack111llll1ll_opy_ = {}
  bstack111lll1l1l_opy_ = 300
  bstack111l11l11l_opy_ = False
  logger = None
  bstack111ll1lll1_opy_ = False
  bstack111llll11l_opy_ = bstack111lll1_opy_ (u"ࠪࠫጵ")
  bstack111l1l1ll1_opy_ = {
    bstack111lll1_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫጶ") : 1,
    bstack111lll1_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽ࠭ጷ") : 2,
    bstack111lll1_opy_ (u"࠭ࡥࡥࡩࡨࠫጸ") : 3,
    bstack111lll1_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࠧጹ") : 4
  }
  def __init__(self) -> None: pass
  def bstack111l11llll_opy_(self):
    bstack111lll1l11_opy_ = bstack111lll1_opy_ (u"ࠨࠩጺ")
    bstack111l1l1l1l_opy_ = sys.platform
    bstack111l1ll11l_opy_ = bstack111lll1_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨጻ")
    if re.match(bstack111lll1_opy_ (u"ࠥࡨࡦࡸࡷࡪࡰࡿࡱࡦࡩࠠࡰࡵࠥጼ"), bstack111l1l1l1l_opy_) != None:
      bstack111lll1l11_opy_ = bstack11ll11ll11_opy_ + bstack111lll1_opy_ (u"ࠦ࠴ࡶࡥࡳࡥࡼ࠱ࡴࡹࡸ࠯ࡼ࡬ࡴࠧጽ")
      self.bstack111llll11l_opy_ = bstack111lll1_opy_ (u"ࠬࡳࡡࡤࠩጾ")
    elif re.match(bstack111lll1_opy_ (u"ࠨ࡭ࡴࡹ࡬ࡲࢁࡳࡳࡺࡵࡿࡱ࡮ࡴࡧࡸࡾࡦࡽ࡬ࡽࡩ࡯ࡾࡥࡧࡨࡽࡩ࡯ࡾࡺ࡭ࡳࡩࡥࡽࡧࡰࡧࢁࡽࡩ࡯࠵࠵ࠦጿ"), bstack111l1l1l1l_opy_) != None:
      bstack111lll1l11_opy_ = bstack11ll11ll11_opy_ + bstack111lll1_opy_ (u"ࠢ࠰ࡲࡨࡶࡨࡿ࠭ࡸ࡫ࡱ࠲ࡿ࡯ࡰࠣፀ")
      bstack111l1ll11l_opy_ = bstack111lll1_opy_ (u"ࠣࡲࡨࡶࡨࡿ࠮ࡦࡺࡨࠦፁ")
      self.bstack111llll11l_opy_ = bstack111lll1_opy_ (u"ࠩࡺ࡭ࡳ࠭ፂ")
    else:
      bstack111lll1l11_opy_ = bstack11ll11ll11_opy_ + bstack111lll1_opy_ (u"ࠥ࠳ࡵ࡫ࡲࡤࡻ࠰ࡰ࡮ࡴࡵࡹ࠰ࡽ࡭ࡵࠨፃ")
      self.bstack111llll11l_opy_ = bstack111lll1_opy_ (u"ࠫࡱ࡯࡮ࡶࡺࠪፄ")
    return bstack111lll1l11_opy_, bstack111l1ll11l_opy_
  def bstack111l111lll_opy_(self):
    try:
      bstack111l1l111l_opy_ = [os.path.join(expanduser(bstack111lll1_opy_ (u"ࠧࢄࠢፅ")), bstack111lll1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ፆ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack111l1l111l_opy_:
        if(self.bstack111l11ll11_opy_(path)):
          return path
      raise bstack111lll1_opy_ (u"ࠢࡖࡰࡤࡰࡧ࡫ࠠࡵࡱࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠦፇ")
    except Exception as e:
      self.logger.error(bstack111lll1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩࠥࡶࡡࡵࡪࠣࡪࡴࡸࠠࡱࡧࡵࡧࡾࠦࡤࡰࡹࡱࡰࡴࡧࡤ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࠳ࠠࡼࡿࠥፈ").format(e))
  def bstack111l11ll11_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack111l1l1lll_opy_(self, bstack111lll1l11_opy_, bstack111l1ll11l_opy_):
    try:
      bstack111lll11l1_opy_ = self.bstack111l111lll_opy_()
      bstack111l11lll1_opy_ = os.path.join(bstack111lll11l1_opy_, bstack111lll1_opy_ (u"ࠩࡳࡩࡷࡩࡹ࠯ࡼ࡬ࡴࠬፉ"))
      bstack111l1l1111_opy_ = os.path.join(bstack111lll11l1_opy_, bstack111l1ll11l_opy_)
      if os.path.exists(bstack111l1l1111_opy_):
        self.logger.info(bstack111lll1_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࢀࢃࠬࠡࡵ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠧፊ").format(bstack111l1l1111_opy_))
        return bstack111l1l1111_opy_
      if os.path.exists(bstack111l11lll1_opy_):
        self.logger.info(bstack111lll1_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡾ࡮ࡶࠠࡧࡱࡸࡲࡩࠦࡩ࡯ࠢࡾࢁ࠱ࠦࡵ࡯ࡼ࡬ࡴࡵ࡯࡮ࡨࠤፋ").format(bstack111l11lll1_opy_))
        return self.bstack111l1l1l11_opy_(bstack111l11lll1_opy_, bstack111l1ll11l_opy_)
      self.logger.info(bstack111lll1_opy_ (u"ࠧࡊ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡶࡴࡳࠠࡼࡿࠥፌ").format(bstack111lll1l11_opy_))
      response = bstack1l1111111_opy_(bstack111lll1_opy_ (u"࠭ࡇࡆࡖࠪፍ"), bstack111lll1l11_opy_, {}, {})
      if response.status_code == 200:
        with open(bstack111l11lll1_opy_, bstack111lll1_opy_ (u"ࠧࡸࡤࠪፎ")) as file:
          file.write(response.content)
        self.logger.info(bstack111l1lll1l_opy_ (u"ࠣࡆࡲࡻࡳࡲ࡯ࡢࡦࡨࡨࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤࡦࡴࡤࠡࡵࡤࡺࡪࡪࠠࡢࡶࠣࡿࡧ࡯࡮ࡢࡴࡼࡣࡿ࡯ࡰࡠࡲࡤࡸ࡭ࢃࠢፏ"))
        return self.bstack111l1l1l11_opy_(bstack111l11lll1_opy_, bstack111l1ll11l_opy_)
      else:
        raise(bstack111l1lll1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠠࡵࡪࡨࠤ࡫࡯࡬ࡦ࠰ࠣࡗࡹࡧࡴࡶࡵࠣࡧࡴࡪࡥ࠻ࠢࡾࡶࡪࡹࡰࡰࡰࡶࡩ࠳ࡹࡴࡢࡶࡸࡷࡤࡩ࡯ࡥࡧࢀࠦፐ"))
    except:
      self.logger.error(bstack111lll1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠢፑ"))
  def bstack111ll1llll_opy_(self, bstack111lll1l11_opy_, bstack111l1ll11l_opy_):
    try:
      bstack111l1l1111_opy_ = self.bstack111l1l1lll_opy_(bstack111lll1l11_opy_, bstack111l1ll11l_opy_)
      bstack111llll1l1_opy_ = self.bstack111lll1111_opy_(bstack111lll1l11_opy_, bstack111l1ll11l_opy_, bstack111l1l1111_opy_)
      return bstack111l1l1111_opy_, bstack111llll1l1_opy_
    except Exception as e:
      self.logger.error(bstack111lll1_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡨࡧࡷࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡴࡦࡺࡨࠣፒ").format(e))
    return bstack111l1l1111_opy_, False
  def bstack111lll1111_opy_(self, bstack111lll1l11_opy_, bstack111l1ll11l_opy_, bstack111l1l1111_opy_, bstack111ll1l1l1_opy_ = 0):
    if bstack111ll1l1l1_opy_ > 1:
      return False
    if bstack111l1l1111_opy_ == None or os.path.exists(bstack111l1l1111_opy_) == False:
      self.logger.warn(bstack111lll1_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡵࡧࡴࡩࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨ࠱ࠦࡲࡦࡶࡵࡽ࡮ࡴࡧࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠥፓ"))
      bstack111l1l1111_opy_ = self.bstack111l1l1lll_opy_(bstack111lll1l11_opy_, bstack111l1ll11l_opy_)
      self.bstack111lll1111_opy_(bstack111lll1l11_opy_, bstack111l1ll11l_opy_, bstack111l1l1111_opy_, bstack111ll1l1l1_opy_+1)
    bstack111l11l1ll_opy_ = bstack111lll1_opy_ (u"ࠨ࡞࠯ࠬࡃࡴࡪࡸࡣࡺ࡞࠲ࡧࡱ࡯ࠠ࡝ࡦ࠱ࡠࡩ࠱࠮࡝ࡦ࠮ࠦፔ")
    command = bstack111lll1_opy_ (u"ࠧࡼࡿࠣ࠱࠲ࡼࡥࡳࡵ࡬ࡳࡳ࠭ፕ").format(bstack111l1l1111_opy_)
    bstack111l1l11ll_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack111l11l1ll_opy_, bstack111l1l11ll_opy_) != None:
      return True
    else:
      self.logger.error(bstack111lll1_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡥ࡫ࡩࡨࡱࠠࡧࡣ࡬ࡰࡪࡪࠢፖ"))
      bstack111l1l1111_opy_ = self.bstack111l1l1lll_opy_(bstack111lll1l11_opy_, bstack111l1ll11l_opy_)
      self.bstack111lll1111_opy_(bstack111lll1l11_opy_, bstack111l1ll11l_opy_, bstack111l1l1111_opy_, bstack111ll1l1l1_opy_+1)
  def bstack111l1l1l11_opy_(self, bstack111l11lll1_opy_, bstack111l1ll11l_opy_):
    try:
      working_dir = os.path.dirname(bstack111l11lll1_opy_)
      shutil.unpack_archive(bstack111l11lll1_opy_, working_dir)
      bstack111l1l1111_opy_ = os.path.join(working_dir, bstack111l1ll11l_opy_)
      os.chmod(bstack111l1l1111_opy_, 0o755)
      return bstack111l1l1111_opy_
    except Exception as e:
      self.logger.error(bstack111lll1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡻ࡮ࡻ࡫ࡳࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠥፗ"))
  def bstack111ll1l11l_opy_(self):
    try:
      percy = str(self.config.get(bstack111lll1_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩፘ"), bstack111lll1_opy_ (u"ࠦ࡫ࡧ࡬ࡴࡧࠥፙ"))).lower()
      if percy != bstack111lll1_opy_ (u"ࠧࡺࡲࡶࡧࠥፚ"):
        return False
      self.bstack1lll1111ll_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack111lll1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡧࡩࡹ࡫ࡣࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣ፛").format(e))
  def bstack111l1lll11_opy_(self):
    try:
      bstack111l1lll11_opy_ = str(self.config.get(bstack111lll1_opy_ (u"ࠧࡱࡧࡵࡧࡾࡉࡡࡱࡶࡸࡶࡪࡓ࡯ࡥࡧࠪ፜"), bstack111lll1_opy_ (u"ࠣࡣࡸࡸࡴࠨ፝"))).lower()
      return bstack111l1lll11_opy_
    except Exception as e:
      self.logger.error(bstack111lll1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪࡥࡵࡧࡦࡸࠥࡶࡥࡳࡥࡼࠤࡨࡧࡰࡵࡷࡵࡩࠥࡳ࡯ࡥࡧ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥ፞").format(e))
  def init(self, bstack1ll1l1l1l_opy_, config, logger):
    self.bstack1ll1l1l1l_opy_ = bstack1ll1l1l1l_opy_
    self.config = config
    self.logger = logger
    if not self.bstack111ll1l11l_opy_():
      return
    self.bstack111llll1ll_opy_ = config.get(bstack111lll1_opy_ (u"ࠪࡴࡪࡸࡣࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ፟"), {})
    self.bstack111llll111_opy_ = config.get(bstack111lll1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡆࡥࡵࡺࡵࡳࡧࡐࡳࡩ࡫ࠧ፠"), bstack111lll1_opy_ (u"ࠧࡧࡵࡵࡱࠥ፡"))
    try:
      bstack111lll1l11_opy_, bstack111l1ll11l_opy_ = self.bstack111l11llll_opy_()
      bstack111l1l1111_opy_, bstack111llll1l1_opy_ = self.bstack111ll1llll_opy_(bstack111lll1l11_opy_, bstack111l1ll11l_opy_)
      if bstack111llll1l1_opy_:
        self.binary_path = bstack111l1l1111_opy_
        thread = Thread(target=self.bstack111l1llll1_opy_)
        thread.start()
      else:
        self.bstack111ll1lll1_opy_ = True
        self.logger.error(bstack111lll1_opy_ (u"ࠨࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡱࡧࡵࡧࡾࠦࡰࡢࡶ࡫ࠤ࡫ࡵࡵ࡯ࡦࠣ࠱ࠥࢁࡽ࠭ࠢࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡕ࡫ࡲࡤࡻࠥ።").format(bstack111l1l1111_opy_))
    except Exception as e:
      self.logger.error(bstack111lll1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣ፣").format(e))
  def bstack111ll11111_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack111lll1_opy_ (u"ࠨ࡮ࡲ࡫ࠬ፤"), bstack111lll1_opy_ (u"ࠩࡳࡩࡷࡩࡹ࠯࡮ࡲ࡫ࠬ፥"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack111lll1_opy_ (u"ࠥࡔࡺࡹࡨࡪࡰࡪࠤࡵ࡫ࡲࡤࡻࠣࡰࡴ࡭ࡳࠡࡣࡷࠤࢀࢃࠢ፦").format(logfile))
      self.bstack111ll1111l_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack111lll1_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡧࡷࠤࡵ࡫ࡲࡤࡻࠣࡰࡴ࡭ࠠࡱࡣࡷ࡬࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧ፧").format(e))
  def bstack111l1llll1_opy_(self):
    bstack111ll11lll_opy_ = self.bstack111l1ll1l1_opy_()
    if bstack111ll11lll_opy_ == None:
      self.bstack111ll1lll1_opy_ = True
      self.logger.error(bstack111lll1_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡹࡵ࡫ࡦࡰࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩ࠲ࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹࠣ፨"))
      return False
    command_args = [bstack111lll1_opy_ (u"ࠨࡡࡱࡲ࠽ࡩࡽ࡫ࡣ࠻ࡵࡷࡥࡷࡺࠢ፩") if self.bstack1ll1l1l1l_opy_ else bstack111lll1_opy_ (u"ࠧࡦࡺࡨࡧ࠿ࡹࡴࡢࡴࡷࠫ፪")]
    bstack111l1l11l1_opy_ = self.bstack111lll11ll_opy_()
    if bstack111l1l11l1_opy_ != None:
      command_args.append(bstack111lll1_opy_ (u"ࠣ࠯ࡦࠤࢀࢃࠢ፫").format(bstack111l1l11l1_opy_))
    env = os.environ.copy()
    env[bstack111lll1_opy_ (u"ࠤࡓࡉࡗࡉ࡙ࡠࡖࡒࡏࡊࡔࠢ፬")] = bstack111ll11lll_opy_
    bstack111ll11l1l_opy_ = [self.binary_path]
    self.bstack111ll11111_opy_()
    self.bstack111lll1ll1_opy_ = self.bstack111l11ll1l_opy_(bstack111ll11l1l_opy_ + command_args, env)
    self.logger.debug(bstack111lll1_opy_ (u"ࠥࡗࡹࡧࡲࡵ࡫ࡱ࡫ࠥࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠦ፭"))
    bstack111ll1l1l1_opy_ = 0
    while self.bstack111lll1ll1_opy_.poll() == None:
      bstack111ll1l1ll_opy_ = self.bstack111lll111l_opy_()
      if bstack111ll1l1ll_opy_:
        self.logger.debug(bstack111lll1_opy_ (u"ࠦࡍ࡫ࡡ࡭ࡶ࡫ࠤࡈ࡮ࡥࡤ࡭ࠣࡷࡺࡩࡣࡦࡵࡶࡪࡺࡲࠢ፮"))
        self.bstack111l11l11l_opy_ = True
        return True
      bstack111ll1l1l1_opy_ += 1
      self.logger.debug(bstack111lll1_opy_ (u"ࠧࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠤࡗ࡫ࡴࡳࡻࠣ࠱ࠥࢁࡽࠣ፯").format(bstack111ll1l1l1_opy_))
      time.sleep(2)
    self.logger.error(bstack111lll1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠬࠡࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠠࡇࡣ࡬ࡰࡪࡪࠠࡢࡨࡷࡩࡷࠦࡻࡾࠢࡤࡸࡹ࡫࡭ࡱࡶࡶࠦ፰").format(bstack111ll1l1l1_opy_))
    self.bstack111ll1lll1_opy_ = True
    return False
  def bstack111lll111l_opy_(self, bstack111ll1l1l1_opy_ = 0):
    try:
      if bstack111ll1l1l1_opy_ > 10:
        return False
      bstack111l11l111_opy_ = os.environ.get(bstack111lll1_opy_ (u"ࠧࡑࡇࡕࡇ࡞ࡥࡓࡆࡔ࡙ࡉࡗࡥࡁࡅࡆࡕࡉࡘ࡙ࠧ፱"), bstack111lll1_opy_ (u"ࠨࡪࡷࡸࡵࡀ࠯࠰࡮ࡲࡧࡦࡲࡨࡰࡵࡷ࠾࠺࠹࠳࠹ࠩ፲"))
      bstack111ll1l111_opy_ = bstack111l11l111_opy_ + bstack11ll111l11_opy_
      response = requests.get(bstack111ll1l111_opy_)
      return True if response.json() else False
    except:
      return False
  def bstack111l1ll1l1_opy_(self):
    bstack111ll1ll1l_opy_ = bstack111lll1_opy_ (u"ࠩࡤࡴࡵ࠭፳") if self.bstack1ll1l1l1l_opy_ else bstack111lll1_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬ፴")
    bstack11l1ll11ll_opy_ = bstack111lll1_opy_ (u"ࠦࡦࡶࡩ࠰ࡣࡳࡴࡤࡶࡥࡳࡥࡼ࠳࡬࡫ࡴࡠࡲࡵࡳ࡯࡫ࡣࡵࡡࡷࡳࡰ࡫࡮ࡀࡰࡤࡱࡪࡃࡻࡾࠨࡷࡽࡵ࡫࠽ࡼࡿࠥ፵").format(self.config[bstack111lll1_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪ፶")], bstack111ll1ll1l_opy_)
    uri = bstack11ll111l_opy_(bstack11l1ll11ll_opy_)
    try:
      response = bstack1l1111111_opy_(bstack111lll1_opy_ (u"࠭ࡇࡆࡖࠪ፷"), uri, {}, {bstack111lll1_opy_ (u"ࠧࡢࡷࡷ࡬ࠬ፸"): (self.config[bstack111lll1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ፹")], self.config[bstack111lll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ፺")])})
      if response.status_code == 200:
        bstack111ll111ll_opy_ = response.json()
        if bstack111lll1_opy_ (u"ࠥࡸࡴࡱࡥ࡯ࠤ፻") in bstack111ll111ll_opy_:
          return bstack111ll111ll_opy_[bstack111lll1_opy_ (u"ࠦࡹࡵ࡫ࡦࡰࠥ፼")]
        else:
          raise bstack111lll1_opy_ (u"࡚ࠬ࡯࡬ࡧࡱࠤࡓࡵࡴࠡࡈࡲࡹࡳࡪࠠ࠮ࠢࡾࢁࠬ፽").format(bstack111ll111ll_opy_)
      else:
        raise bstack111lll1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡩࡩࡹࡩࡨࠡࡲࡨࡶࡨࡿࠠࡵࡱ࡮ࡩࡳ࠲ࠠࡓࡧࡶࡴࡴࡴࡳࡦࠢࡶࡸࡦࡺࡵࡴࠢ࠰ࠤࢀࢃࠬࠡࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡆࡴࡪࡹࠡ࠯ࠣࡿࢂࠨ፾").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack111lll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡲࡨࡶࡨࡿࠠࡱࡴࡲ࡮ࡪࡩࡴࠣ፿").format(e))
  def bstack111lll11ll_opy_(self):
    bstack111ll11ll1_opy_ = os.path.join(tempfile.gettempdir(), bstack111lll1_opy_ (u"ࠣࡲࡨࡶࡨࡿࡃࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠦᎀ"))
    try:
      if bstack111lll1_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪᎁ") not in self.bstack111llll1ll_opy_:
        self.bstack111llll1ll_opy_[bstack111lll1_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫᎂ")] = 2
      with open(bstack111ll11ll1_opy_, bstack111lll1_opy_ (u"ࠫࡼ࠭ᎃ")) as fp:
        json.dump(self.bstack111llll1ll_opy_, fp)
      return bstack111ll11ll1_opy_
    except Exception as e:
      self.logger.error(bstack111lll1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡥࡵࡩࡦࡺࡥࠡࡲࡨࡶࡨࡿࠠࡤࡱࡱࡪ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᎄ").format(e))
  def bstack111l11ll1l_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack111llll11l_opy_ == bstack111lll1_opy_ (u"࠭ࡷࡪࡰࠪᎅ"):
        bstack111ll11l11_opy_ = [bstack111lll1_opy_ (u"ࠧࡤ࡯ࡧ࠲ࡪࡾࡥࠨᎆ"), bstack111lll1_opy_ (u"ࠨ࠱ࡦࠫᎇ")]
        cmd = bstack111ll11l11_opy_ + cmd
      cmd = bstack111lll1_opy_ (u"ࠩࠣࠫᎈ").join(cmd)
      self.logger.debug(bstack111lll1_opy_ (u"ࠥࡖࡺࡴ࡮ࡪࡰࡪࠤࢀࢃࠢᎉ").format(cmd))
      with open(self.bstack111ll1111l_opy_, bstack111lll1_opy_ (u"ࠦࡦࠨᎊ")) as bstack111l1ll111_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack111l1ll111_opy_, text=True, stderr=bstack111l1ll111_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack111ll1lll1_opy_ = True
      self.logger.error(bstack111lll1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡱࡧࡵࡧࡾࠦࡷࡪࡶ࡫ࠤࡨࡳࡤࠡ࠯ࠣࡿࢂ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࢀࢃࠢᎋ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack111l11l11l_opy_:
        self.logger.info(bstack111lll1_opy_ (u"ࠨࡓࡵࡱࡳࡴ࡮ࡴࡧࠡࡒࡨࡶࡨࡿࠢᎌ"))
        cmd = [self.binary_path, bstack111lll1_opy_ (u"ࠢࡦࡺࡨࡧ࠿ࡹࡴࡰࡲࠥᎍ")]
        self.bstack111l11ll1l_opy_(cmd)
        self.bstack111l11l11l_opy_ = False
    except Exception as e:
      self.logger.error(bstack111lll1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺ࡯ࡱࠢࡶࡩࡸࡹࡩࡰࡰࠣࡻ࡮ࡺࡨࠡࡥࡲࡱࡲࡧ࡮ࡥࠢ࠰ࠤࢀࢃࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱ࠾ࠥࢁࡽࠣᎎ").format(cmd, e))
  def bstack1l111l1ll_opy_(self):
    if not self.bstack1lll1111ll_opy_:
      return
    try:
      bstack111l11l1l1_opy_ = 0
      while not self.bstack111l11l11l_opy_ and bstack111l11l1l1_opy_ < self.bstack111lll1l1l_opy_:
        if self.bstack111ll1lll1_opy_:
          self.logger.info(bstack111lll1_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡵࡨࡸࡺࡶࠠࡧࡣ࡬ࡰࡪࡪࠢᎏ"))
          return
        time.sleep(1)
        bstack111l11l1l1_opy_ += 1
      os.environ[bstack111lll1_opy_ (u"ࠪࡔࡊࡘࡃ࡚ࡡࡅࡉࡘ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࠩ᎐")] = str(self.bstack111l1lllll_opy_())
      self.logger.info(bstack111lll1_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡷࡪࡺࡵࡱࠢࡦࡳࡲࡶ࡬ࡦࡶࡨࡨࠧ᎑"))
    except Exception as e:
      self.logger.error(bstack111lll1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠠࡱࡧࡵࡧࡾ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨ᎒").format(e))
  def bstack111l1lllll_opy_(self):
    if self.bstack1ll1l1l1l_opy_:
      return
    try:
      bstack111ll111l1_opy_ = [platform[bstack111lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ᎓")].lower() for platform in self.config.get(bstack111lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ᎔"), [])]
      bstack111ll1ll11_opy_ = sys.maxsize
      bstack111l1ll1ll_opy_ = bstack111lll1_opy_ (u"ࠨࠩ᎕")
      for browser in bstack111ll111l1_opy_:
        if browser in self.bstack111l1l1ll1_opy_:
          bstack111lll1lll_opy_ = self.bstack111l1l1ll1_opy_[browser]
        if bstack111lll1lll_opy_ < bstack111ll1ll11_opy_:
          bstack111ll1ll11_opy_ = bstack111lll1lll_opy_
          bstack111l1ll1ll_opy_ = browser
      return bstack111l1ll1ll_opy_
    except Exception as e:
      self.logger.error(bstack111lll1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡦࡪࡹࡴࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥ᎖").format(e))