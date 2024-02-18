import pickle
import pandas as pd
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def read(
    filename,
    textfileparamsdict={
        "sep": ",",
        "header": "infer",
        "names": None,
        "index_col": None,
        "usecols": None,
        "nrows": None,
        "encoding": None},
    excelfileparamsdict={
        "sheetname": 0,
        "header": 0,
        "names": None,
        "index_col": None,
        "usecols": None,
        "nrows": None}
):
    """
    这是读取数据的文档字符串。

    参数:
    filename (str): 带后缀的文件名{.txt, .csv, .xlsx, .xls, .pkl, .sav, .dta, .xpt, .sas7bdat}。
    textfileparamsdict (dict): 控制读取文本文件(.csv, .txt)的参数。
    {
        sep (str): 分隔符{",", "\t", ......}。
        header (int or None): 用作列名称的行号，None表示不指定任何一行作为列名。
        names (list of str): 列名称。
        index_col (int or str or None or False): 指定哪一列作为行名，None表示猜测，False表示不指定任何一列作为行名。
        usecols (list of int or list of str or callable): 读取哪些列。
        nrows (int): 要读取的文件行数。
        encoding (str): 文件编码方式{https://docs.python.org/3/library/codecs.html#standard-encodings}。
    }
    excelfileparamsdict (dict): 控制读取excel文件(.xlsx或者.xls)的参数。
    {
        sheetname (str or int or list): 要读取的sheet表名称或者第几张sheet表。
        header (int or None): 用作列名称的行号，None表示不指定列名。
        names (list of str): 列名称。
        index_col (int or str or None): 指定哪一列作为行名，None表示不指定任何一列作为行名。
        usecols (list of int or list of str or callable): 读取哪些列。
        nrows (int): 要读取的文件行数。
    }

    示例:
    ===============================================================================0
    >>> with open("../read.py", "rt", encoding="utf8") as fp: exec(fp.read())
    测试csv参数
    ===============================================================================1
    基本用法
    >>> df = read("../data/iris.csv")
    >>> print(df.head())
    ===============================================================================2
    读取其他分隔符
    >>> df = read("../data/iris.csv", textfileparamsdict={"sep": ","})
    >>> print(df.head())
    ===============================================================================3
    不指定任何行作为列名
    >>> df = read("../data/iris.csv", textfileparamsdict={"header": None})
    >>> print(df.head())
    ===============================================================================4
    指定列名
    >>> df = read("../data/iris.csv", textfileparamsdict={"names": ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]})
    >>> print(df.head())
    ===============================================================================5
    指定索引
    >>> df = read("../data/iris.csv", textfileparamsdict={"index_col": 1})
    >>> print(df.head())
    ===============================================================================6
    指定读取的列名
    >>> df = read("../data/iris.csv", textfileparamsdict={"usecols": ["Sepal.Length", "Sepal.Width", "Species"]})
    >>> print(df.head())
    ===============================================================================7
    指定读取的文件行数
    >>> df = read("../data/iris.csv", textfileparamsdict={"names": ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"], "nrows": 3})
    >>> print(df.head())
    ===============================================================================8
    测试excel文件读取
    ===============================================================================9
    将第一列作为行名
    >>> df = read("../data/iris.xlsx", excelfileparamsdict={"index_col": 0})
    >>> print(df.head())
    不将第一列作为行名
    >>> df = read("../data/iris.xlsx")
    >>> print(df.head())
    不将第一行作为列名
    >>> df = read("../data/iris.xlsx", excelfileparamsdict={"header": None})
    >>> print(df.head())
    将第一列作为行名且指定列名
    >>> df = read("../data/iris.xlsx", excelfileparamsdict={"index_col": 0, "names": ["v1", "v2", "v3", "v4", "v5"]})
    >>> print(df.head())
    指定要读取的列
    >>> df = read("../data/iris.xlsx", excelfileparamsdict={"usecols": ["Sepal.Length", "Sepal.Width", "Species"], "index_col": 0})
    >>> print(df.head())
    指定读取的行数
    >>> df = read("../data/iris.xlsx", excelfileparamsdict={"usecols": ["Sepal.Length", "Sepal.Width", "Species"], "nrows": 50})
    >>> print(df.head())
    读取xls文件
    >>> df = read("../data/womenexport.xls")
    >>> print(df.head())
    ===============================================================================10
    测试pkl参数
    ===============================================================================11
    >>> df = read("../data/iris.pkl")
    >>> print(df.head())
    ===============================================================================12
    测试dta参数
    >>> df = read("../data/auto.dta")
    >>> print(df.head())
    ===============================================================================13
    测试xpt参数
    >>> df = read("../data/hh.xpt")
    >>> print(df.head())
    ===============================================================================14
    测试sav参数
    >>> df = read("../data/iris.sav")
    >>> print(df.head())
    ===============================================================================15
    """
    df = None
    if filename.__contains__(".csv") or filename.__contains__(".txt"):
        textfileparamsdictdefault = {
            "sep": ",",
            "header": "infer",
            "names": None,
            "index_col": None,
            "usecols": None,
            "nrows": None,
            "converts": None,
            "parse_dates": False,
            "keep_date_col": False,
            "date_format": None,
            "encoding": None,
            "dtype": None}
        # 更新字典
        textfileparamsdictdefault.update(textfileparamsdict)
        df = pd.read_csv(
            filename,
            sep=textfileparamsdictdefault["sep"],
            header=textfileparamsdictdefault["header"],
            names=textfileparamsdictdefault["names"],
            index_col=textfileparamsdictdefault["index_col"],
            usecols=textfileparamsdictdefault["usecols"],
            nrows=textfileparamsdictdefault["nrows"],
            converters=textfileparamsdictdefault["converts"],
            parse_dates=textfileparamsdictdefault["parse_dates"],
            keep_date_col=textfileparamsdictdefault["keep_date_col"],
            date_format=textfileparamsdictdefault["date_format"],
            encoding=textfileparamsdictdefault["encoding"],
            dtype=textfileparamsdictdefault["dtype"])
    elif filename.__contains__(".xlsx") or filename.__contains__(".xls"):
        excelfileparamsdictdefault = {
            "sheetname": 0,
            "header": 0,
            "names": None,
            "index_col": None,
            "usecols": None,
            "nrows": None,
            "converts": None,
            "parse_dates": False,
            "dtype": None,
            "engine": None}
        # 更新字典
        excelfileparamsdictdefault.update(excelfileparamsdict)
        df = pd.read_excel(
            filename,
            sheet_name=excelfileparamsdictdefault["sheetname"],
            header=excelfileparamsdictdefault["header"],
            names=excelfileparamsdictdefault["names"],
            index_col=excelfileparamsdictdefault["index_col"],
            usecols=excelfileparamsdictdefault["usecols"],
            nrows=excelfileparamsdictdefault["nrows"],
            converters=excelfileparamsdictdefault["converts"],
            parse_dates=excelfileparamsdictdefault["parse_dates"],
            dtype=excelfileparamsdictdefault["dtype"],
            engine=excelfileparamsdictdefault["engine"])
    elif filename.__contains__(".pkl"):
        with open(filename, "rb") as fp:
            df = pickle.load(fp)
    elif filename.__contains__(".sav"):
        df = pd.read_spss(filename)
    elif filename.__contains__(".xpt") or filename.__contains__(".sas7bdat"):
        df = pd.read_sas(filename)
    elif filename.__contains__(".dta"):
        df = pd.read_stata(filename)
    else:
        print("请指定正确的文件名")
    return df
