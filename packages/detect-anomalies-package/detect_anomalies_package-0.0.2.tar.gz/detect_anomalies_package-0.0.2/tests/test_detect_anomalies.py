import unittest
import numpy as np
from detect_anomalies_package.detect_anomalies import DetectAnomalies

class TestDetectAnomalies(unittest.TestCase):
    def setUp(self):
        # Sample data for testing
        self.data_univariate = np.array([1, 2, 3, 4, 5])
        self.data_multivariate = np.array([[1, 2], [3, 4], [5, 6]])

    def test_univariate_anomaly_detection_methods(self):
        detector = DetectAnomalies(self.data_univariate)
        
        # Test boxplot_anomaly_detection method
        anomalies, message = detector.boxplot_anomaly_detection()
        self.assertIsNone(anomalies)
        self.assertEqual(message, "No anomalies detected using Boxplot.")
        
        # Test histogram_anomaly_detection method
        anomalies, message = detector.histogram_anomaly_detection(bin_size=2)
        self.assertIsNone(anomalies)
        self.assertEqual(message, "No anomalies detected using Histogram.")
        
        # Test gaussian_anomaly_detection method
        anomalies, message = detector.gaussian_anomaly_detection()
        self.assertIsNone(anomalies)
        self.assertEqual(message, "No anomalies detected using Gaussian model.")
        
        # Add more tests for other univariate anomaly detection methods

    def test_multivariate_anomaly_detection_methods(self):
        # Test initialization with multivariate data
        with self.assertRaises(ValueError):
            detector = DetectAnomalies(self.data_multivariate)
            
    def test_invalid_input(self):
        # Test initialization with invalid input type
        with self.assertRaises(TypeError):
            detector = DetectAnomalies("invalid data")

    def test_multimodal_data(self):
        # Test histogram_anomaly_detection method with multimodal data
        detector = DetectAnomalies(np.array([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
        anomalies, message = detector.histogram_anomaly_detection(bin_size=2)
        self.assertIsNone(anomalies)
        self.assertEqual(message, "No anomalies detected using Histogram.")

    # Add more test methods to cover other scenarios

if __name__ == "__main__":
    unittest.main()