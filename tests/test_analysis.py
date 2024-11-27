import unittest

from utils.analysis import detect_anomalies


class TestAnalysis(unittest.TestCase):
    def test_detect_anomalies(self):
        sample_connections = [
            {"remote_ip": "192.168.1.1"},
            {"remote_ip": "192.168.1.1"},
            {"remote_ip": "10.0.0.1"},
            {"remote_ip": "10.0.0.2"},
            {"remote_ip": "10.0.0.3"},
        ]
        anomalies = detect_anomalies(sample_connections)
        self.assertIsInstance(anomalies, list)


if __name__ == "__main__":
    unittest.main()
