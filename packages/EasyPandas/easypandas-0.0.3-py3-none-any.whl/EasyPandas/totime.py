import pandas as pd
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def totime(
        obj,
        format=None,
        unit=None,
        origin="unix"
        ):
    """
    这是一个将字符串转为时间对象的函数帮助文档。

    参数:
    obj (Series or list or 1D-array or str): 一维对象或者字符串。
    format (str): 时间日期的格式，例如%Y/%m/%D %H:%M%S。
    表示各个时间的字母及对应的含义如下：
    1. %y Year without century as a zero-padded decimal number, such as 01,02,99.
    2. %Y Year with century as a decimal number, such as 0001,...,2020.
    3. %d Day of the month as a zero-padded decimal number.
    4. %m Month as a zero-padded decimal number.
    5. %H Hour (24-hour clock) as a zero-padded decimal number.
    6. %M Minute as a zero-padded decimal number.
    7. %S Second as a zero-padded decimal number.
    8. %f Microsecond as a decimal number, zero-padded to 6 digits.
    unit (str): 数字表示的时间单位。
    表示时间单位的字母和对应含义如下
    1. D day
    2. s second
    3. ms millisecond
    4. us microsecond
    4. ns nanosecond
    origin (str): 起始时间。

    示例:
    ===============================================================================0
    导入模块
    >>> import pandas as pd
    >>> with open("../totime.py", "rt", encoding="utf8") as fp: exec(fp.read())
    ===============================================================================1
    基本测试
    >>> timestr = "Jul 31, 2009"
    >>> res = totime(timestr)
    >>> print(res)
    ===============================================================================2
    基本测试
    >>> timestr = "2005/11/23"
    >>> res = totime(timestr)
    >>> print(res)
    ===============================================================================3
    基本测试
    >>> timestr = None
    >>> res = totime(timestr)
    >>> print(res)
    ===============================================================================4
    基本测试
    >>> timestr = "04-14-2012 10:00"
    >>> res = totime(timestr)
    >>> print(res)
    ===============================================================================5
    基本测试
    >>> timestr = "2018-01-01"
    >>> res = totime(timestr)
    >>> print(res)
    ===============================================================================6
    基本测试，定制格式
    >>> timestr = "2018*01||01"
    >>> res = totime(timestr, format="%Y*%m||%d")
    >>> print(res)
    ===============================================================================7
    基本测试，将数字转为时间
    >>> timestr = [2018, 2020, 10000]
    >>> res = totime(timestr, unit="D")
    >>> print(res)
    ===============================================================================8
    基本测试，将数字转为时间，给定原始时间
    >>> timestr = [2018, 2020, 10000]
    >>> res = totime(timestr, unit="D", origin="2000-01-01")
    >>> print(res)
    ===============================================================================9
    """
    try:
        res = pd.to_datetime(obj, format=format, unit=unit, origin=origin)
    except:
        res = pd.to_datetime(obj, format=format, unit=unit, origin=pd.Timestamp(origin))
    return res
