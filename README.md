# Amazon India Web Automation Framework

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Selenium](https://img.shields.io/badge/Selenium-4+-43B02A?logo=selenium&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Framework-0A9EDC?logo=pytest&logoColor=white)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

## Overview

This project is a Python-based Selenium automation framework built using **Selenium WebDriver**, **Pytest**, and the **Page Object Model (POM)** to automate key user journeys on Amazon India.

The framework covers END-TO-END workflows across the **Homepage**, **Sign-in**, **Product Search**, **Search Results**, **Product Selection**, **Add to Cart**, **Cart Management**, **Address Selection**, **Payment Selection**, and **Checkout** modules. It validates one of the most commonly used customer purchase journeys up to the point where the **"Use this payment method"** button on the Checkout page becomes enabled, without placing any actual orders or performing real transactions.

In addition to end-to-end workflow automation, the framework also automates FUNCTIONAL sign-in scenarios for some valid and invalid input combinations through both **MODULAR** and **DATA-DRIVEN** test execution.

---

# Key Features:
- Python Selenium WebDriver
- Hybrid Automation Framework (Page Object Model, Pytest, Data-Driven Testing, and Modular Design)
- Centralized Configuration Management
- Utility Classes
- Explicit Wait-Based Synchronization
- Cross-Browser Support (Chrome, Firefox, and Edge)
- HTML Reporting using `pytest-html`
- Screenshot Capture on Assertion Failure
- End-to-End and Functional Test Automation
- Maintainable, Scalable, and Reusable Framework Design
  
# Tech Stack

| Category | Technology |
|----------|------------|
| **Programming Language** | Python |
| **Automation Tool** | Selenium WebDriver |
| **Testing Framework** | Pytest |
| **Design Pattern** | Page Object Model (POM) |
| **Reporting** | pytest-html |
| **Test Data** | Excel (xlrd) |
| **Configuration Management** | ConfigParser (`config.ini`) |
| **Supported Browsers** | Google Chrome, Mozilla Firefox, Microsoft Edge |

# Framework Design: **Hybrid Automation Framework**

- **Page Object Model (POM)** for modular and maintainable test automation.
- **Base Page** class to centralize common Selenium actions and explicit wait methods.
- **Base Test** class containing reusable business flows and common assertion logic.
- **Pytest** for setup and teardown, fixture management, and test execution.
- **Explicit Waits** (WebDriverWait) for reliable element synchronization.
- **Data-Driven** Testing using Excel files to execute sign-in tests with multiple valid and invalid credential combinations.
- Configuration Management using config.ini to externalize application URL, browser, and credentials.
- Reusable Utility Modules for configuration reading, credential management, test data handling, and screenshot path generation.
- Automatic **Screenshot** Capture on assertion failures.
- **HTML Test Reports** generated using pytest-html.

# Project Structure

```
AMAZON_Checkout_Workflow_Automation/
│
├── Configurations/
│   └── config.ini
│
├── PageObject/
│   ├── __init__.py
│   ├── BasePage.py
│   ├── homepage.py
│   ├── signinpage.py
│   ├── searchresults.py
│   ├── productdetails.py
│   ├── cartconfirmation.py
│   ├── cart.py
│   └── checkout.py
│
├── TestCase/
│   ├── __init__.py
│   ├── conftest.py
│   ├── BaseTest.py
│   ├── test_homepage.py
│   ├── test_signin.py
│   ├── test_signin_inputs.py
│   └── test_checkoutworkflow.py
│
├── TestData/
│   └── SigninInput.xlsx
│
├── Utilities/
│   ├── __init__.py
│   ├── ReadConfigini.py
│   ├── ReadCredentials.py
│   ├── ReadExcelFile.py
│   ├── ReadAddressData.py
│   └── ReadScreenshotPath.py
│
├── requirements.txt
├── Screenshots/
└── Reports/

```

---

# Automated Test Scenarios

### Functional Testing

| Test ID | Scenario |
|---------|----------|
| **FT-001** | Sign-in page verification |
| **FT-002** | Sign-in with valid credentials |
| **FT-003** | Sign-in with no input |
| **FT-004** | Sign-in with an invalid email address |
| **FT-005** | Sign-in with an invalid mobile number |
| **FT-006** | Sign-in with an incorrect email address or mobile number |
| **FT-011** | Homepage verification |

### Data-Driven Testing

| Test ID | Scenario |
|---------|----------|
| **DD-001** | Sign-in validation using multiple valid and invalid credential combinations from an Excel data source |

### End-to-End (E2E) Testing

| Test ID | Scenario |
|---------|----------|
| **E2E-001** | Complete checkout using an existing address and UPI (Scan & Pay) |
| **E2E-002** | Complete checkout using Net Banking through the Buy Now workflow |
| **E2E-003** | Increase and decrease product quantity, then verify price consistency |
| **E2E-004** | Delete all products from the cart |
| **E2E-005** | Add a product from the Search Results page |
| **E2E-006** | Complete checkout after adding multiple products to the cart |
| **E2E-007** | Select and verify a new delivery address |
| **E2E-008** | Complete checkout using the Gift option from the Cart page |

> **Note: The checkout automation validates the workflow only up to the payment confirmation stage by verifying that the *"Use this payment method"* button becomes enabled after a valid payment option is selected. The framework *does not place actual orders***.

---

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.12 or later
- pip (Python package manager)
- Google Chrome, Mozilla Firefox, or Microsoft Edge
- Git (for cloning the repository)
- Internet connection (required to access Amazon India)
- All required Python dependencies listed in `requirements.txt`

**Note:** This project uses **Selenium 4+**, which includes **Selenium Manager** for automatic browser driver management. No manual installation of ChromeDriver, GeckoDriver, or EdgeDriver is required.

---

# How to Run

### Clone Repository

```bash
git clone https://github.com/poojanokhwal04-tech/amazon-india-web-automation-framework.git
```

### Navigate to the Project Directory

```bash
cd <project-directory>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run All Tests

```bash
pytest -vs
```

### Generate HTML Report

```bash
pytest --html=Reports\\report.html --self-contained-html
```

---

# Challenges Addressed

- Handling Dynamic Web Elements
- Checkout Flow Complexity
- Inconsistent User Interfaces and Popups Across Test Executions
- Unexpected application behavior *disrupting* the expected automation workflow
- Live vs. Automated Execution Behavior Differences
- Synchronization Challenges Despite Using Explicit Waits
- Certain Payment Method Selection Failure
- OTP Verification Challenges During Authentication
- Bot Detection and CAPTCHA Verification
- Framework Design and Reusability Complexity

---

# Future Improvements

- Implement **CI/CD pipelines** using Jenkins.
- Add **Docker** support for a portable and consistent execution environment.
- Configure **Selenium Grid** for parallel cross-browser execution.
- Replace remaining `sleep()` statements with more robust synchronization strategies where feasible.
- Integrate advanced reporting tools such as **Allure Reports**.
- Expand data-driven testing to additional workflows beyond authentication.
- Add comprehensive logging using Python's `logging` module.
- Increase test coverage for additional checkout workflows, payment methods, and edge cases.
- Improve resilience against dynamic UI changes and intermittent pop-ups on the live application.
- Introduce retry mechanisms for handling transient failures caused by network latency or dynamic page behavior.
- Add support for execution across multiple browsers and browser versions simultaneously.

---

# Learning Outcomes

Building this project was both challenging and rewarding, especially as my first automation framework. Throughout the development process, I learned the following lessons:

- Break down a complex user journey into smaller, reusable automation components.
- Think beyond writing test scripts and focus on designing a maintainable automation framework.
- Debug failures caused by both the automation code and the application's dynamic behavior.
- Adapt/Update automation scripts to handle changing interfaces, unexpected pop-ups, and unpredictable application flows.
- *Developed a realistic understanding that building automation for live production applications is far more challenging than practice projects or demo applications.*
- Appreciated that successful automation depends not only on coding skills but also on observation, patience, and continuous problem-solving.
- Learnt to *analyze* test failures methodically instead of assuming the automation code was always at fault.
- Gained practical experience in identifying *stable element* locators and implementing reliable synchronization strategies for dynamic web pages.
- Developed the habit of writing modular, reusable, and maintainable automation code that is easier to extend and debug.
- Recognized the practical limitations of automating live production applications, including authentication challenges, bot detection mechanisms, and other factors that may interrupt automated execution.
- Built confidence in approaching unfamiliar automation challenges through experimentation, documentation, debugging, and continuous refinement.
- Strengthened my understanding of how automation frameworks are structured and how individual components work together to support scalable test execution.

---

## License

This project is intended solely for educational and learning purposes. It automates navigation and validation of Amazon workflows without placing actual orders or performing real transactions.
