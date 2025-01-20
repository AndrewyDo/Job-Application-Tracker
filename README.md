# Job Tracker

## Overview
The **Job Tracker** project is a Python-based application designed to help users track their job applications directly from their Gmail inbox. By leveraging the Gmail API, this program searches for emails that contain specific keywords related to job applications, counts the number of applications submitted, and displays the results in a user-friendly format.

## Features
- **Authenticate with Gmail**: Securely access your Gmail account using OAuth 2.0.
- **Keyword-Based Search**: Search your inbox for job application-related emails using customizable keywords.
- **Track Total Applications**: Display the total number of job applications submitted.
- **Modular Design**: Easily expand functionality, such as adding advanced analytics or integrating with external tools.

## Prerequisites
- Python (version 3.8 or higher recommended)
- Gmail API enabled in your [Google Cloud Console](https://console.cloud.google.com/).
- `credentials.json`: Download the credentials file for your Google Cloud project.
- Basic familiarity with Python and virtual environments.

## Installation
```bash
- git clone https://github.com/your-username/job-tracker.git
- cd job-tracker
- python3 -m venv .venv
- source .venv/bin/activate
- pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

## Usage
When you run the script for the first time, it will open a browser window. Log into your Gmail account and grant the application read-only access to your inbox. A token.pickle file will be created to store your authentication token for subsequent runs. The script will search your inbox for job application-related emails based on the specified keywords and display the total count in the terminal.

## Customization
You can add or modify the keywords used to search for job application emails. Update the keywords list in the script:
```bash
keywords = [
      'Thank you for applying',
      'Your application was sent',
      'We received your application',
      'Application submitted successfully'
]
```

## License
This project is licensed under the MIT License.
