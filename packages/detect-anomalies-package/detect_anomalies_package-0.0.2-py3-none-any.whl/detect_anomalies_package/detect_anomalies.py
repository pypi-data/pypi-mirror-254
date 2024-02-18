import numpy as np
from scipy.stats import (
    gaussian_kde,
    norm,
    multivariate_normal,
    kstest,
    anderson_ksamp,
    zscore,
    t,
)
from sklearn.mixture import GaussianMixture
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
from scipy.spatial.distance import mahalanobis
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN


class DetectAnomalies:
    def __init__(self, data):
        if not isinstance(data, (np.ndarray, list)):
            raise TypeError("Data must be a numpy array or list.")
        if isinstance(data, np.ndarray):
            if len(data.shape) != 1:
                raise ValueError(
                    "Univariate anomaly detection requires 1-dimensional data."
                )
        self.data = np.array(data)

    def boxplot_anomaly_detection(self):
        if self.data.ndim > 1:
            raise ValueError("Boxplot method is applicable only to univariate data.")
        if not np.issubdtype(self.data.dtype, np.number):
            raise ValueError("Boxplot method is applicable only to numerical data.")
        q1 = np.percentile(self.data, 25)
        q3 = np.percentile(self.data, 75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        anomalies = [x for x in self.data if x < lower_bound or x > upper_bound]
        if len(anomalies) > 0:
            if self.is_multimodal():
                return (
                    anomalies,
                    "Anomalies detected using Boxplot, and the data appears to be multimodal.",
                )
            else:
                return anomalies, "Anomalies detected using Boxplot."
        else:
            return None, "No anomalies detected using Boxplot."

    def histogram_anomaly_detection(self, bin_size=10):
        if not np.issubdtype(self.data.dtype, np.number):
            raise ValueError("Histogram method is applicable only to numerical data.")
        hist, bin_edges = np.histogram(self.data, bins=bin_size)
        peaks = np.where((hist[1:-1] > hist[:-2]) & (hist[1:-1] > hist[2:]))[0] + 1
        if len(peaks) > 1:
            return (
                self.data,
                "Anomalies detected using Histogram, and the data appears to be multimodal.",
            )
        else:
            return None, "No anomalies detected using Histogram."



    def gaussian_anomaly_detection(self):
        if not np.issubdtype(self.data.dtype, np.number):
            raise ValueError(
                "Gaussian model method is applicable only to numerical data."
            )
        mean = np.mean(self.data)
        std = np.std(self.data)
        anomalies = [x for x in self.data if abs(x - mean) > 2 * std]
        if len(anomalies) > 0:
            return anomalies, "Anomalies detected using Gaussian model."
        else:
            return None, "No anomalies detected using Gaussian model."

    def gaussian_mixture_anomaly_detection(self, n_components=2):
        if not np.issubdtype(self.data.dtype, np.number):
            raise ValueError(
                "Gaussian mixture model method is applicable only to numerical data."
            )
        gmm = GaussianMixture(n_components=n_components)
        gmm.fit(self.data.reshape(-1, 1))
        labels = gmm.predict(self.data.reshape(-1, 1))
        anomalies = [
            self.data[i]
            for i, label in enumerate(labels)
            if label != np.argmax(np.bincount(labels))
        ]
        if len(anomalies) > 0:
            return anomalies, "Anomalies detected using Gaussian Mixture model."
        else:
            return None, "No anomalies detected using Gaussian Mixture model."

    def histogram_based_outlier_score(self):
        if not np.issubdtype(self.data.dtype, np.number):
            raise ValueError(
                "Histogram-based outlier score method is applicable only to numerical data."
            )
        hist, _ = np.histogram(self.data, bins="auto", density=True)
        scores = -np.log(hist)
        threshold = np.percentile(scores, 95)
        anomalies = [val for val, score in zip(self.data, scores) if score > threshold]
        if len(anomalies) > 0:
            return anomalies, "Anomalies detected using Histogram-based Outlier Score."
        else:
            return None, "No anomalies detected using Histogram-based Outlier Score."

    def k_nearest_neighbours(self, k=5):
        if not np.issubdtype(self.data.dtype, np.number):
            raise ValueError(
                "K Nearest Neighbors method is applicable only to numerical data."
            )
        nbrs = NearestNeighbors(n_neighbors=k).fit(self.data.reshape(-1, 1))
        distances, indices = nbrs.kneighbors(self.data.reshape(-1, 1))
        mean_distance = np.mean(distances, axis=1)
        threshold = np.percentile(mean_distance, 95)
        anomalies = [
            self.data[i]
            for i, distance in enumerate(mean_distance)
            if distance > threshold
        ]
        if len(anomalies) > 0:
            return anomalies, "Anomalies detected using K Nearest Neighbors."
        else:
            return None, "No anomalies detected using K Nearest Neighbors."

    def local_outlier_factor(self, k=20):
        if not np.issubdtype(self.data.dtype, np.number):
            raise ValueError(
                "Local Outlier Factor method is applicable only to numerical data."
            )
        lof = LocalOutlierFactor(n_neighbors=k, contamination=0.1)
        labels = lof.fit_predict(self.data.reshape(-1, 1))
        anomalies = [self.data[i] for i, label in enumerate(labels) if label == -1]
        if len(anomalies) > 0:
            return anomalies, "Anomalies detected using Local Outlier Factor."
        else:
            return None, "No anomalies detected using Local Outlier Factor."

    def zscore_anomaly_detection(self):
        if not np.issubdtype(self.data.dtype, np.number):
            raise ValueError("Z-score method is applicable only to numerical data.")
        threshold = 3
        anomalies = [
            self.data[i] for i, z in enumerate(zscore(self.data)) if abs(z) > threshold
        ]
        if len(anomalies) > 0:
            return anomalies, "Anomalies detected using Z-score."
        else:
            return None, "No anomalies detected using Z-score."

    def grubbs_test(self, alpha=0.05):
        if not np.issubdtype(self.data.dtype, np.number):
            raise ValueError("Grubbs test method is applicable only to numerical data.")
        n = len(self.data)
        mean = np.mean(self.data)
        std = np.std(self.data)
        test_statistic = max(abs(val - mean) / std for val in self.data) * np.sqrt(
            n / (n - 2)
        )
        threshold = t.ppf(1 - alpha / (2 * n), n - 2)
        if test_statistic > threshold:
            return self.data, "Anomalies detected using Grubbs test."
        else:
            return None, "No anomalies detected using Grubbs test."

    def dixons_q_test(self, alpha=0.05):
        if not np.issubdtype(self.data.dtype, np.number):
            raise ValueError(
                "Dixon's Q test method is applicable only to numerical data."
            )
        n = len(self.data)
        sorted_data = sorted(self.data)
        q_statistic = (sorted_data[1] - sorted_data[0]) / (
            sorted_data[-1] - sorted_data[0]
        )
        q_critical = 0.297  # For alpha=0.05 and n=10 (reference values)
        if q_statistic > q_critical:
            return self.data, "Anomalies detected using Dixon's Q test."
        else:
            return None, "No anomalies detected using Dixon's Q test."

    def isolation_forest(self):
        if not np.issubdtype(self.data.dtype, np.number):
            raise ValueError(
                "Isolation Forest method is applicable only to numerical data."
            )
        clf = IsolationForest(
            contamination=0.1
        )  # Adjust contamination parameter as needed
        clf.fit(self.data.reshape(-1, 1))
        labels = clf.predict(self.data.reshape(-1, 1))
        anomalies = [self.data[i] for i, label in enumerate(labels) if label == -1]
        if len(anomalies) > 0:
            return anomalies, "Anomalies detected using Isolation Forest."
        else:
            return None, "No anomalies detected using Isolation Forest."

    def one_class_svm(self):
        if not np.issubdtype(self.data.dtype, np.number):
            raise ValueError(
                "One-Class SVM method is applicable only to numerical data."
            )
        clf = OneClassSVM(nu=0.1)  # Adjust nu parameter as needed
        clf.fit(self.data.reshape(-1, 1))
        labels = clf.predict(self.data.reshape(-1, 1))
        anomalies = [self.data[i] for i, label in enumerate(labels) if label == -1]
        if len(anomalies) > 0:
            return anomalies, "Anomalies detected using One-Class SVM."
        else:
            return None, "No anomalies detected using One-Class SVM."

    def kmeans(self, n_clusters=2):
        if not np.issubdtype(self.data.dtype, np.number):
            raise ValueError("KMeans method is applicable only to numerical data.")
        kmeans = KMeans(n_clusters=n_clusters)
        kmeans.fit(self.data.reshape(-1, 1))
        labels = kmeans.labels_
        centroids = [np.mean(self.data[labels == i]) for i in range(n_clusters)]
        anomalies = [
            self.data[i]
            for i, label in enumerate(labels)
            if abs(self.data[i] - centroids[label])
            > 2 * np.std(self.data[labels == label])
        ]
        if len(anomalies) > 0:
            return anomalies, "Anomalies detected using KMeans."
        else:
            return None, "No anomalies detected using KMeans."

    def dbscan(self, eps=0.5, min_samples=5):
        if not np.issubdtype(self.data.dtype, np.number):
            raise ValueError("DBSCAN method is applicable only to numerical data.")
        dbscan = DBSCAN(eps=eps, min_samples=min_samples)
        labels = dbscan.fit_predict(self.data.reshape(-1, 1))
        noise_indices = np.where(labels == -1)[0]
        anomalies = [self.data[i] for i in noise_indices]
        if len(anomalies) > 0:
            return anomalies, "Anomalies detected using DBSCAN."
        else:
            return None, "No anomalies detected using DBSCAN."

    def exponential_distribution(self, alpha=0.05):
        if not np.issubdtype(self.data.dtype, np.number):
            raise ValueError(
                "Exponential Distribution method is applicable only to numerical data."
            )
        mu = np.mean(self.data)
        threshold = np.percentile(self.data, 100 * (1 - alpha))
        anomalies = [val for val in self.data if val > threshold]
        if len(anomalies) > 0:
            return anomalies, "Anomalies detected using Exponential Distribution."
        else:
            return None, "No anomalies detected using Exponential Distribution."

    def kernel_density_estimation(self):
        if not np.issubdtype(self.data.dtype, np.number):
            raise ValueError(
                "Kernel Density Estimation method is applicable only to numerical data."
            )
        kde = gaussian_kde(self.data)
        threshold = np.percentile(self.data, 95)
        anomalies = [val for val in self.data if kde.evaluate(val) < threshold]
        if len(anomalies) > 0:
            return anomalies, "Anomalies detected using Kernel Density Estimation."
        else:
            return None, "No anomalies detected using Kernel Density Estimation."

    def percentile_thresholding(self, percentile=95):
        if not np.issubdtype(self.data.dtype, np.number):
            raise ValueError(
                "Percentile Thresholding method is applicable only to numerical data."
            )
        threshold = np.percentile(self.data, percentile)
        anomalies = [val for val in self.data if val > threshold]
        if len(anomalies) > 0:
            return anomalies, "Anomalies detected using Percentile Thresholding."
        else:
            return None, "No anomalies detected using Percentile Thresholding."

    def quantile_regression(self, alpha=0.05):
        if not np.issubdtype(self.data.dtype, np.number):
            raise ValueError(
                "Quantile Regression method is applicable only to numerical data."
            )
        q_low = np.percentile(self.data, 100 * alpha / 2)
        q_high = np.percentile(self.data, 100 * (1 - alpha / 2))
        anomalies = [val for val in self.data if val < q_low or val > q_high]
        if len(anomalies) > 0:
            return anomalies, "Anomalies detected using Quantile Regression."
        else:
            return None, "No anomalies detected using Quantile Regression."

    def anderson_darling_test(self):
        if not np.issubdtype(self.data.dtype, np.number):
            raise ValueError(
                "Anderson-Darling test method is applicable only to numerical data."
            )
        ad_statistic, _, _ = anderson_ksamp([self.data], midrank=False)
        ad_critical_values = [0.5, 1.0, 1.5, 2.0]  # Add appropriate critical values
        if ad_statistic > ad_critical_values:
            return self.data, "Anomalies detected using Anderson-Darling test."
        else:
            return None, "No anomalies detected using Anderson-Darling test."

    def is_multimodal(self):
        if not np.issubdtype(self.data.dtype, np.number):
            raise ValueError(
                "Multimodal detection is applicable only to numerical data."
            )
        hist, _ = np.histogram(self.data, bins="auto", density=True)
        peak_indices = np.where(hist == np.max(hist))[0]
        return len(peak_indices) > 1

    def detect_anomalies(self):
        methods = [
            self.boxplot_anomaly_detection,
            self.histogram_anomaly_detection,
            self.gaussian_anomaly_detection,
            self.gaussian_mixture_anomaly_detection,
            self.histogram_based_outlier_score,
            self.k_nearest_neighbours,
            self.local_outlier_factor,
            self.zscore_anomaly_detection,
            self.grubbs_test,
            self.dixons_q_test,
            self.isolation_forest,
            self.one_class_svm,
            self.kmeans,
            self.dbscan,
            self.exponential_distribution,
            self.kernel_density_estimation,
            self.percentile_thresholding,
            self.quantile_regression,
            self.anderson_darling_test,
        ]

        anomalies = {}
        for method in methods:
            try:
                anomalies[method.__name__] = method()
            except Exception as e:
                anomalies[method.__name__] = (None, str(e))

        return anomalies
