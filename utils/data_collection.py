# utils/data_collection.py

import socket

import psutil


def get_active_connections():
    """
    Retrieves a list of active network connections with hostnames and IP addresses.

    Returns:
        list: A list of dictionaries containing connection details.
    """
    connections = []
    for conn in psutil.net_connections(kind="inet"):
        # Filter for established connections with a remote address
        if conn.status == psutil.CONN_ESTABLISHED and conn.raddr:
            local_ip = conn.laddr.ip
            local_port = conn.laddr.port
            remote_ip = conn.raddr.ip
            remote_port = conn.raddr.port
            try:
                # Resolve hostname from IP address
                hostname = socket.gethostbyaddr(remote_ip)[0]
            except socket.herror:
                hostname = "Unknown"
            connections.append(
                {
                    "local_ip": local_ip,
                    "local_port": local_port,
                    "remote_ip": remote_ip,
                    "remote_port": remote_port,
                    "hostname": hostname,
                }
            )
    return connections
