# library to access API Data from 'polygon.io and then export that data
import re
import requests
import json
import yaml
import exceptions.exceptions as AuthEx
from datetime import datetime
import os.path as ospath
import toolkit 


class GetApiData():
    """class serves as an engine to access API data"""

    def generate_request_url2(self, endpoint: str, options_ticker: str=None, ticker: str=None, date: str=None) -> str:
        '''Returns a properly formatted request url for 'polygon.io:
           - endpoint: str -> Needs to be the name of an endpoint listed in 'request_parameters.yaml
           - options_ticker, ticker, date: str -> If not supplied, function will use defaults from request_parameters.yaml  
        '''

        try:

            opt_tick = options_ticker
            stock_ticker = ticker
            day = date

            req_param_yaml = toolkit.req_params()
            request_parameters = dict(req_param_yaml[endpoint]["parameters"])
            endpoint_url = req_param_yaml[endpoint]["url"]

            default_opt_tick = req_param_yaml["asset_parameters"]["options_ticker"]
            default_stock_tick = req_param_yaml["asset_parameters"]["ticker"]
            default_date = req_param_yaml["asset_parameters"]["date"]

            toolkit.verbose("Validating parameters for {}...".format(self.generate_request_url2.__name__))

            ensure_end_exist = toolkit.validate_parameters_exist(endpoint)
            ensure_end_str = toolkit.validate_parameters_type(str, endpoint)
            ensure_defaults_exist = toolkit.validate_parameters_exist(default_opt_tick, default_stock_tick, default_date)
            ensure_default_types = toolkit.validate_parameters_type(str, default_opt_tick, default_stock_tick, default_date)
            

            if ensure_end_exist == True:
                pass
            else:
                raise AuthEx.EmptyParameter(self.generate_request_url2.__name__)
            if ensure_end_str == True:
                pass
            else:
                raise AuthEx.InvalidParameterType(ensure_end_str, str, self.generate_request_url2.__name__)
            if ensure_defaults_exist == True:
                pass
            else:
                print(AuthEx.ErrorMessage.req_params_yaml_err)
                raise AuthEx.EmptyParameter(self.generate_request_url2.__name__)
            if ensure_default_types == True:
                pass
            else:
                print(AuthEx.ErrorMessage.req_params_yaml_err)
                raise AuthEx.InvalidParameterType(ensure_default_types, str, self.generate_request_url2.__name__)
            
            if toolkit.validate_parameters_exist(opt_tick) == True:
                pass
            else:
                opt_tick = default_opt_tick
            if toolkit.validate_parameters_exist(stock_ticker) == True:
                pass
            else:
                stock_ticker = default_stock_tick
            if toolkit.validate_parameters_exist(day) == True:
                pass
            else:
                day = default_date
            if toolkit.validate_parameters_type(str, opt_tick, stock_ticker, day) == True:
                pass
            else:
                raise AuthEx.InvalidParameterType(toolkit.validate_parameters_type(str, opt_tick, stock_ticker, day), str, self.generate_request_url2.__name__)
            
            toolkit.verbose("OK!\n")

            date_regex = re.compile("(?<=/)\{(?:date)\}")
            options_ticker_regex = re.compile("(?<=/)\{(?:optionsTicker)\}")
            ticker_regex = re.compile("(?<=/)\{(?:ticker)\}")

            url_buffer = re.sub(date_regex, day, endpoint_url)
            url_buffer2 = re.sub(options_ticker_regex, opt_tick, url_buffer)
            url_buffer3 = re.sub(ticker_regex, stock_ticker, url_buffer2)

            parameters_list = []
            endpoint_string = ""

            toolkit.verbose("Validating filters from 'request_parameters.yaml'...")

            for key, value in request_parameters.items():
                type_check = toolkit.validate_parameters_type(str, value)
                if value == None:
                    pass
                elif type_check != True:
                    print(AuthEx.ErrorMessage.req_params_yaml_err)
                    raise AuthEx.InvalidParameterType(type_check, str, self.generate_request_url2.__name__)
                else:
                    parameters_list.append(key + "=" + value)
            
            toolkit.verbose("OK!\n")

            endpoint_string = "&".join(parameters_list)

            request_url = url_buffer3 + endpoint_string    
            
            toolkit.verbose("Created request url for endpoint: {}\n".format(request_url))

            return request_url
    
        except AuthEx.EmptyParameter as err:
            print(err.error_msg())
            return None
        except AuthEx.InvalidParameterType as err:
            print(err.error_msg())
            return None
        except Exception as err:
            print(err.__cause__)
            print(err.with_traceback)
            print("AuthorError: This is an unexpected and unhandled error. Investigate immediately!")
            return None
            

    def request_data(self, url: str) -> dict:
        '''Makes a 'GET' API request to polygon.io and returns the response:
           - url: str -> Formatted endpoint request url. Use the 'generate_request_url2()' return value! 
        '''

        try:

            settings = toolkit.settings()
            api_key = settings["static"]["api_key"]

            ensure_value_exists = toolkit.validate_parameters_exist(url, api_key)
            ensure_str_type = toolkit.validate_parameters_type(str, url, api_key)

            toolkit.verbose("Validating parameters for {}...".format(self.request_data.__name__))
            
            if ensure_value_exists == True:
                pass
            else:
                raise AuthEx.EmptyParameter(self.request_data.__name__)
            if ensure_str_type == True:
                pass
            else:
                raise AuthEx.InvalidParameterType(ensure_str_type, str, self.request_data.__name__)
            
            
            toolkit.verbose("OK!\n")
            
            toolkit.verbose("Sending 'GET' request to: {}".format(url))
            headers = {"Authorization" : api_key}
            response = requests.get(url, headers=headers)

            if response.status_code != 200:
                raise AuthEx.RequestStatusCodeError(response.reason, response.status_code)
            else:
                if response.content == None:
                    raise AuthEx.NoDataInResponse(url)
                else:
                    toolkit.verbose("Request successful!\n")
                    response_object = json.loads(response.content)
                    return response_object

        except AuthEx.EmptyParameter as err:
            print(err.error_msg())
            return None
        except AuthEx.InvalidParameterType as err:
            print(err.error_msg())
            return None
        except AuthEx.RequestStatusCodeError as err:
            print(err.error_msg())
            return None
        except AuthEx.NoDataInResponse as err:
            print(err.error_msg())
            return None
        


