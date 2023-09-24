
# Flask Attendance App Documentation

## Introduction

The Flask Attendance App is a web-based application designed for marking attendance. This documentation provides an overview of the app's functionality, prerequisites for usage, installation instructions, and usage guidelines.

## Prerequisites

Before using the Flask Attendance App, ensure you have the following prerequisites installed:

- Python 3.x
- Flask
- Pandas
- gspread
- Google Sheets API credentials (JSON file)
- uuid
- os

## Installation

Follow these steps to install and set up the Flask Attendance App:


1. Install the required dependencies:
   ```
    pip install flask pandas gspread
   ```
   ```
    pip install subprocess
     ```

4. Set up Google Sheets API credentials:
   - Create a Google Cloud project.
   - Enable the Google Sheets API for your project.
   - Generate API credentials in JSON format and save them to a file (e.g., `credentials.json`).
   - Place the `credentials.json` file in the project directory.

## Usage

To use the Flask Attendance App, follow these steps:

1. Start the Flask app:
   ```
   python app.py
   ```

2. Open a web browser and navigate to [http://localhost:5000/](http://localhost:5000/).

3. On the homepage, you'll see a form that requires you to enter your name and email address.

4. Fill in your name and email address.

5. Click the "Submit" button to mark your attendance.

6. The app will verify your credentials, including your email, MAC address, and Wi-Fi network name.

7. Depending on the time of day and verification results, you'll receive one of the following messages:
   - "Already Marked": If you have already marked your attendance for the day.
   - "Unmarked": If it's the right time to mark attendance and your credentials are valid.
   - "Time over": If it's past the attendance marking time.
   - "Window will open at 9 am": If it's not yet time to mark attendance.

## Project Structure

The Flask Attendance App project is structured as follows:

- **app.py**: The main Flask application that handles routes and views.
- **static**: Directory containing static assets such as CSS files.
- **templates**: Directory containing HTML templates used by the app.
- **email.xlsx**: An Excel file used for storing email-related data.
- **credentials.json**: JSON file containing Google Sheets API credentials (not included in the repository).

### Code Analysis

1. **Imports**: The code begins by importing various Python modules and libraries, including Flask, subprocess, uuid, json, ast, datetime, gspread, pandas, os, and signal. These modules are used for various purposes in the application.

2. **Flask App Setup**: An instance of the Flask web application is created with `app = Flask(__name__)`.

3. **Functions for Gathering System Information**:
   - `get_connected_wifi_name()`: This function uses the `subprocess` module to obtain the name of the currently connected Wi-Fi network.
   - `get_mac_address()`: This function retrieves the MAC address of the system.
   
4. **Open URL in Browser**: The code opens a web browser to the URL "http://127.0.0.1:5000/".

5. **Routes and Views**:
   - The `/` and `/home` routes are defined, and the `home()` function is associated with them. This function renders the "index.html" template.
   - The `/result` route is defined for handling form submissions. The `result()` function handles form data, checks the email against credentials, and marks attendance accordingly.

6. **Google Sheets Integration**: The code interacts with Google Sheets to mark attendance and verify credentials. It uses the `gspread` library to connect to a Google Sheets document named "attendance."

7. **Credential Verification and Attendance Marking**:
   - `get_cred(Email)`: Retrieves user credentials (Name, Batch, MAC, WiFi) based on their email.
   - `verf_cred(Email)`: Verifies user credentials by comparing the system's MAC address and Wi-Fi network name with the stored values.
   - `mark_attd(Email, name, batch)`: Marks attendance in the Google Sheets document if credentials are verified.
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

With this documentation, users and contributors will have a clear understanding of your Flask Attendance App, its requirements, and how to use it.
