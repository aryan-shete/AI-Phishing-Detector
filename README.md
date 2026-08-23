# AI Phishing Detector

An AI-powered phishing email detector that analyzes email content for suspicious keywords and URLs to identify potential phishing attacks.

## Features

* Detects suspicious phishing-related keywords
* Identifies suspicious URLs and domains
* Generates a phishing risk score
* Classifies emails into Low, Medium, or High risk
* Provides reasons for the detection result
* Simple web interface built with Flask

## Technologies Used

* Python
* Flask
* HTML
* CSS
* Regular Expressions

## Project Structure

```text
AI-Phishing-Detector/
│
├── app.py
├── detector.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## Installation

Clone the repository:

```bash
git clone https://github.com/aryan-shete/AI-Phishing-Detector.git
```

Move into the project folder:

```bash
cd AI-Phishing-Detector
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Then open the application in your browser:

```text
http://127.0.0.1:5000
```

## How It Works

The application analyzes the submitted email for suspicious keywords such as:

* urgent
* verify
* click here
* update payment
* password
* account suspended

It also checks URLs for suspicious domains such as:

* bit.ly
* tinyurl
* .ru
* .xyz

Based on the detected indicators, the application calculates a risk score and classifies the email as:

* Low Risk
* Medium Risk
* High Risk

## Future Improvements

* Machine Learning-based phishing detection
* Email header analysis
* Domain reputation checking
* Dataset training using real phishing emails
* Improved URL analysis
* User authentication and detection history

## Author

**Aryan Shete**

B.Sc. Cyber Security Student
