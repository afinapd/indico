# Indico Automation Testing Project

This repository contains automated test suites for API, Web UI, and Mobile App testing using Python, Behave, and Appium.

## Project Structure

### 1. API Automation (`automation_api/`)
API testing suite for the Petstore Swagger API.
- Uses Python requests library and Behave BDD framework
- Test scenarios include:
  - Adding new pets
  - Finding pets by status (available)
  - Finding pets by status (pending)

API: [Petstore Swagger](https://petstore.swagger.io/#/)

### 2. Web UI Automation (`automation_web/`)
Web UI testing suite for a demo registration form.
- Uses Python Selenium WebDriver and Behave BDD framework
- Test scenarios include:
  - Form submission with dummy profile
  - Date picker interaction
  - File upload functionality

Website: [Test Automation Practice](https://testautomationpractice.blogspot.com/)

### 3. Mobile App Automation (`automation_app/`)
Mobile app testing suite for Trust Wallet Android app.
- Uses Python Appium and Behave BDD framework
- Test scenarios include:
  - Wallet creation flow
  - Passcode setup
  - Biometric authentication handling
  - Backup skip functionality

App: [Trust Wallet](https://trustwallet.com/id)

## Demo Videos How To Run

- API Automation Demo: [Watch Demo](https://drive.google.com/file/d/132qDKOxTpc99i5Hy10qYM1-miRAMTsIL/view?usp=sharing)
- Web UI Automation Demo: [Watch Demo](https://drive.google.com/file/d/1X4uTuXFpE-4SLwNVuNVyNFvHn1lfjl6I/view?usp=sharing)
- Mobile App Automation Demo: [Watch Demo](https://drive.google.com/file/d/1TYLuU86znELHCo0SGeasOlivs2lkIMrq/view?usp=sharing)

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/afinapd/indico.git
cd indico
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Unix/macOS
```

3. Install dependencies for each project:
```bash
cd automation_api && pip install -r requirements.txt
cd ../automation_web && pip install -r requirements.txt
cd ../automation_app && pip install -r requirements.txt
```

## Running Tests

### API Tests
```bash
cd automation_api
behave features/pet.feature
```

### Web UI Tests
```bash
cd automation_web
behave features/registration.feature
```

### Mobile App Tests
```bash
cd automation_app
behave features/wallet_creation.feature
```

## Project Architecture

- Uses Page Object Model design pattern for web and mobile testing
- Implements BDD with Gherkin syntax for clear test specifications
- Maintains separation of concerns between test steps, page objects, and test data
- Includes comprehensive logging for better debugging
- Follows Python best practices and coding standards