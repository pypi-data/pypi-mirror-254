from __future__ import annotations
from dknovautils.dk_imports import *


def iprint(obj: Any, level: LLevel = LLevel.Debug) -> bool:
    """
    提供True返回值，是为了将该语句直接用于 assert语句中。

    """
    _iprint(obj, level=level)
    return True


def iprint_trace(obj: Any) -> bool:
    return _iprint(obj, level=LLevel.Trace)


def iprint_debug(obj: Any) -> bool:
    return _iprint(obj, level=LLevel.Debug)


def iprint_info(obj: Any) -> bool:
    return _iprint(obj, level=LLevel.Info)


def iprint_warn(obj: Any) -> bool:
    return _iprint(obj, level=LLevel.Warn)


def iprint_error(obj: Any) -> bool:
    return _iprint(obj, level=LLevel.Error)


# 用try语句 只是防止vscode格式化代码 将import语句自动往前移动到文件头部
# 本文件后续会用到AT等对象
try:
    from dknovautils.dkat import *
    from dknovautils.dkipy import *
finally:
    pass


def _write_async() -> None:
    AT.unimplemented("err70375 2025删除")
    pass


def _dtprint(s: str) -> bool:
    AT.unimplemented("err75654 2025删除")
    return iprint(s)


_iprint_logging_inited: bool = False


def _iprint(obj: Any, level: LLevel) -> bool:
    """


    iprint_xxx 函数可以任何时候使用 或者直接使用 没有任何初始化代码就可以直接使用 此时没有文件保存

        如果有执行函数 将执行该函数
        否则 会在没有初始化的时候进行一次内置的初始化 然后执行

    可以调用 init_logging_v1 进行初始化
        将读取yaml配置文件进行初始化
        将设置 _innerLoggerFun_ 用来作为 iprint的执行函数




    """
    # 将Trace级别提升一下。不知为何 NotSET的设置没有生效 并不会打印。
    if level == LLevel.Trace:
        level = LLevel.Debug

    if AT._inner_logger_fun is not None:
        # if level == LLevel.Error:
        #     AT._AstErrorCnt_ += 1
        #     AT._err_msgs.append(str(obj))
        AT._inner_logger_fun(obj, level)
        return True

    if True:
        global _iprint_logging_inited
        if not _iprint_logging_inited:
            # 只在没有配置的时候起作用 不会重复执行
            _iprint_logging_inited = True
            logging.basicConfig(
                level=logging.NOTSET,
                datefmt=AT.STRFMT_ISO_SEC_A,
                format=AT._LOG_FORMAT_106,
            )

            """
            formatter = logging.Formatter('%(asctime)s.%(msecs)03d-%(name)s-%(filename)s-[line:%(lineno)d]'
                                    '-%(levelname)s-[日志信息]: %(message)s',
                                    datefmt='%Y-%m-%d,%H:%M:%S')
            
            """

        AT.logger.log(level.value, obj)
        # logging.log(level.value, obj)

        return True
