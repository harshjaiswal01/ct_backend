# 3. Python Loops and Tuples in Analytical Applications
# Objective:

# This assignment is designed to strengthen your expertise in using Python loops and tuples, 
# particularly in data analysis and processing scenarios. By completing these tasks, 
# you will gain practical experience in handling and analyzing data using these fundamental Python concepts.

# Task 1: Stock Market Data Analysis Enhance your skills in data manipulation and analysis using tuples and loops.

# Problem Statement: You have been provided with stock market data, 
# where each data point is a tuple containing a company's stock symbol, 
# the date, and the closing price. 

# Your task is to write a function to find the average closing price of a specified stock.

# Sample Data:

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]

def average_closing(stock_symbol, stock_data_average):
    i = 0
    sum = 0
    for stock in stock_data_average:
        if stock_symbol == stock[0]:
            sum += stock[2]
            i += 1
    if i > 0:
        average = sum / i
    else:
        print("Stock Data not found!")
        average = 0
    return(average)

stock_ticker = input("Please enter the Stock Ticker: ").upper()
average = average_closing(stock_ticker, stock_data)
print(f"The average closing price of {stock_ticker} is {average}")