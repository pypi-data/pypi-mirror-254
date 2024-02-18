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
import os
import platform
import re
import subprocess
import traceback
import tempfile
import multiprocessing
import threading
from urllib.parse import urlparse
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import bstack11ll11l1l1_opy_, bstack11l11ll1l_opy_, bstack1ll11111l1_opy_, bstack111llll1l_opy_
from bstack_utils.messages import bstack1111l111l_opy_, bstack11l1l1ll_opy_
from bstack_utils.proxy import bstack1l1l11llll_opy_, bstack1l1lll11l_opy_
bstack11l11l111_opy_ = Config.bstack111l1ll1_opy_()
def bstack11ll1l1l11_opy_(config):
    return config[bstack111lll1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨᄲ")]
def bstack11ll1ll1l1_opy_(config):
    return config[bstack111lll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪᄳ")]
def bstack1111lll1_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack11l1l111ll_opy_(obj):
    values = []
    bstack11l11l1lll_opy_ = re.compile(bstack111lll1_opy_ (u"ࡳࠤࡡࡇ࡚࡙ࡔࡐࡏࡢࡘࡆࡍ࡟࡝ࡦ࠮ࠨࠧᄴ"), re.I)
    for key in obj.keys():
        if bstack11l11l1lll_opy_.match(key):
            values.append(obj[key])
    return values
def bstack11l1l11l11_opy_(config):
    tags = []
    tags.extend(bstack11l1l111ll_opy_(os.environ))
    tags.extend(bstack11l1l111ll_opy_(config))
    return tags
def bstack11l1l1l111_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack11l11lll11_opy_(bstack11ll111111_opy_):
    if not bstack11ll111111_opy_:
        return bstack111lll1_opy_ (u"ࠩࠪᄵ")
    return bstack111lll1_opy_ (u"ࠥࡿࢂࠦࠨࡼࡿࠬࠦᄶ").format(bstack11ll111111_opy_.name, bstack11ll111111_opy_.email)
def bstack11ll1l1ll1_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack11l1l1ll11_opy_ = repo.common_dir
        info = {
            bstack111lll1_opy_ (u"ࠦࡸ࡮ࡡࠣᄷ"): repo.head.commit.hexsha,
            bstack111lll1_opy_ (u"ࠧࡹࡨࡰࡴࡷࡣࡸ࡮ࡡࠣᄸ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack111lll1_opy_ (u"ࠨࡢࡳࡣࡱࡧ࡭ࠨᄹ"): repo.active_branch.name,
            bstack111lll1_opy_ (u"ࠢࡵࡣࡪࠦᄺ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack111lll1_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡵࡧࡵࠦᄻ"): bstack11l11lll11_opy_(repo.head.commit.committer),
            bstack111lll1_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡶࡨࡶࡤࡪࡡࡵࡧࠥᄼ"): repo.head.commit.committed_datetime.isoformat(),
            bstack111lll1_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࠥᄽ"): bstack11l11lll11_opy_(repo.head.commit.author),
            bstack111lll1_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࡣࡩࡧࡴࡦࠤᄾ"): repo.head.commit.authored_datetime.isoformat(),
            bstack111lll1_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡤࡳࡥࡴࡵࡤ࡫ࡪࠨᄿ"): repo.head.commit.message,
            bstack111lll1_opy_ (u"ࠨࡲࡰࡱࡷࠦᅀ"): repo.git.rev_parse(bstack111lll1_opy_ (u"ࠢ࠮࠯ࡶ࡬ࡴࡽ࠭ࡵࡱࡳࡰࡪࡼࡥ࡭ࠤᅁ")),
            bstack111lll1_opy_ (u"ࠣࡥࡲࡱࡲࡵ࡮ࡠࡩ࡬ࡸࡤࡪࡩࡳࠤᅂ"): bstack11l1l1ll11_opy_,
            bstack111lll1_opy_ (u"ࠤࡺࡳࡷࡱࡴࡳࡧࡨࡣ࡬࡯ࡴࡠࡦ࡬ࡶࠧᅃ"): subprocess.check_output([bstack111lll1_opy_ (u"ࠥ࡫࡮ࡺࠢᅄ"), bstack111lll1_opy_ (u"ࠦࡷ࡫ࡶ࠮ࡲࡤࡶࡸ࡫ࠢᅅ"), bstack111lll1_opy_ (u"ࠧ࠳࠭ࡨ࡫ࡷ࠱ࡨࡵ࡭࡮ࡱࡱ࠱ࡩ࡯ࡲࠣᅆ")]).strip().decode(
                bstack111lll1_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬᅇ")),
            bstack111lll1_opy_ (u"ࠢ࡭ࡣࡶࡸࡤࡺࡡࡨࠤᅈ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack111lll1_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡴࡡࡶ࡭ࡳࡩࡥࡠ࡮ࡤࡷࡹࡥࡴࡢࡩࠥᅉ"): repo.git.rev_list(
                bstack111lll1_opy_ (u"ࠤࡾࢁ࠳࠴ࡻࡾࠤᅊ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack11l1llllll_opy_ = []
        for remote in remotes:
            bstack11l11l11ll_opy_ = {
                bstack111lll1_opy_ (u"ࠥࡲࡦࡳࡥࠣᅋ"): remote.name,
                bstack111lll1_opy_ (u"ࠦࡺࡸ࡬ࠣᅌ"): remote.url,
            }
            bstack11l1llllll_opy_.append(bstack11l11l11ll_opy_)
        return {
            bstack111lll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᅍ"): bstack111lll1_opy_ (u"ࠨࡧࡪࡶࠥᅎ"),
            **info,
            bstack111lll1_opy_ (u"ࠢࡳࡧࡰࡳࡹ࡫ࡳࠣᅏ"): bstack11l1llllll_opy_
        }
    except Exception as err:
        print(bstack111lll1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡱࡳࡹࡱࡧࡴࡪࡰࡪࠤࡌ࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠦᅐ").format(err))
        return {}
def bstack1lll11l1ll_opy_():
    env = os.environ
    if (bstack111lll1_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢ࡙ࡗࡒࠢᅑ") in env and len(env[bstack111lll1_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣ࡚ࡘࡌࠣᅒ")]) > 0) or (
            bstack111lll1_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤࡎࡏࡎࡇࠥᅓ") in env and len(env[bstack111lll1_opy_ (u"ࠧࡐࡅࡏࡍࡌࡒࡘࡥࡈࡐࡏࡈࠦᅔ")]) > 0):
        return {
            bstack111lll1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᅕ"): bstack111lll1_opy_ (u"ࠢࡋࡧࡱ࡯࡮ࡴࡳࠣᅖ"),
            bstack111lll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᅗ"): env.get(bstack111lll1_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧᅘ")),
            bstack111lll1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᅙ"): env.get(bstack111lll1_opy_ (u"ࠦࡏࡕࡂࡠࡐࡄࡑࡊࠨᅚ")),
            bstack111lll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᅛ"): env.get(bstack111lll1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᅜ"))
        }
    if env.get(bstack111lll1_opy_ (u"ࠢࡄࡋࠥᅝ")) == bstack111lll1_opy_ (u"ࠣࡶࡵࡹࡪࠨᅞ") and bstack1lllll111l_opy_(env.get(bstack111lll1_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡅࡌࠦᅟ"))):
        return {
            bstack111lll1_opy_ (u"ࠥࡲࡦࡳࡥࠣᅠ"): bstack111lll1_opy_ (u"ࠦࡈ࡯ࡲࡤ࡮ࡨࡇࡎࠨᅡ"),
            bstack111lll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᅢ"): env.get(bstack111lll1_opy_ (u"ࠨࡃࡊࡔࡆࡐࡊࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤᅣ")),
            bstack111lll1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᅤ"): env.get(bstack111lll1_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡠࡌࡒࡆࠧᅥ")),
            bstack111lll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᅦ"): env.get(bstack111lll1_opy_ (u"ࠥࡇࡎࡘࡃࡍࡇࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࠨᅧ"))
        }
    if env.get(bstack111lll1_opy_ (u"ࠦࡈࡏࠢᅨ")) == bstack111lll1_opy_ (u"ࠧࡺࡲࡶࡧࠥᅩ") and bstack1lllll111l_opy_(env.get(bstack111lll1_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࠨᅪ"))):
        return {
            bstack111lll1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᅫ"): bstack111lll1_opy_ (u"ࠣࡖࡵࡥࡻ࡯ࡳࠡࡅࡌࠦᅬ"),
            bstack111lll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᅭ"): env.get(bstack111lll1_opy_ (u"ࠥࡘࡗࡇࡖࡊࡕࡢࡆ࡚ࡏࡌࡅࡡ࡚ࡉࡇࡥࡕࡓࡎࠥᅮ")),
            bstack111lll1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᅯ"): env.get(bstack111lll1_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢᅰ")),
            bstack111lll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᅱ"): env.get(bstack111lll1_opy_ (u"ࠢࡕࡔࡄ࡚ࡎ࡙࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨᅲ"))
        }
    if env.get(bstack111lll1_opy_ (u"ࠣࡅࡌࠦᅳ")) == bstack111lll1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᅴ") and env.get(bstack111lll1_opy_ (u"ࠥࡇࡎࡥࡎࡂࡏࡈࠦᅵ")) == bstack111lll1_opy_ (u"ࠦࡨࡵࡤࡦࡵ࡫࡭ࡵࠨᅶ"):
        return {
            bstack111lll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᅷ"): bstack111lll1_opy_ (u"ࠨࡃࡰࡦࡨࡷ࡭࡯ࡰࠣᅸ"),
            bstack111lll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᅹ"): None,
            bstack111lll1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᅺ"): None,
            bstack111lll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᅻ"): None
        }
    if env.get(bstack111lll1_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡂࡓࡃࡑࡇࡍࠨᅼ")) and env.get(bstack111lll1_opy_ (u"ࠦࡇࡏࡔࡃࡗࡆࡏࡊ࡚࡟ࡄࡑࡐࡑࡎ࡚ࠢᅽ")):
        return {
            bstack111lll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᅾ"): bstack111lll1_opy_ (u"ࠨࡂࡪࡶࡥࡹࡨࡱࡥࡵࠤᅿ"),
            bstack111lll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᆀ"): env.get(bstack111lll1_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡌࡏࡔࡠࡊࡗࡘࡕࡥࡏࡓࡋࡊࡍࡓࠨᆁ")),
            bstack111lll1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᆂ"): None,
            bstack111lll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᆃ"): env.get(bstack111lll1_opy_ (u"ࠦࡇࡏࡔࡃࡗࡆࡏࡊ࡚࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨᆄ"))
        }
    if env.get(bstack111lll1_opy_ (u"ࠧࡉࡉࠣᆅ")) == bstack111lll1_opy_ (u"ࠨࡴࡳࡷࡨࠦᆆ") and bstack1lllll111l_opy_(env.get(bstack111lll1_opy_ (u"ࠢࡅࡔࡒࡒࡊࠨᆇ"))):
        return {
            bstack111lll1_opy_ (u"ࠣࡰࡤࡱࡪࠨᆈ"): bstack111lll1_opy_ (u"ࠤࡇࡶࡴࡴࡥࠣᆉ"),
            bstack111lll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᆊ"): env.get(bstack111lll1_opy_ (u"ࠦࡉࡘࡏࡏࡇࡢࡆ࡚ࡏࡌࡅࡡࡏࡍࡓࡑࠢᆋ")),
            bstack111lll1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᆌ"): None,
            bstack111lll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᆍ"): env.get(bstack111lll1_opy_ (u"ࠢࡅࡔࡒࡒࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧᆎ"))
        }
    if env.get(bstack111lll1_opy_ (u"ࠣࡅࡌࠦᆏ")) == bstack111lll1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᆐ") and bstack1lllll111l_opy_(env.get(bstack111lll1_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࠨᆑ"))):
        return {
            bstack111lll1_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᆒ"): bstack111lll1_opy_ (u"࡙ࠧࡥ࡮ࡣࡳ࡬ࡴࡸࡥࠣᆓ"),
            bstack111lll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᆔ"): env.get(bstack111lll1_opy_ (u"ࠢࡔࡇࡐࡅࡕࡎࡏࡓࡇࡢࡓࡗࡍࡁࡏࡋ࡝ࡅ࡙ࡏࡏࡏࡡࡘࡖࡑࠨᆕ")),
            bstack111lll1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᆖ"): env.get(bstack111lll1_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢᆗ")),
            bstack111lll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᆘ"): env.get(bstack111lll1_opy_ (u"ࠦࡘࡋࡍࡂࡒࡋࡓࡗࡋ࡟ࡋࡑࡅࡣࡎࡊࠢᆙ"))
        }
    if env.get(bstack111lll1_opy_ (u"ࠧࡉࡉࠣᆚ")) == bstack111lll1_opy_ (u"ࠨࡴࡳࡷࡨࠦᆛ") and bstack1lllll111l_opy_(env.get(bstack111lll1_opy_ (u"ࠢࡈࡋࡗࡐࡆࡈ࡟ࡄࡋࠥᆜ"))):
        return {
            bstack111lll1_opy_ (u"ࠣࡰࡤࡱࡪࠨᆝ"): bstack111lll1_opy_ (u"ࠤࡊ࡭ࡹࡒࡡࡣࠤᆞ"),
            bstack111lll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᆟ"): env.get(bstack111lll1_opy_ (u"ࠦࡈࡏ࡟ࡋࡑࡅࡣ࡚ࡘࡌࠣᆠ")),
            bstack111lll1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᆡ"): env.get(bstack111lll1_opy_ (u"ࠨࡃࡊࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᆢ")),
            bstack111lll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᆣ"): env.get(bstack111lll1_opy_ (u"ࠣࡅࡌࡣࡏࡕࡂࡠࡋࡇࠦᆤ"))
        }
    if env.get(bstack111lll1_opy_ (u"ࠤࡆࡍࠧᆥ")) == bstack111lll1_opy_ (u"ࠥࡸࡷࡻࡥࠣᆦ") and bstack1lllll111l_opy_(env.get(bstack111lll1_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋࠢᆧ"))):
        return {
            bstack111lll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᆨ"): bstack111lll1_opy_ (u"ࠨࡂࡶ࡫࡯ࡨࡰ࡯ࡴࡦࠤᆩ"),
            bstack111lll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᆪ"): env.get(bstack111lll1_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢᆫ")),
            bstack111lll1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᆬ"): env.get(bstack111lll1_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡌࡂࡄࡈࡐࠧᆭ")) or env.get(bstack111lll1_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡑࡅࡒࡋࠢᆮ")),
            bstack111lll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᆯ"): env.get(bstack111lll1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡐࡏࡔࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᆰ"))
        }
    if bstack1lllll111l_opy_(env.get(bstack111lll1_opy_ (u"ࠢࡕࡈࡢࡆ࡚ࡏࡌࡅࠤᆱ"))):
        return {
            bstack111lll1_opy_ (u"ࠣࡰࡤࡱࡪࠨᆲ"): bstack111lll1_opy_ (u"ࠤ࡙࡭ࡸࡻࡡ࡭ࠢࡖࡸࡺࡪࡩࡰࠢࡗࡩࡦࡳࠠࡔࡧࡵࡺ࡮ࡩࡥࡴࠤᆳ"),
            bstack111lll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᆴ"): bstack111lll1_opy_ (u"ࠦࢀࢃࡻࡾࠤᆵ").format(env.get(bstack111lll1_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡉࡓ࡚ࡔࡄࡂࡖࡌࡓࡓ࡙ࡅࡓࡘࡈࡖ࡚ࡘࡉࠨᆶ")), env.get(bstack111lll1_opy_ (u"࠭ࡓ࡚ࡕࡗࡉࡒࡥࡔࡆࡃࡐࡔࡗࡕࡊࡆࡅࡗࡍࡉ࠭ᆷ"))),
            bstack111lll1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᆸ"): env.get(bstack111lll1_opy_ (u"ࠣࡕ࡜ࡗ࡙ࡋࡍࡠࡆࡈࡊࡎࡔࡉࡕࡋࡒࡒࡎࡊࠢᆹ")),
            bstack111lll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᆺ"): env.get(bstack111lll1_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠥᆻ"))
        }
    if bstack1lllll111l_opy_(env.get(bstack111lll1_opy_ (u"ࠦࡆࡖࡐࡗࡇ࡜ࡓࡗࠨᆼ"))):
        return {
            bstack111lll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᆽ"): bstack111lll1_opy_ (u"ࠨࡁࡱࡲࡹࡩࡾࡵࡲࠣᆾ"),
            bstack111lll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᆿ"): bstack111lll1_opy_ (u"ࠣࡽࢀ࠳ࡵࡸ࡯࡫ࡧࡦࡸ࠴ࢁࡽ࠰ࡽࢀ࠳ࡧࡻࡩ࡭ࡦࡶ࠳ࢀࢃࠢᇀ").format(env.get(bstack111lll1_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣ࡚ࡘࡌࠨᇁ")), env.get(bstack111lll1_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡇࡃࡄࡑࡘࡒ࡙ࡥࡎࡂࡏࡈࠫᇂ")), env.get(bstack111lll1_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡐࡓࡑࡍࡉࡈ࡚࡟ࡔࡎࡘࡋࠬᇃ")), env.get(bstack111lll1_opy_ (u"ࠬࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩᇄ"))),
            bstack111lll1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᇅ"): env.get(bstack111lll1_opy_ (u"ࠢࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦᇆ")),
            bstack111lll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᇇ"): env.get(bstack111lll1_opy_ (u"ࠤࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥᇈ"))
        }
    if env.get(bstack111lll1_opy_ (u"ࠥࡅ࡟࡛ࡒࡆࡡࡋࡘ࡙ࡖ࡟ࡖࡕࡈࡖࡤࡇࡇࡆࡐࡗࠦᇉ")) and env.get(bstack111lll1_opy_ (u"࡙ࠦࡌ࡟ࡃࡗࡌࡐࡉࠨᇊ")):
        return {
            bstack111lll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᇋ"): bstack111lll1_opy_ (u"ࠨࡁࡻࡷࡵࡩࠥࡉࡉࠣᇌ"),
            bstack111lll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᇍ"): bstack111lll1_opy_ (u"ࠣࡽࢀࡿࢂ࠵࡟ࡣࡷ࡬ࡰࡩ࠵ࡲࡦࡵࡸࡰࡹࡹ࠿ࡣࡷ࡬ࡰࡩࡏࡤ࠾ࡽࢀࠦᇎ").format(env.get(bstack111lll1_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡆࡐࡗࡑࡈࡆ࡚ࡉࡐࡐࡖࡉࡗ࡜ࡅࡓࡗࡕࡍࠬᇏ")), env.get(bstack111lll1_opy_ (u"ࠪࡗ࡞࡙ࡔࡆࡏࡢࡘࡊࡇࡍࡑࡔࡒࡎࡊࡉࡔࠨᇐ")), env.get(bstack111lll1_opy_ (u"ࠫࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡋࡇࠫᇑ"))),
            bstack111lll1_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᇒ"): env.get(bstack111lll1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡍࡉࠨᇓ")),
            bstack111lll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᇔ"): env.get(bstack111lll1_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡏࡄࠣᇕ"))
        }
    if any([env.get(bstack111lll1_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢᇖ")), env.get(bstack111lll1_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡒࡆࡕࡒࡐ࡛ࡋࡄࡠࡕࡒ࡙ࡗࡉࡅࡠࡘࡈࡖࡘࡏࡏࡏࠤᇗ")), env.get(bstack111lll1_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡔࡑࡘࡖࡈࡋ࡟ࡗࡇࡕࡗࡎࡕࡎࠣᇘ"))]):
        return {
            bstack111lll1_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᇙ"): bstack111lll1_opy_ (u"ࠨࡁࡘࡕࠣࡇࡴࡪࡥࡃࡷ࡬ࡰࡩࠨᇚ"),
            bstack111lll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᇛ"): env.get(bstack111lll1_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡕ࡛ࡂࡍࡋࡆࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢᇜ")),
            bstack111lll1_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᇝ"): env.get(bstack111lll1_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠣᇞ")),
            bstack111lll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᇟ"): env.get(bstack111lll1_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᇠ"))
        }
    if env.get(bstack111lll1_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡢࡶ࡫࡯ࡨࡓࡻ࡭ࡣࡧࡵࠦᇡ")):
        return {
            bstack111lll1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧᇢ"): bstack111lll1_opy_ (u"ࠣࡄࡤࡱࡧࡵ࡯ࠣᇣ"),
            bstack111lll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧᇤ"): env.get(bstack111lll1_opy_ (u"ࠥࡦࡦࡳࡢࡰࡱࡢࡦࡺ࡯࡬ࡥࡔࡨࡷࡺࡲࡴࡴࡗࡵࡰࠧᇥ")),
            bstack111lll1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᇦ"): env.get(bstack111lll1_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡹࡨࡰࡴࡷࡎࡴࡨࡎࡢ࡯ࡨࠦᇧ")),
            bstack111lll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᇨ"): env.get(bstack111lll1_opy_ (u"ࠢࡣࡣࡰࡦࡴࡵ࡟ࡣࡷ࡬ࡰࡩࡔࡵ࡮ࡤࡨࡶࠧᇩ"))
        }
    if env.get(bstack111lll1_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࠤᇪ")) or env.get(bstack111lll1_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࡢࡑࡆࡏࡎࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡗ࡙ࡇࡒࡕࡇࡇࠦᇫ")):
        return {
            bstack111lll1_opy_ (u"ࠥࡲࡦࡳࡥࠣᇬ"): bstack111lll1_opy_ (u"ࠦ࡜࡫ࡲࡤ࡭ࡨࡶࠧᇭ"),
            bstack111lll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᇮ"): env.get(bstack111lll1_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᇯ")),
            bstack111lll1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᇰ"): bstack111lll1_opy_ (u"ࠣࡏࡤ࡭ࡳࠦࡐࡪࡲࡨࡰ࡮ࡴࡥࠣᇱ") if env.get(bstack111lll1_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࡢࡑࡆࡏࡎࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡗ࡙ࡇࡒࡕࡇࡇࠦᇲ")) else None,
            bstack111lll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᇳ"): env.get(bstack111lll1_opy_ (u"ࠦ࡜ࡋࡒࡄࡍࡈࡖࡤࡍࡉࡕࡡࡆࡓࡒࡓࡉࡕࠤᇴ"))
        }
    if any([env.get(bstack111lll1_opy_ (u"ࠧࡍࡃࡑࡡࡓࡖࡔࡐࡅࡄࡖࠥᇵ")), env.get(bstack111lll1_opy_ (u"ࠨࡇࡄࡎࡒ࡙ࡉࡥࡐࡓࡑࡍࡉࡈ࡚ࠢᇶ")), env.get(bstack111lll1_opy_ (u"ࠢࡈࡑࡒࡋࡑࡋ࡟ࡄࡎࡒ࡙ࡉࡥࡐࡓࡑࡍࡉࡈ࡚ࠢᇷ"))]):
        return {
            bstack111lll1_opy_ (u"ࠣࡰࡤࡱࡪࠨᇸ"): bstack111lll1_opy_ (u"ࠤࡊࡳࡴ࡭࡬ࡦࠢࡆࡰࡴࡻࡤࠣᇹ"),
            bstack111lll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᇺ"): None,
            bstack111lll1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᇻ"): env.get(bstack111lll1_opy_ (u"ࠧࡖࡒࡐࡌࡈࡇ࡙ࡥࡉࡅࠤᇼ")),
            bstack111lll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᇽ"): env.get(bstack111lll1_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡉࡅࠤᇾ"))
        }
    if env.get(bstack111lll1_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࠦᇿ")):
        return {
            bstack111lll1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢሀ"): bstack111lll1_opy_ (u"ࠥࡗ࡭࡯ࡰࡱࡣࡥࡰࡪࠨሁ"),
            bstack111lll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢሂ"): env.get(bstack111lll1_opy_ (u"࡙ࠧࡈࡊࡒࡓࡅࡇࡒࡅࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦሃ")),
            bstack111lll1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣሄ"): bstack111lll1_opy_ (u"ࠢࡋࡱࡥࠤࠨࢁࡽࠣህ").format(env.get(bstack111lll1_opy_ (u"ࠨࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡏࡕࡂࡠࡋࡇࠫሆ"))) if env.get(bstack111lll1_opy_ (u"ࠤࡖࡌࡎࡖࡐࡂࡄࡏࡉࡤࡐࡏࡃࡡࡌࡈࠧሇ")) else None,
            bstack111lll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤለ"): env.get(bstack111lll1_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨሉ"))
        }
    if bstack1lllll111l_opy_(env.get(bstack111lll1_opy_ (u"ࠧࡔࡅࡕࡎࡌࡊ࡞ࠨሊ"))):
        return {
            bstack111lll1_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦላ"): bstack111lll1_opy_ (u"ࠢࡏࡧࡷࡰ࡮࡬ࡹࠣሌ"),
            bstack111lll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦል"): env.get(bstack111lll1_opy_ (u"ࠤࡇࡉࡕࡒࡏ࡚ࡡࡘࡖࡑࠨሎ")),
            bstack111lll1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧሏ"): env.get(bstack111lll1_opy_ (u"ࠦࡘࡏࡔࡆࡡࡑࡅࡒࡋࠢሐ")),
            bstack111lll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦሑ"): env.get(bstack111lll1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡏࡄࠣሒ"))
        }
    if bstack1lllll111l_opy_(env.get(bstack111lll1_opy_ (u"ࠢࡈࡋࡗࡌ࡚ࡈ࡟ࡂࡅࡗࡍࡔࡔࡓࠣሓ"))):
        return {
            bstack111lll1_opy_ (u"ࠣࡰࡤࡱࡪࠨሔ"): bstack111lll1_opy_ (u"ࠤࡊ࡭ࡹࡎࡵࡣࠢࡄࡧࡹ࡯࡯࡯ࡵࠥሕ"),
            bstack111lll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨሖ"): bstack111lll1_opy_ (u"ࠦࢀࢃ࠯ࡼࡿ࠲ࡥࡨࡺࡩࡰࡰࡶ࠳ࡷࡻ࡮ࡴ࠱ࡾࢁࠧሗ").format(env.get(bstack111lll1_opy_ (u"ࠬࡍࡉࡕࡊࡘࡆࡤ࡙ࡅࡓࡘࡈࡖࡤ࡛ࡒࡍࠩመ")), env.get(bstack111lll1_opy_ (u"࠭ࡇࡊࡖࡋ࡙ࡇࡥࡒࡆࡒࡒࡗࡎ࡚ࡏࡓ࡛ࠪሙ")), env.get(bstack111lll1_opy_ (u"ࠧࡈࡋࡗࡌ࡚ࡈ࡟ࡓࡗࡑࡣࡎࡊࠧሚ"))),
            bstack111lll1_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥማ"): env.get(bstack111lll1_opy_ (u"ࠤࡊࡍ࡙ࡎࡕࡃࡡ࡚ࡓࡗࡑࡆࡍࡑ࡚ࠦሜ")),
            bstack111lll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤም"): env.get(bstack111lll1_opy_ (u"ࠦࡌࡏࡔࡉࡗࡅࡣࡗ࡛ࡎࡠࡋࡇࠦሞ"))
        }
    if env.get(bstack111lll1_opy_ (u"ࠧࡉࡉࠣሟ")) == bstack111lll1_opy_ (u"ࠨࡴࡳࡷࡨࠦሠ") and env.get(bstack111lll1_opy_ (u"ࠢࡗࡇࡕࡇࡊࡒࠢሡ")) == bstack111lll1_opy_ (u"ࠣ࠳ࠥሢ"):
        return {
            bstack111lll1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢሣ"): bstack111lll1_opy_ (u"࡚ࠥࡪࡸࡣࡦ࡮ࠥሤ"),
            bstack111lll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢሥ"): bstack111lll1_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࢁࡽࠣሦ").format(env.get(bstack111lll1_opy_ (u"࠭ࡖࡆࡔࡆࡉࡑࡥࡕࡓࡎࠪሧ"))),
            bstack111lll1_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤረ"): None,
            bstack111lll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢሩ"): None,
        }
    if env.get(bstack111lll1_opy_ (u"ࠤࡗࡉࡆࡓࡃࡊࡖ࡜ࡣ࡛ࡋࡒࡔࡋࡒࡒࠧሪ")):
        return {
            bstack111lll1_opy_ (u"ࠥࡲࡦࡳࡥࠣራ"): bstack111lll1_opy_ (u"࡙ࠦ࡫ࡡ࡮ࡥ࡬ࡸࡾࠨሬ"),
            bstack111lll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣር"): None,
            bstack111lll1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣሮ"): env.get(bstack111lll1_opy_ (u"ࠢࡕࡇࡄࡑࡈࡏࡔ࡚ࡡࡓࡖࡔࡐࡅࡄࡖࡢࡒࡆࡓࡅࠣሯ")),
            bstack111lll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢሰ"): env.get(bstack111lll1_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣሱ"))
        }
    if any([env.get(bstack111lll1_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࠨሲ")), env.get(bstack111lll1_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋ࡟ࡖࡔࡏࠦሳ")), env.get(bstack111lll1_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࡠࡗࡖࡉࡗࡔࡁࡎࡇࠥሴ")), env.get(bstack111lll1_opy_ (u"ࠨࡃࡐࡐࡆࡓ࡚ࡘࡓࡆࡡࡗࡉࡆࡓࠢስ"))]):
        return {
            bstack111lll1_opy_ (u"ࠢ࡯ࡣࡰࡩࠧሶ"): bstack111lll1_opy_ (u"ࠣࡅࡲࡲࡨࡵࡵࡳࡵࡨࠦሷ"),
            bstack111lll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧሸ"): None,
            bstack111lll1_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧሹ"): env.get(bstack111lll1_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧሺ")) or None,
            bstack111lll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦሻ"): env.get(bstack111lll1_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡏࡄࠣሼ"), 0)
        }
    if env.get(bstack111lll1_opy_ (u"ࠢࡈࡑࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧሽ")):
        return {
            bstack111lll1_opy_ (u"ࠣࡰࡤࡱࡪࠨሾ"): bstack111lll1_opy_ (u"ࠤࡊࡳࡈࡊࠢሿ"),
            bstack111lll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨቀ"): None,
            bstack111lll1_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨቁ"): env.get(bstack111lll1_opy_ (u"ࠧࡍࡏࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥቂ")),
            bstack111lll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧቃ"): env.get(bstack111lll1_opy_ (u"ࠢࡈࡑࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤࡉࡏࡖࡐࡗࡉࡗࠨቄ"))
        }
    if env.get(bstack111lll1_opy_ (u"ࠣࡅࡉࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨቅ")):
        return {
            bstack111lll1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢቆ"): bstack111lll1_opy_ (u"ࠥࡇࡴࡪࡥࡇࡴࡨࡷ࡭ࠨቇ"),
            bstack111lll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢቈ"): env.get(bstack111lll1_opy_ (u"ࠧࡉࡆࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦ቉")),
            bstack111lll1_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣቊ"): env.get(bstack111lll1_opy_ (u"ࠢࡄࡈࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤࡔࡁࡎࡇࠥቋ")),
            bstack111lll1_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢቌ"): env.get(bstack111lll1_opy_ (u"ࠤࡆࡊࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢቍ"))
        }
    return {bstack111lll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ቎"): None}
def get_host_info():
    return {
        bstack111lll1_opy_ (u"ࠦ࡭ࡵࡳࡵࡰࡤࡱࡪࠨ቏"): platform.node(),
        bstack111lll1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࠢቐ"): platform.system(),
        bstack111lll1_opy_ (u"ࠨࡴࡺࡲࡨࠦቑ"): platform.machine(),
        bstack111lll1_opy_ (u"ࠢࡷࡧࡵࡷ࡮ࡵ࡮ࠣቒ"): platform.version(),
        bstack111lll1_opy_ (u"ࠣࡣࡵࡧ࡭ࠨቓ"): platform.architecture()[0]
    }
def bstack1lllllll1_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack11l1ll111l_opy_():
    if bstack11l11l111_opy_.get_property(bstack111lll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪቔ")):
        return bstack111lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩቕ")
    return bstack111lll1_opy_ (u"ࠫࡺࡴ࡫࡯ࡱࡺࡲࡤ࡭ࡲࡪࡦࠪቖ")
def bstack11l1lll1ll_opy_(driver):
    info = {
        bstack111lll1_opy_ (u"ࠬࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ቗"): driver.capabilities,
        bstack111lll1_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠪቘ"): driver.session_id,
        bstack111lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨ቙"): driver.capabilities.get(bstack111lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ቚ"), None),
        bstack111lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫቛ"): driver.capabilities.get(bstack111lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫቜ"), None),
        bstack111lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࠭ቝ"): driver.capabilities.get(bstack111lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠫ቞"), None),
    }
    if bstack11l1ll111l_opy_() == bstack111lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ቟"):
        info[bstack111lll1_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࠨበ")] = bstack111lll1_opy_ (u"ࠨࡣࡳࡴ࠲ࡧࡵࡵࡱࡰࡥࡹ࡫ࠧቡ") if bstack1ll1l1l1l_opy_() else bstack111lll1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫቢ")
    return info
