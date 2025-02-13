import psutil
import time

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
