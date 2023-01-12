import streamlit as st
from tvDatafeed import TvDatafeed, Interval
import pandas as pd

tv = TvDatafeed()
def visualize_data(df):
    # Normalize the data by dividing all values by the first value in each column
    df_normalized = df.div(df.iloc[0])

    # Get a list of the cryptocurrency symbols
    symbols = df.columns.tolist()

    # Let the user select which symbols to include in the plot
    selected_symbols = st.multiselect('Which symbols do you want to include in the plot?', symbols)

    # Create a multi-line plot of the normalized close prices
    st.line_chart(df_normalized[selected_symbols])



# Define a list of symbols to retrieve data for
symbols = ['SANDUSDT', 'BTCUSDT', 'ETHUSDT', 'LUNAUSDT', 'FTMUSDT', 'SUSHIUSDT', 'MATICUSDT', 'DOTUSDT', 'NEARUSDT', 'LINKUSDT', 'XRPUSDT', 'ADAUSDT', 'AVAXUSDT', 'SHIBUSDT', 'ALGOUSDT', 'BNBUSDT', 'LRCUSDT', 'CHZUSDT', 'BATUSDT']

# Initialize an empty DataFrame
df = pd.DataFrame()

time_frame_options = {'1 min': Interval.in_1_minute, '5 min': Interval.in_5_minute,
    '15 min': Interval.in_15_minute, '30 min': Interval.in_30_minute, '1 hour': Interval.in_1_hour, '4 hour': Interval.in_4_hour}
selected_time_frame = st.selectbox('Select the time frame', list(time_frame_options.keys()))


number_of_candles = st.slider('Select the number of candles', min_value=10, max_value=5000, value=1000, step=50)


# Use a loop to retrieve the data for each symbol
for symbol in symbols:
    hist = tv.get_hist(symbol, 'KUCOIN', time_frame_options[selected_time_frame], n_bars=number_of_candles)
    df[symbol] = hist['close']

# Rename the columns using the symbol names
df.columns = symbols

visualize_data(df)

