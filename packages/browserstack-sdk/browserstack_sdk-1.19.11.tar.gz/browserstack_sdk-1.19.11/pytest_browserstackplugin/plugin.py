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
import datetime
import inspect
import logging
import os
import signal
import sys
import threading
from uuid import uuid4
from bstack_utils.percy_sdk import PercySDK
import tempfile
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack11l11l1l1_opy_, bstack1lll1l1111_opy_, update, bstack1l1ll1llll_opy_,
                                       bstack1l1lll1111_opy_, bstack1ll111l11_opy_, bstack1l1ll11lll_opy_, bstack1l1l111l_opy_,
                                       bstack11llllll1_opy_, bstack1lll11l11l_opy_, bstack1l11ll11l_opy_, bstack1ll1111l1l_opy_,
                                       bstack1lll111ll_opy_, getAccessibilityResults, getAccessibilityResultsSummary)
from browserstack_sdk.bstack1l111l11_opy_ import bstack11ll1l1l1_opy_
from browserstack_sdk._version import __version__
from bstack_utils.capture import bstack1l11ll1111_opy_
from bstack_utils.config import Config
from bstack_utils.constants import bstack1l1ll1ll_opy_, bstack11111l1l_opy_, bstack11llll11l_opy_, bstack11111ll1_opy_, \
    bstack1ll1111lll_opy_
from bstack_utils.helper import bstack1ll1111111_opy_, bstack1lllllll1_opy_, bstack11l1l11l1l_opy_, bstack1ll1l11lll_opy_, \
    bstack11l1ll1l1l_opy_, \
    bstack11l1l1l111_opy_, bstack1lll1l11l_opy_, bstack11111lll1_opy_, bstack11l1l1ll1l_opy_, bstack1l1111ll1_opy_, Notset, \
    bstack1llll1l1ll_opy_, bstack11l1lllll1_opy_, bstack11l1llll1l_opy_, Result, bstack11ll1111l1_opy_, bstack11l1ll1l11_opy_, bstack1l11ll1ll1_opy_, \
    bstack1l1l1llll_opy_, bstack1l1llllll_opy_, bstack1lllll111l_opy_, bstack11l11ll111_opy_
from bstack_utils.bstack11l111ll11_opy_ import bstack11l111l1l1_opy_
from bstack_utils.messages import bstack1ll1l1ll1l_opy_, bstack1l111111l_opy_, bstack1l1lll1ll1_opy_, bstack1ll1ll1ll1_opy_, bstack1l1lll1lll_opy_, \
    bstack11l1l1ll_opy_, bstack111lll1ll_opy_, bstack1l1l11lll_opy_, bstack1lll1l111l_opy_, bstack11ll11ll1_opy_, \
    bstack1111111l1_opy_, bstack1llllllll1_opy_
from bstack_utils.proxy import bstack1l1lll11l_opy_, bstack1llll1l11_opy_
from bstack_utils.bstack11l1lll11_opy_ import bstack1111l11ll1_opy_, bstack1111l111ll_opy_, bstack1111l1l11l_opy_, bstack1111l11l1l_opy_, \
    bstack1111l1llll_opy_, bstack1111l1l1l1_opy_, bstack1111l11lll_opy_, bstack1ll1l11111_opy_, bstack1111l11l11_opy_
from bstack_utils.bstack11l1111ll_opy_ import bstack111l1l1l1_opy_
from bstack_utils.bstack111l11l11_opy_ import bstack11lll111l_opy_, bstack11l1llll1_opy_, bstack11111l111_opy_, \
    bstack1l11ll11_opy_, bstack1lll11l11_opy_
from bstack_utils.bstack1l1111l11l_opy_ import bstack1l11lll1ll_opy_
from bstack_utils.bstack111l1111l_opy_ import bstack1llll11l1_opy_
import bstack_utils.bstack1l1l1lll11_opy_ as bstack1lllll1111_opy_
bstack11ll1lll_opy_ = None
bstack1llll1l111_opy_ = None
bstack111l11l1l_opy_ = None
bstack1ll1lllll_opy_ = None
bstack11l11111l_opy_ = None
bstack1111llll_opy_ = None
bstack1lllll11l1_opy_ = None
bstack1l11llll1_opy_ = None
bstack1lll1l1l1l_opy_ = None
bstack1ll11l1l1_opy_ = None
bstack1llllll1l1_opy_ = None
bstack11111llll_opy_ = None
bstack1111lllll_opy_ = None
bstack1llll11l11_opy_ = bstack111lll1_opy_ (u"ࠧࠨᔸ")
CONFIG = {}
bstack1ll1l1l11l_opy_ = False
bstack1llll11lll_opy_ = bstack111lll1_opy_ (u"ࠨࠩᔹ")
bstack1111l1l1l_opy_ = bstack111lll1_opy_ (u"ࠩࠪᔺ")
bstack11l1l11ll_opy_ = False
bstack1lllllllll_opy_ = []
bstack11l1ll11l_opy_ = bstack11111l1l_opy_
bstack1llll1l111l_opy_ = bstack111lll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪᔻ")
bstack1lllll11111_opy_ = False
bstack11l1l1l1_opy_ = {}
logger = logging.getLogger(__name__)
logging.basicConfig(level=bstack11l1ll11l_opy_,
                    format=bstack111lll1_opy_ (u"ࠫࡡࡴࠥࠩࡣࡶࡧࡹ࡯࡭ࡦࠫࡶࠤࡠࠫࠨ࡯ࡣࡰࡩ࠮ࡹ࡝࡜ࠧࠫࡰࡪࡼࡥ࡭ࡰࡤࡱࡪ࠯ࡳ࡞ࠢ࠰ࠤࠪ࠮࡭ࡦࡵࡶࡥ࡬࡫ࠩࡴࠩᔼ"),
                    datefmt=bstack111lll1_opy_ (u"ࠬࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧᔽ"),
                    stream=sys.stdout)
