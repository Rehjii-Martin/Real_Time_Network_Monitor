import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def visualize_connections(get_connections_func):
    """
    Visualizes the number of active connections in real-time.

    Args:
        get_connections_func (function): Function to retrieve current connections.
    """
    connection_counts = []

    def animate(i):
        connections = get_connections_func()
        connection_counts.append(len(connections))
        plt.cla()
        plt.plot(connection_counts, label="Active Connections")
        plt.xlabel("Time (s)")
        plt.ylabel("Number of Connections")
        plt.legend(loc="upper left")
        plt.tight_layout()

    ani = FuncAnimation(plt.gcf(), animate, interval=1000)
    plt.show()
