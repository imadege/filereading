## Data Input and validation Test 

This command-line program simply extracts data from files, probrabbly CSV(Support of other files can easily be added by extending the main RowbasedImport class).

 ## Validation
Validates the data extracted and outputs in the format specified by the user. Validation rules can also be extended from the utils files and update on the validation schema of the dictionary. 

``` path to validation utils (./utils.py)```
``` Validation Schema Snapshot
   validations = {
    "name": lambda x: isinstance(x, str) and max_length(x, 100),
    "address": lambda x: len(x) > 0,
    "stars": lambda x: is_within_range(x, 0, 5),
    "contact": lambda x: len(x) > 0,
    "phone": lambda x: len(x) > 0,
    "url": lambda x: is_url(x),
}
```
Assumptions made during validation is that all columns must have data 

## OutPut 

The script can outpudata in either ```JSON FORMAT``` or ```XML Format``` however, the script can be modified to add more output formats 

## Requirements 
Please make sure your environment supports the following

``` Python3.6 and above ```

``` Pipenv ``` 

```Linux or Mac Os ```


## Installation

Follow this instruction to set up the command line program

```bash
pip install pipenv

pipenv install
```

## Usage

```
python3 server.py path-to-csv-file 

```
Specify output format and input file type 
```
python3 server.py path-to-csv-file --type='csv' --output='json'

python3 server.py path-to-csv-file --type='csv' --output='xml'

python3 server.py path-to-csv-file --type='xml' --output='json'

```
## Assumption made while working on the code 

```
- All the data will be rejected if any of the data is invalid 
- Invalid Filetypes (Not csv)  uploaded will be rejected
- The default output is json 
- The default file is csv
```

## Improvements 
Validate data against exisitng data to avoid duplicates 

## Thank you! 