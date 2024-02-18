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
import threading
bstack11111ll1ll_opy_ = 1000
bstack11111llll1_opy_ = 5
bstack11111ll111_opy_ = 30
bstack1111l1111l_opy_ = 2
class bstack1111l11111_opy_:
    def __init__(self, handler, bstack11111ll11l_opy_=bstack11111ll1ll_opy_, bstack1111l111l1_opy_=bstack11111llll1_opy_):
        self.queue = []
        self.handler = handler
        self.bstack11111ll11l_opy_ = bstack11111ll11l_opy_
        self.bstack1111l111l1_opy_ = bstack1111l111l1_opy_
        self.lock = threading.Lock()
        self.timer = None
    def start(self):
        if not self.timer:
            self.bstack11111lllll_opy_()
    def bstack11111lllll_opy_(self):
        self.timer = threading.Timer(self.bstack1111l111l1_opy_, self.bstack11111ll1l1_opy_)
        self.timer.start()
    def bstack11111l1lll_opy_(self):
        self.timer.cancel()
    def bstack11111lll1l_opy_(self):
        self.bstack11111l1lll_opy_()
        self.bstack11111lllll_opy_()
    def add(self, event):
        with self.lock:
            self.queue.append(event)
            if len(self.queue) >= self.bstack11111ll11l_opy_:
                t = threading.Thread(target=self.bstack11111ll1l1_opy_)
                t.start()
                self.bstack11111lll1l_opy_()
    def bstack11111ll1l1_opy_(self):
        if len(self.queue) <= 0:
            return
        data = self.queue[:self.bstack11111ll11l_opy_]
        del self.queue[:self.bstack11111ll11l_opy_]
        self.handler(data)
    def shutdown(self):
        self.bstack11111l1lll_opy_()
        while len(self.queue) > 0:
            self.bstack11111ll1l1_opy_()