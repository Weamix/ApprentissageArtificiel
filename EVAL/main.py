import pandas as pd


def analyze(data, type):
    print(data.shape)
    print(data.info())
    print(data.describe())
    print(data.head())
    print(data[type].value_counts())


if __name__ == '__main__':
    dataCCfinal_1 = pd.read_csv('csv/dataCCfinal_1.csv')
    dataCCfinal_2 = pd.read_csv('csv/dataCCfinal_2.csv')
    analyze(dataCCfinal_1, 'Z')
    analyze(dataCCfinal_2, 'Z')


