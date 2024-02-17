# This module is simply to provide a basic working example of data_access module. It is primitive and relies only on the
#   built in error handling of the 'data_access.py' module. The basic command prompt is binded to these two functions below.  

#import needed libraries
import data_access
import time
import toolkit

# initialize classes from the data_access module
api_access = data_access.GetApiData()
export_api = data_access.ExportApiData()

# function to test a basic implementation of the program. This will make one request and then write the sorted response to a .yaml AND a .json file
def test(endpoint_yaml: str) -> None:
    '''Just a test'''
    # create request url, make the request and then sort/stamp the response object in that order
    # Can easily make the next three lines a one-liner 
    url = api_access.generate_request_url2(endpoint_yaml)
    api_data = api_access.request_data(url)
    sorted_data = export_api.sort_api_data(api_data, url)

    # write data to .yaml and .json respectively
    export_api.write_yaml(sorted_data, "test.yaml")
    export_api.write_json(sorted_data, "test.json")
    return

# A more advanced example of how we can use pagination to recursively gather large amounts of data
def test_pagination(endpoint_yaml: str) -> None:
    '''Just a test'''

    file_series_id = "test"
    loop = True

    toolkit.verbose("Accessing initial API call...")

    next_page_url = ""
    api_data = {}
    file_count = 1
    primary_url = ""
    file_name = "{}{}".format(file_series_id, str(file_count))

    primary_url = api_access.generate_request_url2(endpoint_yaml)
    api_data = api_access.request_data(primary_url)
    sorted_data = export_api.sort_api_data(api_data, primary_url)

    export_api.write_yaml(sorted_data, file_name)
    file_count += 1
    
    time.sleep(15)
    
    while loop == True:
        next_page_url = ""
        page_url_stamp = "page_{}_from: {}".format(str(file_count), primary_url)
        file_name = "{}{}".format(file_series_id, str(file_count))
        if "next_url" in api_data.keys():
            next_page_url = api_data["next_url"]
            api_data = api_access.request_data(next_page_url)
            data_sorted = export_api.sort_api_data(api_data, page_url_stamp)
            export_api.write_yaml(data_sorted, file_name)
            file_count += 1
            time.sleep(15)
            toolkit.verbose("DONE!")
        else:
            loop = False
            toolkit.verbose("No more pages to get. Terminating pagination stream!")
            return
                

## == powerful data harvesting in under 100 lines of code! Thanks for checking out the project