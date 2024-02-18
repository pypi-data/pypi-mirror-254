# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xer_reader', 'xer_reader.src']

package_data = \
{'': ['*']}

install_requires = \
['openpyxl>=3.1.2,<4.0.0']

entry_points = \
{'console_scripts': ['test = scripts:test']}

setup_kwargs = {
    'name': 'xer-reader',
    'version': '0.2.0',
    'description': 'Read and parse a Primavera P6 xer file.',
    'long_description': '# Xer-Reader\n\nRead the contents of a Primavera P6 XER file using Python.  \n\nXer-Reader makes it easy to read, parse, and convert the data in a XER file to other formats.\n\n*Refer to the [Oracle Documentation]( https://docs.oracle.com/cd/F25600_01/English/Mapping_and_Schema/xer_import_export_data_map_project/index.htm) for more information regarding how data is mapped to the XER format.  \nTested on XER files exported as versions 15.2 through 19.12.*  \n\n## Install\n\n**Windows**:\n\n```bash\npip install xer-reader\n```\n\n**Linux/Mac**:\n\n```bash\npip3 install xer-reader\n```\n\n## Usage  \n\nImport the `XerReader` class from `xer_reader`.\n```python\nfrom xer_reader import XerReader\n```\n\nCreate a new instance of an `XerReader` object by passing in the XER file as an argument. `XerReader` can accept the file path represented as a `str` or pathlib `Path` object, or a Binary file received as a response from requests, Flask, FastAPI, etc...\n\n```python\nfile = r"/path/to/file.xer"\nreader = XerReader(file)\n```\n\n### Attributes  \n\n* `data` [str] - *The contents of the XER file as a string.*\n* `export_date` [datetime] - *The date the XER file was exported.*\n* `export_user` [str] - *The P6 user who export the XER file.*\n* `export_version` [str] - *The P6 verison used to export the XER file.*\n* `file_name` [str] - *The name of the file without the \'.xer\' extension.*\n\n### Methods\n\n**`check_errors()`** -> *list[str]*  \nChecks the XER file for missing tables and orphan data, and returns the results as a list of errors.  \n\n* Missing tables can occur when an entry in *Table 1* points to an entry in *Table 2* but *Table 2* does not exist at all.\n* Orphan data occurs when an entry in *Table 1* points to an entry *Table 2* but the entry in *Table 2* does not exist.\n\n**`delete_tables(*table_names: str)`** -> *str*  \nDelete a variable number of tables (*table_names*) from the XER file data and returns a new string (*Does not modify `XerReader.data` attribute*).  \n\nIn the following example the tables associated with User Defined Fields are removed from the XER file contents and stored in a new variable `new_xer_data`, which can then be written to a new XER file:\n```python\nnew_xer_data = reader.delete_tables("UDFTYPE", "UDFVALUE")\n\nwith open("New_XER.xer", "w", encoding=XerReader.CODEC) as new_xer_file:\n    new_xer_file.write(new_xer_data)\n```\n\n**`get_table_names()`** -> *list[str]*  \nReturns a list of table names included in the XER file.  \n\n**`get_table_str(table_name: str)`** -> *str*  \nReturns the tab seperated text for a specific table in the XER file.\n\n**`has_table(table_name: str)`** -> *bool*  \nReturn True if table (`table_name`) if found in the XER file.\n\n**`parse_tables()`** -> *dict[str, Table]*  \nReturns a dictionary with the table name as the key and a `Table` object as the value.  \n\n**`to_csv(file_directory: str | Path)`** -> *None*  \nGenerate a CSV file for each table in the XER file using \'tab\' as the delimiter. CSV files will be created in the current working directory.   \nOptional: Pass a string or Path object (`file_directory`) to speficy a folder to store the CSV files in.  \n\n**`to_excel()`** -> *None*  \nGenerate an Excel (.xlsx) file with each table in the XER file on its own spreadsheet. The Excel file will be create in the \ncurrent working directory.  \n\n**`to_json(*tables: str)`** -> *str*  \nGenerate a json compliant string representation of the tables in the XER file.  \nOptional: Pass in specific table names to include in the json string.\n',
    'author': 'Jesse Jones',
    'author_email': 'code@seqmanagement.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/jjCode01/xer-reader',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
