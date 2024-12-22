import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Define a function to predict stock price
def predict_stock_price(stock, start_date, end_date):
    # Fetch stock data
    data = yf.download(stock, start=start_date, end=end_date)
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df.index)

    # Making a Candlestick graph
    fig = go.Figure(data=[go.Candlestick(
        x=df['date'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close']
    )])

    # Updating the layout
    fig.update_layout(
        title='Stock Price Chart',
        yaxis_title='Price (rupees)',
        xaxis_rangeslider_visible=False
    )

    # Display interactive candlestick chart
    st.write("Stock Price Chart")
    st.plotly_chart(fig)

    # Dropping date and volume to make it less complex
    df.drop(['date', 'Volume'], axis=1, inplace=True)
    df.reset_index(drop=True, inplace=True)

    # Features
    X = df[['Open', 'Close', 'High', 'Low', 'Adj Close']]
    # Target Values
    y = df['Close']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    # Training
    rf.fit(X_train.values, y_train.values)

    # Using R-squared to check accuracy in the model
    y_pred = rf.predict(X_test.values)
    r2 = r2_score(y_test, y_pred)
    # st.write("R-squared (R²) Score:", r2)

    # Inputting Value of features
    initial_array = np.array([['x', 'y', 'z', 'a', 'b']])
    updated_array = np.concatenate((initial_array[:-1], df.tail(1).values))
    # st.write(updated_array)

    # Predicting
    predicted_price = rf.predict(updated_array)

    # Scatter plot of y_pred and y_test
    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred, color='blue', label='Predicted')  # Scatter plot for y_pred with blue color
    ax.scatter(y_test, y_test, color='red', label='Actual')  # Scatter plot for y_test with red color
    ax.set_xlabel('Actual Values (y_test)')
    ax.set_ylabel('Predicted Values (y_pred)')
    ax.set_title('Actual vs Predicted Values')
    ax.legend()  # Add legend to differentiate the scatter plots

    # Display the plot using st.pyplot()
    st.pyplot(fig)

    return predicted_price[0]

# Streamlit app
st.title("Stock Price Prediction App")
st.sidebar.header("About Us")
st.sidebar.write("This is a simple stock price prediction app built with Streamlit.")
st.sidebar.write("It uses historical stock data to predict the future stock price using a machine learning model.")

# User input for stock, start date, and end date
stock = st.text_input("Enter a Ticker")
start_date = st.date_input("Enter start date to fetch records")
end_date = st.date_input("Enter end date to fetch records")

# Button to trigger predictions
if st.button("Predict Stock Price"):
    predicted_price = predict_stock_price(stock, start_date, end_date)
    st.write(f"Predicted Stock Price: {predicted_price}")
    
# IBM Watson Assistant

# JavaScript code to display
javascript_code = """
<script>
  window.watsonAssistantChatOptions = {
    integrationID: "34f9a0ec-5f40-46bb-91c3-39d62e62ae77", // The ID of this integration.
    region: "au-syd", // The region your integration is hosted in.
    serviceInstanceID: "1d2d2879-fd7d-4143-aa80-cf031a012b6d", // The ID of your service instance.
    onLoad: function(instance) { instance.render(); }
  };
  setTimeout(function(){
    const t=document.createElement('script');
    t.src="https://web-chat.global.assistant.watson.appdomain.cloud/versions/" + (window.watsonAssistantChatOptions.clientVersion || 'latest') + "/WatsonAssistantChatEntry.js";
    document.head.appendChild(t);
  });
</script>
"""

# Display JavaScript code using st.components.v1.html
st.components.v1.html(javascript_code)