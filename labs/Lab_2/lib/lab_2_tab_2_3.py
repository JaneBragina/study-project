import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def lab_2_tab_2():
    wine_df = pd.read_csv("wine.csv", header=None, skiprows=1)

    print("Количество семплов:", len(wine_df))
    print("\nТипы данных в ячейках:")
    print(wine_df.dtypes)

    print("\nОписательная статистика:")
    print(wine_df.describe())

    correlation_matrix = wine_df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Матрица корреляции признаков")
    plt.show()

    wine_df.hist(figsize=(12, 10))
    plt.suptitle("Распределение признаков")
    plt.show()