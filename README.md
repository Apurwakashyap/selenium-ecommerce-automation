# Selenium E-Commerce Automation Framework

## Overview

This project is a scalable Selenium automation framework built using Python and Pytest to automate end-to-end testing of an e-commerce application.

The framework follows the Page Object Model (POM) design pattern and supports data-driven testing, HTML reporting, screenshots on failure, and CI/CD using GitHub Actions.

---

## Features

- Page Object Model (POM)
- Pytest Fixtures
- Data-driven Testing
- Cross Browser Support
- HTML Reports
- Automatic Screenshot Capture
- GitHub Actions CI
- Logging
- Explicit Waits

---

## Tech Stack

- Python
- Selenium
- Pytest
- webdriver-manager
- GitHub Actions

---

## Project Structure

```
project/
│
├── pages/
├── tests/
├── utilities/
├── testdata/
├── reports/
├── screenshots/
└── conftest.py
```

---

## Test Scenarios

- Login
- Invalid Login
- Add Product
- Remove Product
- Checkout
- Logout

---

## Run

```bash
pip install -r requirements.txt

pytest
```

---

## Future Improvements

- Parallel Execution
- Docker Support
- Allure Reports
- Jenkins Pipeline
