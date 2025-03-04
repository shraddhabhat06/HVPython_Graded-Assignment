import configparser
import json
import os
from flask import Flask, jsonify

"""
    Reads, parses, and serves configuration data from an INI file using Flask.

    - Reads a configuration file (`config.ini`) using `configparser`.
    - Stores the parsed configuration data in a global dictionary.
    - Displays the configuration in a readable format.
    - Provides an API endpoint (`/config`) to return the configuration as JSON.
    - Starts a Flask server to serve configuration data.

    Args:
        file_path (str): The path to the configuration file.

    Returns:
        dict: Parsed configuration data with section names as keys 
              and corresponding key-value pairs as values.
"""


# Flask App
app = Flask(__name__)

# Global dictionary to store configuration
config_data = {}

# Function to Read Configuration File
def read_config(file_path):
    global config_data  # Modify global variable

    if not os.path.exists(file_path):
        raise FileNotFoundError("Configuration file not found.")
    
    config = configparser.ConfigParser()
    config.read(file_path)
    
    config_data = {section: dict(config.items(section)) for section in config.sections()}

# Function to Pretty Print Configuration Data
def display_config():
    output = "\nConfiguration File Parser Results:\n"
    for section, values in config_data.items():
        output += f"\n{section}:\n"
        for key, value in values.items():
            output += f"- {key}: {value}\n"
    return output.strip()

# API Endpoint to Get Configuration Data
@app.route("/config", methods=["GET"])
def get_config():
    return jsonify(config_data)

if __name__ == "__main__":
    try:
        read_config("config.ini")
        print(display_config()) 

        print("\nStarting API Server at http://127.0.0.1:5000/config")
        app.run(debug=True)
    
    except FileNotFoundError as e:
        print("Error:", e)
    except Exception as e:
        print("Unexpected Error:", e)
