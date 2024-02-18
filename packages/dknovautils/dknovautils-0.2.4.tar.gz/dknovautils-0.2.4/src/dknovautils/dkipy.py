from __future__ import annotations

# from dknovautils.dk_imports import *

# from typing import Any

# 导入module 而不是导入函数或者类 可以避免循环import的问题
from dknovautils import commons
from dknovautils.commons import *


class DkIpyUtils(object):
    @staticmethod
    def hello(a: Any) -> Any:
        commons.iprint_info("hello")
        return a  # 为了测试该文件是否正常

    @staticmethod
    def mfc(cmd: str, logcmd: bool = True) -> None:
        DkIpyUtils.mfr(cmd, logcmd)

    _cmd_id = 1000

    @staticmethod
    def mfr(cmd: str, logcmd: bool = True) -> Any:
        from IPython.core.getipython import get_ipython  # type ignore[import-untyped]

        assert isinstance(cmd, str) and len(cmd) > 0, "err3581"
        DkIpyUtils._cmd_id += 1
        if logcmd:
            commons.iprint_info(f"run cmd begin {DkIpyUtils._cmd_id}: {cmd}")

        r = get_ipython().getoutput(cmd)  # type:ignore

        if logcmd:
            commons.iprint_info(f"run cmd end {DkIpyUtils._cmd_id}")

        return r


def dk_mfc(cmd: str, logcmd: bool = True) -> None:
    DkIpyUtils.mfc(cmd, logcmd)


def dk_mfr(cmd: str, logcmd: bool = True) -> Any:
    return DkIpyUtils.mfr(cmd, logcmd)


"""

!{cmd}

r=get_ipython().getoutput('{cmd}')



不能用 %cd 格式化会出错 用 os.chdir()

不用 echo 用 iprint






"""
