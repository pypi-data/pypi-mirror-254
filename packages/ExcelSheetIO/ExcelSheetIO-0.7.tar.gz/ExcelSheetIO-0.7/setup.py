import codecs
from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='ExcelSheetIO',
    version='0.7',
    author="Soumyajit Pan",
    author_email="soumyajitmahi7@gmail.com",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='A Python package for efficient Excel sheet operations. Enables easy read/write functionality, data manipulation, and workflow automation. Ideal for handling both small and large datasets. Get started with ExcelSheetIO for a simplified data processing experience.',
    keywords=['excelsheetio', 'excel', 'excelreader', 'excelwriter', 'python', 'excel reader and writer', 'read excel data using python', 'write data in excel using python', 'excelsheetio'],
    install_requires=[
        'attrs>=23.2.0',
        'certifi>=2023.11.17',
        'cffi>=1.16.0',
        'contourpy>=1.1.1',
        'cycler>=0.12.1',
        'et-xmlfile>=1.1.0',
        'exceptiongroup>=1.2.0',
        'fonttools>=4.47.2',
        'h11>=0.14.0',
        'idna>=3.6',
        'importlib-resources>=6.1.1',
        'kiwisolver>=1.4.5',
        'matplotlib>=3.7.4',
        'natsort>=8.4.0',
        'numpy>=1.24.4',
        'openpyxl>=3.1.2',
        'outcome>=1.3.0.post0',
        'packaging>=23.2',
        'pillow>=10.2.0',
        'pycparser>=2.21',
        'pyparsing>=3.1.1',
        'PySocks>=1.7.1',
        'python-dateutil>=2.8.2',
        'robotframework>=7.0',
        'robotframework-pabot>=2.17.0',
        'robotframework-pythonlibcore>=4.3.0',
        'robotframework-seleniumlibrary>=6.2.0',
        'robotframework-stacktrace>=0.4.1',
        'selenium>=4.17.2',
        'six>=1.16.0',
        'sniffio>=1.3.0',
        'sortedcontainers>=2.4.0',
        'trio>=0.24.0',
        'trio-websocket>=0.11.1',
        'typing-extensions>=4.9.0',
        'urllib3>=2.1.0',
        'wsproto>=1.2.0',
        'zipp>=3.17.0',
    ],
    url="https://pypi.org/project/ExcelSheetIO/",
    license="MIT",
)
