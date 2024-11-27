import threading
import time
from datetime import datetime

from utils.analysis import detect_anomalies
from utils.data_collection import get_active_connections
from utils.logging_module import log_connections
from utils.visualization import visualize_connections


def main():
    """
    Main function to run the network activity monitor.
    """
    log_file = "network_logs.csv"
    monitoring_interval = 5  # in seconds

    def monitor():
        while True:
            connections = get_active_connections()
            anomalies = detect_anomalies(connections)
            if anomalies:
                print(f"\n[ALERT] Anomalies detected at {datetime.now()}:")
                for anomaly in anomalies:
                    print(
                        f"IP: {anomaly['ip']}, Count: {anomaly['count']}, Z-Score: {anomaly['z_score']:.2f}"
                    )
            log_connections(connections, log_file=log_file)
            time.sleep(monitoring_interval)

    # Run the monitor in a separate thread
    monitor_thread = threading.Thread(target=monitor)
    monitor_thread.daemon = True
    monitor_thread.start()

    # Start visualization in the main thread
    visualize_connections(get_active_connections)


if __name__ == "__main__":
    main()
