'''
This is the main application file for the In-N-Out program. It uses the Streamlit library to create a frontend interface for the user to upload a CSV file, transpose it, and download the result.
'''
import streamlit as st
import pandas as pd
import os
def upload_file():
    '''
    This function handles the file upload process in the Streamlit frontend.
    '''
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        return data
    else:
        return None
def check_file(data):
    '''
    This function ensures that the uploaded file is a CSV file.
    '''
    if data is not None:
        return True
    else:
        st.error("Please upload a CSV file.")
        return False
def transpose_csv(data):
    '''
    This function transposes the content of the input CSV file.
    '''
    transposed_data = data.transpose()
    transposed_data.to_csv('transposed.csv', index=False)
    return transposed_data
def download_file():
    '''
    This function enables the download button after successful transpose run.
    '''
    if os.path.exists('transposed.csv'):
        return st.download_button(
            label="Download transposed CSV",
            data=open('transposed.csv', 'rb'),
            file_name='transposed.csv',
            mime='text/csv',
        )
def delete_temp_files():
    '''
    This function deletes all temporary files after the transpose operation.
    '''
    if os.path.exists('transposed.csv'):
        os.remove('transposed.csv')
def main():
    data = upload_file()
    if check_file(data):
        transposed_data = transpose_csv(data)
        st.dataframe(transposed_data)
        download_file()
        delete_temp_files()
    else:
        st.error("File upload unsuccessful or file is not a CSV. Please try again.")
if __name__ == "__main__":
    main()