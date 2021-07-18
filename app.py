import os
import streamlit as st
#EDA packages
import pandas as pd



#VIZ Pkgs
import matplotlib.pyplot as plt
import matplotlib
# matplotlib.use('Agg')
import seaborn as sns

def main():
    """ML dataset explorer"""
    st.title("Dataset explorer")
    st.subheader("Simple dataset explorer")
    html_temp = """
    <div style="background-color:tomato;"><p>Streamlit is awesome</p></div>

    """
    st.markdown(html_temp, unsafe_allow_html=True)
    def file_selector(folder_path='./datasets'):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox("Selecte A file", filenames)
        return os.path.join(folder_path,selected_filename)

    filename = file_selector()
    st.info("You have selected {}".format(filename))

    #Read data
    df = pd.read_csv(filename)
 

    # Show dataset
    if st.checkbox("Show Dataset"):
        number = st.number_input("Number of Rows to view max=10",5,10)
        st.dataframe(df.head(number))
    #show columns
    if st.button("Show Column Names"):
        st.write(df.columns)
    #show shape
    if st.checkbox("Shape Of Dataset"):
        st.write(df.shape)
        data_dim = st.radio("Show Dimension By",("Rows","Columns"))
        if data_dim == 'Rows':
            st.text("Number of Rows")
            st.write(df.shape[0])
        if data_dim == 'Columns':
            st.text("Number of Columns")
            st.write(df.shape[1])
        else:
            st.write(df.shape)
    #select columns
    if st.checkbox("Select Columns to show"):
        all_columns = df.columns.tolist()
        selected_columns = st.multiselect("Select", all_columns)
        new_df = df[selected_columns]
        st.dataframe(new_df)
    #show Values
    if st.button("Value Counts"):
        st.text("Value Counts By Target/Class")
        st.write(df.iloc[:,-1].value_counts())
        #Data types
    if st.button("Data Types"):
        st.write(df.dtypes)
    

    #show summary
    if st.checkbox("Summary"):
        st.write(df.describe().T)
    #Plot and visualization

if __name__ =='__main__':
    main()