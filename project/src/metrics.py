from scipy.stats import wasserstein_distance

def compute_wasserstein(a,b):
    return wasserstein_distance(a,b)
