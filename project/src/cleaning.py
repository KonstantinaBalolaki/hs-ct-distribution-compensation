import numpy as np
import pandas as pd


def clean_deviations(df):

    # remove NaN values
    df = df.dropna()

    # keep only finite values
    df = df[np.isfinite(df["dev"])]

    # remove extreme outliers (3 sigma rule)
    mean = df["dev"].mean()
    std = df["dev"].std()

    lower = mean - 3 * std
    upper = mean + 3 * std

    df = df[
        (df["dev"] >= lower) &
        (df["dev"] <= upper)
    ]

    return df
