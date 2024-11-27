import numpy as np


def detect_anomalies(connections):
    """
    Detects anomalies in the list of network connections based on connection frequency.

    Args:
        connections (list): A list of connection dictionaries.

    Returns:
        list: A list of anomalies detected.
    """
    ip_list = [conn["remote_ip"] for conn in connections]
    unique_ips, counts = np.unique(ip_list, return_counts=True)
    mean = np.mean(counts)
    std_dev = np.std(counts)
    anomalies = []
    for ip, count in zip(unique_ips, counts):
        # Compute the z-score for each IP
        z_score = (count - mean) / std_dev if std_dev > 0 else 0
        if np.abs(z_score) > 2:  # Threshold for anomaly detection
            anomalies.append({"ip": ip, "count": count, "z_score": z_score})
    return anomalies
