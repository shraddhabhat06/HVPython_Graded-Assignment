import psutil
import time

"""
Monitors CPU usage and raises an alert if it exceeds a defined threshold.

- Continuously checks CPU usage percentage at 1-second intervals.
- Alerts when CPU usage exceeds the specified threshold (default: 80%).
- Runs indefinitely until manually stopped by the user.

Args:
    threshold (int): The CPU usage percentage threshold for triggering an alert.

Returns:
    None
"""

# Define the CPU usage threshold
CPU_THRESHOLD = 80

def get_cpu_usage():
    """Returns the current CPU usage percentage."""
    return psutil.cpu_percent(interval=1)

def check_cpu_usage(threshold):
    """Checks if CPU usage exceeds the threshold and returns an alert message."""
    cpu_usage = get_cpu_usage()
    if cpu_usage > threshold:
        print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
    return cpu_usage

def monitor_cpu(threshold):
    """Continuously monitors CPU usage until interrupted."""
    print("Monitoring CPU usage...")
    try:
        while True:
            check_cpu_usage(threshold)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

monitor_cpu(CPU_THRESHOLD)
