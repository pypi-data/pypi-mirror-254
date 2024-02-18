import statsmodels.api as sm
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def GetRData(dataname, rpackage):
    """
    这是一个获取R数据集函数的文档字符串。

    参数:
    dataname (str): 数据集名称。
    rpackage (str): R包名称。

    返回:
    dataframe对象, 数据信息

    示例:
    ===============================================================================0
    导入模块
    >>> import sys
    >>> sys.path.append(r"D:\document\statistics\TidyStatsProject")
    >>> from SoEasyData import GetRData
    ===============================================================================1
    测试各种数据获取
    ===============================================================================2
    >>> df, _ = GetRData("women", "datasets")
    >>> print(df.head())
    >>> print(_)
    ===============================================================================3
    >>> df, _ = GetRData("Arrests", "carData")
    >>> print(df.head())
    >>> print(_)
    ===============================================================================4
    """
    data = sm.datasets.get_rdataset(dataname, rpackage)
    df = data.data
    data_info = data.__doc__
    return df, data_info
