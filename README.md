# 🚀 Stock Prediction - Stock Genie

## 📖 Overview

Welcome to **Stock Genie**, a stock prediction tool that leverages historical stock price data to analyze trends and provide buy/sell recommendations. This project uses a Python-based GUI built with **PyQt5** and integrates financial data using **Pandas** and **Matplotlib**.

It visualizes the stock price along with its **Moving Average** (MA) to assist investors in making informed decisions. You can input the **Ticker Symbol** of a stock, and **Stock Genie** will show you the prediction based on historical data since January 2015.

---

## 🛠️ Technologies Used

- 🐍 **Python** (3.x)
- 🖥️ **PyQt5** - for the graphical user interface (GUI)
- 📊 **Matplotlib** - for plotting graphs
- 🗂️ **Pandas** - for handling stock data
- 🌐 **Pandas DataReader** - to fetch stock market data from Yahoo Finance

---

## 🖼️ Preview

![Stock Predictor Preview](Stock%20Predictor/image.png)

---

## 🔧 Features

- ✅ **User-friendly interface** with a textbox to enter a stock ticker.
- 📈 **Stock Price Graph** with **Yellow** representing the stock price and **Cyan** showing the 5-day moving average.
- 📢 **Buy/Hold** or **Sell** recommendation based on the stock price relative to the moving average.
- ⏳ Fetch historical stock data since **1st January 2015**.

---

## 🚀 Installation & Setup

### 🔽 Clone the Repository
```bash
git clone https://github.com/FNICKE/stock-genie.git
cd stock-genie
```

### 📦 Install Required Dependencies
```bash
pip install pyqt5 matplotlib pandas pandas-datareader
```

### ▶️ Run the Application
```bash
python PythonFinance.py
```

---

## 🛠️ How It Works

1. **📊 Data Collection:** The program fetches the stock data for the ticker symbol entered using **Yahoo Finance API** (pandas_datareader).
2. **📉 Moving Average Calculation:** The program calculates the **5-day moving average** for the stock.
3. **📈 Graph Generation:** The stock price and moving average are plotted using **Matplotlib**.
4. **📢 Recommendation:** The system compares the stock price with the moving average to recommend whether to **BUY/HOLD** or **SELL** the stock.

---

## 📂 Code Structure

📄 **PythonFinance.py**  
This file contains the core **Finance** class, which fetches historical stock data, calculates the moving average, and generates the necessary graph for predictions.

- 🛠️ **get_stock_price()**: Fetches historical stock data.
- 📊 **get_moving_avg()**: Calculates the moving average and plots the stock price graph with predictions.

---

## 📊 Sample Output

### **Stock Price & Moving Average Visualization**
A sample graph might look like this, with **Yellow** representing the stock price and **Cyan** for the **5-day moving average**.

📅 **Date:** Timeline of stock price  
💰 **Price:** Price of the stock over time  
📢 **BUY/HOLD or SELL:** Action based on moving average comparison  

---

💡 *Stock Genie helps you make smarter investment decisions using historical data trends!* 📈✨

