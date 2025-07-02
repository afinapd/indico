# Trust Wallet Mobile App Automation

This project contains automated tests for Trust Wallet mobile app using Appium, Behave (Cucumber for Python), and Page Object Model.

## Prerequisites

1. Python 3.8 or higher
2. Appium Server
3. Android SDK and emulator/real device
4. Trust Wallet APK

## Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Unix/macOS
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables in `.env`:
```
DEVICE_NAME=your_device_name
APP_PATH=/path/to/trustwallet.apk
```

4. Start Appium server:
```bash
appium
```

## Running Tests

To run all tests:
```bash
behave features/wallet_creation.feature
```

To run specific tags:
```bash
behave --tags=@test_wallet_creation
```

## Project Structure

```
automation_app/
├── features/
│   ├── pages/
│   │   ├── base_page.py
│   │   └── wallet_page.py
│   ├── steps/
│   │   └── wallet_steps.py
│   ├── environment.py
│   └── wallet_creation.feature
├── test_data/
├── requirements.txt
└── README.md
```
