# 💰 Finance Calculator Dashboard

An interactive **Personal Finance Calculator & Dashboard** built with **Python, Streamlit, Plotly, and Pandas**.

🔗 **Live App:** https://finance-calc-app.streamlit.app/

## 📊 Features

- 💰 Monthly income calculator
- 🧾 Expense tracking by category
- 📈 Monthly savings calculation
- 📊 Savings-rate percentage
- 📌 Expense-to-income ratio
- 🥧 Interactive expense distribution donut chart
- 📊 Expense category bar chart
- 🎯 Savings-rate gauge
- 📈 Income allocation visualization
- 💡 Automated financial insights
- 📋 Interactive summary tables
- 🎨 Responsive Streamlit dashboard layout

## 🧮 Metrics

The dashboard calculates:

### Monthly Savings

```text
Savings = Income - Total Expenses
```

### Savings Rate

```text
Savings Rate = (Savings / Income) × 100
```

### Expense Ratio

```text
Expense Ratio = (Total Expenses / Income) × 100
```

### Expense Percentage

```text
Category % = (Category Expense / Total Expenses) × 100
```

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Interactive web application |
| Pandas | Data preparation and calculations |
| Plotly | Interactive dashboards and charts |
| Git/GitHub | Version control and deployment |

## 📁 Project Structure

```text
streamlit-finance-app/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/streamlit-finance-app.git
cd streamlit-finance-app
```

### 2. Create a virtual environment

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Streamlit

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud** from a GitHub repository.

Deployment flow:

```text
Python + Streamlit
        ↓
      Git
        ↓
     GitHub
        ↓
Streamlit Community Cloud
        ↓
Live Web App
```

## 🎯 Portfolio Use

This project demonstrates practical skills in:

- Python application development
- Interactive data visualization
- KPI dashboard design
- Percentage-based analysis
- Data transformation with Pandas
- Plotly visualization
- Streamlit UI development
- Git/GitHub workflow
- Cloud deployment

## ⚠️ Disclaimer

This application is an educational budgeting and visualization tool. It uses only the values entered by the user and does not provide personalized financial advice.

## 👤 Author

**Shubham K. Jha**

Live application:

https://finance-calc-app.streamlit.app/
