import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix, andrews_curves, parallel_coordinates, lag_plot, autocorrelation_plot
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def plot(
    obj,
    plottype="line",
    savefilename=None,
    **kwargs
):
    """
    这是快速绘图函数的文档字符串。

    参数:
    obj (Series or DataFrame): Series对象或者DataFrame对象。
    plottype (str): 绘图类型{"line", "bar", "barh", "hist", "box", "kde", "area", "scatter", "pie", "scattermatrix", "andrews_curves", "parallel_coordinates", "lag_plot", "autocorrelation_plot"}
    savefilename (str): 保存图像的文件名。

    示例:
    ===============================================================================0
    导入模块
    >>> import numpy as np
    >>> with open("../read.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> with open("../plot.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> with open("../factor.py", "rt", encoding="utf8") as fp: exec(fp.read())
    >>> iris = read("../data/iris.xlsx")
    ===============================================================================1
    Series的线图绘制
    >>> np.random.seed(123456)
    >>> ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
    >>> ts = ts.cumsum()
    >>> plot(ts, plottype="line")
    ===============================================================================2
    DataFrame的线图绘制
    >>> np.random.seed(123456)
    >>> df = pd.DataFrame(np.random.randn(1000, 4), index=pd.date_range("1/1/2000", periods=1000), columns=list("ABCD"))
    >>> df = df.cumsum()
    >>> plot(df, plottype="line")
    ===============================================================================3
    Series的线图绘制，给定参数
    >>> np.random.seed(123456)
    >>> ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
    >>> ts = ts.cumsum()
    >>> plot(ts, plottype="line", color="black")
    ===============================================================================4
    绘制xy之间的线图
    >>> np.random.seed(123456)
    >>> df = pd.DataFrame(np.random.randn(1000, 4), index=pd.date_range("1/1/2000", periods=1000), columns=list("ABCD"))
    >>> df = df.cumsum()
    >>> df["A"] = range(1, 1+df.shape[0])
    >>> plot(df, plottype="line", x="A", y="C")
    ===============================================================================5
    Series的柱状图
    >>> np.random.seed(123456)
    >>> df = pd.DataFrame(np.random.randn(1000, 4), index=pd.date_range("1/1/2000", periods=1000), columns=list("ABCD"))
    >>> df = df.cumsum()
    >>> plot(df.iloc[4, ], plottype="bar")
    ===============================================================================6
    DataFrame的柱状图
    >>> np.random.seed(123456)
    >>> df = pd.DataFrame(np.random.randn(1000, 4), index=pd.date_range("1/1/2000", periods=1000), columns=list("ABCD"))
    >>> df = df.cumsum()
    >>> plot(df.iloc[:4, ], plottype="bar")
    ===============================================================================7
    DataFrame的柱状图，堆叠形式
    >>> np.random.seed(123456)
    >>> df = pd.DataFrame(np.random.randn(1000, 4), index=pd.date_range("1/1/2000", periods=1000), columns=list("ABCD"))
    >>> df = df.cumsum()
    >>> plot(df.iloc[:4, ], plottype="bar", stacked=True)
    ===============================================================================8
    Series的水平柱状图
    >>> np.random.seed(123456)
    >>> df = pd.DataFrame(np.random.randn(1000, 4), index=pd.date_range("1/1/2000", periods=1000), columns=list("ABCD"))
    >>> df = df.cumsum()
    >>> plot(df.iloc[4, ], plottype="barh")
    ===============================================================================9
    DataFrame的水平柱状图
    >>> np.random.seed(123456)
    >>> df = pd.DataFrame(np.random.randn(1000, 4), index=pd.date_range("1/1/2000", periods=1000), columns=list("ABCD"))
    >>> df = df.cumsum()
    >>> plot(df.iloc[:4, ], plottype="barh")
    ===============================================================================10
    DataFrame的水平柱状图，堆叠形式
    >>> np.random.seed(123456)
    >>> df = pd.DataFrame(np.random.randn(1000, 4), index=pd.date_range("1/1/2000", periods=1000), columns=list("ABCD"))
    >>> df = df.cumsum()
    >>> plot(df.iloc[:4, ], plottype="barh", stacked=True)
    ===============================================================================11
    Series的直方图
    >>> np.random.seed(123456)
    >>> df = pd.DataFrame(np.random.randn(1000, 4), index=pd.date_range("1/1/2000", periods=1000), columns=list("ABCD"))
    >>> df = df.cumsum()
    >>> plot(df.iloc[:, 0], plottype="hist")
    ===============================================================================12
    DataFrame的直方图
    >>> np.random.seed(123456)
    >>> df = pd.DataFrame(np.random.randn(1000, 4), index=pd.date_range("1/1/2000", periods=1000), columns=list("ABCD"))
    >>> df = df.cumsum()
    >>> plot(df, plottype="hist")
    ===============================================================================13
    DataFrame的直方图，堆叠形式
    >>> np.random.seed(123456)
    >>> df = pd.DataFrame(np.random.randn(1000, 4), index=pd.date_range("1/1/2000", periods=1000), columns=list("ABCD"))
    >>> df = df.cumsum()
    >>> plot(df, plottype="hist", stacked=True)
    ===============================================================================14
    Series的箱线图
    >>> np.random.seed(123456)
    >>> df = pd.DataFrame(np.random.rand(10, 5), columns=["A", "B", "C", "D", "E"])
    >>> plot(df["A"], plottype="box")
    ===============================================================================15
    DataFrame的箱线图
    >>> np.random.seed(123456)
    >>> df = pd.DataFrame(np.random.rand(10, 5), columns=["A", "B", "C", "D", "E"])
    >>> plot(df, plottype="box")
    ===============================================================================16
    DataFrame的分组箱线图
    >>> np.random.seed(123456)
    >>> df = pd.DataFrame(np.random.rand(10, 5), columns=["A", "B", "C", "D", "E"])
    >>> df["X"] = pd.Series(["A", "A", "A", "A", "A", "B", "B", "B", "B", "B"])
    >>> plot(df, plottype="box", by="X")
    ===============================================================================17
    Series的面积图
    >>> np.random.seed(123456)
    >>> df = pd.DataFrame(np.random.rand(1000, 4), index=pd.date_range("1/1/2000", periods=1000), columns=list("ABCD"))
    >>> plot(df.loc[: ,"A"], plottype="area")
    ===============================================================================18
    DataFrame的面积图
    >>> np.random.seed(123456)
    >>> df = pd.DataFrame(np.random.rand(1000, 4), index=pd.date_range("1/1/2000", periods=1000), columns=list("ABCD"))
    >>> plot(df, plottype="area")
    ===============================================================================19
    散点图
    >>> plot(iris, plottype="scatter", x="Sepal.Length", y="Sepal.Width")
    ===============================================================================20
    散点图，参数
    >>> plot(iris, plottype="scatter", x="Sepal.Length", y="Sepal.Width", s=50, color="black", alpha=0.3)
    ===============================================================================21
    散点图，参数
    >>> iris["category_species"] = factor(iris["Species"], as_category=1)
    >>> plot(iris, plottype="scatter", x="Sepal.Length", y="Sepal.Width", s=50, c="category_species", alpha=0.3, colormap="Set2")
    ===============================================================================22
    Series的饼图
    >>> np.random.seed(123456)
    >>> series = pd.Series(3 * np.random.rand(4), index=["a", "b", "c", "d"], name="series")
    >>> plot(series, plottype="pie")
    ===============================================================================23
    DataFrame的饼图
    >>> np.random.seed(123456)
    >>> df = pd.DataFrame(3 * np.random.rand(4, 2), index=["a", "b", "c", "d"], columns=["x", "y"])
    >>> plot(df, plottype="pie")
    ===============================================================================24
    DataFrame的scattermatrix
    >>> np.random.seed(123456)
    >>> plot(iris.iloc[:, 1:-1], plottype="scatter_matrix")
    ===============================================================================25
    DataFrame的andrew曲线
    >>> np.random.seed(123456)
    >>> plot(iris.iloc[:, 1:], plottype="andrews_curves", class_column="Species")
    ===============================================================================26
    DataFrame的parallel_coordinates曲线
    >>> np.random.seed(123456)
    >>> plot(iris.iloc[:, 1:], plottype="parallel_coordinates", class_column="Species")
    ===============================================================================27
    Series的lag_plot曲线
    >>> np.random.seed(123456)
    >>> spacing = np.linspace(-99 * np.pi, 99 * np.pi, num=1000)
    >>> data = pd.Series(0.1 * np.random.rand(1000) + 0.9 * np.sin(spacing))
    >>> plot(data, plottype="lag_plot")
    ===============================================================================28
    Series的lag_plot曲线，给定参数
    >>> np.random.seed(123456)
    >>> spacing = np.linspace(-99 * np.pi, 99 * np.pi, num=1000)
    >>> data = pd.Series(0.1 * np.random.rand(1000) + 0.9 * np.sin(spacing))
    >>> plot(data, plottype="lag_plot", lag=3)
    ===============================================================================29
    Series的autocorrelation_plot曲线
    >>> np.random.seed(123456)
    >>> spacing = np.linspace(-99 * np.pi, 99 * np.pi, num=1000)
    >>> data = pd.Series(0.1 * np.random.rand(1000) + 0.9 * np.sin(spacing))
    >>> plot(data, plottype="autocorrelation_plot")
    ===============================================================================30
    保存文件
    >>> np.random.seed(123456)
    >>> spacing = np.linspace(-99 * np.pi, 99 * np.pi, num=1000)
    >>> data = pd.Series(0.1 * np.random.rand(1000) + 0.9 * np.sin(spacing))
    >>> plot(data, "autocorrelation_plot", "../data/自相关系数图.pdf")
    ===============================================================================31
    """
    plt.style.use("bmh")
    fig, ax = plt.subplots(figsize=(6,6))
    if plottype not in ["scatter_matrix", "andrews_curves", "parallel_coordinates", "lag_plot", "autocorrelation_plot"]:
        if plottype == "pie":
            obj.plot(kind=plottype, ax=ax, subplots=True, **kwargs)
        else:
            obj.plot(kind=plottype, ax=ax, **kwargs)
    else:
        if plottype == "scatter_matrix":
            scatter_matrix(obj, ax=ax, **kwargs)
        elif plottype == "andrews_curves":
            andrews_curves(obj, ax=ax, **kwargs)
        elif plottype == "parallel_coordinates":
            parallel_coordinates(obj, ax=ax, **kwargs)
        elif plottype == "lag_plot":
            lag_plot(obj, ax=ax, **kwargs)
        elif plottype == "autocorrelation_plot":
            autocorrelation_plot(obj, ax=ax, **kwargs)
        else:
            print("请输入正确的参数")
    print(savefilename)
    if savefilename is not None:
        fig.savefig(savefilename)
    else:
        pass
    plt.show()
