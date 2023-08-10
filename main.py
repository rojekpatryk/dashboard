#!/usr/bin/env python
# coding: utf-8

# In[9]:


import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px
import datetime


# In[10]:


with st.form(key='my_form'):
    start_input = st.date_input("Pick the start date", datetime.date.today() - datetime.timedelta(days=6))
    end_input = st.date_input("Pick the end date", datetime.date.today() + datetime.timedelta(1))
    submit_button = st.form_submit_button(label='Submit')


# In[19]:


class Graph:

    def price(data):
        price_chart = px.line(data, labels={
            "index": "Date",
            "value": "USD",
            "variable": "Ticker"
        })
        
        return price_chart


# In[20]:


def main():
    
    st.title('Dashboard')
    
    with st.form(key='my_form'):
        start_input = st.date_input("Pick the start date", datetime.date.today() - datetime.timedelta(days=6))
        end_input = st.date_input("Pick the end date", datetime.date.today() + datetime.timedelta(1))
        submit_button = st.form_submit_button(label='Submit')
    
    start = pd.Timestamp(start_input.strftime('%Y%m%d'), tz='Europe/Warsaw')
    end = pd.Timestamp(end_input.strftime('%Y%m%d'), tz='Europe/Warsaw')
    
    data = yf.download("TTF=F CO2.L HO=F", start=start.tz_localize(None), end=end.tz_localize(None))
    data = data[[('Close', 'CO2.L'), ('Close', 'TTF=F'), ('Close', 'HO=F')]].droplevel(0, axis=1)
    
    st.subheader('Chart')
    st.plotly_chart(Graph.price(data), use_container_width=True)
    
    st.subheader('Table')
    st.table(data)


if __name__ == "__main__":
    main()
