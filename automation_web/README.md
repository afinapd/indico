# Web UI Automation Framework

This project implements UI automation testing for the Test Automation Practice website using Python with Behave (Cucumber) and Selenium WebDriver following the Page Object Model pattern.

## Project Structure
```
automation_web/
├── features/
│   ├── pages/           # Page Object Model implementations
│   ├── steps/           # Step definitions
│   ├── environment.py   # Behave environment hooks
│   └── registration_form.feature  # Feature files
└── requirements.txt     # Project dependencies
```

## Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests
To run all tests:
```bash
behave
```

To run specific feature:
```bash
behave features/registration_form.feature
```

## Test Scenarios
1. Registration Form Submission
   - Navigate to the test automation practice website
   - Fill in form with dummy data
   - Select date using date picker
   - Upload a file
   - Submit form and verify success

## Notes
- The framework uses Chrome WebDriver by default
- WebDriver is managed automatically using webdriver-manager
- Tests follow Page Object Model pattern for better maintainability
