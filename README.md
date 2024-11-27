# Real-Time Network Activity Monitor

## Introduction

The Real-Time Network Activity Monitor is a tool designed to track and analyze real-time network activity on a system. It displays all active connections with process names, hostnames, IP addresses, and ports. The monitor detects unusual traffic patterns, notifies the user, and logs historical data for deeper analysis.

## Features

- **Detailed Active Connections Display**: Shows all active network connections with process names, hostnames, IP addresses, and ports.
- **Anomaly Detection**: Detects unusual traffic patterns using statistical methods.
- **Data Logging**: Logs detailed historical network data to a CSV file.
- **Real-Time Visualization**: Provides a real-time updating table of active connections.

## Prerequisites

- Python 3.x
- Pip

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/real_time_network_monitor.git
   cd real_time_network_monitor

   ```

2. **Create and Activate Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

## Usage

Run the network monitor:

```bash
python network_monitor.py
```

The application will:

### Display detailed connection information in the console.

### Show a real-time updating table of active connections.

## Testing

Run unit tests:

```bash
python -m unittest discover tests
```

## Deployment

### PyInstaller

Create an executable:

```bash
pyinstaller --onefile network_monitor.py
```

### Docker

Build Docker image:

```bash
docker build -t network-monitor .
```

Run Docker container:

```bash
docker run --rm -it --name network-monitor network-monitor
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
