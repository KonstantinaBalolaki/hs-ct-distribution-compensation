import numpy as np


def quantile_compensation(hs_dev, ct_dev, n_quantiles=1000):
    """
    Apply quantile mapping to transform HandySCAN deviations
    into CT-reference-equivalent deviations.
    """

    hs_dev = np.asarray(hs_dev)
    ct_dev = np.asarray(ct_dev)

    hs_dev = hs_dev[~np.isnan(hs_dev)]
    ct_dev = ct_dev[~np.isnan(ct_dev)]

    q = np.linspace(0, 1, n_quantiles)

    hs_q = np.quantile(hs_dev, q)
    ct_q = np.quantile(ct_dev, q)

    compensated_dev = np.interp(
        hs_dev,
        hs_q,
        ct_q
    )

    return compensated_dev