class ExportApiData():
    """class serves as an engine to export api data"""

    def sort_api_data(self, data_object: dict, request_url_stamp: str) -> dict:
        '''changes certain values to be human readable and adds program stamp(s) to an API response from polygon.io:
           - date_object: dict -> Give the raw response from 'request_data()'
           - request_url_stamp: str -> Will stamp 'request_url' into the raw response. Encouraged to enter the url/endpoint from which you recieved the response. Can use 'generate_request_url2()' as the value.
        '''
        try:
            ensure_values_exist = toolkit.validate_parameters_exist(data_object, request_url_stamp)
            ensure_str_type = toolkit.validate_parameters_type(str, request_url_stamp)
            ensure_dict_type = toolkit.validate_parameters_type(dict, data_object)

            toolkit.verbose("Validating parameters for {}...".format(self.sort_api_data.__name__))

            if ensure_values_exist == True:
                pass
            else:
                raise AuthEx.EmptyParameter(self.sort_api_data.__name__)
            if ensure_str_type == True:
                pass
            else:
                raise AuthEx.InvalidParameterType(ensure_str_type, str, self.sort_api_data.__name__)
            if ensure_dict_type == True:
                pass
            else:
                raise AuthEx.InvalidParameterType(ensure_dict_type, dict, self.sort_api_data.__name__)

            toolkit.verbose("OK!\n")

            timestamp_object = datetime.now()
            timestamp = str(timestamp_object)
            data = data_object

            toolkit.verbose("Adding program metadata...\n")

            data.update({"auto": {}})
            data["auto"]["auto_timestamp"] = timestamp 
            data["auto"]["auto_url"] = request_url_stamp 

            values_dict = data["results"]["values"]

            toolkit.verbose("Converting UNIX timestamps to datetime...")
            
            for entry in values_dict:
                for key in entry:
                    if key == "timestamp":
                        entry[key] = toolkit.unix_to_date(entry[key])

            toolkit.verbose("Success!\n")
            return data

        except AuthEx.EmptyParameter as err:
            print(err.error_msg())
            return None
        except AuthEx.InvalidParameterType as err:
            print(err.error_msg())
            return None
        except KeyError as err:
            if "values" in err.args:
                print("Warning: No values found in response!")
                return data
            else:
                print("UNHANDLED ERROR!")
                return None
        except TypeError as err:
            return data



    def write_yaml(self, data_object: dict, filename: str, write_file_dir: str=None) -> None:
        '''Writes a dictionary data object (ex. api response) to a .yaml file'''

        try:        
            ensure_values_exist = toolkit.validate_parameters_exist(data_object, filename)
            ensure_str_type = toolkit.validate_parameters_type(str, filename)
            ensure_dict_type = toolkit.validate_parameters_type(dict, data_object)

            write_directory = write_file_dir

            toolkit.verbose("Validating parameters for {}...".format(self.write_yaml.__name__))

            if ensure_values_exist == True:
                pass
            else:
                raise AuthEx.EmptyParameter(self.write_yaml.__name__)
            if ensure_str_type == True:
                pass
            else:
                raise AuthEx.InvalidParameterType(ensure_str_type, str, self.write_yaml.__name__)
            if ensure_dict_type == True:
                pass
            else:
                raise AuthEx.InvalidParameterType(ensure_dict_type, dict, self.write_yaml.__name__)
            
            if toolkit.validate_parameters_exist(write_directory) == True:
                if toolkit.validate_parameters_type(str, write_directory) == True:
                    pass
                else:
                    raise AuthEx.InvalidParameterType(toolkit.validate_parameters_type(str, write_directory), str, self.write_yaml.__name__)
            else:
                file_paths = toolkit.file_paths()
                write_directory = file_paths["api_files"]["api_export"]
                if toolkit.validate_parameters_type(str, write_directory) == True:
                    pass
                else:
                    print(AuthEx.ErrorMessage.file_paths_yaml_err)
                    raise AuthEx.InvalidParameterType(toolkit.validate_parameters_type(str, write_directory), str, self.write_yaml.__name__)

            toolkit.verbose("OK!\n")
            toolkit.verbose("Validating file extension...")

            split_ext = ospath.splitext(filename)
            file_ext = split_ext[1].lower()
            if file_ext != ".yaml":
                file_ext = ".yaml"
                filename = split_ext[0] + file_ext
            elif file_ext == None:
                filename = filename + ".yaml"
            else:
                pass

            toolkit.verbose("OK!\n")

            full_path = write_directory + filename

            toolkit.verbose("Opening {} for writing...".format(full_path))
            
            with open(full_path, mode='a+') as write_file:
                yaml.safe_dump(data_object, write_file, explicit_start=True)

            toolkit.verbose("Successfully wrote data to file: {}\n".format(full_path))
            return
        
        except AuthEx.EmptyParameter as err:
            print(err.error_msg())
            return None
        except AuthEx.InvalidParameterType as err:
            print(err.error_msg())
            return None
        except FileNotFoundError as err:
            print("\nFileNotFoundError: {}\n".format(err.__cause__))
            return None
        
        

    def write_json(self, data_object: dict, filename: str, write_file_dir: str=None) -> None:
        '''Writes a dictionary data object (api response)to a .json file'''

        try:        
            ensure_values_exist = toolkit.validate_parameters_exist(data_object, filename)
            ensure_str_type = toolkit.validate_parameters_type(str, filename)
            ensure_dict_type = toolkit.validate_parameters_type(dict, data_object)

            write_directory = write_file_dir

            toolkit.verbose("Validating parameters for {}...".format(self.write_json.__name__))

            if ensure_values_exist == True:
                pass
            else:
                raise AuthEx.EmptyParameter(self.write_json.__name__)
            if ensure_str_type == True:
                pass
            else:
                raise AuthEx.InvalidParameterType(ensure_str_type, str, self.write_json.__name__)
            if ensure_dict_type == True:
                pass
            else:
                raise AuthEx.InvalidParameterType(ensure_dict_type, dict, self.write_json.__name__)
            
            if toolkit.validate_parameters_exist(write_directory) == True:
                if toolkit.validate_parameters_type(str, write_directory) == True:
                    pass
                else:
                    raise AuthEx.InvalidParameterType(toolkit.validate_parameters_type(str, write_directory), str, self.write_json.__name__)
            else:
                file_paths = toolkit.file_paths()
                write_directory = file_paths["api_files"]["api_export"]
                if toolkit.validate_parameters_type(str, write_directory) == True:
                    pass
                else:
                    print(AuthEx.ErrorMessage.file_paths_yaml_err)
                    raise AuthEx.InvalidParameterType(toolkit.validate_parameters_type(str, write_directory), str, self.write_json.__name__)

            toolkit.verbose("OK!\n")
            toolkit.verbose("Validating file extension...")

            split_ext = ospath.splitext(filename)
            file_ext = split_ext[1].lower()
            if file_ext != ".json":
                file_ext = ".json"
                filename = split_ext[0] + file_ext
            elif file_ext == None:
                filename = filename + ".json"
            else:
                pass

            toolkit.verbose("OK!\n")

            full_path = write_directory + filename

            toolkit.verbose("Opening {} for writing...".format(full_path))

            with open(full_path, mode='a+') as write_file:
                json.dump(data_object, write_file, indent=4)

            toolkit.verbose("Successfully wrote data to file: {}\n".format(full_path))
            return
        
        except AuthEx.EmptyParameter as err:
            print(err.error_msg())
            return None
        except AuthEx.InvalidParameterType as err:
            print(err.error_msg())
            return None
        except FileNotFoundError as err:
            print("Error!: Invalid file directory specified in 'file_paths.yaml'[api_parameters][api_export].\n Could not write file.\n")
            return None
