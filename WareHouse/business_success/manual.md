# In-N-Out User Manual

In-N-Out is a Python-based software that allows users to transpose CSV files. The software uses a Streamlit frontend for user interaction. This manual provides a detailed guide on how to install and use the software.

## Quick Install

1. Clone the repository.
2. Install the required Python packages using pip: `pip install -r requirements.txt`
3. Run the program with: `streamlit run main.py`

## Software Overview

In-N-Out is designed to take a CSV file as input, transpose it, and save the transposed file locally. The software ensures that the uploaded file is a CSV file and allows the user to download the transposed file once the operation is complete.

## Main Functions

1. **CSV File Upload:** The software provides an input field to upload the CSV file.

2. **CSV File Transposition:** Upon clicking the submit button, the software transposes the content of the uploaded CSV file.

3. **File Download:** After the transposition operation, a download button is enabled, allowing the user to download the transposed file.

## How to Use

1. Start the program from a Python window.

2. Upload a CSV file using the provided input field.

3. Click the submit button to start the transposition operation.

4. Once the operation is complete, click the download button to download the transposed file.

## Constraints and Dependencies

The software does not use external APIs and is hosted locally. It requires Python to be installed on the user's machine, and certain Python packages might need to be installed locally.

## Performance and Design

The software is designed to transpose a CSV file in less than 2 minutes. The interface is center-aligned for easy use. The software adheres to clean code standards and consistent naming conventions.

## Deliverables

The software includes a Streamlit run file, optional helper Python files, a requirements.txt file, and documentation.

## Support

For any issues or queries, please reach out to our support team. We're here to help you make the most of In-N-Out.