from setuptools import setup,find_packages


long_description = """Provides various methods for anomaly detection.
1. Traditional Statistical Methods:
   - Boxplot Anomaly Detection: Identifies anomalies based on the interquartile range (IQR) method.
   - Gaussian Anomaly Detection: Detects anomalies based on deviations from the mean using standard deviation.
   - Grubbs Test: Identifies outliers using the Grubbs test.
   - Dixon's Q Test: Identifies outliers using Dixon's Q test.
   - Percentile Thresholding: Detects anomalies based on a specified percentile threshold.

2. Histogram-Based Methods:
   - Histogram Anomaly Detection: Detects anomalies based on histogram peaks, indicating multimodal distributions.
   - Histogram-Based Outlier Score: Identifies anomalies based on the density of data points in the histogram.

3. Model-Based Methods:
   - Gaussian Mixture Model: Uses Gaussian mixture models to identify anomalies.
   - Kernel Density Estimation: Estimates the probability density function of the data using kernel density estimation.
   - Exponential Distribution: Detects anomalies based on extreme values using exponential distribution.

4. Nearest Neighbors and Clustering:
   - K Nearest Neighbors (KNN): Identifies anomalies based on distances to nearest neighbors.
   - Local Outlier Factor (LOF): Computes the local density deviation of a given data point with respect to its neighbors.
   - Isolation Forest: Constructs an ensemble of isolation trees for anomaly detection.
   - One-Class SVM: Identifies anomalies by separating data points from the origin in a high-dimensional space.

5. Clustering-Based Methods:
   - KMeans: Uses KMeans clustering to identify anomalies based on centroid distances.
   - DBSCAN: Density-based spatial clustering of applications with noise (DBSCAN) for anomaly detection.

6. Additional Techniques:
   - Z-Score Anomaly Detection: Detects anomalies based on z-scores.
   - Quantile Regression: Identifies anomalies based on quantiles of the data distribution.
   - Anderson-Darling Test: A non-parametric test to assess whether a sample comes from a specified distribution.


Sample Usage

import numpy as np
from detect_anomalies_package.detect_anomalies import DetectAnomalies

# Sample data
data = np.random.normal(loc=0, scale=1, size=100)

# Initialize DetectAnomalies object
anomaly_detector = DetectAnomalies(data)

# Detect anomalies using various methods
anomalies = anomaly_detector.detect_anomalies()

# Print anomalies detected by each method
for method, result in anomalies.items():
    if result[0] is not None:
        print(f"Anomalies detected by {method}: {result[0]}")
    else:
        print(f"No anomalies detected by {method}: {result[1]}")"""
setup(
    name='detect_anomalies_package',
    version='0.0.1',
    description='A Python package for anomaly detection using various techniques.',
    long_description = long_description,
    long_description_content_type = "text/plain",
    author='Nikhil Mugganawar',
    author_email='nikhil.mugganawar@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'scikit-learn'
    ],
)