# ExcelSheetIO

A Python package for efficient Excel sheet operations. Enables easy read/write functionality, data manipulation, and workflow automation. Ideal for handling both small and large datasets. Get started with ExcelSheetIO for a simplified data processing experience.

## Installation Guide

```python
pip install ExcelSheetIO

# For upgrade to the latest version
pip install --upgrade ExcelSheetIO 
```

## Method : `Read Data From Excel Sheet`

The `ExcelReaderWriter` class in Python provides an efficient way to read and retrieve data from Excel sheets. This guide will help you understand how to use the `readCellData` method in this class.

Sure, here's a more refined explanation:

![ExcelSheet](https://raw.githubusercontent.com/Soumyajit7/ExcelSheetIO/main/assets/img/excel_clip.png "excel logo")

To use the `readCellData` method in Python, you need to identify the specific cell data you want to read. Let's say, for example, you want to read the cell value `Sr. Analyst` from an Excel sheet.

First, identify the sheet that contains the data you're looking for. In this case, the sheet name is `Sheet1`.

Next, determine the row where your data resides. In this example, `Sr. Analyst` is in row number `6`. To better identify the row, we use the data from the first column as a unique identifier(make sure the data of the 1st column of the sheet should be uniquely identifier data).

Then, identify the column header that contains your data. In this scenario, the column header name is `Job Title`.

With these parameters - the sheet name, the unique identifier from the first column, and the column header name - you can use the `readCellData` method to read the data. The syntax would be:

```python
data = excel_reader_writer.readCellData('SheetName', 'UniqueIdentifierInRow', 'ColumnHeaderName')
```

In this code, replace `'SheetName'`, `'UniqueIdentifierInRow'`, and `'ColumnHeaderName'` with your actual values (`Sheet1`, `E5`, and `Job Title`, respectively) when you use this method. This will return the data from the specified cell.

### Python Usage

```python
# import the ExcelSheetIO library package
from ExcelSheetIO import ExcelReaderWriter

# Create an instance of the ExcelReaderWriter class
excel_reader_writer = ExcelReaderWriter('path_to_your_excel_file')

# Use the readCellData method
data = excel_reader_writer.readCellData('SheetName', 'UniqueIdentifierInRow', 'ColumnHeaderName')

# Print the retrieved data
print(data)
```

In the above code, replace `'path_to_your_excel_file'`, `'SheetName'`, `'UniqueIdentifierInRow'`, and `'ColumnName'` with the path to your Excel file, the name of the sheet in the Excel file, the unique identifier from the first column, and the name of the column header, respectively.

### Robot Framework Usage

If you're using Robot Framework, you can create a custom keyword that uses the `readCellData` method. Here's how you can do it:

```robotframework
*** Settings ***
Library    ExcelSheetIO.ExcelReaderWriter    relative_path_to_your_excel_file

*** Keywords ***
Keyword for read data from excel sheet
    [Arguments]    ${sheetName}    ${UniqueIdentifierInRow}    ${ColumnHeaderName}
    ${data}=    Read Cell Data    ${sheetName}    ${UniqueIdentifierInRow}    ${ColumnHeaderName}
    Log To Console    ${\n}${data}

*** Test Cases ***
Test case for read data from excel sheet
    Keyword for read data from excel sheet    Sheet1    E5    Job Title
    [Tags]    read     test
```

In the above code, replace `'relative_path_to_your_excel_file'`, `'SheetName'`, `'UniqueIdentifierInRow'`, and `'ColumnHeaderName'` with the path to your Excel file, the name of the sheet in the Excel file, the unique identifier from the first column, and the name of the column header, respectively.

Please replace `'relative_path_to_your_excel_file'`, `'SheetName'`, `'UniqueIdentifierInRow'`, and `'ColumnHeaderName'` with your actual values (`.\\Data\\Employee.xlsx`, `Sheet1`, `E5`, and `Job Title`, respectively) when you use this code.

## Method : `Write Data In Excel Sheet`

The `ExcelReaderWriter` class in Python provides an efficient way to read and write data to Excel sheets. This guide will help you understand how to use the `writeCellData` method in this class.

To use the `writeCellData` method in Python, you need to identify the specific cell where you want to write data. Let's say, for example, you want to write the value `Sr. Analyst` into a cell in an Excel sheet.

First, identify the sheet where you want to write the data. In this case, the sheet name is `Sheet1`.

Next, determine the row where you want to write your data. In this example, `Sr. Analyst` is to be written in row number `6`. To better identify the row, we use the data from the first column as a unique identifier (make sure the data of the 1st column of the sheet should be uniquely identifier data).

Then, identify the column header where you want to write your data. In this scenario, the column header name is `Job Title`.

Finally, determine the data you want to write. In this case, the data is `Sr. Analyst`.

With these parameters - the sheet name, the unique identifier from the first column, the column header name, and the data to be written - you can use the `writeCellData` method to write the data. The syntax would be:

```python
excel_reader_writer.writeCellData('SheetName', 'UniqueIdentifierInRow', 'ColumnHeaderName', 'WritableData')
```

In this code, replace `'SheetName'`, `'UniqueIdentifierInRow'`, `'ColumnHeaderName'`, and `'WritableData'` with your actual values (`Sheet1`, `E5`, `Job Title`, and `Sr. Analyst`, respectively) when you use this method. This will write the data into the specified cell. Please ensure that you have write permissions for the Excel file.

### Python Usage

Here's how you can use the `writeCellData` method in Python:

```python
# import the ExcelSheetIO library package
from ExcelSheetIO import ExcelReaderWriter

# Create an instance of the ExcelReaderWriter class
excel_reader_writer = ExcelReaderWriter('path_to_your_excel_file')

# Use the writeCellData method
excel_reader_writer.writeCellData('SheetName', 'UniqueIdentifierInRow', 'ColumnHeaderName', 'WritableData')
```

In the above code, replace `'path_to_your_excel_file'`, `'SheetName'`, `'UniqueIdentifierInRow'`, `'ColumnHeaderName'`, and `'WritableData'` with the path to your Excel file, the name of the sheet in the Excel file, the unique identifier from the first column, the name of the column header, and the order number, respectively.

### Robot Framework Usage

If you're using Robot Framework, you can create a custom keyword that uses the `writeCellData` method. Here's how you can do it:

```robotframework
*** Settings ***
Library    ExcelSheetIO.ExcelReaderWriter    path_to_your_excel_file

*** Keywords ***
Keyword For Write Data in Excel Sheet
    [Arguments]    ${sheetName}    ${UniqueIdentifierInRow}    ${ColumnHeaderName}    ${WritableData}
    Write Cell Data    ${sheetName}    ${UniqueIdentifierInRow}    ${ColumnHeaderName}    ${WritableData}

*** Test Cases ***
Test case for write data in excel sheet
    Keyword For Write Data in Excel Sheet    Sheet1    E6    Job Title    Software Developer
    [Tags]    write     test
```

In the above code, replace `'path_to_your_excel_file'`, `'SheetName'`, `'UniqueIdentifierInRow'`, `'ColumnHeaderName'`, and `'WritableData'` with the path to your Excel file, the name of the sheet in the Excel file, the unique identifier from the first column, the name of the column header, and the order number, respectively.

### Breakdowns

Let's break down how the `writeCellData` method works internally, in a more understandable way :

**`Creating a Copy`** : The method starts by creating a copy of the original Excel file. This is done to ensure that the original file remains unchanged until all write operations are successfully executed. The copy is stored in a folder named `CopyFolder` and is given a temporary file name like `*_Temp*.xlsx`. Make sure add `CopyFolder` in `.gitignore` in your project.

**`Writing Data`** : The method then performs the write operation on this temporary Excel file. It writes data to a specific cell in an Excel sheet. The cell is identified by the sheet name, the unique identifier from the first column (which should be unique), and the column header name.

**`Saving Changes`** : After all write operations are completed, the method saves the changes made to the temporary file.

**`Updating the Original File`** : The method then transfers the data from the temporary file back into the original file. This ensures that the original file is updated with all the new data.

**`Cleaning Up`** : Finally, the method removes the temporary Excel file after all operations are finished. This is done to free up storage space and maintain cleanliness in your file system.

By using this method, you can efficiently write data to an Excel file while ensuring the integrity of the original file until all operations are successfully completed. It's a safe and efficient way to manipulate Excel data in Python. Please ensure that you have write permissions for the Excel file.

## Method : `Remove Temporary TestData Files`

The `removeTemporaryTestDataFiles` method is a utility function in this Python script that is designed to clean up temporary Excel files that may have been created during the execution of the script. This method is particularly useful in maintaining a clean workspace and ensuring that temporary files do not consume unnecessary storage. Make sure add `CopyFolder` in `.gitignore` in your project.

### How it works:

**`Locate the Current Directory`** : The method first identifies the directory where the Python script is currently located.

**`Construct the Path`**  It then constructs the path to a subdirectory named 'CopyFolder' within the current directory.

**`Iterate Over Files`** : The method iterates over all files present in the 'CopyFolder' subdirectory.

**`Identify and Remove Temporary Files`** : If a file name contains the string 'temp', the method attempts to remove (delete) the file.

**`Error Handling`** : If an error occurs during the file removal process, the method captures the error and logs it using the logger.error function.

### Python Usage

Here's how you can use the `removeTemporaryTestDataFiles` method in Python:

```python
# import the ExcelSheetIO library package
from ExcelSheetIO import ExcelReaderWriter

# Create an instance of the ExcelReaderWriter class
excel_reader_writer = ExcelReaderWriter('path_to_your_excel_file')

# Use the removeTemporaryTestDataFiles method
excel_reader_writer.removeTemporaryTestDataFiles()
```

### Robot Framework Usage

If you're using Robot Framework, you can create a custom keyword that uses the `removeTemporaryTestDataFiles` method. Here's how you can do it:

```robotframework
*** Settings ***
Library    ExcelSheetIO.ExcelReaderWriter    .\\Data\\Employee.xlsx

*** Keywords ***
Keyword For Remove Temporary Test Data Files
    [Arguments]
    Remove Temporary Test Data Files


*** Test Cases ***
Test case for remove temporary data files in excel sheet
    Keyword For Remove Temporary Test Data Files
    [Tags]    remove     test
```

This will remove all files in the `CopyFolder` subdirectory of the current directory that contain temporary file name like `*_Temp*.xlsx`.

## Method : `Read All Data In Given Column`

The `readAllDataInGivenColumn` method is a utility function in this Python script that is designed to read all non-null data for a particular column from a given sheet. This method is particularly useful in extracting specific data from a sheet for further processing or analysis.

### How it works:

**`Check Sheet Existence`** : The method first checks if the given sheet name exists in the data.

**`Initialize Column Data List`** : If the sheet exists, it initializes an empty list to store the column data.

**`Iterate Over Test Cases`** : The method then iterates over all test cases in the sheet.

**`Append Column Data`** : If the given column name exists in the test case and its value is not None, it appends the value to the column data list.

**`Return Column Data`** : If the column data list is not empty after the iteration, it returns the list. If the column data list is empty, it returns a message indicating that no data was found in the given column in the given sheet.

**`Handle Non-existent Sheet`** : If the sheet does not exist in the data, it returns a message indicating that the sheet was not found.

### Python Usage:

Here's how you can use the `readAllDataInGivenColumn` method in Python:

```python
# import the ExcelSheetIO library package
from ExcelSheetIO import ExcelReaderWriter

# Create an instance of the ExcelReaderWriter class
excel_reader_writer = ExcelReaderWriter('path_to_your_excel_file')

# Use the readAllDataInGivenColumn method, it'll return data as a list
column_data = excel_reader_writer.readAllDataInGivenColumn('SheetName', 'ColumnHeaderName')
```

### Robot Framework Usage:

In Robot Framework, you can call this method in a similar way. First, you need to create a keyword that calls this method, and then you can use this keyword in your test case:

```robotframework
*** Settings ***
Library    ExcelSheetIO.ExcelReaderWriter    .\\Data\\Employee.xlsx

*** Keywords ***
Keyword for read all data in given column in excel sheet
    [Arguments]    ${sheetName}    ${columnHeaderName}
    ${column_data}=    Read All Data In Given Column    ${sheetName}    ${columnHeaderName}
    Log To Console    ${\n}${column_data}

*** Test Cases ***
Test case for read all data in given column in excel sheet
    Keyword for read all data in given column in excel sheet    Sheet1    Job Title
    [Tags]    read2     test    
```

## Method : `Read All Data In Given Row`

The `readAllDataInGivenRow` method is a utility function in this Python script that is designed to fetch all data for a particular row from a given sheet. This method is particularly useful in extracting specific data from a row for further processing or analysis.

### How it works:

**`Check Sheet Existence`** : The method first checks if the given sheet name exists in the data.

**`Check Test Case Existence`** : If the sheet exists, it checks if the given test case name exists in the sheet.

**`Retrieve Row Data`** : If the test case exists, it retrieves all data for the test case. This data is a dictionary where the keys are column names and the values are cell values.

**`Return Row Data`** : It returns this dictionary, which represents all data in the given row.

**`Handle Non-existent Test Case`** : If the test case does not exist in the sheet, it returns a message indicating that the test case was not found in the given sheet.

**`Handle Non-existent Sheet`** : If the sheet does not exist in the data, it returns a message indicating that the sheet was not found.

### Python Usage :

Here's how you can use the `readAllDataInGivenRow` method in Python:

```python
# import the ExcelSheetIO library package
from ExcelSheetIO import ExcelReaderWriter

# Create an instance of the ExcelReaderWriter class
excel_reader_writer = ExcelReaderWriter('path_to_your_excel_file')

# Use the readAllDataInGivenRow method, it'll return data as a dictionary
row_data = excel_reader_writer.readAllDataInGivenRow('SheetName', 'ColumnHeaderName')
```

### Robot Framework Usage :

In Robot Framework, you can call this method in a similar way. First, you need to create a keyword that calls this method, and then you can use this keyword in your test case:

```robotframework
*** Settings ***
Library    ExcelSheetIO.ExcelReaderWriter    .\\Data\\Employee.xlsx

*** Keywords ***
Keyword for read all data in given row in excel sheet
    [Arguments]    ${sheetName}    ${UniqueIdentifierInRow}
    ${row_data}=    Read All Data In Given Row    ${sheetName}    ${UniqueIdentifierInRow}
    Log To Console    ${\n}${row_data}

*** Test Cases ***
Test case for read all data in given row in excel sheet
    Keyword for read all data in given row in excel sheet    Sheet1    E6
    [Tags]    read3     test
```

## Method : `Modify Color And Font Of The Cell`

The `modifyColorAndFontOfTheCell` method is a utility function in this Python script that is designed to modify the color and font of a specific cell in an Excel sheet. This method is particularly useful for highlighting specific test cases in an Excel sheet, such as failed test cases in a test suite.

### How it works:

**`Create a Temporary Copy`** : The method first creates a temporary copy of the original Excel file.

**`Load the Workbook`** : It then loads the workbook from this temporary file and selects the specified sheet.

**`Find the Specific Cell`** : The method iterates over the rows in the sheet until it finds the row with the specified test case name. Then, it iterates over the columns in this row until it finds the specified column name.

**`Modify the Cell`** : Once the specific cell is found, it changes the cell's fill color and font color as per the parameters.

**`Save and Close the Workbook`** : Finally, it saves and closes the workbook.

In the below image for the cell value `Software Developer`, modified the cell color as `pink`, font color as `red` and font type as **`BOLD`** using this method.

![ExcelSheetColor](https://raw.githubusercontent.com/Soumyajit7/ExcelSheetIO/main/assets/img/excel_clip_color.png "excel sheet color")

### Python Usage:

Here's how you can use the `modifyColorAndFontOfTheCell` method in Python:

```python
# import the ExcelSheetIO library package
from ExcelSheetIO import ExcelReaderWriter

# Create an instance of the ExcelReaderWriter class
excel_reader_writer = ExcelReaderWriter('path_to_your_excel_file')

# Use the modifyCellStyles method to create a CellStyler object for a specific cell in a given sheet.
# Replace 'sheetName', 'uniqueIdentifierInRow', 'columnHeaderName' with your actual data.
# Then, use the set_cell_color, set_font_color, set_font_type, and font_size methods to set the cell's styles.
# The color parameters should be hex color codes.
# The font family should be like 'Arial', 'Bradley Hand ITC' and etc.
# The font type can be 'bold', 'italic', 'underline', or 'double underline'.
# The font size should be an integer.
# The apply_styles method applies the styles to the cell.
# Finally, the save_changes method saves the changes to the Excel file.

excel_reader_writer.modifyCellStyles('sheetName', 'uniqueIdentifierInRow', 'columnHeaderName').set_cell_color('salmon').set_font_color('green').set_font_family('Arial').set_font_styles('bold', 'italic', 'underline', 'double underline').set_font_size(11).apply_styles().save_changes()

# or

excel_obj = e.modifyCellStyles('Sheet1', 'E7', 'Full Name').set_cell_color('salmon').set_font_color('green').set_font_family('Arial').set_font_styles('bold', 'italic', 'underline').set_font_size(11)
excel_obj.apply_styles().save_changes()
```

### Robot Framework:

In Robot Framework, you can call this method in a similar way. First, you need to create a keyword that calls this method, and then you can use this keyword in your test case:

```robotframework
*** Settings ***
Library    ExcelSheetIO.ExcelReaderWriter    .\\Data\\Employee.xlsx

*** Keywords ***
Modify Cell Styles
    [Arguments]    ${sheet_name}    ${unique_identifier_in_row}    ${column_header_name}    ${cell_color}    ${font_color}  ${font_family}    ${font_type}    ${font_size}
    ${excel_reader_writer}=    Get Library Instance    ExcelSheetIO.ExcelReaderWriter
    ${excel_reader_writer}.modifyCellStyles(${sheet_name}, ${unique_identifier_in_row}, ${column_header_name}).set_cell_color(${cell_color}).set_font_color(${font_color}).set_font_family(${font_family}).set_font_styles(${font_type}).set_font_size(${font_size}).apply_styles().save_changes()

*** Test Cases ***
Test Modify Cell Styles
    Modify Cell Styles    Sheet1    E6    Job Title    salmon    green  Arial    bold, italic, underline, double underline    12
    [Tags]    color1     test
    # Replace 'Sheet1', 'E6', 'Job Title', 'salmon', 'green', 'bold, italic, underline, double underline', and '12' with your sheet name, unique identifier in row, column header name, cell color, font color, font type, and font size respectively
```

## Method : `Reset Cell Styles`

The `resetCellStyles` method is part of the ExcelReaderWriter class. This method resets the styles of a specific cell in an Excel sheet to default values.

### How it works:

This method creates a `CellStyler` object for the specified cell, identified by its sheet name, unique identifier in the row, and column header name. It then sets the cell color to white, the font color to black, the font family to Calibri, the font style to normal, and the font size to 11. After applying these styles, it saves the changes to the Excel file.

### Python Usage:

Here's how you can use the `resetCellStyles` method in Python:

```python
# import the ExcelSheetIO library package
from ExcelSheetIO import ExcelReaderWriter

# Create an instance of the ExcelReaderWriter class
excel_reader_writer = ExcelReaderWriter('path_to_your_excel_file')

# Use the resetCellStyles method to create a CellStyler object for a specific cell in a given sheet.
# Replace 'sheetName', 'uniqueIdentifierInRow', 'columnHeaderName' with your actual data.
excel_reader_writere.resetCellStyles('sheetName', 'uniqueIdentifierInRow', 'columnHeaderName')
```

### Robot Framework:

In Robot Framework, you can call this method in a similar way. First, you need to create a keyword that calls this method, and then you can use this keyword in your test case:

```robotframework
*** Settings ***
Library    ExcelReaderWriter    .\\Data\\Employee.xlsx

*** Keywords ***
Keyword for reset cell styles in excel sheet
    [Arguments]    ${sheetName}    ${UniqueIdentifierInRow}     ${columnHeaderName}
    Reset Cell Styles    ${sheetName}    ${UniqueIdentifierInRow}     ${columnHeaderName}

*** Test Cases ***
Testcase For Reset Cell Styles
    Keyword for reset cell styles in excel sheet    Sheet1    E7    Full Name
    [Tags]    color2     test
```