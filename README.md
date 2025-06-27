# 🔐 Automated Login Tests | Automation Practice

This project aims to automate login page tests for the website [Automation Practice](http://automationpractice.pl/index.php?controller=authentication&back=my-account), using **Selenium WebDriver** and **Pytest**.

---

## 🧪 Technologies Used

- **Language:** Python 3  
- **Testing framework:** Pytest  
- **Web automation:** Selenium WebDriver  
- **Dependency manager:** `pip`  
- **IDE:** VSCode  

---

## 📂 Project Structure

```

.
├── pages/
│   └── login\_page.py      # Page Object Model for the login page
├── tests/
│   └── test\_login.py      # Automated test cases
├── requirements.txt       # Project dependencies
└── README.md              # Instructions and documentation

```

## ✅ Automated Test Scenarios

### 🧪 Scenario 1: Login with valid credentials

- **Given** the user is on the Automation Practice login page  
- **When** the user enters a valid email and password, then clicks "Sign in"  
- **Then** the system should redirect the user to their account page, confirming a successful login  

> **Expected result:** Redirect to a URL containing `/my-account`

---

### 🧪 Scenario 2: Login with invalid email format

- **Given** the user is on the Automation Practice login page  
- **When** the user enters a poorly formatted email (e.g., `invalidemail.com`) and any password  
- **Then** the system should display the error message: **"Invalid email address."**

---

### 🧪 Scenario 3: Login with incorrect password

- **Given** the user is on the Automation Practice login page  
- **When** the user enters a valid email and an incorrect password  
- **Then** the system should display the error message: **"Authentication failed."**

---

## 🚀 How to Run the Tests

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/automated-login-tests.git
cd automated-login-tests
```


### 2. Create a virtual environment (optional, but recommended)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the tests

```bash
pytest
```

---

## ⚙️ Requirements

* Python 3.8+
* Google Chrome (or another browser with WebDriver installed)
* ChromeDriver (compatible with your browser version)

