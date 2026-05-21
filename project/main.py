from src.load_data import load_excel
from src.quantile_mapping import quantile_compensation


def main():

    print("Loading datasets...")

    df_hs = load_excel("data/raw/HS_points.xlsx")
    df_ct = load_excel("data/raw/CT_points.xlsx")

    print("Extracting deviation values...")

    hs_dev = df_hs["dev"].values
    ct_dev = df_ct["dev"].values

    print("Applying quantile compensation...")

    compensated_dev = quantile_compensation(hs_dev, ct_dev)

    print("Saving compensated results...")

    df_hs["compensated_dev"] = compensated_dev

    df_hs.to_excel(
        "data/processed/HS_compensated.xlsx",
        index=False
    )

    print("Done.")


if __name__ == "__main__":
    main()
