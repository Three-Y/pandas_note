import pandas as pd
from datetime import datetime


def to_excel_index():
    """index:是否输出行索引，默认为true"""
    df = pd.DataFrame({"销量": [1, 1, 1, 1, 1],
                       "单价": [2, 2, 2, 2, 2],
                       "商品": [3, 3, 3, 3, 3]})
    df.to_excel("test1.xlsx", index=False)
    df = pd.DataFrame({"销量": [1, 1, 1, 1, 1],
                       "单价": [2, 2, 2, 2, 2],
                       "商品": [3, 3, 3, 3, 3]},
                      index=list("abcde"))
    df.to_excel("test2.xlsx")
    df = pd.DataFrame({"销量": [1, 1, 1, 1, 1],
                       "单价": [2, 2, 2, 2, 2],
                       "商品": [3, 3, 3, 3, 3]},
                      index=list("abcde"))
    df.index.name = "idx"  # 给索引列取个列名
    df.to_excel("test3.xlsx")


def to_excel_sheetname_float_format_na_rep():
    """
    sheet_name:设置sheet名
    float_format:浮点数的输出格式
    na_rep:空值的输出形式
    """
    df = pd.DataFrame({"销量": [1, 1, 1, 1, 1],
                       "单价": [2.666, 2.1, 2, 2, 2],
                       "商品": [3, None, 3, None, 3]})
    df.to_excel("test4.xlsx", sheet_name="商品销售情况列表", float_format="%.2f", na_rep="空")


def excel_writer():
    """
    ExcelWriter:pandas的一个类，作用就两个
        1.设置datatime输出格式，默认格式是：2020/1/1  0:00:00
        2.输出多个sheet
    """
    df1 = pd.DataFrame({"日期": [datetime(2020, 1, 1), datetime(2020, 5, 5)],
                        "价格": [2.666, 2.1]})
    print(df1)
    df2 = pd.DataFrame({"日期": [datetime(2020, 1, 1), datetime(2020, 5, 5)],
                        "价格": [2.666, 2.1]})
    print(df2)
    with pd.ExcelWriter("test5.xlsx") as writer:
        df1.to_excel(writer, sheet_name="A")
        df2.to_excel(writer, sheet_name="B")
    with pd.ExcelWriter("test6.xlsx", datetime_format="YYYY-MM-DD") as writer:
        df1.to_excel(writer, sheet_name="A")
        df2.to_excel(writer, sheet_name="B")


def read_or_to_csv():
    """
    read_csv:读取csv
    to_csv:写出csv
    参数:
        sep:读取或写出使用的分隔符
        encoding:读取或写出使用的编码
    """
    df = pd.read_csv("test7.csv")
    print(df)
    df.to_csv("test8.csv", sep="⭐")
    df.to_csv("test9.csv", encoding="gbk")


if __name__ == '__main__':
    read_or_to_csv()