def bstack1ll1l1l1l_opy_():
    if bstack11l11l111_opy_.get_property(bstack111lll1_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠩባ")):
        return True
    if bstack1lllll111l_opy_(os.environ.get(bstack111lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬቤ"), None)):
        return True
    return False
def bstack1l1111111_opy_(bstack11ll1111ll_opy_, url, data, config):
    headers = config.get(bstack111lll1_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭ብ"), None)
    proxies = bstack1l1l11llll_opy_(config, url)
    auth = config.get(bstack111lll1_opy_ (u"࠭ࡡࡶࡶ࡫ࠫቦ"), None)
    response = requests.request(
            bstack11ll1111ll_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1llll1ll1_opy_(bstack1l1llll1_opy_, size):
    bstack1lll1l11l1_opy_ = []
    while len(bstack1l1llll1_opy_) > size:
        bstack11lll11l1_opy_ = bstack1l1llll1_opy_[:size]
        bstack1lll1l11l1_opy_.append(bstack11lll11l1_opy_)
        bstack1l1llll1_opy_ = bstack1l1llll1_opy_[size:]
    bstack1lll1l11l1_opy_.append(bstack1l1llll1_opy_)
    return bstack1lll1l11l1_opy_
def bstack11l11l111l_opy_(message, bstack11l1lll111_opy_=False):
    os.write(1, bytes(message, bstack111lll1_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ቧ")))
    os.write(1, bytes(bstack111lll1_opy_ (u"ࠨ࡞ࡱࠫቨ"), bstack111lll1_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨቩ")))
    if bstack11l1lll111_opy_:
        with open(bstack111lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠰ࡳ࠶࠷ࡹ࠮ࠩቪ") + os.environ[bstack111lll1_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆࠪቫ")] + bstack111lll1_opy_ (u"ࠬ࠴࡬ࡰࡩࠪቬ"), bstack111lll1_opy_ (u"࠭ࡡࠨቭ")) as f:
            f.write(message + bstack111lll1_opy_ (u"ࠧ࡝ࡰࠪቮ"))
def bstack11l1l11l1l_opy_():
    return os.environ[bstack111lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫቯ")].lower() == bstack111lll1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧተ")
def bstack11ll111l_opy_(bstack11l1ll11ll_opy_):
    return bstack111lll1_opy_ (u"ࠪࡿࢂ࠵ࡻࡾࠩቱ").format(bstack11ll11l1l1_opy_, bstack11l1ll11ll_opy_)
def bstack1ll1l11lll_opy_():
    return datetime.datetime.utcnow().isoformat() + bstack111lll1_opy_ (u"ࠫ࡟࠭ቲ")
def bstack11l1lllll1_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack111lll1_opy_ (u"ࠬࡠࠧታ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack111lll1_opy_ (u"࡚࠭ࠨቴ")))).total_seconds() * 1000
def bstack11ll1111l1_opy_(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp).isoformat() + bstack111lll1_opy_ (u"࡛ࠧࠩት")
def bstack11l1l1l1ll_opy_(bstack11ll11111l_opy_):
    date_format = bstack111lll1_opy_ (u"ࠨࠧ࡜ࠩࡲࠫࡤࠡࠧࡋ࠾ࠪࡓ࠺ࠦࡕ࠱ࠩ࡫࠭ቶ")
    bstack11l1lll11l_opy_ = datetime.datetime.strptime(bstack11ll11111l_opy_, date_format)
    return bstack11l1lll11l_opy_.isoformat() + bstack111lll1_opy_ (u"ࠩ࡝ࠫቷ")
def bstack11l1ll1l1l_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack111lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪቸ")
    else:
        return bstack111lll1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫቹ")
def bstack1lllll111l_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack111lll1_opy_ (u"ࠬࡺࡲࡶࡧࠪቺ")
def bstack11l1l11lll_opy_(val):
    return val.__str__().lower() == bstack111lll1_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬቻ")
def bstack1l11ll1ll1_opy_(bstack11l11l1l11_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack11l11l1l11_opy_ as e:
                print(bstack111lll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡽࢀࠤ࠲ࡄࠠࡼࡿ࠽ࠤࢀࢃࠢቼ").format(func.__name__, bstack11l11l1l11_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack11l1l1lll1_opy_(bstack11l1l1111l_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack11l1l1111l_opy_(cls, *args, **kwargs)
            except bstack11l11l1l11_opy_ as e:
                print(bstack111lll1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࡾࢁࠥ࠳࠾ࠡࡽࢀ࠾ࠥࢁࡽࠣች").format(bstack11l1l1111l_opy_.__name__, bstack11l11l1l11_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack11l1l1lll1_opy_
    else:
        return decorator
def bstack1ll1l1l1l1_opy_(bstack11llll11ll_opy_):
    if bstack111lll1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ቾ") in bstack11llll11ll_opy_ and bstack11l1l11lll_opy_(bstack11llll11ll_opy_[bstack111lll1_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧቿ")]):
        return False
    if bstack111lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ኀ") in bstack11llll11ll_opy_ and bstack11l1l11lll_opy_(bstack11llll11ll_opy_[bstack111lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠧኁ")]):
        return False
    return True
def bstack1l1111ll1_opy_():
    try:
        from pytest_bdd import reporting
        return True
    except Exception as e:
        return False
def bstack11111lll1_opy_(hub_url):
    if bstack1lll1l11l_opy_() <= version.parse(bstack111lll1_opy_ (u"࠭࠳࠯࠳࠶࠲࠵࠭ኂ")):
        if hub_url != bstack111lll1_opy_ (u"ࠧࠨኃ"):
            return bstack111lll1_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤኄ") + hub_url + bstack111lll1_opy_ (u"ࠤ࠽࠼࠵࠵ࡷࡥ࠱࡫ࡹࡧࠨኅ")
        return bstack1ll11111l1_opy_
    if hub_url != bstack111lll1_opy_ (u"ࠪࠫኆ"):
        return bstack111lll1_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨኇ") + hub_url + bstack111lll1_opy_ (u"ࠧ࠵ࡷࡥ࠱࡫ࡹࡧࠨኈ")
    return bstack111llll1l_opy_
def bstack11l1l1ll1l_opy_():
    return isinstance(os.getenv(bstack111lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖ࡙ࡕࡇࡖࡘࡤࡖࡌࡖࡉࡌࡒࠬ኉")), str)
def bstack1l1l1111l_opy_(url):
    return urlparse(url).hostname
def bstack1ll11l111_opy_(hostname):
    for bstack111l1lll_opy_ in bstack11l11ll1l_opy_:
        regex = re.compile(bstack111l1lll_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack11l11lll1l_opy_(bstack11l1l111l1_opy_, file_name, logger):
    bstack1ll11llll_opy_ = os.path.join(os.path.expanduser(bstack111lll1_opy_ (u"ࠧࡿࠩኊ")), bstack11l1l111l1_opy_)
    try:
        if not os.path.exists(bstack1ll11llll_opy_):
            os.makedirs(bstack1ll11llll_opy_)
        file_path = os.path.join(os.path.expanduser(bstack111lll1_opy_ (u"ࠨࢀࠪኋ")), bstack11l1l111l1_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack111lll1_opy_ (u"ࠩࡺࠫኌ")):
                pass
            with open(file_path, bstack111lll1_opy_ (u"ࠥࡻ࠰ࠨኍ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1111l111l_opy_.format(str(e)))
def bstack11l1llll11_opy_(file_name, key, value, logger):
    file_path = bstack11l11lll1l_opy_(bstack111lll1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ኎"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack111llllll_opy_ = json.load(open(file_path, bstack111lll1_opy_ (u"ࠬࡸࡢࠨ኏")))
        else:
            bstack111llllll_opy_ = {}
        bstack111llllll_opy_[key] = value
        with open(file_path, bstack111lll1_opy_ (u"ࠨࡷࠬࠤነ")) as outfile:
            json.dump(bstack111llllll_opy_, outfile)
def bstack1llll111_opy_(file_name, logger):
    file_path = bstack11l11lll1l_opy_(bstack111lll1_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧኑ"), file_name, logger)
    bstack111llllll_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack111lll1_opy_ (u"ࠨࡴࠪኒ")) as bstack1l1lllllll_opy_:
            bstack111llllll_opy_ = json.load(bstack1l1lllllll_opy_)
    return bstack111llllll_opy_
def bstack111lllll1_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack111lll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡩ࡫࡬ࡦࡶ࡬ࡲ࡬ࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ና") + file_path + bstack111lll1_opy_ (u"ࠪࠤࠬኔ") + str(e))
def bstack1lll1l11l_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack111lll1_opy_ (u"ࠦࡁࡔࡏࡕࡕࡈࡘࡃࠨን")
def bstack1llll1l1ll_opy_(config):
    if bstack111lll1_opy_ (u"ࠬ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫኖ") in config:
        del (config[bstack111lll1_opy_ (u"࠭ࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬኗ")])
        return False
    if bstack1lll1l11l_opy_() < version.parse(bstack111lll1_opy_ (u"ࠧ࠴࠰࠷࠲࠵࠭ኘ")):
        return False
    if bstack1lll1l11l_opy_() >= version.parse(bstack111lll1_opy_ (u"ࠨ࠶࠱࠵࠳࠻ࠧኙ")):
        return True
    if bstack111lll1_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩኚ") in config and config[bstack111lll1_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪኛ")] is False:
        return False
    else:
        return True
def bstack1l1llllll1_opy_(args_list, bstack11l1lll1l1_opy_):
    index = -1
    for value in bstack11l1lll1l1_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1l11ll1l1l_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1l11ll1l1l_opy_ = bstack1l11ll1l1l_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack111lll1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫኜ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack111lll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬኝ"), exception=exception)
    def bstack11lll1l1ll_opy_(self):
        if self.result != bstack111lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ኞ"):
            return None
        if bstack111lll1_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥኟ") in self.exception_type:
            return bstack111lll1_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤአ")
        return bstack111lll1_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥኡ")
    def bstack11l11l1ll1_opy_(self):
        if self.result != bstack111lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪኢ"):
            return None
        if self.bstack1l11ll1l1l_opy_:
            return self.bstack1l11ll1l1l_opy_
        return bstack11l1llll1l_opy_(self.exception)
def bstack11l1llll1l_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack11l1ll1l11_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1ll1111111_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack1ll11111ll_opy_(config, logger):
    try:
        import playwright
        bstack11l11ll1ll_opy_ = playwright.__file__
        bstack11l1l11111_opy_ = os.path.split(bstack11l11ll1ll_opy_)
        bstack11l1l1llll_opy_ = bstack11l1l11111_opy_[0] + bstack111lll1_opy_ (u"ࠫ࠴ࡪࡲࡪࡸࡨࡶ࠴ࡶࡡࡤ࡭ࡤ࡫ࡪ࠵࡬ࡪࡤ࠲ࡧࡱ࡯࠯ࡤ࡮࡬࠲࡯ࡹࠧኣ")
        os.environ[bstack111lll1_opy_ (u"ࠬࡍࡌࡐࡄࡄࡐࡤࡇࡇࡆࡐࡗࡣࡍ࡚ࡔࡑࡡࡓࡖࡔ࡞࡙ࠨኤ")] = bstack1l1lll11l_opy_(config)
        with open(bstack11l1l1llll_opy_, bstack111lll1_opy_ (u"࠭ࡲࠨእ")) as f:
            bstack111ll111_opy_ = f.read()
            bstack11l11ll11l_opy_ = bstack111lll1_opy_ (u"ࠧࡨ࡮ࡲࡦࡦࡲ࠭ࡢࡩࡨࡲࡹ࠭ኦ")
            bstack11l11lllll_opy_ = bstack111ll111_opy_.find(bstack11l11ll11l_opy_)
            if bstack11l11lllll_opy_ == -1:
              process = subprocess.Popen(bstack111lll1_opy_ (u"ࠣࡰࡳࡱࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡧ࡭ࡱࡥࡥࡱ࠳ࡡࡨࡧࡱࡸࠧኧ"), shell=True, cwd=bstack11l1l11111_opy_[0])
              process.wait()
              bstack11l1l1l11l_opy_ = bstack111lll1_opy_ (u"ࠩࠥࡹࡸ࡫ࠠࡴࡶࡵ࡭ࡨࡺࠢ࠼ࠩከ")
              bstack11l11l1l1l_opy_ = bstack111lll1_opy_ (u"ࠥࠦࠧࠦ࡜ࠣࡷࡶࡩࠥࡹࡴࡳ࡫ࡦࡸࡡࠨ࠻ࠡࡥࡲࡲࡸࡺࠠࡼࠢࡥࡳࡴࡺࡳࡵࡴࡤࡴࠥࢃࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࠫ࡬ࡲ࡯ࡣࡣ࡯࠱ࡦ࡭ࡥ࡯ࡶࠪ࠭ࡀࠦࡩࡧࠢࠫࡴࡷࡵࡣࡦࡵࡶ࠲ࡪࡴࡶ࠯ࡉࡏࡓࡇࡇࡌࡠࡃࡊࡉࡓ࡚࡟ࡉࡖࡗࡔࡤࡖࡒࡐ࡚࡜࠭ࠥࡨ࡯ࡰࡶࡶࡸࡷࡧࡰࠩࠫ࠾ࠤࠧࠨࠢኩ")
              bstack11l1l1l1l1_opy_ = bstack111ll111_opy_.replace(bstack11l1l1l11l_opy_, bstack11l11l1l1l_opy_)
              with open(bstack11l1l1llll_opy_, bstack111lll1_opy_ (u"ࠫࡼ࠭ኪ")) as f:
                f.write(bstack11l1l1l1l1_opy_)
    except Exception as e:
        logger.error(bstack11l1l1ll_opy_.format(str(e)))
def bstack1l1l111lll_opy_():
  try:
    bstack11l1l11ll1_opy_ = os.path.join(tempfile.gettempdir(), bstack111lll1_opy_ (u"ࠬࡵࡰࡵ࡫ࡰࡥࡱࡥࡨࡶࡤࡢࡹࡷࡲ࠮࡫ࡵࡲࡲࠬካ"))
    bstack11l11llll1_opy_ = []
    if os.path.exists(bstack11l1l11ll1_opy_):
      with open(bstack11l1l11ll1_opy_) as f:
        bstack11l11llll1_opy_ = json.load(f)
      os.remove(bstack11l1l11ll1_opy_)
    return bstack11l11llll1_opy_
  except:
    pass
  return []
def bstack1l1l1llll_opy_(bstack1l1l11ll1_opy_):
  try:
    bstack11l11llll1_opy_ = []
    bstack11l1l11ll1_opy_ = os.path.join(tempfile.gettempdir(), bstack111lll1_opy_ (u"࠭࡯ࡱࡶ࡬ࡱࡦࡲ࡟ࡩࡷࡥࡣࡺࡸ࡬࠯࡬ࡶࡳࡳ࠭ኬ"))
    if os.path.exists(bstack11l1l11ll1_opy_):
      with open(bstack11l1l11ll1_opy_) as f:
        bstack11l11llll1_opy_ = json.load(f)
    bstack11l11llll1_opy_.append(bstack1l1l11ll1_opy_)
    with open(bstack11l1l11ll1_opy_, bstack111lll1_opy_ (u"ࠧࡸࠩክ")) as f:
        json.dump(bstack11l11llll1_opy_, f)
  except:
    pass
def bstack1l1llllll_opy_(logger, bstack11l1ll11l1_opy_ = False):
  try:
    test_name = os.environ.get(bstack111lll1_opy_ (u"ࠨࡒ࡜ࡘࡊ࡙ࡔࡠࡖࡈࡗ࡙ࡥࡎࡂࡏࡈࠫኮ"), bstack111lll1_opy_ (u"ࠩࠪኯ"))
    if test_name == bstack111lll1_opy_ (u"ࠪࠫኰ"):
        test_name = threading.current_thread().__dict__.get(bstack111lll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡆࡩࡪ࡟ࡵࡧࡶࡸࡤࡴࡡ࡮ࡧࠪ኱"), bstack111lll1_opy_ (u"ࠬ࠭ኲ"))
    bstack11l11ll1l1_opy_ = bstack111lll1_opy_ (u"࠭ࠬࠡࠩኳ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack11l1ll11l1_opy_:
        bstack11l1l1111_opy_ = os.environ.get(bstack111lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧኴ"), bstack111lll1_opy_ (u"ࠨ࠲ࠪኵ"))
        bstack1llll1lll1_opy_ = {bstack111lll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ኶"): test_name, bstack111lll1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ኷"): bstack11l11ll1l1_opy_, bstack111lll1_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪኸ"): bstack11l1l1111_opy_}
        bstack11l1ll1111_opy_ = []
        bstack11l11l11l1_opy_ = os.path.join(tempfile.gettempdir(), bstack111lll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡶࡰࡱࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫኹ"))
        if os.path.exists(bstack11l11l11l1_opy_):
            with open(bstack11l11l11l1_opy_) as f:
                bstack11l1ll1111_opy_ = json.load(f)
        bstack11l1ll1111_opy_.append(bstack1llll1lll1_opy_)
        with open(bstack11l11l11l1_opy_, bstack111lll1_opy_ (u"࠭ࡷࠨኺ")) as f:
            json.dump(bstack11l1ll1111_opy_, f)
    else:
        bstack1llll1lll1_opy_ = {bstack111lll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬኻ"): test_name, bstack111lll1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧኼ"): bstack11l11ll1l1_opy_, bstack111lll1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨኽ"): str(multiprocessing.current_process().name)}
        if bstack111lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺࠧኾ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack1llll1lll1_opy_)
  except Exception as e:
      logger.warn(bstack111lll1_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡲࡶࡪࠦࡰࡺࡶࡨࡷࡹࠦࡦࡶࡰࡱࡩࡱࠦࡤࡢࡶࡤ࠾ࠥࢁࡽࠣ኿").format(e))
def bstack1l1lllll1l_opy_(error_message, test_name, index, logger):
  try:
    bstack11l1ll1ll1_opy_ = []
    bstack1llll1lll1_opy_ = {bstack111lll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪዀ"): test_name, bstack111lll1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ዁"): error_message, bstack111lll1_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ዂ"): index}
    bstack11l1ll1lll_opy_ = os.path.join(tempfile.gettempdir(), bstack111lll1_opy_ (u"ࠨࡴࡲࡦࡴࡺ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩዃ"))
    if os.path.exists(bstack11l1ll1lll_opy_):
        with open(bstack11l1ll1lll_opy_) as f:
            bstack11l1ll1ll1_opy_ = json.load(f)
    bstack11l1ll1ll1_opy_.append(bstack1llll1lll1_opy_)
    with open(bstack11l1ll1lll_opy_, bstack111lll1_opy_ (u"ࠩࡺࠫዄ")) as f:
        json.dump(bstack11l1ll1ll1_opy_, f)
  except Exception as e:
    logger.warn(bstack111lll1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡱࡵࡩࠥࡸ࡯ࡣࡱࡷࠤ࡫ࡻ࡮࡯ࡧ࡯ࠤࡩࡧࡴࡢ࠼ࠣࡿࢂࠨዅ").format(e))
def bstack1l11111ll_opy_(bstack1l1l1111_opy_, name, logger):
  try:
    bstack1llll1lll1_opy_ = {bstack111lll1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ዆"): name, bstack111lll1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ዇"): bstack1l1l1111_opy_, bstack111lll1_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬወ"): str(threading.current_thread()._name)}
    return bstack1llll1lll1_opy_
  except Exception as e:
    logger.warn(bstack111lll1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡵࡲࡦࠢࡥࡩ࡭ࡧࡶࡦࠢࡩࡹࡳࡴࡥ࡭ࠢࡧࡥࡹࡧ࠺ࠡࡽࢀࠦዉ").format(e))
  return
def bstack11l11ll111_opy_():
    return platform.system() == bstack111lll1_opy_ (u"ࠨ࡙࡬ࡲࡩࡵࡷࡴࠩዊ")