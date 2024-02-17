import yaml
from datetime import datetime
import exceptions.exceptions as AuthEx


def validate_parameters_exist(*args) -> bool: 
    '''Returns True if *params have values or False is a given argument's value is None'''

    for arg in args:
        if arg == None:
            return False
        else:
            continue
    return True
    


def validate_parameters_type(exp_type: type, *args ) -> bool|type:
    '''Returns True if *params are of exp_type or the argument type that failes the check'''

    for arg in args:
        if type(arg) == exp_type:
            continue
        else:
            return type(arg)
    return True



def unix_to_date(unix_timestamp: int) -> str:
    '''Converts a Unix timestampt to a human readable datetime'''

    try:
        if validate_parameters_exist(unix_timestamp) == True:
            if validate_parameters_type(int, unix_timestamp) == True: 
                unit_conv = float(unix_timestamp / 1000)
                date_conv = str(datetime.utcfromtimestamp(unit_conv))
                return date_conv
            else:
                raise AuthEx.InvalidParameterType(unix_timestamp, float, unix_to_date.__name__)
        else:
            raise AuthEx.EmptyParameter(unix_to_date.__name__)
    except AuthEx.EmptyParameter as err:
        print(err.error_msg())
        return None
    except AuthEx.InvalidParameterType as err:
        print(err.error_msg())
        return None  


def settings() -> dict:
    '''loads the program's settings file into a python dict'''

    try:

        with open("file_paths.yaml") as paths_file:
            paths = yaml.safe_load(paths_file)
            settings_file_path = paths["program_files"]["settings"]

        with open(settings_file_path, mode='r') as settings_file:
            settings = yaml.safe_load(settings_file)
            return settings
        
    except FileNotFoundError as err:
        print("FileNotFoundError: Could not open <File: {}>. 1. Check to make sure that the file exists.\n2. That the file is in the program's working directory.\n".format(err.filename))
        return None
    except FileExistsError as err:
        print("FileNotFoundError: Could not open <File: {}>. 1. Check to make sure that the file exists.\n2. That the file is in the program's working directory.\n".format(err.filename))
        return None
    

def req_params() -> dict:
    '''loads the program's request parameters file into a python dict'''

    try:

        with open("file_paths.yaml") as paths_file:
            paths = yaml.safe_load(paths_file)
            request_file_path = paths["api_files"]["request_parameters"]

        with open(request_file_path, mode='r') as req_param_file:
            request_parameters = yaml.safe_load(req_param_file)
            return request_parameters
        
    except FileNotFoundError as err:
        print("FileNotFoundError: Could not open <File: {}>. 1. Check to make sure that the file exists.\n2. That the file is in the program's working directory.\n".format(err.filename))
        return None
    except FileExistsError as err:
        print("FileNotFoundError: Could not open <File: {}>. 1. Check to make sure that the file exists.\n2. That the file is in the program's working directory.\n".format(err.filename))
        return None
    

def file_paths() -> dict:
    '''loads the local file_paths.yaml configuration file into a python dict'''

    try:
        
        with open("file_paths.yaml") as paths_file:
            paths = yaml.safe_load(paths_file)
            return paths
        
    except FileNotFoundError as err:
        print("FileNotFoundError: Could not open <File: {}>. 1. Check to make sure that the file exists.\n2. That the file is in the program's working directory.\n".format(err.filename))
        return None
    except FileExistsError as err:
        print("FileNotFoundError: Could not open <File: {}>. 1. Check to make sure that the file exists.\n2. That the file is in the program's working directory.\n".format(err.filename))
        return None
    

def verbose(console_message: str) -> None:
    '''For printing verbose program actions:
       - console_message: str -> The message desired to print 
    '''

    set_att = settings()
    is_verbose = set_att["preferences"]["verbose?"]

    ensure_values_exist = validate_parameters_exist(is_verbose)
    ensure_bool_type = validate_parameters_type(bool, is_verbose)

    if ensure_values_exist == True:
        pass
    else:
        print(AuthEx.ErrorMessage.settings_file_err)
        raise AuthEx.EmptyParameter(verbose.__name__)
    if ensure_bool_type == True:
        pass
    else:
        print(AuthEx.ErrorMessage.settings_file_err)
        raise AuthEx.InvalidParameterType(ensure_bool_type, bool, verbose.__name__)
    
    if is_verbose == True:
        print(console_message)
        return
    else:
        return
