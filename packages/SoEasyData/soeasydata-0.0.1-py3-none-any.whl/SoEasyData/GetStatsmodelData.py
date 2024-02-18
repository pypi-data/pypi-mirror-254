import statsmodels.api as sm
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def GetStatsmodelData(dataname):
    """
    这是一个获取Statsmodel自带数据集函数的文档字符串。

    参数:
    dataname (str): 数据集名称{"anes96", "cancer", "ccard", "china_smoking", "co2", "committee", "copper", "cpunish", "danish_data", "elnino", "engel", "fair", "fertility", "grunfeld", "heart", "interest_inflation", "longley", "macrodata", "modechoice", "nile", "randhie", "scotland", "spector", "stackloss", "star98", "statecrime", "strikes", "sunspots"}。

    返回:
    dataframe对象, 数据信息

    示例:
    ===============================================================================0
    导入模块
    >>> import sys
    >>> sys.path.append(r"D:\document\statistics\TidyStatsProject")
    >>> from SoEasyData import GetStatsmodelData
    ===============================================================================1
    测试各种数据获取
    ===============================================================================2
    >>> df, _ = GetStatsmodelData("anes96")
    >>> print(df.head())
    ===============================================================================3
    >>> df, _ = GetStatsmodelData("cancer")
    >>> print(df.head())
    ===============================================================================4
    >>> df, _ = GetStatsmodelData("ccard")
    >>> print(df.head())
    ===============================================================================5
    >>> df, _ = GetStatsmodelData("china_smoking")
    >>> print(df.head())
    ===============================================================================6
    >>> df, _ = GetStatsmodelData("co2")
    >>> print(df.head())
    ===============================================================================7
    >>> df, _ = GetStatsmodelData("committee")
    >>> print(df.head())
    ===============================================================================8
    >>> df, _ = GetStatsmodelData("copper")
    >>> print(df.head())
    ===============================================================================9
    >>> df, _ = GetStatsmodelData("cpunish")
    >>> print(df.head())
    ===============================================================================10
    >>> df, _ = GetStatsmodelData("danish_data")
    >>> print(df.head())
    ===============================================================================11
    >>> df, _ = GetStatsmodelData("elnino")
    >>> print(df.head())
    ===============================================================================12
    >>> df, _ = GetStatsmodelData("engel")
    >>> print(df.head())
    ===============================================================================13
    >>> df, _ = GetStatsmodelData("fair")
    >>> print(df.head())
    ===============================================================================14
    >>> df, _ = GetStatsmodelData("fertility")
    >>> print(df.head())
    ===============================================================================15
    >>> df, _ = GetStatsmodelData("grunfeld")
    >>> print(df.head())
    ===============================================================================16
    >>> df, _ = GetStatsmodelData("heart")
    >>> print(df.head())
    ===============================================================================17
    >>> df, _ = GetStatsmodelData("interest_inflation")
    >>> print(df.head())
    ===============================================================================18
    >>> df, _ = GetStatsmodelData("longley")
    >>> print(df.head())
    ===============================================================================19
    >>> df, _ = GetStatsmodelData("macrodata")
    >>> print(df.head())
    ===============================================================================20
    >>> df, _ = GetStatsmodelData("modechoice")
    >>> print(df.head())
    ===============================================================================21
    >>> df, _ = GetStatsmodelData("nile")
    >>> print(df.head())
    ===============================================================================22
    >>> df, _ = GetStatsmodelData("randhie")
    >>> print(df.head())
    ===============================================================================23
    >>> df, _ = GetStatsmodelData("scotland")
    >>> print(df.head())
    ===============================================================================24
    >>> df, _ = GetStatsmodelData("spector")
    >>> print(df.head())
    ===============================================================================25
    >>> df, _ = GetStatsmodelData("stackloss")
    >>> print(df.head())
    ===============================================================================26
    >>> df, _ = GetStatsmodelData("star98")
    >>> print(df.head())
    ===============================================================================27
    >>> df, _ = GetStatsmodelData("statecrime")
    >>> print(df.head())
    ===============================================================================28
    >>> df, _ = GetStatsmodelData("strikes")
    >>> print(df.head())
    ===============================================================================29
    >>> df, _ = GetStatsmodelData("sunspots")
    >>> print(df.head())
    ===============================================================================30
    """
    df = eval("sm.datasets.{}.load_pandas().data".format(dataname))
    data_info = eval("sm.datasets.{}.NOTE".format(dataname))
    return df, data_info
