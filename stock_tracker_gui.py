import tkinter as tk
from tkinter import messagebox
import yfinance as yf

def get_stock_data():
    ticker_symbol = entry.get().upper()
    if not ticker_symbol:
        messagebox.showwarning("Input Error", "Please enter a stock ticker symbol.")
        return
    
    try:
        stock = yf.Ticker(ticker_symbol)
        hist = stock.history(period="1d")
        todays_data = hist.tail(1)
        price = todays_data['Close'].iloc[0]
        high = todays_data['High'].iloc[0]
        low = todays_data['Low'].iloc[0]
        previous_close = stock.history(period="2d")['Close'].iloc[0]
        change_percent = ((price - previous_close) / previous_close) * 100

        result.set(f"Price: ₹{price:.2f}\nDay High: ₹{high:.2f}\nDay Low: ₹{low:.2f}\nChange: {change_percent:.2f}%")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve data.\n{e}")

# GUI Setup
root = tk.Tk()
root.title("Stock Market Tracker")
root.geometry("350x250")

tk.Label(root, text="Enter Stock Ticker:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root, text="Get Price", command=get_stock_data, font=("Arial", 12), bg="lightblue").pack(pady=10)

result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 12), justify="left").pack(pady=10)

root.mainloop()
