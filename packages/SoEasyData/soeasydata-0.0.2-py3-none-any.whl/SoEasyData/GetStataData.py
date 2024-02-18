import statsmodels.api as sm
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def GetStataData(dataname):
    """
    这是一个获取Stata数据集函数的文档字符串。

    参数:
    dataname (str): 数据集名称。

    返回:
    dataframe对象, 数据信息

    示例:
    ===============================================================================0
    导入模块
    >>> import sys
    >>> sys.path.append(r"D:\document\statistics\TidyStatsProject")
    >>> from SoEasyData import GetStataData
    ===============================================================================1
    测试各种数据获取
    ===============================================================================2
    >>> df = GetStataData("auto")
    >>> print(df.head())
    ===============================================================================3
    >>> df = GetStataData("sat")
    >>> print(df.head())
    ===============================================================================4
    """
    df = sm.datasets.webuse(dataname, baseurl='https://www.stata-press.com/data/r18/')
    return df
