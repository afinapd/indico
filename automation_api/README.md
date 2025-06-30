# API Automation Framework

This project implements API automation testing for the Swagger Petstore API using Python with Behave (Cucumber) following the Page Object Model pattern.

## Project Structure
```
automation_api/
├── features/
│   ├── pages/           # Page Object Model implementations
│   ├── steps/           # Step definitions
│   ├── environment.py   # Behave environment hooks
│   └── pet.feature      # Feature files
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
behave features/pet.feature
```

## Test Scenarios
1. Add New Pet
   - Sends POST request to add a new pet
   - Verifies response status and pet details

2. Find Pets by Status
   - Tests retrieving pets by "available" status
   - Tests retrieving pets by "pending" status
   - Verifies all returned pets have the correct status
