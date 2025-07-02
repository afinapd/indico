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

### Pre-run Checklist
1. Connect Android device via USB and enable USB debugging
2. Verify device is connected:
```bash
adb devices
# Should show something like:
# RR8R708RESJ    device
```

3. Kill any existing Appium server:
```bash
pkill -f appium
```

4. Start Appium server in a new terminal:
```bash
appium --log-level debug
```

### Running the Tests

1. Run wallet creation test:
```bash
behave features/wallet_creation.feature -f pretty
```

2. Or run with specific tags:
```bash
behave --tags=@test_wallet_creation -f pretty
```

### Troubleshooting

If test fails:
1. Check device connection:
```bash
adb devices
```

2. Restart Appium server:
```bash
pkill -f appium
appium --log-level debug
```

3. Verify:
- Trust Wallet APK exists in correct path
- Trust Wallet app is not running in background
- Device screen is unlocked and awake

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
