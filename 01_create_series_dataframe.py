import pandas as pd


def create_series():
    """创建series"""
    # 使用列表创建，不指定dtype，会自动识别类型
    s1 = pd.Series([1, 2, 3, 4, 5.0])
    print(s1)
    # 使用字典创建，key就是index
    s2 = pd.Series({"A": 1, "B": 2, "C": 3})
    print(s2)
    # 指定index，name，dtype
    s3 = pd.Series([1, 2, 3, 4, 5.0],
                   index=["a", "b", "c", "d", "e"],
                   name="索引",
                   dtype="int64")
    print(s3)
    # 值相同，根据索引个数创建
    s4 = pd.Series(5, index=["a", "b"])
    print(s4)


def create_dataframe():
    """创建dataframe"""
    # 通过2维listlike创建
    list_2d = [[1, 2, 3], [4, 5, 6]]
    df1 = pd.DataFrame(list_2d, columns=["a", "b", "c"])
    print(df1)
    # 字典创建（key是列名）
    dic = {"a": [1, 2, 3], "b": [4, 5, 6]}
    df2 = pd.DataFrame(dic, index=["row1", "row2", "row3"])
    print(df2)
    # 读取Excel表格创建（要安装xlrd或openpyxl，xlrd只支持xls）
    df3 = pd.read_excel("test.xlsx")
    print(df3)


if __name__ == '__main__':
    create_series()
    create_dataframe()