store = {
    bstack111lll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᔾ"): []
}
bstack1llll1l11l1_opy_ = False
def bstack1ll11l11l_opy_():
    global CONFIG
    global bstack11l1ll11l_opy_
    if bstack111lll1_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩᔿ") in CONFIG:
        bstack11l1ll11l_opy_ = bstack1l1ll1ll_opy_[CONFIG[bstack111lll1_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪᕀ")]]
        logging.getLogger().setLevel(bstack11l1ll11l_opy_)
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_1l11lllll1_opy_ = {}
current_test_uuid = None
def bstack1l1l1l1l_opy_(page, bstack11ll1l1ll_opy_):
    try:
        page.evaluate(bstack111lll1_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥᕁ"),
                      bstack111lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠧᕂ") + json.dumps(
                          bstack11ll1l1ll_opy_) + bstack111lll1_opy_ (u"ࠦࢂࢃࠢᕃ"))
    except Exception as e:
        print(bstack111lll1_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡼࡿࠥᕄ"), e)
def bstack1ll1lll1l_opy_(page, message, level):
    try:
        page.evaluate(bstack111lll1_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢᕅ"), bstack111lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬᕆ") + json.dumps(
            message) + bstack111lll1_opy_ (u"ࠨ࠮ࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠫᕇ") + json.dumps(level) + bstack111lll1_opy_ (u"ࠩࢀࢁࠬᕈ"))
    except Exception as e:
        print(bstack111lll1_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡡ࡯ࡰࡲࡸࡦࡺࡩࡰࡰࠣࡿࢂࠨᕉ"), e)
def pytest_configure(config):
    bstack11l11l111_opy_ = Config.bstack111l1ll1_opy_()
    config.args = bstack1llll11l1_opy_.bstack1lllll1ll11_opy_(config.args)
    bstack11l11l111_opy_.bstack111l1llll_opy_(bstack1lllll111l_opy_(config.getoption(bstack111lll1_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᕊ"))))
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    bstack1llll11ll1l_opy_ = item.config.getoption(bstack111lll1_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧᕋ"))
    plugins = item.config.getoption(bstack111lll1_opy_ (u"ࠨࡰ࡭ࡷࡪ࡭ࡳࡹࠢᕌ"))
    report = outcome.get_result()
    bstack1llll11l111_opy_(item, call, report)
    if bstack111lll1_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡶ࡬ࡶࡩ࡬ࡲࠧᕍ") not in plugins or bstack1l1111ll1_opy_():
        return
    summary = []
    driver = getattr(item, bstack111lll1_opy_ (u"ࠣࡡࡧࡶ࡮ࡼࡥࡳࠤᕎ"), None)
    page = getattr(item, bstack111lll1_opy_ (u"ࠤࡢࡴࡦ࡭ࡥࠣᕏ"), None)
    try:
        if (driver == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None):
        bstack1llll11llll_opy_(item, report, summary, bstack1llll11ll1l_opy_)
    if (page is not None):
        bstack1llll1llll1_opy_(item, report, summary, bstack1llll11ll1l_opy_)
def bstack1llll11llll_opy_(item, report, summary, bstack1llll11ll1l_opy_):
    if report.when == bstack111lll1_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩᕐ") and report.skipped:
        bstack1111l11l11_opy_(report)
    if report.when in [bstack111lll1_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࠥᕑ"), bstack111lll1_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴࠢᕒ")]:
        return
    if not bstack11l1l11l1l_opy_():
        return
    try:
        if (str(bstack1llll11ll1l_opy_).lower() != bstack111lll1_opy_ (u"࠭ࡴࡳࡷࡨࠫᕓ")):
            item._driver.execute_script(
                bstack111lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠤࠬᕔ") + json.dumps(
                    report.nodeid) + bstack111lll1_opy_ (u"ࠨࡿࢀࠫᕕ"))
        os.environ[bstack111lll1_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕࡡࡗࡉࡘ࡚࡟ࡏࡃࡐࡉࠬᕖ")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack111lll1_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡ࡯ࡤࡶࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩ࠿ࠦࡻ࠱ࡿࠥᕗ").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack111lll1_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨᕘ")))
    bstack1l1ll1lll1_opy_ = bstack111lll1_opy_ (u"ࠧࠨᕙ")
    bstack1111l11l11_opy_(report)
    if not passed:
        try:
            bstack1l1ll1lll1_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack111lll1_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠࡧࡣ࡬ࡰࡺࡸࡥࠡࡴࡨࡥࡸࡵ࡮࠻ࠢࡾ࠴ࢂࠨᕚ").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack1l1ll1lll1_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack111lll1_opy_ (u"ࠢࡸࡣࡶࡼ࡫ࡧࡩ࡭ࠤᕛ")))
        bstack1l1ll1lll1_opy_ = bstack111lll1_opy_ (u"ࠣࠤᕜ")
        if not passed:
            try:
                bstack1l1ll1lll1_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack111lll1_opy_ (u"ࠤ࡚ࡅࡗࡔࡉࡏࡉ࠽ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡥࡧࡷࡩࡷࡳࡩ࡯ࡧࠣࡪࡦ࡯࡬ࡶࡴࡨࠤࡷ࡫ࡡࡴࡱࡱ࠾ࠥࢁ࠰ࡾࠤᕝ").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack1l1ll1lll1_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack111lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡩ࡯ࡨࡲࠦ࠱ࠦ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡤࡢࡶࡤࠦ࠿ࠦࠧᕞ")
                    + json.dumps(bstack111lll1_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠥࠧᕟ"))
                    + bstack111lll1_opy_ (u"ࠧࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽࠣᕠ")
                )
            else:
                item._driver.execute_script(
                    bstack111lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤࡨࡶࡷࡵࡲࠣ࠮ࠣࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡨࡦࡺࡡࠣ࠼ࠣࠫᕡ")
                    + json.dumps(str(bstack1l1ll1lll1_opy_))
                    + bstack111lll1_opy_ (u"ࠢ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࢀࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿࠥᕢ")
                )
        except Exception as e:
            summary.append(bstack111lll1_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡡ࡯ࡰࡲࡸࡦࡺࡥ࠻ࠢࡾ࠴ࢂࠨᕣ").format(e))
def bstack1llll11l1ll_opy_(test_name, error_message):
    try:
        bstack1llll11ll11_opy_ = []
        bstack11l1l1111_opy_ = os.environ.get(bstack111lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩᕤ"), bstack111lll1_opy_ (u"ࠪ࠴ࠬᕥ"))
        bstack1llll1lll1_opy_ = {bstack111lll1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᕦ"): test_name, bstack111lll1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᕧ"): error_message, bstack111lll1_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᕨ"): bstack11l1l1111_opy_}
        bstack1lllll1111l_opy_ = os.path.join(tempfile.gettempdir(), bstack111lll1_opy_ (u"ࠧࡱࡹࡢࡴࡾࡺࡥࡴࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬᕩ"))
        if os.path.exists(bstack1lllll1111l_opy_):
            with open(bstack1lllll1111l_opy_) as f:
                bstack1llll11ll11_opy_ = json.load(f)
        bstack1llll11ll11_opy_.append(bstack1llll1lll1_opy_)
        with open(bstack1lllll1111l_opy_, bstack111lll1_opy_ (u"ࠨࡹࠪᕪ")) as f:
            json.dump(bstack1llll11ll11_opy_, f)
    except Exception as e:
        logger.debug(bstack111lll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵ࡫ࡲࡴ࡫ࡶࡸ࡮ࡴࡧࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡶࡹࡵࡧࡶࡸࠥ࡫ࡲࡳࡱࡵࡷ࠿ࠦࠧᕫ") + str(e))
def bstack1llll1llll1_opy_(item, report, summary, bstack1llll11ll1l_opy_):
    if report.when in [bstack111lll1_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤᕬ"), bstack111lll1_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨᕭ")]:
        return
    if (str(bstack1llll11ll1l_opy_).lower() != bstack111lll1_opy_ (u"ࠬࡺࡲࡶࡧࠪᕮ")):
        bstack1l1l1l1l_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack111lll1_opy_ (u"ࠨࡷࡢࡵࡻࡪࡦ࡯࡬ࠣᕯ")))
    bstack1l1ll1lll1_opy_ = bstack111lll1_opy_ (u"ࠢࠣᕰ")
    bstack1111l11l11_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack1l1ll1lll1_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack111lll1_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡤࡦࡶࡨࡶࡲ࡯࡮ࡦࠢࡩࡥ࡮ࡲࡵࡳࡧࠣࡶࡪࡧࡳࡰࡰ࠽ࠤࢀ࠶ࡽࠣᕱ").format(e)
                )
        try:
            if passed:
                bstack1lll11l11_opy_(getattr(item, bstack111lll1_opy_ (u"ࠩࡢࡴࡦ࡭ࡥࠨᕲ"), None), bstack111lll1_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥᕳ"))
            else:
                error_message = bstack111lll1_opy_ (u"ࠫࠬᕴ")
                if bstack1l1ll1lll1_opy_:
                    bstack1ll1lll1l_opy_(item._page, str(bstack1l1ll1lll1_opy_), bstack111lll1_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦᕵ"))
                    bstack1lll11l11_opy_(getattr(item, bstack111lll1_opy_ (u"࠭࡟ࡱࡣࡪࡩࠬᕶ"), None), bstack111lll1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢᕷ"), str(bstack1l1ll1lll1_opy_))
                    error_message = str(bstack1l1ll1lll1_opy_)
                else:
                    bstack1lll11l11_opy_(getattr(item, bstack111lll1_opy_ (u"ࠨࡡࡳࡥ࡬࡫ࠧᕸ"), None), bstack111lll1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤᕹ"))
                bstack1llll11l1ll_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack111lll1_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡷࡳࡨࡦࡺࡥࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࡿ࠵ࢃࠢᕺ").format(e))
try:
    from typing import Generator
    import pytest_playwright.pytest_playwright as p
    @pytest.fixture
    def page(context: BrowserContext, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
        page = context.new_page()
        request.node._page = page
        yield page
except:
    pass
def pytest_addoption(parser):
    parser.addoption(bstack111lll1_opy_ (u"ࠦ࠲࠳ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣᕻ"), default=bstack111lll1_opy_ (u"ࠧࡌࡡ࡭ࡵࡨࠦᕼ"), help=bstack111lll1_opy_ (u"ࠨࡁࡶࡶࡲࡱࡦࡺࡩࡤࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠧᕽ"))
    parser.addoption(bstack111lll1_opy_ (u"ࠢ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨᕾ"), default=bstack111lll1_opy_ (u"ࠣࡈࡤࡰࡸ࡫ࠢᕿ"), help=bstack111lll1_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡧࠥࡹࡥࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠣᖀ"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack111lll1_opy_ (u"ࠥ࠱࠲ࡪࡲࡪࡸࡨࡶࠧᖁ"), action=bstack111lll1_opy_ (u"ࠦࡸࡺ࡯ࡳࡧࠥᖂ"), default=bstack111lll1_opy_ (u"ࠧࡩࡨࡳࡱࡰࡩࠧᖃ"),
                         help=bstack111lll1_opy_ (u"ࠨࡄࡳ࡫ࡹࡩࡷࠦࡴࡰࠢࡵࡹࡳࠦࡴࡦࡵࡷࡷࠧᖄ"))
def bstack1l1111l111_opy_(log):
    if not (log[bstack111lll1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᖅ")] and log[bstack111lll1_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᖆ")].strip()):
        return
    active = bstack1l111lllll_opy_()
    log = {
        bstack111lll1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᖇ"): log[bstack111lll1_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩᖈ")],
        bstack111lll1_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧᖉ"): datetime.datetime.utcnow().isoformat() + bstack111lll1_opy_ (u"ࠬࡠࠧᖊ"),
        bstack111lll1_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᖋ"): log[bstack111lll1_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᖌ")],
    }
    if active:
        if active[bstack111lll1_opy_ (u"ࠨࡶࡼࡴࡪ࠭ᖍ")] == bstack111lll1_opy_ (u"ࠩ࡫ࡳࡴࡱࠧᖎ"):
            log[bstack111lll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᖏ")] = active[bstack111lll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᖐ")]
        elif active[bstack111lll1_opy_ (u"ࠬࡺࡹࡱࡧࠪᖑ")] == bstack111lll1_opy_ (u"࠭ࡴࡦࡵࡷࠫᖒ"):
            log[bstack111lll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᖓ")] = active[bstack111lll1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᖔ")]
    bstack1llll11l1_opy_.bstack1l11lll111_opy_([log])
def bstack1l111lllll_opy_():
    if len(store[bstack111lll1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ᖕ")]) > 0 and store[bstack111lll1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧᖖ")][-1]:
        return {
            bstack111lll1_opy_ (u"ࠫࡹࡿࡰࡦࠩᖗ"): bstack111lll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪᖘ"),
            bstack111lll1_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᖙ"): store[bstack111lll1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᖚ")][-1]
        }
    if store.get(bstack111lll1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬᖛ"), None):
        return {
            bstack111lll1_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᖜ"): bstack111lll1_opy_ (u"ࠪࡸࡪࡹࡴࠨᖝ"),
            bstack111lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᖞ"): store[bstack111lll1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩᖟ")]
        }
    return None
