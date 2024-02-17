# **PolyPy**
## Intro:
Polypy is meant to a be a small, straightforward library that interfaces with the official **`Polygon.io`** Api. The library is currently in Alpha developement, as it lacks a complete configuration file of api endpoints to interface with as well as does not support **polygon.io's** websocket endpoints for real time data. It currently only has core functionality surrounding _stock-options_ related endpoints. That being said, the core module **`data_access.py`** depends on _.yaml_ configuration files for all api endpoints (and other configurations), and is coded in a way that makes adding functionality a matter of copy and paste (which will be done after unit testing this release's framework). The most important limitation is that the polygon.io api itself is _extremely_ limited unless you pay a subscription for premium data rates. The free data rate is 5 api calls/minute along with only previous day data available. This is far too slow for any high performance project, but would be fine for gathering backtesting data. There is more information on these subjects below. Thanks for checking out the project!

## **Table Of Contents:**
1. Functions
2. Configuration
3. End

## 1. Functions:
This release has the core functionality broken down into two classes within the **`data_access.py`** module. 
1. **GetApiData** - Functions make up a sort of modular engine for generating formatted request urls, and then making those api calls.
2. **ExportApiData** - Functions to stamp and export the data to .yaml files and/or .json files.

The polypy library also has a module, **toolkit.py** that contains functions for internal type checking, checks for existing parameters, program verbosity, retrieving configuration values and data conversion. Some of these functions are used internally in **data_access.py**, but can also aid in the flow of programming when using polypy.

The full function list for the `toolkit.py` module is as follows:
1. ### toolkit
    + `def validate_parameters_exist(*args) -> bool`: 
        '''Returns True if *params have values or False is a given argument's value is None'''
    + `def validate_parameters_type(exp_type: type, *args ) -> bool|type`:
        '''Returns True if *params are of exp_type or the argument type that failes the check'''
    + `def unix_to_date(unix_timestamp: int) -> str`:
        '''Converts a Unix timestampt to a human readable datetime'''
    + `def settings() -> dict`:
        '''loads the program's settings file into a python dict'''
    + `def req_params() -> dict`:
        '''loads the program's request parameters file into a python dict'''
    + `def file_paths() -> dict`:
        '''loads the local file_paths.yaml configuration file into a python dict'''
    + `def verbose(console_message: str) -> None`:
        '''For printing verbose program actions:
            - console_message: str -> The message desired to print 
        '''

    The **toolkit.py** module streamlines the task of accessing configuration file values via the `settings()`, `req_params()` and `file_paths()` functions. The three afromentioned functions do the work of locating, then opening configuration files and returning a python dictionary representing the values within.
    + **settings()** - returns a dictionary of program settings. Takes no arguments.
    + **req_params()** - returns a dictionary of request parameters, which are used to configure api calls. Takes no arguments.
    + **file_paths()** - returns a dictionary of file paths for all other program files. Takes no arguments.

    These functions help clean up code from this for each configuration file:
    ```
    try:

            settings = {}

            with open("file_paths.yaml") as paths_file:
                paths = yaml.safe_load(paths_file)
                settings_file_path = paths["program_files"]["settings"]

            with open(settings_file_path, mode='r') as settings_file:
                settings = yaml.safe_load(settings_file)

            some_config_value = settings[value][value2]
            
        except FileNotFoundError as err:
            print("FileNotFoundError: Could not open <File: {}>. 1. Check to make sure that the file exists.\n2. That the file is in the program's working directory.\n".format(err.filename))
            return None
        except FileExistsError as err:
            print("FileNotFoundError: Could not open <File: {}>. 1. Check to make sure that the file exists.\n2. That the file is in the program's working directory.\n".format(err.filename))
            return None
    ```
    Into this:
    ```
    from polypy import toolkit
    settings = toolkit.settings()
    some_config_value = settings[value][value2]
    ```

