import sys
sys.path.append(r"D:\document\statistics\TidyStatsProject")
from SoEasyData import GetMLData
df, _ = GetMLData(31)
print(df.head())
print(_)
