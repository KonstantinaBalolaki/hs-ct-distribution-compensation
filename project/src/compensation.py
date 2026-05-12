import numpy as np

def quantile_compensation(hs_dev, ct_dev):

    q = np.linspace(0,1,1000)

    hs_q = np.quantile(hs_dev, q)
    ct_q = np.quantile(ct_dev, q)

    comp = np.interp(
        hs_dev,
        hs_q,
        ct_q
    )

    return comp