bstack1l11l11lll_opy_ = bstack1l11ll1111_opy_(bstack1l1111l111_opy_)
def pytest_runtest_call(item):
    try:
        global CONFIG
        global bstack1lllll11111_opy_
        item._1llll1l1lll_opy_ = True
        bstack11l1ll111_opy_ = bstack1lllll1111_opy_.bstack1l11l1ll1_opy_(CONFIG, bstack11l1l1l111_opy_(item.own_markers))
        item._a11y_test_case = bstack11l1ll111_opy_
        if bstack1lllll11111_opy_:
            driver = getattr(item, bstack111lll1_opy_ (u"࠭࡟ࡥࡴ࡬ࡺࡪࡸࠧᖠ"), None)
            item._a11y_started = bstack1lllll1111_opy_.bstack1l1ll1lll_opy_(driver, bstack11l1ll111_opy_)
        if not bstack1llll11l1_opy_.on() or bstack1llll1l111l_opy_ != bstack111lll1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧᖡ"):
            return
        global current_test_uuid, bstack1l11l11lll_opy_
        bstack1l11l11lll_opy_.start()
        bstack1l11ll11ll_opy_ = {
            bstack111lll1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᖢ"): uuid4().__str__(),
            bstack111lll1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ᖣ"): datetime.datetime.utcnow().isoformat() + bstack111lll1_opy_ (u"ࠪ࡞ࠬᖤ")
        }
        current_test_uuid = bstack1l11ll11ll_opy_[bstack111lll1_opy_ (u"ࠫࡺࡻࡩࡥࠩᖥ")]
        store[bstack111lll1_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩᖦ")] = bstack1l11ll11ll_opy_[bstack111lll1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᖧ")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _1l11lllll1_opy_[item.nodeid] = {**_1l11lllll1_opy_[item.nodeid], **bstack1l11ll11ll_opy_}
        bstack1llll1lll1l_opy_(item, _1l11lllll1_opy_[item.nodeid], bstack111lll1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨᖨ"))
    except Exception as err:
        print(bstack111lll1_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡳࡷࡱࡸࡪࡹࡴࡠࡥࡤࡰࡱࡀࠠࡼࡿࠪᖩ"), str(err))
def pytest_runtest_setup(item):
    global bstack1llll1l11l1_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack11l1l1ll1l_opy_():
        atexit.register(bstack1ll11llll1_opy_)
        if not bstack1llll1l11l1_opy_:
            try:
                bstack1llll11l11l_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack11l11ll111_opy_():
                    bstack1llll11l11l_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack1llll11l11l_opy_:
                    signal.signal(s, bstack1llll1lll11_opy_)
                bstack1llll1l11l1_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack111lll1_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡷ࡫ࡧࡪࡵࡷࡩࡷࠦࡳࡪࡩࡱࡥࡱࠦࡨࡢࡰࡧࡰࡪࡸࡳ࠻ࠢࠥᖪ") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack1111l11ll1_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack111lll1_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᖫ")
    try:
        if not bstack1llll11l1_opy_.on():
            return
        bstack1l11l11lll_opy_.start()
        uuid = uuid4().__str__()
        bstack1l11ll11ll_opy_ = {
            bstack111lll1_opy_ (u"ࠫࡺࡻࡩࡥࠩᖬ"): uuid,
            bstack111lll1_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᖭ"): datetime.datetime.utcnow().isoformat() + bstack111lll1_opy_ (u"࡚࠭ࠨᖮ"),
            bstack111lll1_opy_ (u"ࠧࡵࡻࡳࡩࠬᖯ"): bstack111lll1_opy_ (u"ࠨࡪࡲࡳࡰ࠭ᖰ"),
            bstack111lll1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡵࡻࡳࡩࠬᖱ"): bstack111lll1_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠨᖲ"),
            bstack111lll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡱࡥࡲ࡫ࠧᖳ"): bstack111lll1_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫᖴ")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack111lll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪᖵ")] = item
        store[bstack111lll1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᖶ")] = [uuid]
        if not _1l11lllll1_opy_.get(item.nodeid, None):
            _1l11lllll1_opy_[item.nodeid] = {bstack111lll1_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧᖷ"): [], bstack111lll1_opy_ (u"ࠩࡩ࡭ࡽࡺࡵࡳࡧࡶࠫᖸ"): []}
        _1l11lllll1_opy_[item.nodeid][bstack111lll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᖹ")].append(bstack1l11ll11ll_opy_[bstack111lll1_opy_ (u"ࠫࡺࡻࡩࡥࠩᖺ")])
        _1l11lllll1_opy_[item.nodeid + bstack111lll1_opy_ (u"ࠬ࠳ࡳࡦࡶࡸࡴࠬᖻ")] = bstack1l11ll11ll_opy_
        bstack1lllll111ll_opy_(item, bstack1l11ll11ll_opy_, bstack111lll1_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧᖼ"))
    except Exception as err:
        print(bstack111lll1_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡲࡶࡰࡷࡩࡸࡺ࡟ࡴࡧࡷࡹࡵࡀࠠࡼࡿࠪᖽ"), str(err))
def pytest_runtest_teardown(item):
    try:
        global bstack11l1l1l1_opy_
        if CONFIG.get(bstack111lll1_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧᖾ"), False):
            if CONFIG.get(bstack111lll1_opy_ (u"ࠩࡳࡩࡷࡩࡹࡄࡣࡳࡸࡺࡸࡥࡎࡱࡧࡩࠬᖿ"), bstack111lll1_opy_ (u"ࠥࡥࡺࡺ࡯ࠣᗀ")) == bstack111lll1_opy_ (u"ࠦࡹ࡫ࡳࡵࡥࡤࡷࡪࠨᗁ"):
                bstack1lllll11l1l_opy_ = bstack1ll1111111_opy_(threading.current_thread(), bstack111lll1_opy_ (u"ࠬࡶࡥࡳࡥࡼࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨᗂ"), None)
                bstack1l1111lll_opy_ = bstack1lllll11l1l_opy_ + bstack111lll1_opy_ (u"ࠨ࠭ࡵࡧࡶࡸࡨࡧࡳࡦࠤᗃ")
                driver = getattr(item, bstack111lll1_opy_ (u"ࠧࡠࡦࡵ࡭ࡻ࡫ࡲࠨᗄ"), None)
                PercySDK.screenshot(driver, bstack1l1111lll_opy_)
        if getattr(item, bstack111lll1_opy_ (u"ࠨࡡࡤ࠵࠶ࡿ࡟ࡴࡶࡤࡶࡹ࡫ࡤࠨᗅ"), False):
            bstack11ll1l1l1_opy_.bstack1lllll1l11_opy_(getattr(item, bstack111lll1_opy_ (u"ࠩࡢࡨࡷ࡯ࡶࡦࡴࠪᗆ"), None), bstack11l1l1l1_opy_, logger, item)
        if not bstack1llll11l1_opy_.on():
            return
        bstack1l11ll11ll_opy_ = {
            bstack111lll1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᗇ"): uuid4().__str__(),
            bstack111lll1_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᗈ"): datetime.datetime.utcnow().isoformat() + bstack111lll1_opy_ (u"ࠬࡠࠧᗉ"),
            bstack111lll1_opy_ (u"࠭ࡴࡺࡲࡨࠫᗊ"): bstack111lll1_opy_ (u"ࠧࡩࡱࡲ࡯ࠬᗋ"),
            bstack111lll1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫᗌ"): bstack111lll1_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍ࠭ᗍ"),
            bstack111lll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡰࡤࡱࡪ࠭ᗎ"): bstack111lll1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭ᗏ")
        }
        _1l11lllll1_opy_[item.nodeid + bstack111lll1_opy_ (u"ࠬ࠳ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨᗐ")] = bstack1l11ll11ll_opy_
        bstack1lllll111ll_opy_(item, bstack1l11ll11ll_opy_, bstack111lll1_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧᗑ"))
    except Exception as err:
        print(bstack111lll1_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡲࡶࡰࡷࡩࡸࡺ࡟ࡵࡧࡤࡶࡩࡵࡷ࡯࠼ࠣࡿࢂ࠭ᗒ"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if not bstack1llll11l1_opy_.on():
        yield
        return
    start_time = datetime.datetime.now()
    if bstack1111l11l1l_opy_(fixturedef.argname):
        store[bstack111lll1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡰࡳࡩࡻ࡬ࡦࡡ࡬ࡸࡪࡳࠧᗓ")] = request.node
    elif bstack1111l1llll_opy_(fixturedef.argname):
        store[bstack111lll1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡧࡱࡧࡳࡴࡡ࡬ࡸࡪࡳࠧᗔ")] = request.node
    outcome = yield
    try:
        fixture = {
            bstack111lll1_opy_ (u"ࠪࡲࡦࡳࡥࠨᗕ"): fixturedef.argname,
            bstack111lll1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᗖ"): bstack11l1ll1l1l_opy_(outcome),
            bstack111lll1_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧᗗ"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack111lll1_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪᗘ")]
        if not _1l11lllll1_opy_.get(current_test_item.nodeid, None):
            _1l11lllll1_opy_[current_test_item.nodeid] = {bstack111lll1_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩᗙ"): []}
        _1l11lllll1_opy_[current_test_item.nodeid][bstack111lll1_opy_ (u"ࠨࡨ࡬ࡼࡹࡻࡲࡦࡵࠪᗚ")].append(fixture)
    except Exception as err:
        logger.debug(bstack111lll1_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡨ࡬ࡼࡹࡻࡲࡦࡡࡶࡩࡹࡻࡰ࠻ࠢࡾࢁࠬᗛ"), str(err))
if bstack1l1111ll1_opy_() and bstack1llll11l1_opy_.on():
    def pytest_bdd_before_step(request, step):
        try:
            _1l11lllll1_opy_[request.node.nodeid][bstack111lll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭ᗜ")].bstack111111l1l1_opy_(id(step))
        except Exception as err:
            print(bstack111lll1_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴ࠿ࠦࡻࡾࠩᗝ"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        try:
            _1l11lllll1_opy_[request.node.nodeid][bstack111lll1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨᗞ")].bstack1l1111llll_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack111lll1_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡶࡸࡪࡶ࡟ࡦࡴࡵࡳࡷࡀࠠࡼࡿࠪᗟ"), str(err))
    def pytest_bdd_after_step(request, step):
        try:
            bstack1l1111l11l_opy_: bstack1l11lll1ll_opy_ = _1l11lllll1_opy_[request.node.nodeid][bstack111lll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪᗠ")]
            bstack1l1111l11l_opy_.bstack1l1111llll_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack111lll1_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡸࡺࡥࡱࡡࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠬᗡ"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack1llll1l111l_opy_
        try:
            if not bstack1llll11l1_opy_.on() or bstack1llll1l111l_opy_ != bstack111lll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩ࠭ᗢ"):
                return
            global bstack1l11l11lll_opy_
            bstack1l11l11lll_opy_.start()
            if not _1l11lllll1_opy_.get(request.node.nodeid, None):
                _1l11lllll1_opy_[request.node.nodeid] = {}
            bstack1l1111l11l_opy_ = bstack1l11lll1ll_opy_.bstack11111111l1_opy_(
                scenario, feature, request.node,
                name=bstack1111l1l1l1_opy_(request.node, scenario),
                bstack1l111l1l1l_opy_=bstack1ll1l11lll_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack111lll1_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶ࠰ࡧࡺࡩࡵ࡮ࡤࡨࡶࠬᗣ"),
                tags=bstack1111l11lll_opy_(feature, scenario)
            )
            _1l11lllll1_opy_[request.node.nodeid][bstack111lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧᗤ")] = bstack1l1111l11l_opy_
            bstack1lllll111l1_opy_(bstack1l1111l11l_opy_.uuid)
            bstack1llll11l1_opy_.bstack1l111l11ll_opy_(bstack111lll1_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ᗥ"), bstack1l1111l11l_opy_)
        except Exception as err:
            print(bstack111lll1_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲ࠾ࠥࢁࡽࠨᗦ"), str(err))
def bstack1llll1ll1ll_opy_(bstack1lllll11lll_opy_):
    if bstack1lllll11lll_opy_ in store[bstack111lll1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫᗧ")]:
        store[bstack111lll1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬᗨ")].remove(bstack1lllll11lll_opy_)
def bstack1lllll111l1_opy_(bstack1llll111lll_opy_):
    store[bstack111lll1_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠࡷࡸ࡭ࡩ࠭ᗩ")] = bstack1llll111lll_opy_
    threading.current_thread().current_test_uuid = bstack1llll111lll_opy_
@bstack1llll11l1_opy_.bstack1llllll1lll_opy_
def bstack1llll11l111_opy_(item, call, report):
    global bstack1llll1l111l_opy_
    bstack1ll1l1lll_opy_ = bstack1ll1l11lll_opy_()
    if hasattr(report, bstack111lll1_opy_ (u"ࠪࡷࡹࡵࡰࠨᗪ")):
        bstack1ll1l1lll_opy_ = bstack11ll1111l1_opy_(report.stop)
    if hasattr(report, bstack111lll1_opy_ (u"ࠫࡸࡺࡡࡳࡶࠪᗫ")):
        bstack1ll1l1lll_opy_ = bstack11ll1111l1_opy_(report.start)
    try:
        if getattr(report, bstack111lll1_opy_ (u"ࠬࡽࡨࡦࡰࠪᗬ"), bstack111lll1_opy_ (u"࠭ࠧᗭ")) == bstack111lll1_opy_ (u"ࠧࡤࡣ࡯ࡰࠬᗮ"):
            bstack1l11l11lll_opy_.reset()
        if getattr(report, bstack111lll1_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭ᗯ"), bstack111lll1_opy_ (u"ࠩࠪᗰ")) == bstack111lll1_opy_ (u"ࠪࡧࡦࡲ࡬ࠨᗱ"):
            if bstack1llll1l111l_opy_ == bstack111lll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᗲ"):
                _1l11lllll1_opy_[item.nodeid][bstack111lll1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᗳ")] = bstack1ll1l1lll_opy_
                bstack1llll1lll1l_opy_(item, _1l11lllll1_opy_[item.nodeid], bstack111lll1_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨᗴ"), report, call)
                store[bstack111lll1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᗵ")] = None
            elif bstack1llll1l111l_opy_ == bstack111lll1_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠧᗶ"):
                bstack1l1111l11l_opy_ = _1l11lllll1_opy_[item.nodeid][bstack111lll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᗷ")]
                bstack1l1111l11l_opy_.set(hooks=_1l11lllll1_opy_[item.nodeid].get(bstack111lll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᗸ"), []))
                exception, bstack1l11ll1l1l_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack1l11ll1l1l_opy_ = [call.excinfo.exconly(), getattr(report, bstack111lll1_opy_ (u"ࠫࡱࡵ࡮ࡨࡴࡨࡴࡷࡺࡥࡹࡶࠪᗹ"), bstack111lll1_opy_ (u"ࠬ࠭ᗺ"))]
                bstack1l1111l11l_opy_.stop(time=bstack1ll1l1lll_opy_, result=Result(result=getattr(report, bstack111lll1_opy_ (u"࠭࡯ࡶࡶࡦࡳࡲ࡫ࠧᗻ"), bstack111lll1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᗼ")), exception=exception, bstack1l11ll1l1l_opy_=bstack1l11ll1l1l_opy_))
                bstack1llll11l1_opy_.bstack1l111l11ll_opy_(bstack111lll1_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪᗽ"), _1l11lllll1_opy_[item.nodeid][bstack111lll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᗾ")])
        elif getattr(report, bstack111lll1_opy_ (u"ࠪࡻ࡭࡫࡮ࠨᗿ"), bstack111lll1_opy_ (u"ࠫࠬᘀ")) in [bstack111lll1_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫᘁ"), bstack111lll1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨᘂ")]:
            bstack1l11l11l1l_opy_ = item.nodeid + bstack111lll1_opy_ (u"ࠧ࠮ࠩᘃ") + getattr(report, bstack111lll1_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭ᘄ"), bstack111lll1_opy_ (u"ࠩࠪᘅ"))
            if getattr(report, bstack111lll1_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᘆ"), False):
                hook_type = bstack111lll1_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠩᘇ") if getattr(report, bstack111lll1_opy_ (u"ࠬࡽࡨࡦࡰࠪᘈ"), bstack111lll1_opy_ (u"࠭ࠧᘉ")) == bstack111lll1_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ᘊ") else bstack111lll1_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᘋ")
                _1l11lllll1_opy_[bstack1l11l11l1l_opy_] = {
                    bstack111lll1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᘌ"): uuid4().__str__(),
                    bstack111lll1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᘍ"): bstack1ll1l1lll_opy_,
                    bstack111lll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧᘎ"): hook_type
                }
            _1l11lllll1_opy_[bstack1l11l11l1l_opy_][bstack111lll1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᘏ")] = bstack1ll1l1lll_opy_
            bstack1llll1ll1ll_opy_(_1l11lllll1_opy_[bstack1l11l11l1l_opy_][bstack111lll1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᘐ")])
            bstack1lllll111ll_opy_(item, _1l11lllll1_opy_[bstack1l11l11l1l_opy_], bstack111lll1_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩᘑ"), report, call)
            if getattr(report, bstack111lll1_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭ᘒ"), bstack111lll1_opy_ (u"ࠩࠪᘓ")) == bstack111lll1_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩᘔ"):
                if getattr(report, bstack111lll1_opy_ (u"ࠫࡴࡻࡴࡤࡱࡰࡩࠬᘕ"), bstack111lll1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᘖ")) == bstack111lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᘗ"):
                    bstack1l11ll11ll_opy_ = {
                        bstack111lll1_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᘘ"): uuid4().__str__(),
                        bstack111lll1_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᘙ"): bstack1ll1l11lll_opy_(),
                        bstack111lll1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᘚ"): bstack1ll1l11lll_opy_()
                    }
                    _1l11lllll1_opy_[item.nodeid] = {**_1l11lllll1_opy_[item.nodeid], **bstack1l11ll11ll_opy_}
                    bstack1llll1lll1l_opy_(item, _1l11lllll1_opy_[item.nodeid], bstack111lll1_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᘛ"))
                    bstack1llll1lll1l_opy_(item, _1l11lllll1_opy_[item.nodeid], bstack111lll1_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ᘜ"), report, call)
    except Exception as err:
        print(bstack111lll1_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡭ࡧ࡮ࡥ࡮ࡨࡣࡴ࠷࠱ࡺࡡࡷࡩࡸࡺ࡟ࡦࡸࡨࡲࡹࡀࠠࡼࡿࠪᘝ"), str(err))
def bstack1llll1l11ll_opy_(test, bstack1l11ll11ll_opy_, result=None, call=None, bstack1ll11ll11_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack1l1111l11l_opy_ = {
        bstack111lll1_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᘞ"): bstack1l11ll11ll_opy_[bstack111lll1_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᘟ")],
        bstack111lll1_opy_ (u"ࠨࡶࡼࡴࡪ࠭ᘠ"): bstack111lll1_opy_ (u"ࠩࡷࡩࡸࡺࠧᘡ"),
        bstack111lll1_opy_ (u"ࠪࡲࡦࡳࡥࠨᘢ"): test.name,
        bstack111lll1_opy_ (u"ࠫࡧࡵࡤࡺࠩᘣ"): {
            bstack111lll1_opy_ (u"ࠬࡲࡡ࡯ࡩࠪᘤ"): bstack111lll1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ᘥ"),
            bstack111lll1_opy_ (u"ࠧࡤࡱࡧࡩࠬᘦ"): inspect.getsource(test.obj)
        },
        bstack111lll1_opy_ (u"ࠨ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬᘧ"): test.name,
        bstack111lll1_opy_ (u"ࠩࡶࡧࡴࡶࡥࠨᘨ"): test.name,
        bstack111lll1_opy_ (u"ࠪࡷࡨࡵࡰࡦࡵࠪᘩ"): bstack1llll11l1_opy_.bstack1l11ll1l11_opy_(test),
        bstack111lll1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧᘪ"): file_path,
        bstack111lll1_opy_ (u"ࠬࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠧᘫ"): file_path,
        bstack111lll1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᘬ"): bstack111lll1_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨᘭ"),
        bstack111lll1_opy_ (u"ࠨࡸࡦࡣ࡫࡯࡬ࡦࡲࡤࡸ࡭࠭ᘮ"): file_path,
        bstack111lll1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ᘯ"): bstack1l11ll11ll_opy_[bstack111lll1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᘰ")],
        bstack111lll1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧᘱ"): bstack111lll1_opy_ (u"ࠬࡖࡹࡵࡧࡶࡸࠬᘲ"),
        bstack111lll1_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡘࡥࡳࡷࡱࡔࡦࡸࡡ࡮ࠩᘳ"): {
            bstack111lll1_opy_ (u"ࠧࡳࡧࡵࡹࡳࡥ࡮ࡢ࡯ࡨࠫᘴ"): test.nodeid
        },
        bstack111lll1_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭ᘵ"): bstack11l1l1l111_opy_(test.own_markers)
    }
    if bstack1ll11ll11_opy_ in [bstack111lll1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖ࡯࡮ࡶࡰࡦࡦࠪᘶ"), bstack111lll1_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬᘷ")]:
        bstack1l1111l11l_opy_[bstack111lll1_opy_ (u"ࠫࡲ࡫ࡴࡢࠩᘸ")] = {
            bstack111lll1_opy_ (u"ࠬ࡬ࡩࡹࡶࡸࡶࡪࡹࠧᘹ"): bstack1l11ll11ll_opy_.get(bstack111lll1_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨᘺ"), [])
        }
    if bstack1ll11ll11_opy_ == bstack111lll1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔ࡭࡬ࡴࡵ࡫ࡤࠨᘻ"):
        bstack1l1111l11l_opy_[bstack111lll1_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᘼ")] = bstack111lll1_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪᘽ")
        bstack1l1111l11l_opy_[bstack111lll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᘾ")] = bstack1l11ll11ll_opy_[bstack111lll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪᘿ")]
        bstack1l1111l11l_opy_[bstack111lll1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᙀ")] = bstack1l11ll11ll_opy_[bstack111lll1_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᙁ")]
    if result:
        bstack1l1111l11l_opy_[bstack111lll1_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᙂ")] = result.outcome
        bstack1l1111l11l_opy_[bstack111lll1_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩᙃ")] = result.duration * 1000
        bstack1l1111l11l_opy_[bstack111lll1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᙄ")] = bstack1l11ll11ll_opy_[bstack111lll1_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᙅ")]
        if result.failed:
            bstack1l1111l11l_opy_[bstack111lll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪᙆ")] = bstack1llll11l1_opy_.bstack11lll1l1ll_opy_(call.excinfo.typename)
            bstack1l1111l11l_opy_[bstack111lll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ᙇ")] = bstack1llll11l1_opy_.bstack1lllllll111_opy_(call.excinfo, result)
        bstack1l1111l11l_opy_[bstack111lll1_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᙈ")] = bstack1l11ll11ll_opy_[bstack111lll1_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ᙉ")]
    if outcome:
        bstack1l1111l11l_opy_[bstack111lll1_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᙊ")] = bstack11l1ll1l1l_opy_(outcome)
        bstack1l1111l11l_opy_[bstack111lll1_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪᙋ")] = 0
        bstack1l1111l11l_opy_[bstack111lll1_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᙌ")] = bstack1l11ll11ll_opy_[bstack111lll1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᙍ")]
        if bstack1l1111l11l_opy_[bstack111lll1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᙎ")] == bstack111lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᙏ"):
            bstack1l1111l11l_opy_[bstack111lll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪ࠭ᙐ")] = bstack111lll1_opy_ (u"ࠨࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠩᙑ")  # bstack1lllll11l11_opy_
            bstack1l1111l11l_opy_[bstack111lll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪᙒ")] = [{bstack111lll1_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭ᙓ"): [bstack111lll1_opy_ (u"ࠫࡸࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠨᙔ")]}]
        bstack1l1111l11l_opy_[bstack111lll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᙕ")] = bstack1l11ll11ll_opy_[bstack111lll1_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᙖ")]
    return bstack1l1111l11l_opy_
def bstack1llll1l1111_opy_(test, bstack1l11l1ll11_opy_, bstack1ll11ll11_opy_, result, call, outcome, bstack1lllll11ll1_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack1l11l1ll11_opy_[bstack111lll1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪᙗ")]
    hook_name = bstack1l11l1ll11_opy_[bstack111lll1_opy_ (u"ࠨࡪࡲࡳࡰࡥ࡮ࡢ࡯ࡨࠫᙘ")]
    hook_data = {
        bstack111lll1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᙙ"): bstack1l11l1ll11_opy_[bstack111lll1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᙚ")],
        bstack111lll1_opy_ (u"ࠫࡹࡿࡰࡦࠩᙛ"): bstack111lll1_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪᙜ"),
        bstack111lll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᙝ"): bstack111lll1_opy_ (u"ࠧࡼࡿࠪᙞ").format(bstack1111l111ll_opy_(hook_name)),
        bstack111lll1_opy_ (u"ࠨࡤࡲࡨࡾ࠭ᙟ"): {
            bstack111lll1_opy_ (u"ࠩ࡯ࡥࡳ࡭ࠧᙠ"): bstack111lll1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪᙡ"),
            bstack111lll1_opy_ (u"ࠫࡨࡵࡤࡦࠩᙢ"): None
        },
        bstack111lll1_opy_ (u"ࠬࡹࡣࡰࡲࡨࠫᙣ"): test.name,
        bstack111lll1_opy_ (u"࠭ࡳࡤࡱࡳࡩࡸ࠭ᙤ"): bstack1llll11l1_opy_.bstack1l11ll1l11_opy_(test, hook_name),
        bstack111lll1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪᙥ"): file_path,
        bstack111lll1_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࠪᙦ"): file_path,
        bstack111lll1_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᙧ"): bstack111lll1_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫᙨ"),
        bstack111lll1_opy_ (u"ࠫࡻࡩ࡟ࡧ࡫࡯ࡩࡵࡧࡴࡩࠩᙩ"): file_path,
        bstack111lll1_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᙪ"): bstack1l11l1ll11_opy_[bstack111lll1_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᙫ")],
        bstack111lll1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪᙬ"): bstack111lll1_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴ࠮ࡥࡸࡧࡺࡳࡢࡦࡴࠪ᙭") if bstack1llll1l111l_opy_ == bstack111lll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩ࠭᙮") else bstack111lll1_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶࠪᙯ"),
        bstack111lll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧᙰ"): hook_type
    }
    bstack1llll1ll111_opy_ = bstack1l111l1ll1_opy_(_1l11lllll1_opy_.get(test.nodeid, None))
    if bstack1llll1ll111_opy_:
        hook_data[bstack111lll1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡪࡦࠪᙱ")] = bstack1llll1ll111_opy_
    if result:
        hook_data[bstack111lll1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᙲ")] = result.outcome
        hook_data[bstack111lll1_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨᙳ")] = result.duration * 1000
        hook_data[bstack111lll1_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᙴ")] = bstack1l11l1ll11_opy_[bstack111lll1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᙵ")]
        if result.failed:
            hook_data[bstack111lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩᙶ")] = bstack1llll11l1_opy_.bstack11lll1l1ll_opy_(call.excinfo.typename)
            hook_data[bstack111lll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬᙷ")] = bstack1llll11l1_opy_.bstack1lllllll111_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack111lll1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᙸ")] = bstack11l1ll1l1l_opy_(outcome)
        hook_data[bstack111lll1_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧᙹ")] = 100
        hook_data[bstack111lll1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᙺ")] = bstack1l11l1ll11_opy_[bstack111lll1_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᙻ")]
        if hook_data[bstack111lll1_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᙼ")] == bstack111lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᙽ"):
            hook_data[bstack111lll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪᙾ")] = bstack111lll1_opy_ (u"࡛ࠬ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷ࠭ᙿ")  # bstack1lllll11l11_opy_
            hook_data[bstack111lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧ ")] = [{bstack111lll1_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪᚁ"): [bstack111lll1_opy_ (u"ࠨࡵࡲࡱࡪࠦࡥࡳࡴࡲࡶࠬᚂ")]}]
    if bstack1lllll11ll1_opy_:
        hook_data[bstack111lll1_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩᚃ")] = bstack1lllll11ll1_opy_.result
        hook_data[bstack111lll1_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡠ࡯ࡶࠫᚄ")] = bstack11l1lllll1_opy_(bstack1l11l1ll11_opy_[bstack111lll1_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᚅ")], bstack1l11l1ll11_opy_[bstack111lll1_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᚆ")])
        hook_data[bstack111lll1_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᚇ")] = bstack1l11l1ll11_opy_[bstack111lll1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᚈ")]
        if hook_data[bstack111lll1_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨᚉ")] == bstack111lll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᚊ"):
            hook_data[bstack111lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩᚋ")] = bstack1llll11l1_opy_.bstack11lll1l1ll_opy_(bstack1lllll11ll1_opy_.exception_type)
            hook_data[bstack111lll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬᚌ")] = [{bstack111lll1_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᚍ"): bstack11l1llll1l_opy_(bstack1lllll11ll1_opy_.exception)}]
    return hook_data
def bstack1llll1lll1l_opy_(test, bstack1l11ll11ll_opy_, bstack1ll11ll11_opy_, result=None, call=None, outcome=None):
    bstack1l1111l11l_opy_ = bstack1llll1l11ll_opy_(test, bstack1l11ll11ll_opy_, result, call, bstack1ll11ll11_opy_, outcome)
    driver = getattr(test, bstack111lll1_opy_ (u"࠭࡟ࡥࡴ࡬ࡺࡪࡸࠧᚎ"), None)
    if bstack1ll11ll11_opy_ == bstack111lll1_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨᚏ") and driver:
        bstack1l1111l11l_opy_[bstack111lll1_opy_ (u"ࠨ࡫ࡱࡸࡪ࡭ࡲࡢࡶ࡬ࡳࡳࡹࠧᚐ")] = bstack1llll11l1_opy_.bstack1l11ll1lll_opy_(driver)
    if bstack1ll11ll11_opy_ == bstack111lll1_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖ࡯࡮ࡶࡰࡦࡦࠪᚑ"):
        bstack1ll11ll11_opy_ = bstack111lll1_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬᚒ")
    bstack1l11l11ll1_opy_ = {
        bstack111lll1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨᚓ"): bstack1ll11ll11_opy_,
        bstack111lll1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧᚔ"): bstack1l1111l11l_opy_
    }
    bstack1llll11l1_opy_.bstack1l11l1l11l_opy_(bstack1l11l11ll1_opy_)
def bstack1lllll111ll_opy_(test, bstack1l11ll11ll_opy_, bstack1ll11ll11_opy_, result=None, call=None, outcome=None, bstack1lllll11ll1_opy_=None):
    hook_data = bstack1llll1l1111_opy_(test, bstack1l11ll11ll_opy_, bstack1ll11ll11_opy_, result, call, outcome, bstack1lllll11ll1_opy_)
    bstack1l11l11ll1_opy_ = {
        bstack111lll1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪᚕ"): bstack1ll11ll11_opy_,
        bstack111lll1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࠩᚖ"): hook_data
    }
    bstack1llll11l1_opy_.bstack1l11l1l11l_opy_(bstack1l11l11ll1_opy_)
def bstack1l111l1ll1_opy_(bstack1l11ll11ll_opy_):
    if not bstack1l11ll11ll_opy_:
        return None
    if bstack1l11ll11ll_opy_.get(bstack111lll1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫᚗ"), None):
        return getattr(bstack1l11ll11ll_opy_[bstack111lll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬᚘ")], bstack111lll1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᚙ"), None)
    return bstack1l11ll11ll_opy_.get(bstack111lll1_opy_ (u"ࠫࡺࡻࡩࡥࠩᚚ"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    yield
    try:
        if not bstack1llll11l1_opy_.on():
            return
        places = [bstack111lll1_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ᚛"), bstack111lll1_opy_ (u"࠭ࡣࡢ࡮࡯ࠫ᚜"), bstack111lll1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩ᚝")]
        bstack1l111l1l11_opy_ = []
        for bstack1llll11l1l1_opy_ in places:
            records = caplog.get_records(bstack1llll11l1l1_opy_)
            bstack1llll1ll11l_opy_ = bstack111lll1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ᚞") if bstack1llll11l1l1_opy_ == bstack111lll1_opy_ (u"ࠩࡦࡥࡱࡲࠧ᚟") else bstack111lll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᚠ")
            bstack1llll111l1l_opy_ = request.node.nodeid + (bstack111lll1_opy_ (u"ࠫࠬᚡ") if bstack1llll11l1l1_opy_ == bstack111lll1_opy_ (u"ࠬࡩࡡ࡭࡮ࠪᚢ") else bstack111lll1_opy_ (u"࠭࠭ࠨᚣ") + bstack1llll11l1l1_opy_)
            bstack1llll111lll_opy_ = bstack1l111l1ll1_opy_(_1l11lllll1_opy_.get(bstack1llll111l1l_opy_, None))
            if not bstack1llll111lll_opy_:
                continue
            for record in records:
                if bstack11l1ll1l11_opy_(record.message):
                    continue
                bstack1l111l1l11_opy_.append({
                    bstack111lll1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪᚤ"): datetime.datetime.utcfromtimestamp(record.created).isoformat() + bstack111lll1_opy_ (u"ࠨ࡜ࠪᚥ"),
                    bstack111lll1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᚦ"): record.levelname,
                    bstack111lll1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᚧ"): record.message,
                    bstack1llll1ll11l_opy_: bstack1llll111lll_opy_
                })
        if len(bstack1l111l1l11_opy_) > 0:
            bstack1llll11l1_opy_.bstack1l11lll111_opy_(bstack1l111l1l11_opy_)
    except Exception as err:
        print(bstack111lll1_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡪࡩ࡯࡯ࡦࡢࡪ࡮ࡾࡴࡶࡴࡨ࠾ࠥࢁࡽࠨᚨ"), str(err))
def bstack1ll1lll1l1_opy_(sequence, driver_command, response=None):
    if sequence == bstack111lll1_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫᚩ"):
        if driver_command == bstack111lll1_opy_ (u"࠭ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠪᚪ"):
            bstack1llll11l1_opy_.bstack1l1l11l111_opy_({
                bstack111lll1_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪ࠭ᚫ"): response[bstack111lll1_opy_ (u"ࠨࡸࡤࡰࡺ࡫ࠧᚬ")],
                bstack111lll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᚭ"): store[bstack111lll1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧᚮ")]
            })
def bstack1ll11llll1_opy_():
    global bstack1lllllllll_opy_
    bstack1llll11l1_opy_.bstack1l11ll111l_opy_()
    for driver in bstack1lllllllll_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1llll1lll11_opy_(*args):
    global bstack1lllllllll_opy_
    bstack1llll11l1_opy_.bstack1l11ll111l_opy_()
    for driver in bstack1lllllllll_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack11lllllll_opy_(self, *args, **kwargs):
    bstack1lll1lll1_opy_ = bstack11ll1lll_opy_(self, *args, **kwargs)
    bstack1llll11l1_opy_.bstack1ll11l1ll_opy_(self)
    return bstack1lll1lll1_opy_
def bstack111111lll_opy_(framework_name):
    global bstack1llll11l11_opy_
    global bstack11lllll1l_opy_
    bstack1llll11l11_opy_ = framework_name
    logger.info(bstack1llllllll1_opy_.format(bstack1llll11l11_opy_.split(bstack111lll1_opy_ (u"ࠫ࠲࠭ᚯ"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack11l1l11l1l_opy_():
            Service.start = bstack1l1ll11lll_opy_
            Service.stop = bstack1l1l111l_opy_
            webdriver.Remote.__init__ = bstack1lll11l1l_opy_
            webdriver.Remote.get = bstack11111l1ll_opy_
            if not isinstance(os.getenv(bstack111lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡇࡒࡂࡎࡏࡉࡑ࠭ᚰ")), str):
                return
            WebDriver.close = bstack11llllll1_opy_
            WebDriver.quit = bstack1111ll111_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.bstack1ll11lll11_opy_ = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.bstack1l1l1l1ll1_opy_ = getAccessibilityResultsSummary
        if not bstack11l1l11l1l_opy_() and bstack1llll11l1_opy_.on():
            webdriver.Remote.__init__ = bstack11lllllll_opy_
        bstack11lllll1l_opy_ = True
    except Exception as e:
        pass
    bstack11l111ll1_opy_()
    if os.environ.get(bstack111lll1_opy_ (u"࠭ࡓࡆࡎࡈࡒࡎ࡛ࡍࡠࡑࡕࡣࡕࡒࡁ࡚࡙ࡕࡍࡌࡎࡔࡠࡋࡑࡗ࡙ࡇࡌࡍࡇࡇࠫᚱ")):
        bstack11lllll1l_opy_ = eval(os.environ.get(bstack111lll1_opy_ (u"ࠧࡔࡇࡏࡉࡓࡏࡕࡎࡡࡒࡖࡤࡖࡌࡂ࡛࡚ࡖࡎࡍࡈࡕࡡࡌࡒࡘ࡚ࡁࡍࡎࡈࡈࠬᚲ")))
    if not bstack11lllll1l_opy_:
        bstack1l11ll11l_opy_(bstack111lll1_opy_ (u"ࠣࡒࡤࡧࡰࡧࡧࡦࡵࠣࡲࡴࡺࠠࡪࡰࡶࡸࡦࡲ࡬ࡦࡦࠥᚳ"), bstack1111111l1_opy_)
    if bstack1l111ll1l_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            RemoteConnection._get_proxy_url = bstack1l1111l1_opy_
        except Exception as e:
            logger.error(bstack11l1l1ll_opy_.format(str(e)))
    if bstack111lll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩᚴ") in str(framework_name).lower():
        if not bstack11l1l11l1l_opy_():
            return
        try:
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
def bstack1111ll111_opy_(self):
    global bstack1llll11l11_opy_
    global bstack1ll1111l11_opy_
    global bstack1llll1l111_opy_
    try:
        if bstack111lll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪᚵ") in bstack1llll11l11_opy_ and self.session_id != None and bstack1ll1111111_opy_(threading.current_thread(), bstack111lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡕࡷࡥࡹࡻࡳࠨᚶ"), bstack111lll1_opy_ (u"ࠬ࠭ᚷ")) != bstack111lll1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᚸ"):
            bstack111lllll_opy_ = bstack111lll1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᚹ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack111lll1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᚺ")
            bstack1l1llllll_opy_(logger, True)
            if self != None:
                bstack1l11ll11_opy_(self, bstack111lllll_opy_, bstack111lll1_opy_ (u"ࠩ࠯ࠤࠬᚻ").join(threading.current_thread().bstackTestErrorMessages))
        item = store.get(bstack111lll1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧᚼ"), None)
        if item is not None and bstack1lllll11111_opy_:
            bstack11ll1l1l1_opy_.bstack1lllll1l11_opy_(self, bstack11l1l1l1_opy_, logger, item)
        threading.current_thread().testStatus = bstack111lll1_opy_ (u"ࠫࠬᚽ")
    except Exception as e:
        logger.debug(bstack111lll1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࠨᚾ") + str(e))
    bstack1llll1l111_opy_(self)
    self.session_id = None
def bstack1lll11l1l_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack1ll1111l11_opy_
    global bstack1l1lll1l11_opy_
    global bstack11l1l11ll_opy_
    global bstack1llll11l11_opy_
    global bstack11ll1lll_opy_
    global bstack1lllllllll_opy_
    global bstack1llll11lll_opy_
    global bstack1111l1l1l_opy_
    global bstack1lllll11111_opy_
    global bstack11l1l1l1_opy_
    CONFIG[bstack111lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨᚿ")] = str(bstack1llll11l11_opy_) + str(__version__)
    command_executor = bstack11111lll1_opy_(bstack1llll11lll_opy_)
    logger.debug(bstack1ll1ll1ll1_opy_.format(command_executor))
    proxy = bstack1lll111ll_opy_(CONFIG, proxy)
    bstack11l1l1111_opy_ = 0
    try:
        if bstack11l1l11ll_opy_ is True:
            bstack11l1l1111_opy_ = int(os.environ.get(bstack111lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧᛀ")))
    except:
        bstack11l1l1111_opy_ = 0
    bstack1lll1l11ll_opy_ = bstack11l11l1l1_opy_(CONFIG, bstack11l1l1111_opy_)
    logger.debug(bstack1l1l11lll_opy_.format(str(bstack1lll1l11ll_opy_)))
    bstack11l1l1l1_opy_ = CONFIG.get(bstack111lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫᛁ"))[bstack11l1l1111_opy_]
    if bstack111lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ᛂ") in CONFIG and CONFIG[bstack111lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧᛃ")]:
        bstack11111l111_opy_(bstack1lll1l11ll_opy_, bstack1111l1l1l_opy_)
    if desired_capabilities:
        bstack11l11ll11_opy_ = bstack1lll1l1111_opy_(desired_capabilities)
        bstack11l11ll11_opy_[bstack111lll1_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫᛄ")] = bstack1llll1l1ll_opy_(CONFIG)
        bstack1lll111lll_opy_ = bstack11l11l1l1_opy_(bstack11l11ll11_opy_)
        if bstack1lll111lll_opy_:
            bstack1lll1l11ll_opy_ = update(bstack1lll111lll_opy_, bstack1lll1l11ll_opy_)
        desired_capabilities = None
    if options:
        bstack1lll11l11l_opy_(options, bstack1lll1l11ll_opy_)
    if not options:
        options = bstack1l1ll1llll_opy_(bstack1lll1l11ll_opy_)
    if bstack1lllll1111_opy_.bstack1lll1llll_opy_(CONFIG, bstack11l1l1111_opy_) and bstack1lllll1111_opy_.bstack1l1lll111l_opy_(bstack1lll1l11ll_opy_, options):
        bstack1lllll11111_opy_ = True
        bstack1lllll1111_opy_.set_capabilities(bstack1lll1l11ll_opy_, CONFIG)
    if proxy and bstack1lll1l11l_opy_() >= version.parse(bstack111lll1_opy_ (u"ࠬ࠺࠮࠲࠲࠱࠴ࠬᛅ")):
        options.proxy(proxy)
    if options and bstack1lll1l11l_opy_() >= version.parse(bstack111lll1_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬᛆ")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack1lll1l11l_opy_() < version.parse(bstack111lll1_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭ᛇ")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack1lll1l11ll_opy_)
    logger.info(bstack1l1lll1ll1_opy_)
    if bstack1lll1l11l_opy_() >= version.parse(bstack111lll1_opy_ (u"ࠨ࠶࠱࠵࠵࠴࠰ࠨᛈ")):
        bstack11ll1lll_opy_(self, command_executor=command_executor,
                  options=options, keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1lll1l11l_opy_() >= version.parse(bstack111lll1_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨᛉ")):
        bstack11ll1lll_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities, options=options,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1lll1l11l_opy_() >= version.parse(bstack111lll1_opy_ (u"ࠪ࠶࠳࠻࠳࠯࠲ࠪᛊ")):
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
        bstack1l1l11ll1_opy_ = bstack111lll1_opy_ (u"ࠫࠬᛋ")
        if bstack1lll1l11l_opy_() >= version.parse(bstack111lll1_opy_ (u"ࠬ࠺࠮࠱࠰࠳ࡦ࠶࠭ᛌ")):
            bstack1l1l11ll1_opy_ = self.caps.get(bstack111lll1_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡱࡦࡲࡈࡶࡤࡘࡶࡱࠨᛍ"))
        else:
            bstack1l1l11ll1_opy_ = self.capabilities.get(bstack111lll1_opy_ (u"ࠢࡰࡲࡷ࡭ࡲࡧ࡬ࡉࡷࡥ࡙ࡷࡲࠢᛎ"))
        if bstack1l1l11ll1_opy_:
            bstack1l1l1llll_opy_(bstack1l1l11ll1_opy_)
            if bstack1lll1l11l_opy_() <= version.parse(bstack111lll1_opy_ (u"ࠨ࠵࠱࠵࠸࠴࠰ࠨᛏ")):
                self.command_executor._url = bstack111lll1_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥᛐ") + bstack1llll11lll_opy_ + bstack111lll1_opy_ (u"ࠥ࠾࠽࠶࠯ࡸࡦ࠲࡬ࡺࡨࠢᛑ")
            else:
                self.command_executor._url = bstack111lll1_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨᛒ") + bstack1l1l11ll1_opy_ + bstack111lll1_opy_ (u"ࠧ࠵ࡷࡥ࠱࡫ࡹࡧࠨᛓ")
            logger.debug(bstack1l111111l_opy_.format(bstack1l1l11ll1_opy_))
        else:
            logger.debug(bstack1ll1l1ll1l_opy_.format(bstack111lll1_opy_ (u"ࠨࡏࡱࡶ࡬ࡱࡦࡲࠠࡉࡷࡥࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠢᛔ")))
    except Exception as e:
        logger.debug(bstack1ll1l1ll1l_opy_.format(e))
    bstack1ll1111l11_opy_ = self.session_id
    if bstack111lll1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧᛕ") in bstack1llll11l11_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack111lll1_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬᛖ"), None)
        if item:
            bstack1llll1l1ll1_opy_ = getattr(item, bstack111lll1_opy_ (u"ࠩࡢࡸࡪࡹࡴࡠࡥࡤࡷࡪࡥࡳࡵࡣࡵࡸࡪࡪࠧᛗ"), False)
            if not getattr(item, bstack111lll1_opy_ (u"ࠪࡣࡩࡸࡩࡷࡧࡵࠫᛘ"), None) and bstack1llll1l1ll1_opy_:
                setattr(store[bstack111lll1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨᛙ")], bstack111lll1_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭ᛚ"), self)
        bstack1llll11l1_opy_.bstack1ll11l1ll_opy_(self)
    bstack1lllllllll_opy_.append(self)
    if bstack111lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩᛛ") in CONFIG and bstack111lll1_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬᛜ") in CONFIG[bstack111lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫᛝ")][bstack11l1l1111_opy_]:
        bstack1l1lll1l11_opy_ = CONFIG[bstack111lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬᛞ")][bstack11l1l1111_opy_][bstack111lll1_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨᛟ")]
    logger.debug(bstack11ll11ll1_opy_.format(bstack1ll1111l11_opy_))
def bstack11111l1ll_opy_(self, url):
    global bstack1lll1l1l1l_opy_
    global CONFIG
    try:
        bstack11l1llll1_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack1lll1l111l_opy_.format(str(err)))
    try:
        bstack1lll1l1l1l_opy_(self, url)
    except Exception as e:
        try:
            bstack111l1l111_opy_ = str(e)
            if any(err_msg in bstack111l1l111_opy_ for err_msg in bstack11111ll1_opy_):
                bstack11l1llll1_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack1lll1l111l_opy_.format(str(err)))
        raise e
def bstack1l1l11l1l1_opy_(item, when):
    global bstack11111llll_opy_
    try:
        bstack11111llll_opy_(item, when)
    except Exception as e:
        pass
def bstack11l1ll1l_opy_(item, call, rep):
    global bstack1111lllll_opy_
    global bstack1lllllllll_opy_
    name = bstack111lll1_opy_ (u"ࠫࠬᛠ")
    try:
        if rep.when == bstack111lll1_opy_ (u"ࠬࡩࡡ࡭࡮ࠪᛡ"):
            bstack1ll1111l11_opy_ = threading.current_thread().bstackSessionId
            bstack1llll11ll1l_opy_ = item.config.getoption(bstack111lll1_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨᛢ"))
            try:
                if (str(bstack1llll11ll1l_opy_).lower() != bstack111lll1_opy_ (u"ࠧࡵࡴࡸࡩࠬᛣ")):
                    name = str(rep.nodeid)
                    bstack1l1l1ll111_opy_ = bstack11lll111l_opy_(bstack111lll1_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩᛤ"), name, bstack111lll1_opy_ (u"ࠩࠪᛥ"), bstack111lll1_opy_ (u"ࠪࠫᛦ"), bstack111lll1_opy_ (u"ࠫࠬᛧ"), bstack111lll1_opy_ (u"ࠬ࠭ᛨ"))
                    os.environ[bstack111lll1_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙ࡥࡔࡆࡕࡗࡣࡓࡇࡍࡆࠩᛩ")] = name
                    for driver in bstack1lllllllll_opy_:
                        if bstack1ll1111l11_opy_ == driver.session_id:
                            driver.execute_script(bstack1l1l1ll111_opy_)
            except Exception as e:
                logger.debug(bstack111lll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠡࡨࡲࡶࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡶࡩࡸࡹࡩࡰࡰ࠽ࠤࢀࢃࠧᛪ").format(str(e)))
            try:
                bstack1ll1l11111_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack111lll1_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩ᛫"):
                    status = bstack111lll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ᛬") if rep.outcome.lower() == bstack111lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ᛭") else bstack111lll1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᛮ")
                    reason = bstack111lll1_opy_ (u"ࠬ࠭ᛯ")
                    if status == bstack111lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᛰ"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack111lll1_opy_ (u"ࠧࡪࡰࡩࡳࠬᛱ") if status == bstack111lll1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᛲ") else bstack111lll1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᛳ")
                    data = name + bstack111lll1_opy_ (u"ࠪࠤࡵࡧࡳࡴࡧࡧࠥࠬᛴ") if status == bstack111lll1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᛵ") else name + bstack111lll1_opy_ (u"ࠬࠦࡦࡢ࡫࡯ࡩࡩࠧࠠࠨᛶ") + reason
                    bstack1l1ll11111_opy_ = bstack11lll111l_opy_(bstack111lll1_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨᛷ"), bstack111lll1_opy_ (u"ࠧࠨᛸ"), bstack111lll1_opy_ (u"ࠨࠩ᛹"), bstack111lll1_opy_ (u"ࠩࠪ᛺"), level, data)
                    for driver in bstack1lllllllll_opy_:
                        if bstack1ll1111l11_opy_ == driver.session_id:
                            driver.execute_script(bstack1l1ll11111_opy_)
            except Exception as e:
                logger.debug(bstack111lll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡤࡱࡱࡸࡪࡾࡴࠡࡨࡲࡶࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡶࡩࡸࡹࡩࡰࡰ࠽ࠤࢀࢃࠧ᛻").format(str(e)))
    except Exception as e:
        logger.debug(bstack111lll1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡶࡤࡸࡪࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡦࡵࡷࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࢁࡽࠨ᛼").format(str(e)))
    bstack1111lllll_opy_(item, call, rep)
notset = Notset()
def bstack1llll11ll_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack1llllll1l1_opy_
    if str(name).lower() == bstack111lll1_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࠬ᛽"):
        return bstack111lll1_opy_ (u"ࠨࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠧ᛾")
    else:
        return bstack1llllll1l1_opy_(self, name, default, skip)
def bstack1l1111l1_opy_(self):
    global CONFIG
    global bstack1lllll11l1_opy_
    try:
        proxy = bstack1l1lll11l_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack111lll1_opy_ (u"ࠧ࠯ࡲࡤࡧࠬ᛿")):
                proxies = bstack1llll1l11_opy_(proxy, bstack11111lll1_opy_())
                if len(proxies) > 0:
                    protocol, bstack1l1l111l11_opy_ = proxies.popitem()
                    if bstack111lll1_opy_ (u"ࠣ࠼࠲࠳ࠧᜀ") in bstack1l1l111l11_opy_:
                        return bstack1l1l111l11_opy_
                    else:
                        return bstack111lll1_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥᜁ") + bstack1l1l111l11_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack111lll1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡰࡳࡱࡻࡽࠥࡻࡲ࡭ࠢ࠽ࠤࢀࢃࠢᜂ").format(str(e)))
    return bstack1lllll11l1_opy_(self)
def bstack1l111ll1l_opy_():
    return (bstack111lll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧᜃ") in CONFIG or bstack111lll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩᜄ") in CONFIG) and bstack1lllllll1_opy_() and bstack1lll1l11l_opy_() >= version.parse(
        bstack11llll11l_opy_)
def bstack1llll11l1l_opy_(self,
               executablePath=None,
               channel=None,
               args=None,
               ignoreDefaultArgs=None,
               handleSIGINT=None,
               handleSIGTERM=None,
               handleSIGHUP=None,
               timeout=None,
               env=None,
               headless=None,
               devtools=None,
               proxy=None,
               downloadsPath=None,
               slowMo=None,
               tracesDir=None,
               chromiumSandbox=None,
               firefoxUserPrefs=None
               ):
    global CONFIG
    global bstack1l1lll1l11_opy_
    global bstack11l1l11ll_opy_
    global bstack1llll11l11_opy_
    CONFIG[bstack111lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨᜅ")] = str(bstack1llll11l11_opy_) + str(__version__)
    bstack11l1l1111_opy_ = 0
    try:
        if bstack11l1l11ll_opy_ is True:
            bstack11l1l1111_opy_ = int(os.environ.get(bstack111lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧᜆ")))
    except:
        bstack11l1l1111_opy_ = 0
    CONFIG[bstack111lll1_opy_ (u"ࠣ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢᜇ")] = True
    bstack1lll1l11ll_opy_ = bstack11l11l1l1_opy_(CONFIG, bstack11l1l1111_opy_)
    logger.debug(bstack1l1l11lll_opy_.format(str(bstack1lll1l11ll_opy_)))
    if CONFIG.get(bstack111lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ᜈ")):
        bstack11111l111_opy_(bstack1lll1l11ll_opy_, bstack1111l1l1l_opy_)
    if bstack111lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ᜉ") in CONFIG and bstack111lll1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩᜊ") in CONFIG[bstack111lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨᜋ")][bstack11l1l1111_opy_]:
        bstack1l1lll1l11_opy_ = CONFIG[bstack111lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩᜌ")][bstack11l1l1111_opy_][bstack111lll1_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬᜍ")]
    import urllib
    import json
    bstack11l111lll_opy_ = bstack111lll1_opy_ (u"ࠨࡹࡶࡷ࠿࠵࠯ࡤࡦࡳ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࡃࡨࡧࡰࡴ࠿ࠪᜎ") + urllib.parse.quote(json.dumps(bstack1lll1l11ll_opy_))
    browser = self.connect(bstack11l111lll_opy_)
    return browser
def bstack11l111ll1_opy_():
    global bstack11lllll1l_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        BrowserType.launch = bstack1llll11l1l_opy_
        bstack11lllll1l_opy_ = True
    except Exception as e:
        pass
def bstack1llll11lll1_opy_():
    global CONFIG
    global bstack1ll1l1l11l_opy_
    global bstack1llll11lll_opy_
    global bstack1111l1l1l_opy_
    global bstack11l1l11ll_opy_
    CONFIG = json.loads(os.environ.get(bstack111lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࠨᜏ")))
    bstack1ll1l1l11l_opy_ = eval(os.environ.get(bstack111lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫᜐ")))
    bstack1llll11lll_opy_ = os.environ.get(bstack111lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡌ࡚ࡈ࡟ࡖࡔࡏࠫᜑ"))
    bstack1ll1111l1l_opy_(CONFIG, bstack1ll1l1l11l_opy_)
    bstack1ll11l11l_opy_()
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
    if (bstack111lll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨᜒ") in CONFIG or bstack111lll1_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪᜓ") in CONFIG) and bstack1lllllll1_opy_():
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
        logger.debug(bstack111lll1_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺ࡯ࠡࡴࡸࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࡳࠨ᜔"))
    bstack1111l1l1l_opy_ = CONFIG.get(bstack111lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷ᜕ࠬ"), {}).get(bstack111lll1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ᜖"))
    bstack11l1l11ll_opy_ = True
    bstack111111lll_opy_(bstack1ll1111lll_opy_)
if (bstack11l1l1ll1l_opy_()):
    bstack1llll11lll1_opy_()
@bstack1l11ll1ll1_opy_(class_method=False)
def bstack1llll1l1l11_opy_(hook_name, event, bstack1llll1ll1l1_opy_=None):
    if hook_name not in [bstack111lll1_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࠫ᜗"), bstack111lll1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨ᜘"), bstack111lll1_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࠫ᜙"), bstack111lll1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨ᜚"), bstack111lll1_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡣ࡭ࡣࡶࡷࠬ᜛"), bstack111lll1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡧࡱࡧࡳࡴࠩ᜜"), bstack111lll1_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠨ᜝"), bstack111lll1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠬ᜞")]:
        return
    node = store[bstack111lll1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡭ࡹ࡫࡭ࠨᜟ")]
    if hook_name in [bstack111lll1_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࠫᜠ"), bstack111lll1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨᜡ")]:
        node = store[bstack111lll1_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠ࡯ࡲࡨࡺࡲࡥࡠ࡫ࡷࡩࡲ࠭ᜢ")]
    elif hook_name in [bstack111lll1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭ᜣ"), bstack111lll1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠪᜤ")]:
        node = store[bstack111lll1_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡨࡲࡡࡴࡵࡢ࡭ࡹ࡫࡭ࠨᜥ")]
    if event == bstack111lll1_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫᜦ"):
        hook_type = bstack1111l1l11l_opy_(hook_name)
        uuid = uuid4().__str__()
        bstack1l11l1ll11_opy_ = {
            bstack111lll1_opy_ (u"ࠬࡻࡵࡪࡦࠪᜧ"): uuid,
            bstack111lll1_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᜨ"): bstack1ll1l11lll_opy_(),
            bstack111lll1_opy_ (u"ࠧࡵࡻࡳࡩࠬᜩ"): bstack111lll1_opy_ (u"ࠨࡪࡲࡳࡰ࠭ᜪ"),
            bstack111lll1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡵࡻࡳࡩࠬᜫ"): hook_type,
            bstack111lll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡰࡤࡱࡪ࠭ᜬ"): hook_name
        }
        store[bstack111lll1_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᜭ")].append(uuid)
        bstack1llll1l1l1l_opy_ = node.nodeid
        if hook_type == bstack111lll1_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠪᜮ"):
            if not _1l11lllll1_opy_.get(bstack1llll1l1l1l_opy_, None):
                _1l11lllll1_opy_[bstack1llll1l1l1l_opy_] = {bstack111lll1_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᜯ"): []}
            _1l11lllll1_opy_[bstack1llll1l1l1l_opy_][bstack111lll1_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ᜰ")].append(bstack1l11l1ll11_opy_[bstack111lll1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᜱ")])
        _1l11lllll1_opy_[bstack1llll1l1l1l_opy_ + bstack111lll1_opy_ (u"ࠩ࠰ࠫᜲ") + hook_name] = bstack1l11l1ll11_opy_
        bstack1lllll111ll_opy_(node, bstack1l11l1ll11_opy_, bstack111lll1_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᜳ"))
    elif event == bstack111lll1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴ᜴ࠪ"):
        bstack1l11l11l1l_opy_ = node.nodeid + bstack111lll1_opy_ (u"ࠬ࠳ࠧ᜵") + hook_name
        _1l11lllll1_opy_[bstack1l11l11l1l_opy_][bstack111lll1_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ᜶")] = bstack1ll1l11lll_opy_()
        bstack1llll1ll1ll_opy_(_1l11lllll1_opy_[bstack1l11l11l1l_opy_][bstack111lll1_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ᜷")])
        bstack1lllll111ll_opy_(node, _1l11lllll1_opy_[bstack1l11l11l1l_opy_], bstack111lll1_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ᜸"), bstack1lllll11ll1_opy_=bstack1llll1ll1l1_opy_)
def bstack1llll1lllll_opy_():
    global bstack1llll1l111l_opy_
    if bstack1l1111ll1_opy_():
        bstack1llll1l111l_opy_ = bstack111lll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩ࠭᜹")
    else:
        bstack1llll1l111l_opy_ = bstack111lll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ᜺")
@bstack1llll11l1_opy_.bstack1llllll1lll_opy_
def bstack1llll111ll1_opy_():
    bstack1llll1lllll_opy_()
    if bstack1lllllll1_opy_():
        bstack111l1l1l1_opy_(bstack1ll1lll1l1_opy_)
    bstack11l111ll11_opy_ = bstack11l111l1l1_opy_(bstack1llll1l1l11_opy_)
bstack1llll111ll1_opy_()