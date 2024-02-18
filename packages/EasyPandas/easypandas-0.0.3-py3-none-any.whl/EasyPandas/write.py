import pickle
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def write(
    obj=None,
    filename=None,
    textfileparamsdict={
        "sep": ",",
        "isheader": 1,
        "columns": None,
        "isindex": 0,
        "encoding": None},
    excelfileparamsdict={
        "sheetname": "Sheet1",
        "columns": None,
        "header": 1,
        "index": 1,
        "index_label": None,
        "engine": None}):
    """
    这是一个写入数据的文档字符串。

    参数:
    obj (Series or DataFrame): dataframe或者series对象。
    filename (str): 文件名{.csv, .xlsx, .xls, .pkl, .txt}。
    textfileparamsdict (dict): 控制写入文本文件(.csv, .txt)的参数。
    {
        sep (str): 分隔符{",", "\t", ......}。
        isheader (binary): 是否将列名写入{1,0}。
        columns (list of str): 要写入哪些列。
        isindex (binary): 是否要将行名写入{1,0}。
        encoding (str): 文件编码方式{https://docs.python.org/3/library/codecs.html#standard-encodings}。
    }
    excelfileparamsdict (dict): 控制写入excel文件(.xlsx或者.xls)的参数。
    {
        sheetname (str): 表单名称。
        columns (list of str): 要写入哪些列。
        header (binary or list of str): 是否写入列名{1,0}或者要写入的列名。
        index (binary): 是否写入行名{1,0}。
        index_label (list or str): 要写入的行名。
        engine (str): 指定excel读写引擎{"openpyxl", "xlsxwriter"}。
    }

    示例:
    ===============================================================================0
    导入模块
    >>> with open("../read.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> with open("../write.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> irisdf = rdata("../data/iris.csv")
    测试csv参数
    ===============================================================================1
    >>> write(irisdf, "../data/wiris.csv")
    ===============================================================================2
    写入行名
    >>> write(irisdf, "../data/wiris.csv", textfileparamsdict={"isindex": 1})
    ===============================================================================3
    不写入列名
    >>> write(irisdf, "../data/wiris.csv", textfileparamsdict={"isheader": 0})
    ===============================================================================4
    设置分隔符
    >>> write(irisdf, "../data/wiris.csv", textfileparamsdict={"sep": "\t"})
    ===============================================================================5
    写入哪些列
    >>> write(irisdf, "../data/wiris.csv", textfileparamsdict={"columns": ["Petal.Length", "Petal.Width", "Species"]})
    ===============================================================================6
    测试excel数据
    ===============================================================================7
    有行名有列名地写入
    >>> write(irisdf, "../data/wiris.xlsx")
    ===============================================================================8
    不写行名
    >>> write(irisdf, "../data/wiris.xlsx", excelfileparamsdict={"index": 0})
    ===============================================================================9
    不写列名
    >>> write(irisdf, "../data/wiris.xlsx", excelfileparamsdict={"header": 0})
    ===============================================================================10
    写入指定的列
    >>> write(irisdf, "../data/wiris.xlsx", excelfileparamsdict={"columns": ["Petal.Length", "Petal.Width", "Species"]})
    ===============================================================================11
    写入xls格式
    >>> write(irisdf, "../data/wiris.xls", excelfileparamsdict={"engine": "xlsxwriter"})
    ===============================================================================12
    测试pkl文件
    ===============================================================================13
    >>> write(irisdf, "../data/wiris.pkl")
    ===============================================================================14
    """
    if filename.__contains__(".csv") or filename.__contains__(".txt"):
        textfileparamsdictdefault = {
            "sep": ",",
            "isheader": 1,
            "columns": None,
            "isindex": 0,
            "encoding": None}
        # 更新字典
        textfileparamsdictdefault.update(textfileparamsdict)
        obj.to_csv(filename, sep=textfileparamsdictdefault["sep"],
                   header=bool(textfileparamsdictdefault["isheader"]),
                   columns=textfileparamsdictdefault["columns"],
                   index=bool(textfileparamsdictdefault["isindex"]),
                   encoding=textfileparamsdictdefault["encoding"]
                   )
    elif filename.__contains__(".xlsx") or filename.__contains__(".xls"):
        excelfileparamsdictdefault = {
            "sheetname": "Sheet1",
            "columns": None,
            "header": 1,
            "index": 1,
            "index_label": None,
            "engine": None}
        # 更新字典
        excelfileparamsdictdefault.update(excelfileparamsdict)
        obj.to_excel(filename, sheet_name=excelfileparamsdictdefault["sheetname"],
                     columns=excelfileparamsdictdefault["columns"],
                     header=bool(excelfileparamsdictdefault["header"]) if excelfileparamsdictdefault[
            "header"] == 0 or excelfileparamsdictdefault["header"] == 1 else excelfileparamsdictdefault["header"],
            index=bool(excelfileparamsdictdefault["index"]),
            index_label=excelfileparamsdictdefault["index_label"],
            engine=excelfileparamsdictdefault["engine"]
        )
    elif filename.__contains__(".pkl"):
        with open(filename, "wb") as fp:
            pickle.dump(obj, fp)
    else:
        print("写入文件失败！")
