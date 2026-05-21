from src.load_data import load_excel
from src.cleaning import clean_deviations
from src.quantile_mapping import quantile_compensation


def main():

    print("====================================")
    print("HS -> CT Distribution Compensation")
    print("====================================")

    # ============================================
    # LOAD DATA
    # ============================================

    print("Loading datasets...")

    df_hs = load_excel("data/raw/HS_points.xlsx")
    df_ct = load_excel("data/raw/CT_points.xlsx")

    # ============================================
    # CLEAN DATA
    # ============================================

    print("Cleaning datasets...")

    df_hs = clean_deviations(df_hs)
    df_ct = clean_deviations(df_ct)

    # ============================================
    # EXTRACT DEVIATIONS
    # ============================================

    print("Extracting deviation values...")

    hs_dev = df_hs["dev"].values
    ct_dev = df_ct["dev"].values

    # ============================================
    # APPLY QUANTILE COMPENSATION
    # ============================================

    print("Applying quantile compensation...")

    compensated_dev = quantile_compensation(
        hs_dev,
        ct_dev
    )

    # ============================================
    # SAVE RESULTS
    # ============================================

    print("Saving compensated results...")

    df_hs["compensated_dev"] = compensated_dev

    df_hs.to_excel(
        "data/processed/HS_compensated.xlsx",
        index=False
    )

    print("====================================")
    print("Compensation completed successfully.")
    print("Results saved to:")
    print("data/processed/HS_compensated.xlsx")
    print("====================================")


if __name__ == "__main__":
    main()
