import pandas as pd


def select_dic_like():
    """series和dataframe都是dic_like，可以进行字典的相关操作"""
    s = pd.Series([1, 2, 3], index=list("abc"))
    print(s)
    df = pd.DataFrame({"AA": [1, 4, 7],
                       "BB": [2, 5, 8],
                       "CC": [3, 6, 9]},
                      index=list("abc"))
    print(df)

    print(s[1])
    print(s["c"])
    print(s[["a", "c"]])
    print(s[[True, False, True]])

    # print(df[1])  # ERROR
    print(df["AA"])
    print(df[["AA", "CC"]])
    print(df[[True, False, True]])
    print(df[(df["BB"] > 3) & (df["BB"] < 7)])
    print(df[(df["BB"] == 2) | (df["BB"] == 8)])
    print(df[df["BB"] != 2])


def select_list_like():
    """series和dataframe都是list_like，可以进行列表的切片操作，都是按行切"""
    s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=list("abcdefghij"))
    print(s)
    df = pd.DataFrame({"AA": [1, 4, 7, "a1", "a2", "a3"],
                       "BB": [2, 5, 8, "b1", "b2", "b3"],
                       "CC": [3, 6, 9, "c1", "c2", "c3"]},
                      index=list("abcdef"))
    print(df)

    print(s[1])
    print(s[0:3])  # 不包含3
    print(s[0:-1])  # 不包含-1
    print(s[0::2])
    print(s["a":"c"])  # 包含c

    # print(df[1])  # ERROR
    print(df[0:3])  # 不包含3
    print(df[0:-2])  # 不包含-2
    print(df[0::2])
    print(df["a":"c"])  # 包含c


def seletc_loc_iloc_at_iat():
    """
    loc:使用label索引选择
    iloc:使用位置索引选择
    at:选择单值时，会比loc效率高一点点
    iat:选择单值时，会比iloc效率高一点点
    """
    df = pd.DataFrame({"AA": [1, 4, 7, "a1", "a2", "a3"],
                       "BB": [2, 5, 8, "b1", "b2", "b3"],
                       "CC": [3, 6, 9, "c1", "c2", "c3"]},
                      index=list("abcdef"))
    print(df)

    # print(df.loc["a"])
    # print(df.loc["a","BB"])
    # print(df.loc["BB","a"])  # ERROR 要先行后列
    # print(df.loc[["a", "c"], ["AA", "CC"]])
    # print(df.loc[[True, False, True, False, False, False], [False, True, False]])
    # print(df.loc[["a", "c"], [False, True, False]])
    # print(df.loc[[True, False, True, False, False, False], ["AA", "CC"]])
    # print(df.loc["a":"e", "AA":"BB"])
    # print(df.loc[::2, ::-1])
    # print(df.loc[lambda df: [True, False, True, False, False, False],
    #              lambda df: [False, True, False]])

    # print(df.iloc[5])
    # print(df.iloc[[5], [1, 2]])
    # print(df.iloc[[True, False, True, False, False, False], [False, True, False]])
    # print(df.iloc[1:-1, :-1])
    # print(df.iloc[::-1, ::-1])
    # print(df.iloc[2::2, :])
    # print(df.iloc[lambda df: [1, 2, 5], lambda df: [0, 1]])

    # print(df.at["a", "CC"])
    # print(df.iat[2, 1])


if __name__ == '__main__':
    seletc_loc_iloc_at_iat()
