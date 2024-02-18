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
from uuid import uuid4
from bstack_utils.helper import bstack1ll1l11lll_opy_, bstack11l1lllll1_opy_
from bstack_utils.bstack11l1lll11_opy_ import bstack1111l1l1ll_opy_
class bstack1l11lll11l_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, bstack1l111l1l1l_opy_=None, framework=None, tags=[], scope=[], bstack1llllllll11_opy_=None, bstack1111111l1l_opy_=True, bstack1111111lll_opy_=None, bstack1ll11ll11_opy_=None, result=None, duration=None, bstack1l11l11l11_opy_=None, meta={}):
        self.bstack1l11l11l11_opy_ = bstack1l11l11l11_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack1111111l1l_opy_:
            self.uuid = uuid4().__str__()
        self.bstack1l111l1l1l_opy_ = bstack1l111l1l1l_opy_
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack1llllllll11_opy_ = bstack1llllllll11_opy_
        self.bstack1111111lll_opy_ = bstack1111111lll_opy_
        self.bstack1ll11ll11_opy_ = bstack1ll11ll11_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
    def bstack1l111l1111_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack1llllllll1l_opy_(self):
        bstack111111ll1l_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack111lll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩᐦ"): bstack111111ll1l_opy_,
            bstack111lll1_opy_ (u"ࠧ࡭ࡱࡦࡥࡹ࡯࡯࡯ࠩᐧ"): bstack111111ll1l_opy_,
            bstack111lll1_opy_ (u"ࠨࡸࡦࡣ࡫࡯࡬ࡦࡲࡤࡸ࡭࠭ᐨ"): bstack111111ll1l_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack111lll1_opy_ (u"ࠤࡘࡲࡪࡾࡰࡦࡥࡷࡩࡩࠦࡡࡳࡩࡸࡱࡪࡴࡴ࠻ࠢࠥᐩ") + key)
            setattr(self, key, val)
    def bstack1111111ll1_opy_(self):
        return {
            bstack111lll1_opy_ (u"ࠪࡲࡦࡳࡥࠨᐪ"): self.name,
            bstack111lll1_opy_ (u"ࠫࡧࡵࡤࡺࠩᐫ"): {
                bstack111lll1_opy_ (u"ࠬࡲࡡ࡯ࡩࠪᐬ"): bstack111lll1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ᐭ"),
                bstack111lll1_opy_ (u"ࠧࡤࡱࡧࡩࠬᐮ"): self.code
            },
            bstack111lll1_opy_ (u"ࠨࡵࡦࡳࡵ࡫ࡳࠨᐯ"): self.scope,
            bstack111lll1_opy_ (u"ࠩࡷࡥ࡬ࡹࠧᐰ"): self.tags,
            bstack111lll1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ᐱ"): self.framework,
            bstack111lll1_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᐲ"): self.bstack1l111l1l1l_opy_
        }
    def bstack11111111ll_opy_(self):
        return {
         bstack111lll1_opy_ (u"ࠬࡳࡥࡵࡣࠪᐳ"): self.meta
        }
    def bstack111111111l_opy_(self):
        return {
            bstack111lll1_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡘࡥࡳࡷࡱࡔࡦࡸࡡ࡮ࠩᐴ"): {
                bstack111lll1_opy_ (u"ࠧࡳࡧࡵࡹࡳࡥ࡮ࡢ࡯ࡨࠫᐵ"): self.bstack1llllllll11_opy_
            }
        }
    def bstack1lllllllll1_opy_(self, bstack1111111111_opy_, details):
        step = next(filter(lambda st: st[bstack111lll1_opy_ (u"ࠨ࡫ࡧࠫᐶ")] == bstack1111111111_opy_, self.meta[bstack111lll1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᐷ")]), None)
        step.update(details)
    def bstack111111l1l1_opy_(self, bstack1111111111_opy_):
        step = next(filter(lambda st: st[bstack111lll1_opy_ (u"ࠪ࡭ࡩ࠭ᐸ")] == bstack1111111111_opy_, self.meta[bstack111lll1_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪᐹ")]), None)
        step.update({
            bstack111lll1_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᐺ"): bstack1ll1l11lll_opy_()
        })
    def bstack1l1111llll_opy_(self, bstack1111111111_opy_, result, duration=None):
        bstack1111111lll_opy_ = bstack1ll1l11lll_opy_()
        if bstack1111111111_opy_ is not None and self.meta.get(bstack111lll1_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬᐻ")):
            step = next(filter(lambda st: st[bstack111lll1_opy_ (u"ࠧࡪࡦࠪᐼ")] == bstack1111111111_opy_, self.meta[bstack111lll1_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧᐽ")]), None)
            step.update({
                bstack111lll1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᐾ"): bstack1111111lll_opy_,
                bstack111lll1_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬᐿ"): duration if duration else bstack11l1lllll1_opy_(step[bstack111lll1_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᑀ")], bstack1111111lll_opy_),
                bstack111lll1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᑁ"): result.result,
                bstack111lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧᑂ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack111111ll11_opy_):
        if self.meta.get(bstack111lll1_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ᑃ")):
            self.meta[bstack111lll1_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧᑄ")].append(bstack111111ll11_opy_)
        else:
            self.meta[bstack111lll1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᑅ")] = [ bstack111111ll11_opy_ ]
    def bstack111111l111_opy_(self):
        return {
            bstack111lll1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᑆ"): self.bstack1l111l1111_opy_(),
            **self.bstack1111111ll1_opy_(),
            **self.bstack1llllllll1l_opy_(),
            **self.bstack11111111ll_opy_()
        }
    def bstack1111111l11_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack111lll1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᑇ"): self.bstack1111111lll_opy_,
            bstack111lll1_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭ᑈ"): self.duration,
            bstack111lll1_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᑉ"): self.result.result
        }
        if data[bstack111lll1_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᑊ")] == bstack111lll1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᑋ"):
            data[bstack111lll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨᑌ")] = self.result.bstack11lll1l1ll_opy_()
            data[bstack111lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫᑍ")] = [{bstack111lll1_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧᑎ"): self.result.bstack11l11l1ll1_opy_()}]
        return data
    def bstack111111l11l_opy_(self):
        return {
            bstack111lll1_opy_ (u"ࠬࡻࡵࡪࡦࠪᑏ"): self.bstack1l111l1111_opy_(),
            **self.bstack1111111ll1_opy_(),
            **self.bstack1llllllll1l_opy_(),
            **self.bstack1111111l11_opy_(),
            **self.bstack11111111ll_opy_()
        }
    def bstack1l11l1l1ll_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack111lll1_opy_ (u"࠭ࡓࡵࡣࡵࡸࡪࡪࠧᑐ") in event:
            return self.bstack111111l111_opy_()
        elif bstack111lll1_opy_ (u"ࠧࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩᑑ") in event:
            return self.bstack111111l11l_opy_()
    def bstack1l11l1ll1l_opy_(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1111111lll_opy_ = time if time else bstack1ll1l11lll_opy_()
        self.duration = duration if duration else bstack11l1lllll1_opy_(self.bstack1l111l1l1l_opy_, self.bstack1111111lll_opy_)
        if result:
            self.result = result
class bstack1l11lll1ll_opy_(bstack1l11lll11l_opy_):
    def __init__(self, hooks=[], bstack1l111ll1ll_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1l111ll1ll_opy_ = bstack1l111ll1ll_opy_
        super().__init__(*args, **kwargs, bstack1ll11ll11_opy_=bstack111lll1_opy_ (u"ࠨࡶࡨࡷࡹ࠭ᑒ"))
    @classmethod
    def bstack11111111l1_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack111lll1_opy_ (u"ࠩ࡬ࡨࠬᑓ"): id(step),
                bstack111lll1_opy_ (u"ࠪࡸࡪࡾࡴࠨᑔ"): step.name,
                bstack111lll1_opy_ (u"ࠫࡰ࡫ࡹࡸࡱࡵࡨࠬᑕ"): step.keyword,
            })
        return bstack1l11lll1ll_opy_(
            **kwargs,
            meta={
                bstack111lll1_opy_ (u"ࠬ࡬ࡥࡢࡶࡸࡶࡪ࠭ᑖ"): {
                    bstack111lll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᑗ"): feature.name,
                    bstack111lll1_opy_ (u"ࠧࡱࡣࡷ࡬ࠬᑘ"): feature.filename,
                    bstack111lll1_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭ᑙ"): feature.description
                },
                bstack111lll1_opy_ (u"ࠩࡶࡧࡪࡴࡡࡳ࡫ࡲࠫᑚ"): {
                    bstack111lll1_opy_ (u"ࠪࡲࡦࡳࡥࠨᑛ"): scenario.name
                },
                bstack111lll1_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪᑜ"): steps,
                bstack111lll1_opy_ (u"ࠬ࡫ࡸࡢ࡯ࡳࡰࡪࡹࠧᑝ"): bstack1111l1l1ll_opy_(test)
            }
        )
    def bstack1llllllllll_opy_(self):
        return {
            bstack111lll1_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᑞ"): self.hooks
        }
    def bstack111111lll1_opy_(self):
        if self.bstack1l111ll1ll_opy_:
            return {
                bstack111lll1_opy_ (u"ࠧࡪࡰࡷࡩ࡬ࡸࡡࡵ࡫ࡲࡲࡸ࠭ᑟ"): self.bstack1l111ll1ll_opy_
            }
        return {}
    def bstack111111l11l_opy_(self):
        return {
            **super().bstack111111l11l_opy_(),
            **self.bstack1llllllllll_opy_()
        }
    def bstack111111l111_opy_(self):
        return {
            **super().bstack111111l111_opy_(),
            **self.bstack111111lll1_opy_()
        }
    def bstack1l11l1ll1l_opy_(self):
        return bstack111lll1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪᑠ")
class bstack1l1111ll11_opy_(bstack1l11lll11l_opy_):
    def __init__(self, hook_type, *args, **kwargs):
        self.hook_type = hook_type
        super().__init__(*args, **kwargs, bstack1ll11ll11_opy_=bstack111lll1_opy_ (u"ࠩ࡫ࡳࡴࡱࠧᑡ"))
    def bstack1l11111111_opy_(self):
        return self.hook_type
    def bstack111111l1ll_opy_(self):
        return {
            bstack111lll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭ᑢ"): self.hook_type
        }
    def bstack111111l11l_opy_(self):
        return {
            **super().bstack111111l11l_opy_(),
            **self.bstack111111l1ll_opy_()
        }
    def bstack111111l111_opy_(self):
        return {
            **super().bstack111111l111_opy_(),
            **self.bstack111111l1ll_opy_()
        }
    def bstack1l11l1ll1l_opy_(self):
        return bstack111lll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳ࠭ᑣ")