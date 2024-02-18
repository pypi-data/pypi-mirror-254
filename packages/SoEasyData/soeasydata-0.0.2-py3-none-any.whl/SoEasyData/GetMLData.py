import openml
import warnings
# 禁用警告
warnings.filterwarnings("ignore")


def GetMLData(dataset_id):
    """
    这是一个获取机器学习数据集函数的文档字符串。

    参数:
    dataset_id (int): 数据集ID名称。
    数据集ID可以从OpenML网站上获取: https://www.openml.org/search?type=data&sort=runs&status=active

    返回:
    dataframe对象, 数据信息

    示例:
    ===============================================================================0
    导入模块
    >>> import sys
    >>> sys.path.append(r"D:\document\statistics\TidyStatsProject")
    >>> from SoEasyData import GetMLData
    ===============================================================================1
    测试各种数据获取
    ===============================================================================2
    >>> df, _ = GetMLData(45027)
    >>> print(df.head())
    >>> print(_)
    ===============================================================================3
    >>> df, _ = GetMLData(31)
    >>> print(df.head())
    >>> print(_)
    ===============================================================================4
    """
    data = openml.datasets.get_dataset(dataset_id)
    df = data.get_data()[0]
    data_info = data.description
    return df, data_info
