# custom error handling

class RequestStatusCodeError(Exception):
    """handles an API request status code != 200"""

    def __init__(self, status_code, reason):
        self.status_code = status_code
        self.reason = reason

    def error_msg(self):
        msg = "\nError!: Response status code: {} > {}.\n".format(self.status_code, self.reason)
        return msg
    
    


class NoDataInResponse(Exception):
    """handles no data from an API response"""
    
    def __init__(self, request_url, function):
        self.request_url = request_url
        self.function = function

    def error_msg(self):
        request_url = str(request_url)
        function = str(self.function)

        msg = "\nError!: No data in response object in <Function: {}> | <Request:{}>\n".format(function, request_url)
        return msg
    


class EmptyParameter(Exception):
    """handles a required program parameter not being present(p=None/p=Null)"""

    def __init__(self, function):
        self.function = function

    def error_msg(self):

        function = str(self.function)

        msg = "\nError!: A parameter in <Function>: {}> had a value of None.\n".format(function)
        return msg



class InvalidParameterType(Exception):
    """handles recieving a parameter with a type that was unexpected"""

    def __init__(self, parameter_type: type, expected_type: type, function):
        self.type = parameter_type
        self._exp_type = expected_type
        self.function = function

    def error_msg(self):

        got_type = self.type
        expected_type = self.type
        function = str(self.function)

        msg = "Error!: Expected a {} type parameter, got a {} type instead in <Function: {}>\n".format(expected_type, got_type, function)
        return msg
    


class InvalidParameter(Exception):
    """Handles parameters that are invalid for another reason other than type or existence"""

    def __init__(self, function):
        self.function = function

    def error_msg(self):

        function = str(self.function)

        msg = "\nError!: Invalid parameter in <Function: {}>\n".format(function)
        return msg
    


class ErrorMessage(Exception):
    """Custom Error messages for built in Exceptions"""

    req_params_yaml_err = "\nError occured in 'request_parameters.yaml':"
    
    file_paths_yaml_err = "\nError occured in 'file_paths.yaml':"

    settings_file_err = "\nError occured in 'settings.yaml':"
