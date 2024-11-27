import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation


def visualize_connections(get_connections_func):
    """
    Visualizes active connections in real-time using a table.

    Args:
        get_connections_func (function): Function to retrieve current connections.
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    fig.canvas.manager.set_window_title("Real-Time Network Connections")

    def animate(i):
        connections = get_connections_func()
        if connections:
            df = pd.DataFrame(connections)
            df = df[
                [
                    "process_name",
                    "local_ip",
                    "local_port",
                    "remote_ip",
                    "remote_port",
                    "hostname",
                ]
            ]
            ax.clear()
            ax.axis("off")
            table = ax.table(cellText=df.values, colLabels=df.columns, loc="center")
            table.auto_set_font_size(False)
            table.set_fontsize(8)
            table.auto_set_column_width(col=list(range(len(df.columns))))
            plt.tight_layout()
        else:
            ax.clear()
            ax.text(
                0.5,
                0.5,
                "No Active Connections",
                horizontalalignment="center",
                verticalalignment="center",
                fontsize=12,
            )
            ax.axis("off")

    ani = FuncAnimation(fig, animate, interval=3000)  # Update every 3 seconds
    plt.show()
