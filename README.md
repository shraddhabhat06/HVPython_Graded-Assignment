# HVPython_Graded-Assignment
This repository contains three Python scripts that perform different tasks: password strength checking, CPU monitoring, and configuration file extraction via a Flask API.

## PasswordChecker.py
**Functionality:**
- Ensures password security by checking length, uppercase, lowercase, digit, and special character requirements.

**Run the script:**
```sh
python PasswordChecker.py
```
**Input:**
- Enter a password when prompted.

**Output:**
- Indicates if the password is strong or lists the missing criteria.

## CPUMonitor.py
**Functionality:**
- Continuously monitors CPU usage and raises an alert if usage exceeds 80%.

**Run the script:**
```sh
python CPUMonitor.py
```
**Output:**
- Prints CPU usage percentage and alerts when it surpasses the threshold.
- Press `Ctrl + C` to stop monitoring.

## DataExtracter.py
**Functionality:**
- Reads `config.ini` and exposes the configuration via a REST API.

**Run the script:**
```sh
python DataExtracter.py
```
**API Endpoint:**
- Configuration data is accessible at `http://127.0.0.1:5000/config`

**Modify Configuration:**
- Update `config.ini` to change settings before running the script.

## Requirements
Ensure the required dependencies are installed:
```sh
pip install flask psutil
```
