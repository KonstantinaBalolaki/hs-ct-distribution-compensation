# Distribution-Based Compensation of HandySCAN Measurements to a CT Reference

This project investigates statistical compensation between HandySCAN and CT metrology systems using empirical distribution alignment and quantile-based compensation mapping.

The framework preserves geometric coordinates while compensating deviation distributions.

Methodology
Import deviation point clouds
Clean outliers
Compute empirical CDFs
Apply quantile mapping
Compare distributions using:
Wasserstein distance
Histogram comparison
CDF comparison

Raw ASCII
↓
Cleaning
↓
Distribution Extraction
↓
Quantile Mapping
↓
Compensated Distribution
↓
Metrics & Plots
