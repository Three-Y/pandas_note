import pandas as pd


def read_excel_sheet_name():
    """sheet_name:选择子，使用索引（默认0）、表名、表名list、None全部表格，多个表格时，返回字典"""
    df = pd.read_excel(io="test.xlsx", sheet_name=2)
    df = pd.read_excel(io="test.xlsx", sheet_name="Sheet2")
    df_dic = pd.read_excel(io="test.xlsx", sheet_name=[1, "Sheet3"])  # list的数据就是字典的key
    df_dic = pd.read_excel(io="test.xlsx", sheet_name=None)  # 表名就是字典的key
    print(df_dic["Sheet1"])


def read_excel_header_index_col():
    """header（默认0） & index_col（默认None）"""
    df = pd.read_excel(io="test.xlsx",header=None)  # 表格无表头
    df = pd.read_excel(io="test.xlsx", header=1)
    df = pd.read_excel(io="test.xlsx", header=[0, 1])  # 多行表头

    df = pd.read_excel(io="test.xlsx", index_col=0)
    df = pd.read_excel(io="test.xlsx", index_col=[0, 1])  # 多列index
    # df = pd.read_excel(io="test.xlsx", index_col=["商品代号", "颜色代号"])  # 这种方式不行
    df = pd.read_excel(io="test.xlsx", index_col="商品代号")  # 这种可以

    print(df)


def read_excel_usecols():
    """usecols:默认None，全部列"""
    df = pd.read_excel(io="test.xlsx", usecols=[1, 3, 5])
    df = pd.read_excel(io="test.xlsx", usecols=[0])  # 现在不支持只传递一个int值，要放到list中[0]
    df = pd.read_excel(io="test.xlsx", usecols=["列1", "列5"])  # ***推荐使用这种***
    df = pd.read_excel(io="test.xlsx", usecols="A,E:G")
    df = pd.read_excel(io="test.xlsx", usecols=lambda x: (x == "列1") | (x == "列5"))
    print(df)


def read_excel_skiprows():
    """skiprows:跳过行"""
    df = pd.read_excel(io="test.xlsx", skiprows=[1, 3])
    print(df)


def read_excel_names():
    """names:设置列名"""
    df = pd.read_excel(io="test.xlsx", names=["Sheet1", "aa", "bb", "cc", "dd", "ee", "ff"])
    print(df)


def read_excel_dtype():
    """
    dtype:设置数据类型，设置类型后，可以使用特定类型特有的一些操作
        整型：int8/int16/int32/int64(默认)
        浮点型：float16/float32/float64(默认)
        字符串：str/string 指定为str会显示object类型，指定为string会显示为string类型
        布尔类型：bool
        分类：category 指定该类型后，可以根据类型设置排序
        时间戳（纳秒）：datetime64[ns]
        时间周期：period[Y/M/D]
        Python对象混合类型：object
    """
    df = pd.read_excel(io="test.xlsx")
    print(df.dtypes)
    df = pd.read_excel(io="test.xlsx",
                       dtype={
                           "商品代号": "str",
                           "颜色代号": "string",
                           "季节": "category",
                           "商品年份": "period[Y]"})
    print(df.dtypes)  # 获取每列数据的数据类型


def read_excel_parse_dates_date_parser():
    """
    parse_dates:指定要解析成日期的那一列
    date_parser:指定按什么格式解析日期
                如果是以下这类日期，pandas可以识别，无需date_parser
                    20200112
                    2020/01/12
                    1/12/2020
                    2020-01-12
                    2020-01-12 00:10:10
    """
    # 尝试解析日期
    df = pd.read_excel(io="test.xlsx", parse_dates=True)
    # 尝试解析指定列为日期
    df = pd.read_excel(io="test.xlsx", parse_dates=["日期"])
    # 尝试解析指定多列合并解析成日期，合并到”年“这一列，”月“和”日“还是int
    df = pd.read_excel(io="test.xlsx", parse_dates=["年", "月", "日"])
    # 尝试解析指定多列合并解析成日期，合并3列为一列”年_月_日“，合并列会跑到第一列
    df = pd.read_excel(io="test.xlsx", parse_dates=[["年", "月", "日"]])
    # 给合并后的日期列取名
    df = pd.read_excel(io="test.xlsx", parse_dates={"合并后的日期": ["年", "月", "日"]})
    # 指定解析日期的格式
    df = pd.read_excel(io="test.xlsx",
                       parse_dates=["预计补货日期"],
                       date_parser=lambda x: pd.to_datetime(x, format="%Y年%m月%d日"))  # 注意：Y是大写

    print(df.dtypes)


def read_excel_na_values():
    """na_values:指定缺失值，某些常见的缺失值（不包括空格）会自动识别为缺失值"""
    # 指定某些值识别为缺失值
    df = pd.read_excel(io="test.xlsx", na_values=["AA", "BB", " "])
    # 指定某列的某些值识别为缺失值
    df = pd.read_excel(io="test.xlsx", na_values={"品牌": ["X", "Y"]})
    print(df)


def read_excel_converters():
    """converters:转换源数据为函数计算后的值"""
    df = pd.read_excel(io="test.xlsx",
                       converters={
                        "商品代号": lambda x: x.strip(),
                        # "商品代号": str.strip(),  # 简写形式
                        "成本": lambda x: x*1.25
                       })
    print(df)


def read_excel_true_values_false_values():
    """
    true_values:指定识别为true的值
    false_values:指定识别为false的值
    注意：1.要一整列的值都能被转换成bool类型，才会进行转换
         2.只对字符串生效
         3.想要转换数值为bool，用dtype指定，0会识别为flase，非0(包括负数)为true
    """
    df = pd.read_excel(io="test.xlsx",
                       usecols=["季节"],
                       true_values=["春", "夏"],
                       false_values=["冬", "秋"])
    print(df)
    df = pd.read_excel(io="test.xlsx",
                       usecols=["颜色代号"],
                       dtype={"颜色代号": "bool"})
    print(df)


def read_excel_squeeze():
    """squeeze:如果数据只有一列，是否返回series，默认是false"""
    df = pd.read_excel(io="test.xlsx", usecols=[1])
    print(type(df))
    df = pd.read_excel(io="test.xlsx", usecols=[1], squeeze=True)
    print(type(df))


def read_excel_mangle_dupe_cols():
    """
    mangle_dupe_cols:
        是否重命名重复的列名，默认false
        设置为true，有重复的列名会重命名为”列名.1“
        如果有重复的列名，而mangle_dupe_cols为false，会报错
    """
    df = pd.read_excel(io="test.xlsx", mangle_dupe_cols=True)
    print(df)


def read_excel_nrows():
    """nrows:要使用的行数，不包括表头"""
    df = pd.read_excel(io="test.xlsx", nrows=3)
    print(df)


def read_excel_thousands():
    """thousands:千位分隔符，默认为None
                 只对非数值类型的数字字符串起作用
                 若文本类型的数值（如：1,000）没有设置thousands，会识别为object"""
    df = pd.read_excel(io="test.xlsx")
    print(df.dtypes["销售额"])
    df = pd.read_excel(io="test.xlsx", thousands=",")
    print(df.dtypes["销售额"])


def read_excel_convert_float():
    """convert_float:是否将float类型转换为int型，如:1.0==>1，默认true"""
    df = pd.read_excel(io="test.xlsx",convert_float=False)  # 1.0==>1.0 1==>1.0
    print(df)
    df = pd.read_excel(io="test.xlsx",convert_float=True)  # 1.0==>1 1==>1
    print(df)


if __name__ == '__main__':
    read_excel_convert_float()