2. ### data_access.py

    The **GetApiData** class is written as an engine to make api calls to `polygon.io`. The `request_parameters.yaml` file contains all configured polygon.io api endpoints and their respective parameters. Each endpoint has a section of configuration values. Take a look at the snippet of the `request_parameters.yaml` file below for a line by line breakdown:
    ```
    simple_moving_average: -> This is the dictionary key you would refer to when wanting to call the 'simple moving average' api endpoint, for example. DO NOT CHANGE 
        url: "https://api.polygon.io/v1/indicators/sma/{optionsTicker}?" -> Base url for this specific endpoint. *see note for the curly {} brackets at the bottom. DO NOT CHANGE
        parameters: -> The collection of keys + values below are the parameters for the request itself. These should be THE ONLY values to change within each endpoint's section/dict.
            timestamp: null
            timespan: "day"
            adjusted: "true"
            window: "200"
            series_type: null
            expand_underlying: "true"
            order: "desc"
            limit: "10"

    NOTE: The curly {} brackets and text within are placeholders for a regular expression engine in the `generate_request_url2()` function and need to be notated in this way.
    ```  
    + `def generate_request_url2(self, endpoint: str, options_ticker: str=None, ticker: str=None, date: str=None) -> str`:
        '''Returns a properly formatted request url for 'polygon.io:
           - endpoint: str -> Needs to be the name of an endpoint listed in 'request_parameters.yaml
           - options_ticker, ticker, date: str -> If not supplied, function will use defaults from request_parameters.yaml  
        '''
        + endpoint: str -> A string with the name of the endpoint in **request_parameters.yaml**, which we just looked over. Ex. "simple_moving_average"
        + options_ticker, ticker, date: str -> Arguments should be strings representing target infromation for making a request. All three values are required. However, if none are supplied to the function as arguments, then defaults from 'request_parameters.yaml' will be used. If no values are present there either, then an error may result depending on what endpoint you are requesting data from. This is due to the regular expression engine within the function.

    + `def request_data(self, url: str) -> dict`:
        '''Makes a 'GET' API request to polygon.io and returns the response:
           - url: str -> Formatted endpoint request url. Use the 'generate_request_url2()' return value! 
        '''
        + url: str -> Needs to be a properly formatted api endpoint url. Simply use **generate_request_url2()** return value.

    NOTE: An example of implementing these functions can be found in `example.py` of this module's working directory! You can try out the simple implementation by running the `api_cmd.py` file.

    
    The **ExportApiData** class contains methods for organizing and exporting an api response to a file.

    + `def sort_api_data(self, data_object: dict, request_url_stamp: str) -> dict`:
        '''changes certain values to be human readable and adds program stamp(s) to an API response from polygon.io:
           - date_object: dict -> Give the raw response from 'request_data()'
           - request_url_stamp: str -> Will stamp 'request_url' into the raw response. Encouraged to enter the url/endpoint from which you recieved the response. Can use 'generate_request_url2()' as the value
        '''
    + `def write_yaml(data_object: dict, filename: str, write_file_dir: str=None) -> None:`
        '''Writes a dictionary data object (ex. api response) to a .yaml file'''
        + data_object: dict -> A data dictionary to write to a file. Can use a raw response, but would reccomend using the return value from **sort_api_data()**
        + filename: str -> A string for the filename you wish to use. This function fixes improper file extensions (including no file extension)
        + write_file_dir: str=None -> Optional parameter, which should be a string notating the directory to write the file into. Defaults to _api_export_ in 'file_paths.yaml' if no argument is given
    + `def write_json(data_object: dict, filename: str, write_file_dir: str=None) -> None:`
        '''Writes a dictionary data object (api response)to a .json file'''
        + data_object: dict -> A data dictionary to write to a file. Can use a raw response, but would reccomend using the return value from **sort_api_data()**
        + filename: str -> A string for the filename you wish to use. This function fixes improper file extensions (including no file extension)
        + write_file_dir: str=None -> Optional parameter, which should be a string notating the directory to write the file into. Defaults to _api_export_ in 'file_paths.yaml' if no argument is given
     


## Configuration:

Configuration in polypy revolves around 3 included program files - _file\_paths.yaml_, _settings.yaml_ and _request\_parameters.yaml_. `file_paths.yaml` is the only one of these files that _can not_ move from the program's working directory. This file contains the file paths for _settings.yaml_, _request\_parameters.yaml_, the path to the directory in which you wish to export files and potentially any other file you may want to work into a program. Both of the other program files are by default stored in the program's working directory (polypy/program_files/), but can be stored anywhere that is convenient for you. Note that you _can_ rename them (besides file_paths.yaml) but are encouraged to keep them named as is and just cut+paste them to avoid confusion. The following configuration tutorial will assume that the user may not want/know how to code. If you do, then you can skip this section with the information you already know about the program. 

The default _file\_paths.yaml_ file looks like this:
```
---
api_files: 
  request_parameters: "path/to/request_parameters.yaml"
  api_export: "path/to/you/data/export/directory"

program_files:
  settings: "path/to/settings.yaml"

```
You probably want your files in a location that makes sense to _you_. Simply move the files where you want them and copy the path to the appropriate entry in the file! Ensure that the file path is written/copied properly and is contained within the double `""` quotes.

The _settings.yaml_ file contains static program configuration values such as your api key. The default file is as follows:
```
---
static: 
  api_key: "Bearer 123apikey321" -> Api key from polygon.io goes in this field formatted with 'Bearer', a space and then the key.
  request_rate: 15 #seconds -> The rate at which the program will make requests, in seconds. Free api key rate is 5 calls/minute. This is set @ 4 calls/minute

preferences: 
  verbose?: true
```
As with the fields in _file\_paths.yaml_, all values must be enclosed in double `""` quotes. This is true for all values in any configuration file for this module! Note that the verbose option is 'true' by default. simply insert 'false' as the value (no qoutes) to remove verbose program activity from the command line while running.

Finally we have the _request\_parameters.yaml_ file. Below is a snippet:
```
simple_moving_average: -> endpoint key used to id the endpoint by the module - **Don't Touch!** 
  url: "https://api.polygon.io/v1/indicators/sma/{optionsTicker}?" - > The base url with placeholder for regular expressions - **Don't Touch!**
  parameters: -> Key for program to get params - **Don't Touch!**
    timestamp: null - > Everything from here down is a parameter that can be adjusted to return different information from the api. All of these can be changed.
    timespan: "day"
    adjusted: "true"
    window: "200"
    series_type: null
    expand_underlying: "true"
    order: "desc"
    limit: "10"

exponential_moving_average: 
  url: "https://api.polygon.io/v1/indicators/ema/{optionsTicker}?"
  parameters: 
    timestamp: null
    timespan: "day"
    adjusted: "true"
    window: "50"
    series_type: "close"
    expand_underlying: "true"
    order: "desc"
    limit: "10"
```
Above we have two api endpoints. One for simple moving average (SMA), and one for exponential moving average (EMA). The SMA is marked up to show you what values can be changed, just as seen previously in this README file. As you can see, all values under the `parameters` key can be changed to suit your needs. Just remember to keep values in quotes as always. To refer to what these values should/can be, take a look at  https://polygon.io/docs/options/getting-started.
   
## End:
As always, thanks for checking out the project! As we are in Alpha release, documentation will be only this page. As the module enters >= Beta, more comprehensive docs will be supplied along with the added functionality. 