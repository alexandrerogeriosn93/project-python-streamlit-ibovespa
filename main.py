import streamlit as st
import yfinance as yf

# ENBR3.SA - EDP Energias do Brasil S.A
# BBAS3.SA - Banco do Brasil S.A
# BBDCA.SA - Banco Bradesco S.A
# PETR4.SA - Petroleo Brasileiro S.A - Petrobrás
# VALE5.SA - VALE5.SA

st.title("Preço de ativo")
st.header("Informações a Respeito do Fechamento e Volume de Alumas Ações")

ticker_symbol = "PETR4.SA"
ticker_data = yf.Ticker(ticker_symbol)
ticker_data_frame = ticker_data.history(period="1d", start="2012-5-19", end="2022-5-19")

st.header("Gráfico de fechamento")
st.line_chart(ticker_data_frame.Close)
