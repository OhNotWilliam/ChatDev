# In-N-Out User Manual

## Introduction
In-N-Out is a Python-based software that allows you to transpose CSV files. It uses a Streamlit frontend to provide a user-friendly interface for uploading, transposing, and downloading CSV files.

## Quick Install
To install the necessary dependencies for running In-N-Out, you need to have Python and pip installed on your system. Once you have these, you can install the required Python libraries by running the following command in your terminal:

```
pip install -r requirements.txt
```

The `requirements.txt` file contains the names of the Python libraries needed for the software, which are Streamlit and pandas.

## How to Use

1. **Start the Program:** Run the program by typing the following command in your terminal:

```
streamlit run main.py
```

2. **Upload CSV File:** On the Streamlit interface that opens in your web browser, you will see an option to upload a CSV file. Click on 'Browse files' and select the CSV file you want to transpose.

3. **Submit:** After uploading the CSV file, click on the 'Submit' button to start the transposition process. The 'Submit' button only becomes available after a file has been uploaded.

4. **Download Transposed File:** Once the transposition is done, a 'Download transposed file' button will appear. Click on it to download the transposed CSV file, which will be named 'transposed.csv'.

## Main Functions

- **CSV Upload:** The software provides an option to upload a CSV file that you want to transpose.

- **CSV Transposition:** The software transposes the content of the uploaded CSV file.

- **CSV Download:** The software allows you to download the transposed CSV file.

## Constraints and Assumptions

- The software does not use any external APIs and everything is hosted locally.

- The software assumes that Streamlit and Python are installed, and that the necessary pip packages are installed locally.

- The software is designed to transpose a CSV file in less than 2 minutes.

## Design and Software System Attributes

- The software uses clean code standards and consistent naming conventions.

- The software interface is center aligned for better user experience.

## Deliverables

- Streamlit run file
- Optional helper Python files
- Requirements.txt
- Documentation

Please note that this software deletes all temporary files created during the transposition process for efficiency and to save storage space.