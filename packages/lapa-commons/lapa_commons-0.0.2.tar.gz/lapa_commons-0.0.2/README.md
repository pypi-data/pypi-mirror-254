# lapa_commons

## About

Lapa commons used for reading the configuration file.

## Installation

> pip install lapa_commons

## Env

- python>=3.12.0

## Usage

### Create sample config.ini

```
[ENVIRONMENT]
log_level = INFO

[DATABASE]
Db_Host = localhost
Db_Port = 5432
Db_Name = my_database
Db_User = my_user
Db_Password = my_password

[API]
API_KEY = abcdef1234567890
BASE_URL = https://api.example.com/v1
```

### Sample code

```
# import lapa_commons
from lapa_commons.main import read_configuration_from_file_path

# call the read_configuration_from_file_path() and provide file path
ldict_configuration = read_configuration_from_file_path('/home/lavsharma/python-project/temp/config.ini')
```

### Output

```
{'API': {'API_KEY': 'abcdef1234567890', 'BASE_URL': 'https://api.example.com/v1'}, 'DATABASE': {'Db_Host': 'localhost', 'Db_Name': 'my_database', 'Db_Password': 'my_password', 'Db_Port': '5432', 'Db_User': 'my_user'}, 'ENVIRONMENT': {'log_level': 'INFO'}}
```

## Changelog

### v0.0.2

- bug fix when reading environment variables.

### v0.0.1

1. configparser added in the dependency.
2. Function read_configuration_from_file_path() added which reads the configuration from a filepath.
3. Support for any number of sections in the configuration file.
4. Environment section variables will be first checked in the OS, if not found in the OS then it will be read from the
   configuration file.
5. MODULE_NAME added in the **init**.py
6. Errors are raised in the module instead of logging.
