from ctypes import c_int
import multiprocessing
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


def sum_values(i, df: pd.Series, arr: multiprocessing.Array):
    """ sums million part of values in df """
    n = 1000  # for artificially adding to the execution time
    mil = int(1e6)

    for _, v in df.items():
        arr[i] += v // mil  # we have to divide to prevent overflow
        for j in range(n):
            arr[i] += 1
            arr[i] -= 1
    print(i, arr[i])


def main():
    df = pd.read_csv(r"covid_trade.csv")
    year_col_name = "Year"
    value_col_name = "Value"

    years = df[year_col_name].unique()
    processes = []
    shared_arr = multiprocessing.Array("i", [0 for _ in range(len(years))], lock=False)

    for i, y in enumerate(years):
        values = df[df[year_col_name] == y][value_col_name]
        p = multiprocessing.Process(target=sum_values, args=(i, values, shared_arr))
        processes.append(p)
        p.start()
        print(f"Process {i} started")

    for p in processes:
        p.join()
    print(type(shared_arr), shared_arr)
    output = np.frombuffer(shared_arr, dtype=c_int)
    plt.bar(years, output)
    plt.xlabel("Year")
    plt.ylabel("Effect of covid on trade in millions")
    plt.show()


if __name__ == '__main__':
    main()
