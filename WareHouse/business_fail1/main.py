'''
This is the main file for the In-N-Out program. It uses the Streamlit library to create a frontend interface for the user to upload a CSV file, transpose it, and download the transposed file.
'''
import streamlit as st
import pandas as pd
import os
def check_file(file):
    '''
    This function checks if the uploaded file is a CSV file.
    '''
    return file.type == 'text/csv'
def transpose(file):
    '''
    This function transposes the content of the input CSV file.
    '''
    df = pd.read_csv(file)
    df_transposed = df.transpose()
    df_transposed.to_csv('transposed.csv', index=False)
    return df_transposed
def delete_temp_files():
    '''
    This function deletes all temporary files created during the process.
    '''
    if os.path.exists('transposed.csv'):
        os.remove('transposed.csv')
def main():
    '''
    This is the main function to run the program.
    '''
    delete_temp_files()  # Delete any existing 'transposed.csv' file
    st.title('In-N-Out')
    file = st.file_uploader('Upload CSV', type=['csv'])
    if file is not None:
        if check_file(file):
            if st.button('Submit'):
                transpose(file)
                st.success('File transposed successfully.')
                st.download_button('Download transposed file', 'transposed.csv')
if __name__ == '__main__':
    main()