import streamlit as st
import yfinance as yf

# BBAS3.SA - Banco do Brasil S.A
# PETR4.SA - Petroleo Brasileiro S.A - Petrobrás

st.title("Preço de ativo")
st.header("Informações a Respeito do Fechamento e Volume de Alumas Ações")

options = st.selectbox(
    "Escolha o Ativo",
    (
        "BBAS3.SA",
        "PETR4.SA",
    ),
)

ticker_symbol = options
ticker_data = yf.Ticker(ticker_symbol)
ticker_data_frame = ticker_data.history(period="1d", start="2012-5-19", end="2022-5-19")

st.header("Gráfico de fechamento")
st.line_chart(ticker_data_frame.Close)

st.header("Gráfico de Volume")
st.line_chart(ticker_data_frame.Volume)

st.header("Gráfico de Dividendos")
st.area_chart(ticker_data_frame.Dividends)
