import os
import streamlit as st
#EDA packages
import pandas as pd



#VIZ Pkgs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns

def main():
    """ML dataset explorer"""
    st.title("Dataset explorer")
    st.subheader("Simple dataset explorer")
    html_temp = """
    <div style="background-color:tomato;"><p>Streamlit is awesome</p></div>

    """
    st.markdown(html_temp, unsafe_allow_html=True)

if __name__ =='__main__':
    main()