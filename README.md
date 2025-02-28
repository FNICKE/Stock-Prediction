# 🚀 Stock Prediction - Stock Genie

## 📖 Overview

Welcome to **Stock Genie**, a stock prediction tool that leverages historical stock price data to analyze trends and provide buy/sell recommendations. This project uses a Python-based GUI built with **PyQt5** and integrates financial data using **Pandas** and **Matplotlib**.

It visualizes the stock price along with its **Moving Average** (MA) to assist investors in making informed decisions. You can input the **Ticker Symbol** of a stock, and **Stock Genie** will show you the prediction based on historical data since January 2015.

---

## 🛠️ Technologies Used

- **Python** (3.x)
- **PyQt5** - for the graphical user interface (GUI)
- **Matplotlib** - for plotting graphs
- **Pandas** - for handling stock data
- **Pandas DataReader** - to fetch stock market data from Yahoo Finance

---

## 🖼️ Screenshot

![Stock Genie GUI](./assets/stock_genie_screenshot.png)

---

## 🔧 Features

- **User-friendly interface** with a textbox to enter a stock ticker.
- **Stock Price Graph** with Yellow representing the stock price and Cyan showing the 5-day moving average.
- **Buy/Hold** or **Sell** recommendation based on the stock price relative to the moving average.
- Fetch historical stock data since **1st January 2015**.

---


## How to Run
- git clone https://github.com/FNICKE/stock-genie.git
- cd stock-genie

- Install required Python libraries (mentioned above)

## How It Works
- Data Collection: The program fetches the stock data for the ticker symbol entered using Yahoo 
 Finance API (pandas_datareader).

- Moving Average Calculation: The program calculates the 5-day moving average for the stock.

-Graph Generation: The stock price and moving average are plotted using Matplotlib.

-Recommendation: The system compares the stock price with the moving average to recommend whether to BUY/HOLD or SELL the stock.

## 📊 Sample Output
### Stock Price & Moving Average Visualization
A sample graph might look like this, with Yellow representing the stock price and Cyan for the 5-day moving average.

---bashS
Date -> Timeline of stock price
Price -> Price of the stock over time
BUY/HOLD or SELL -> Action based on moving average comparison

