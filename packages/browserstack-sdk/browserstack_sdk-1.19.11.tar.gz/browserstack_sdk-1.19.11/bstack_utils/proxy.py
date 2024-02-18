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
from urllib.parse import urlparse
from bstack_utils.messages import bstack11l111111l_opy_
def bstack1111ll1l11_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack1111ll111l_opy_(bstack1111ll11ll_opy_, bstack1111ll1ll1_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack1111ll11ll_opy_):
        with open(bstack1111ll11ll_opy_) as f:
            pac = PACFile(f.read())
    elif bstack1111ll1l11_opy_(bstack1111ll11ll_opy_):
        pac = get_pac(url=bstack1111ll11ll_opy_)
    else:
        raise Exception(bstack111lll1_opy_ (u"ࠫࡕࡧࡣࠡࡨ࡬ࡰࡪࠦࡤࡰࡧࡶࠤࡳࡵࡴࠡࡧࡻ࡭ࡸࡺ࠺ࠡࡽࢀࠫ᎘").format(bstack1111ll11ll_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack111lll1_opy_ (u"ࠧ࠾࠮࠹࠰࠻࠲࠽ࠨ᎙"), 80))
        bstack1111ll11l1_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack1111ll11l1_opy_ = bstack111lll1_opy_ (u"࠭࠰࠯࠲࠱࠴࠳࠶ࠧ᎚")
    proxy_url = session.get_pac().find_proxy_for_url(bstack1111ll1ll1_opy_, bstack1111ll11l1_opy_)
    return proxy_url
def bstack11llllll_opy_(config):
    return bstack111lll1_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪ᎛") in config or bstack111lll1_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ᎜") in config
def bstack1l1lll11l_opy_(config):
    if not bstack11llllll_opy_(config):
        return
    if config.get(bstack111lll1_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬ᎝")):
        return config.get(bstack111lll1_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭᎞"))
    if config.get(bstack111lll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨ᎟")):
        return config.get(bstack111lll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩᎠ"))
def bstack1l1l11llll_opy_(config, bstack1111ll1ll1_opy_):
    proxy = bstack1l1lll11l_opy_(config)
    proxies = {}
    if config.get(bstack111lll1_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩᎡ")) or config.get(bstack111lll1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫᎢ")):
        if proxy.endswith(bstack111lll1_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭Ꭳ")):
            proxies = bstack1llll1l11_opy_(proxy, bstack1111ll1ll1_opy_)
        else:
            proxies = {
                bstack111lll1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨᎤ"): proxy
            }
    return proxies
def bstack1llll1l11_opy_(bstack1111ll11ll_opy_, bstack1111ll1ll1_opy_):
    proxies = {}
    global bstack1111ll1l1l_opy_
    if bstack111lll1_opy_ (u"ࠪࡔࡆࡉ࡟ࡑࡔࡒ࡜࡞࠭Ꭵ") in globals():
        return bstack1111ll1l1l_opy_
    try:
        proxy = bstack1111ll111l_opy_(bstack1111ll11ll_opy_, bstack1111ll1ll1_opy_)
        if bstack111lll1_opy_ (u"ࠦࡉࡏࡒࡆࡅࡗࠦᎦ") in proxy:
            proxies = {}
        elif bstack111lll1_opy_ (u"ࠧࡎࡔࡕࡒࠥᎧ") in proxy or bstack111lll1_opy_ (u"ࠨࡈࡕࡖࡓࡗࠧᎨ") in proxy or bstack111lll1_opy_ (u"ࠢࡔࡑࡆࡏࡘࠨᎩ") in proxy:
            bstack1111ll1lll_opy_ = proxy.split(bstack111lll1_opy_ (u"ࠣࠢࠥᎪ"))
            if bstack111lll1_opy_ (u"ࠤ࠽࠳࠴ࠨᎫ") in bstack111lll1_opy_ (u"ࠥࠦᎬ").join(bstack1111ll1lll_opy_[1:]):
                proxies = {
                    bstack111lll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪᎭ"): bstack111lll1_opy_ (u"ࠧࠨᎮ").join(bstack1111ll1lll_opy_[1:])
                }
            else:
                proxies = {
                    bstack111lll1_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬᎯ"): str(bstack1111ll1lll_opy_[0]).lower() + bstack111lll1_opy_ (u"ࠢ࠻࠱࠲ࠦᎰ") + bstack111lll1_opy_ (u"ࠣࠤᎱ").join(bstack1111ll1lll_opy_[1:])
                }
        elif bstack111lll1_opy_ (u"ࠤࡓࡖࡔ࡞࡙ࠣᎲ") in proxy:
            bstack1111ll1lll_opy_ = proxy.split(bstack111lll1_opy_ (u"ࠥࠤࠧᎳ"))
            if bstack111lll1_opy_ (u"ࠦ࠿࠵࠯ࠣᎴ") in bstack111lll1_opy_ (u"ࠧࠨᎵ").join(bstack1111ll1lll_opy_[1:]):
                proxies = {
                    bstack111lll1_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬᎶ"): bstack111lll1_opy_ (u"ࠢࠣᎷ").join(bstack1111ll1lll_opy_[1:])
                }
            else:
                proxies = {
                    bstack111lll1_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧᎸ"): bstack111lll1_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥᎹ") + bstack111lll1_opy_ (u"ࠥࠦᎺ").join(bstack1111ll1lll_opy_[1:])
                }
        else:
            proxies = {
                bstack111lll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪᎻ"): proxy
            }
    except Exception as e:
        print(bstack111lll1_opy_ (u"ࠧࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠤᎼ"), bstack11l111111l_opy_.format(bstack1111ll11ll_opy_, str(e)))
    bstack1111ll1l1l_opy_ = proxies
    return proxies