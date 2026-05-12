from src.load_data import load_excel
from src.compensation import quantile_compensation

df_hs = load_excel("data/raw/HS_points.xlsx")
df_ct = load_excel("data/raw/CT_points.xlsx")

hs_dev = df_hs["dev"].values
ct_dev = df_ct["dev"].values

comp_dev = quantile_compensation(hs_dev, ct_dev)

df_hs["comp_dev"] = comp_dev

df_hs.to_excel(
    "data/processed/HS_compensated.xlsx",
    index=False
)
