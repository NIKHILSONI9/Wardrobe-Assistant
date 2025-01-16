import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date, timedelta
import matplotlib.dates as mdates
import streamlit as st

# Streamlit app title
st.title("Real-time Stock Price Data")

# User inputs
a = st.text_input("Enter Any Company Ticker (e.g., AAPL, TSLA):")
days = st.number_input(
    "Enter the number of days to view the stock prices:", 
    min_value=1, 
    max_value=1000, 
    value=360
)

if a and days:  # Ensure inputs are valid
    try:
        # Calculate start and end dates
        today = date.today()
        end_date = today.strftime("%Y-%m-%d")
        start_date = (today - timedelta(days=int(days))).strftime("%Y-%m-%d")

        # Fetch stock data
        data = yf.download(a, start=start_date, end=end_date)
        st.write(data.tail())  # Display recent data for debugging

        if not data.empty and "Close" in data.columns:
            # Create the plot
            fig, ax = plt.subplots()
            data["Close"].plot(
                figsize=(12, 8),
                title=f"{a} Stock Prices (Last {days} Days)",
                fontsize=16,
                label="Close Price",
                ax=ax
            )
            
            # Highlight today's price
            if today.strftime("%Y-%m-%d") in data.index:
                today_price = data.loc[today.strftime("%Y-%m-%d"), "Close"]
                ax.plot(
                    today,
                    today_price,
                    'ro',  # Red circle
                    label=f"Today: {today_price:.2f}"
                )
            
            # Improve x-axis date formatting
            ax.xaxis.set_major_locator(mdates.AutoDateLocator())
            ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d, %Y"))
            plt.xticks(rotation=45, fontsize=12)  # Rotate and adjust size of x-axis labels
            plt.legend()
            plt.grid()
            
            # Display the chart in Streamlit
            st.pyplot(fig)
        else:
            st.error("No 'Close' price data available for the provided ticker.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
