import os
from datetime import datetime

import pandas as pd


def log_connections(connections, log_file="network_logs.csv"):
    """
    Logs the network connections to a CSV file.

    Args:
        connections (list): A list of connection dictionaries.
        log_file (str): The path to the log file.
    """
    df = pd.DataFrame(connections)
    df["timestamp"] = datetime.now()
    write_header = not os.path.isfile(log_file)
    df.to_csv(log_file, mode="a", header=write_header, index=False)
