import pandas as pd

def lab_2_tab_1():
    wine_df = pd.read_csv("wine.csv", header=None)

    print("Первые 5 строк:")
    print(wine_df.head())

    print("\nПоследние 5 строк:")
    print(wine_df.tail())