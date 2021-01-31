import pandas as pd


def pandas_index():
    """
    index具有三个功能
        识别：通过索引可以知道每个格子具体的意思
        对齐：两表进行合并操作时，会自动对其相同的行列索引
        获取和设置：获取值，修改值
    index分类：
        位置索引：自带的索引，从0开始
        标签索引：字符串索引
    :return:
    """
    df1 = pd.DataFrame(data={"A": [1, 2, 3],
                             "B": [10, 20, 30]},
                       index=["x", "y", "z"])
    df2 = pd.DataFrame(data={"B": [1, 2, 3],
                             "A": [10, 20, 30]},
                       index=["x", "z", "y"])
    df3 = df1+df2
    print(df3)
    df3["A"] = [666, 666, 666]
    print(df3)


if __name__ == '__main__':
    pandas_index()
