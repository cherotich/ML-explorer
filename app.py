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
    st.subheader("Data Visualization")
    #Correlation

    #Seaborn
    if st.checkbox("Correlation Plot[Seaborn]"):
        st.write(sns.heatmap(df.corr(),annot=True))
        st.pyplot()
    #Count Plot
    #Pie Chart
    if st.checkbox("Pie Plot"):
        all_columns_names = df.columns.tolist()
        if st.button("Generate Pie Plot"):
           st.success("Generating Pie Plot" )
           st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
           st.pyplot()
    #count Plot
    if st.checkbox("Plot of Value Counts"):
        st.text("Value Counts By Target")
        all_columns_names = df.columns.tolist()
        primary_col = st.selectbox("Primary Column to GroupBy", all_columns_names)
        selected_columns_names = st.multiselect("Select Columns", all_columns_names)
        if st.button("Plot"):
            st.text("Generate Plot")
            if selected_columns_names:
                vc_plot = df.groupby(primary_col)[selected_columns_names].count()
            else:
                vc_plot = df.iloc[:,-1].value_counts()
            st.write(vc_plot.plot(kind="bar"))
            st.pyplot()

       
    #Customizable plot

    st.subheader("Customizable Plot")
    all_columns_names = df.columns.tolist()
    type_of_plot = st.selectbox("Select Type of Plot",["area","bar","line","hist","box","kde"])
    selected_columns_names = st.multiselect("Select Columns To Plot",all_columns_names)
    if st.button("Generate Plot"):
        st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))
        # Plot By Streamlit
        if type_of_plot == 'area':
            cust_data = df[selected_columns_names]
            st.area_chart(cust_data)
        
        elif type_of_plot == 'bar':
            cust_data = df[selected_columns_names]
            st.bar_chart(cust_data)

       
        elif type_of_plot == 'line':
            cust_data = df[selected_columns_names]
            st.line_chart(cust_data)

       #custom plot
        elif type_of_plot =='hist' :
            cust_plot = df[selected_columns_names].plot(kind='hist')
            st.write(cust_plot)
            st.pyplot()
        elif type_of_plot =='box' :
            cust_plot = df[selected_columns_names].plot(kind='box')
            st.write(cust_plot)
            st.pyplot()

        elif type_of_plot == 'kde' :
            cust_plot = df[selected_columns_names].plot(kind='kde')
            st.write(cust_plot)
            st.pyplot()

        # elif type_of_plot :
        #     cust_plot = df[selected_columns_names].plot(kind=type_of_plot)
        #     st.write(cust_plot)
        #     st.pyplot()

        
        # elif type_of_plot == 'area':
        #     cust_data = df[selected_columns_names]
        #     st.area_chart(cust_data)


if __name__ =='__main__':
    main()