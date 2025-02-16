# Web App Flask PDF to Excel Table

This project allows converting PDF files containing tables into Excel files using a web application developed with Flask. The application extracts tables from each page of the PDF and combines them into a downloadable Excel file.

## Features

- **PDF to Excel Conversion**: Extracts tables from a PDF file and converts them into an Excel file.
- **Multi-page Support**: Extracts tables from all pages of the PDF, not just the first page.
- **Simple User Interface**: An intuitive web interface to upload the PDF file and retrieve the converted Excel file.

## Technologies Used

- **Flask**: Python web framework for building the application.
- **pdfplumber**: Python library for extracting tables from PDF files.
- **pandas**: Library for manipulating data and converting it into Excel format.
- **HTML, CSS**: For the user interface.
- **PythonAnywhere**: Hosting the web application online.

# Deploying a Flask Application on PythonAnywhere

Follow these steps to deploy your Flask application on **PythonAnywhere**.

## Prerequisites

Before starting, make sure you have:
- An account on **PythonAnywhere** (if you don’t have one, create it on [PythonAnywhere](https://www.pythonanywhere.com/)).
- Your project code ready to be deployed.

## Deployment Steps

### 1. Create a PythonAnywhere Account

- Go to [PythonAnywhere](https://www.pythonanywhere.com/).
- Create an account or log in if you already have one.

### 2. Create a New Web Application

1. Once logged into your PythonAnywhere account, click on the **"Web"** tab at the top of the page.
2. Click the **"Add a new web app"** button.
3. Select the **domain name** you want (e.g., `your_username.pythonanywhere.com`).
4. Choose the **Flask** framework from the available options.
5. Select the version of Python you're using for your application.

### 3. Configure the Flask Application on PythonAnywhere

1. **Upload Your Code to PythonAnywhere**:
   - You can use the built-in file editor to create files or upload your files directly via **SFTP**.
   - You can also use **Git** to clone your GitHub repository directly on PythonAnywhere.

2. **Configure the WSGI File**:
   - PythonAnywhere automatically creates a `wsgi.py` file for your Flask app.
   - Modify this file to add the proper configurations. Your `wsgi.py` file should look like this:
     ```python
     # WSGI.py
     import sys
     sys.path.insert(0, '/home/your_username')  # Replace with the correct path to your project directory
     from MH import app as application  # The 'app' instance of your Flask application is returned as 'application'
     ```
   - Replace `your_username` with your PythonAnywhere username and ensure the path to your project is correct.

### 4. Dependency Explanation

- **Flask**: A lightweight web framework for building web applications in Python.
- **pdfplumber**: A library for extracting tables from PDF files.
- **pandas**: A data manipulation and analysis library, used to convert the extracted tables into Excel format.
- **openpyxl**: A library needed to write Excel files with pandas.

### 5. Configure File Directories

1. Ensure that the `uploads/` and `outputs/` directories are created within your project directory. These folders are used to store the uploaded files and the generated files.

2. You can create these directories using PythonAnywhere’s file management interface or directly from the PythonAnywhere console:
   ```bash
   mkdir /home/your_username/pdf-to-excel-converter/uploads
   mkdir /home/your_username/pdf-to-excel-converter/outputs

## 6. Restart the Web Application

Once all configuration steps are completed, return to the "Web" tab on PythonAnywhere.

Click the "Reload" button to restart your application and apply the changes.

## 7. Access Your Web Application

[https://mhamed.pythonanywhere.com/](https://mhamed.pythonanywhere.com/) 

(replace mhamed with your PythonAnywhere username).

## Contributing
Feel free to contribute by submitting issues or pull requests.

## License
This project is licensed under the MIT License.

## Author
[Kurama-90](https://github.com/Kurama-90)
