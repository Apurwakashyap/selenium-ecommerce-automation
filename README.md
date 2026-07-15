# Selenium E-Commerce Automation Framework

## Overview

A robust and scalable Selenium automation framework developed using **Python**, **Pytest**, and the **Page Object Model (POM)** design pattern to automate end-to-end testing of an e-commerce web application.

The framework is designed with maintainability and reusability in mind. It supports data-driven testing, cross-browser execution, HTML reports, screenshots on test failure, and continuous integration using GitHub Actions.

---

## Features

- Page Object Model (POM)
- Pytest Framework
- Data-Driven Testing
- Cross Browser Support (Chrome & Edge)
- Explicit Waits
- HTML Test Reports
- Automatic Screenshot Capture on Failure
- GitHub Actions CI
- Reusable Utility Functions

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Selenium WebDriver | Browser Automation |
| Pytest | Test Framework |
| webdriver-manager | Driver Management |
| GitHub Actions | Continuous Integration |
| HTML Reports | Test Reporting |

---

## Framework Architecture

```
selenium-ecommerce-automation/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_checkout.py
│
├── utilities/
│
├── testdata/
│
├── reports/
│
├── screenshots/
│
├── conftest.py
│
└── requirements.txt
```

---

## Test Scenarios

### Authentication

- Valid Login
- Invalid Login
- Logout

### Inventory

- Verify Products
- Add Product to Cart
- Remove Product

### Cart

- Verify Cart Items
- Remove Item
- Continue Shopping

### Checkout

- Complete Checkout
- Verify Order Confirmation

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run all tests

```bash
pytest
```

Generate HTML report

```bash
pytest --html=reports/report.html
```

---

## Project Highlights

- Clean Page Object Model architecture
- Modular and reusable code
- Easy to extend with new test cases
- Supports continuous integration using GitHub Actions
- Automatic screenshot capture for failed test cases

---

## Future Improvements

- Docker support
- Parallel execution using pytest-xdist
- Allure reporting
- Jenkins Pipeline Integration
- Browser execution through command-line arguments

---

## Author

Apurwa Kashyap
