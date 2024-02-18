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
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result
def _11l11l1111_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack11l111l1l1_opy_:
    def __init__(self, handler):
        self._11l111lll1_opy_ = {}
        self._11l1111ll1_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        self._11l111lll1_opy_[bstack111lll1_opy_ (u"ࠩࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬዋ")] = Module._inject_setup_function_fixture
        self._11l111lll1_opy_[bstack111lll1_opy_ (u"ࠪࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫዌ")] = Module._inject_setup_module_fixture
        self._11l111lll1_opy_[bstack111lll1_opy_ (u"ࠫࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠫው")] = Class._inject_setup_class_fixture
        self._11l111lll1_opy_[bstack111lll1_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ዎ")] = Class._inject_setup_method_fixture
        Module._inject_setup_function_fixture = self.bstack11l111l111_opy_(bstack111lll1_opy_ (u"࠭ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩዏ"))
        Module._inject_setup_module_fixture = self.bstack11l111l111_opy_(bstack111lll1_opy_ (u"ࠧ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨዐ"))
        Class._inject_setup_class_fixture = self.bstack11l111l111_opy_(bstack111lll1_opy_ (u"ࠨࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨዑ"))
        Class._inject_setup_method_fixture = self.bstack11l111l111_opy_(bstack111lll1_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠪዒ"))
    def bstack11l111l11l_opy_(self, bstack11l111ll1l_opy_, hook_type):
        meth = getattr(bstack11l111ll1l_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._11l1111ll1_opy_[hook_type] = meth
            setattr(bstack11l111ll1l_opy_, hook_type, self.bstack11l1111l1l_opy_(hook_type))
    def bstack11l111llll_opy_(self, instance, bstack11l1111l11_opy_):
        if bstack11l1111l11_opy_ == bstack111lll1_opy_ (u"ࠥࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪࠨዓ"):
            self.bstack11l111l11l_opy_(instance.obj, bstack111lll1_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠧዔ"))
            self.bstack11l111l11l_opy_(instance.obj, bstack111lll1_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠤዕ"))
        if bstack11l1111l11_opy_ == bstack111lll1_opy_ (u"ࠨ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠢዖ"):
            self.bstack11l111l11l_opy_(instance.obj, bstack111lll1_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪࠨ዗"))
            self.bstack11l111l11l_opy_(instance.obj, bstack111lll1_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠥዘ"))
        if bstack11l1111l11_opy_ == bstack111lll1_opy_ (u"ࠤࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠤዙ"):
            self.bstack11l111l11l_opy_(instance.obj, bstack111lll1_opy_ (u"ࠥࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠣዚ"))
            self.bstack11l111l11l_opy_(instance.obj, bstack111lll1_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠧዛ"))
        if bstack11l1111l11_opy_ == bstack111lll1_opy_ (u"ࠧࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪࠨዜ"):
            self.bstack11l111l11l_opy_(instance.obj, bstack111lll1_opy_ (u"ࠨࡳࡦࡶࡸࡴࡤࡳࡥࡵࡪࡲࡨࠧዝ"))
            self.bstack11l111l11l_opy_(instance.obj, bstack111lll1_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠤዞ"))
    @staticmethod
    def bstack11l11111ll_opy_(hook_type, func, args):
        if hook_type in [bstack111lll1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧዟ"), bstack111lll1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠫዠ")]:
            _11l11l1111_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack11l1111l1l_opy_(self, hook_type):
        def bstack11l1111lll_opy_(arg=None):
            self.handler(hook_type, bstack111lll1_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪዡ"))
            result = None
            exception = None
            try:
                self.bstack11l11111ll_opy_(hook_type, self._11l1111ll1_opy_[hook_type], (arg,))
                result = Result(result=bstack111lll1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫዢ"))
            except Exception as e:
                result = Result(result=bstack111lll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬዣ"), exception=e)
                self.handler(hook_type, bstack111lll1_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬዤ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack111lll1_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭ዥ"), result)
        def bstack11l11111l1_opy_(this, arg=None):
            self.handler(hook_type, bstack111lll1_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࠨዦ"))
            result = None
            exception = None
            try:
                self.bstack11l11111ll_opy_(hook_type, self._11l1111ll1_opy_[hook_type], (this, arg))
                result = Result(result=bstack111lll1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩዧ"))
            except Exception as e:
                result = Result(result=bstack111lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪየ"), exception=e)
                self.handler(hook_type, bstack111lll1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࠪዩ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack111lll1_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫዪ"), result)
        if hook_type in [bstack111lll1_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳࡥࡵࡪࡲࡨࠬያ"), bstack111lll1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠩዬ")]:
            return bstack11l11111l1_opy_
        return bstack11l1111lll_opy_
    def bstack11l111l111_opy_(self, bstack11l1111l11_opy_):
        def bstack11l111l1ll_opy_(this, *args, **kwargs):
            self.bstack11l111llll_opy_(this, bstack11l1111l11_opy_)
            self._11l111lll1_opy_[bstack11l1111l11_opy_](this, *args, **kwargs)
        return bstack11l111l1ll_opy_