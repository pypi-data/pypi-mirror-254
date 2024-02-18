import json
import copy
import ast
import pandas as pd
from urllib3.util import Retry
from robot.api import logger
from cqepyutils.PandasUtils import read_csv, filter_df, reset_index
from RequestsLibrary import RequestsLibrary  # Add this import statement


def trigger_api(test_data_full_path, test_input_path, api_name, base_url, auth=None):
    logger.info('*************************************************************************************************')
    logger.info(f'Trigger API using the parameters specified in the test data sheet - {api_name}')
    logger.info('*************************************************************************************************')

    logger.info('Step-01: Start - Read and filter test data sheet based on API_NAME')
    # Example of using functions from the imported module directly
    test_cases_df = read_csv(str(test_data_full_path), dtype=str)
    selected_api_df = filter_df(test_cases_df, 'test_name', api_name).copy()
    selected_api_df = filter_df(selected_api_df, 'tbe', 'YES')
    selected_api_df = reset_index(selected_api_df)
    logger.debug(f'API Name      : {api_name}')
    logger.info('Step-01: End   - Read and filter test data sheet based on API_NAME')

    logger.info('Step-02: Start - Identify the request type')
    request_type = str(selected_api_df['request_type'][0])
    logger.info('Step-02: End   - Identify the request type')

    logger.info('Step-03: Start - Assign default values to None')
    params = None
    data = None
    # auth = None
    files = None
    json_data = None
    cookies = None
    timeout = None
    proxies = None
    verify = False
    logger.info('Step-03: End   - Assign default values to None')

    logger.info('Step-04: Start - Assign project specific values')
    # Check if authorization is required
    if auth is not None:
        auth = auth.split(',')
        logger.debug(auth)
    elif pd.isna(selected_api_df.loc[0, 'auth']):
        auth = None
    else:
        auth = str(selected_api_df['auth'].item()).split(',')
    logger.info('Step-04: End   - Assign project specific values')

    logger.info('Step-05: Start - Identify uri')

    # Unique identifier for creating a session
    alias = str(api_name)

    uri = str(selected_api_df['uri'][0])
    logger.info('Step-05: End   - Identify uri')

    logger.info('Step-06: Start - Update the path parameter in URI')
    # Identify the path parameters specific columns and create a separate data frame
    selected_api_flt_pp_df = selected_api_df.filter(regex='_pp$', axis=1)

    # Identify the path parameters specific for the api
    selected_api_flt_pp_df = selected_api_flt_pp_df.dropna(axis='columns')

    # Path Params value which needs to be passed should be as dictionary
    if selected_api_flt_pp_df.empty:
        path_params = None
    else:
        path_params_list = selected_api_flt_pp_df.to_dict('records')[0]

        # Remove _pp from the parameter name
        path_params = {x.replace('_pp', ''): v for x, v in path_params_list.items()}

        # Iterate through each values and update the URL
        for key, value in path_params.items():
            uri = uri.replace(str('{') + key + str('}'), value)
        logger.debug(uri)

    logger.info('Step-06: End   - Update the path parameter in URI')

    logger.info('Step-07: Start - Create the parameter and assign to params')

    # Identify the parameters specific columns and create a separate data frame
    selected_api_flt_df = selected_api_df.filter(regex='_d$', axis=1)

    # Identify the parameters specific for the api
    selected_api_flt_df = selected_api_flt_df.dropna(axis='columns')

    # Params value which needs to be passed should be as dictionary
    if selected_api_flt_df.empty:
        params = None
    else:
        params_list = selected_api_flt_df.to_dict('records')[0]

        # Remove _d from the parameter name
        params = {x.replace('_d', ''): v for x, v in params_list.items()}
    logger.info('Step-07: End   - Create the parameter and assign to params')

    logger.info('Step-08: Start - Extract other additional information required - data, auth, headers, files')

    # Check if data level json is required (body)
    if pd.isna(selected_api_df.loc[0, 'data']):
        data = None
    else:
        file_name = str(selected_api_df['data'][0])
        with open(test_input_path + api_name + '/' + file_name + '.JSON') as f:
            data = json.load(f)

    # Check if headers is required
    headers = {}
    if pd.isna(selected_api_df.loc[0, 'headers']):
        headers = {}
    else:
        headers = {'Content-Type': 'values', 'Accept': 'values'}
        headers_type = str(selected_api_df['headers'].item())
        headers['Content-Type'] = headers_type
        headers['Accept'] = headers_type

    # Check if files is required
    files_str = ''
    if pd.isna(selected_api_df.loc[0, 'files']):
        files = None
    else:
        # Extract the files column content
        files_str = str(selected_api_df['files'][0])

        # Convert the variable to dict
        files = ast.literal_eval(files_str)

        # Iterate through the dict and open the files specified in the data sheet
        # Files will be opened in binary mode and passed to post
        for k, value in files.items():
            f = open(test_input_path + api_name + '/' + value, 'rb')
            files[k] = f

    # List of parameters required for any type of API
    logger.info('type      :' + request_type)
    logger.info('url       :' + base_url)
    logger.info('uri       :' + uri)
    logger.info('params    :' + str(params))
    logger.info('data      :' + str(data))
    logger.info('auth      :' + str(auth))
    logger.info('headers   :' + str(headers))
    logger.info('files     :' + str(files_str))

    # Static variables for the request
    max_retries = 3
    backoff_factor = 0.1
    disable_warnings = 0
    debug = 0

    logger.info('Step-08: End   - Extract other additional information required - data, auth, headers, files')

    logger.info('Step-09: Start - Trigger the API, extract the response and status code')

    # Condition to check GET/POST method
    if request_type == 'GET':

        # Response with status code, response content and api name will be returned as data frame
        # Create Session
        super(RequestsLibrary, self).create_session(alias=alias, url=base_url, headers=headers, cookies=cookies,
                                                    auth=auth, timeout=timeout, proxies=proxies, verify=verify,
                                                    debug=debug, max_retries=max_retries,
                                                    backoff_factor=backoff_factor,
                                                    disable_warnings=1)
        # Trigger GET method
        response = super(RequestsLibrary, self).get_request(alias=alias, uri=uri, headers=headers, json=data,
                                                            params=params, allow_redirects=None, timeout=timeout)
    elif request_type == 'PUT':

        # Response with status code, response content and api name will be returned as data frame
        # Create Session
        super(RequestsLibrary, self).create_session(alias=alias, url=base_url, headers=headers, cookies=cookies,
                                                    auth=auth, timeout=timeout, proxies=proxies, verify=verify,
                                                    debug=debug, max_retries=max_retries,
                                                    backoff_factor=backoff_factor,
                                                    disable_warnings=1)
        # Trigger PUT method
        response = super(RequestsLibrary, self).put_request(alias=alias, uri=uri, data=data, json=json_data,
                                                            params=params, files=files, headers=headers,
                                                            allow_redirects=None, timeout=timeout)
    elif request_type == 'POST':
        # Create Session
        super(RequestsLibrary, self).create_session(alias=alias, url=base_url, headers=headers, cookies=cookies,
                                                    auth=auth, timeout=timeout, proxies=proxies, verify=verify,
                                                    debug=debug, max_retries=max_retries,
                                                    backoff_factor=backoff_factor,
                                                    disable_warnings=1)
        # Trigger POST method
        response = super(RequestsLibrary, self).post_request(alias=alias, uri=uri, data=data, json=json_data,
                                                             params=params, headers=headers, files=files,
                                                             allow_redirects=None, timeout=timeout)
    elif request_type == 'DELETE':
        # Create Session
        super(RequestsLibrary, self).create_session(alias=alias, url=base_url, headers=headers, cookies=cookies,
                                                    auth=auth, timeout=timeout, proxies=proxies, verify=verify,
                                                    debug=debug, max_retries=max_retries,
                                                    backoff_factor=backoff_factor,
                                                    disable_warnings=1)
        # Trigger DELETE method
        response = super(RequestsLibrary, self).delete_request(alias=alias, uri=uri, data=data, json=json_data,
                                                               params=params, headers=headers, allow_redirects=None,
                                                               timeout=timeout)

    selected_api_df.loc[0, 'API_Response_Code'] = response.status_code
    if response.text != '':
        response_string = str(response.content.decode("utf-8"))
        selected_api_df.loc[0, 'API_Response_Content'] = response_string
    else:
        selected_api_df.loc[0, 'API_Response_Content'] = ''
    logger.info('Step-09: End   - Trigger the API, extract the response and status code')
    logger.info('*************************************************************************************************')

    return selected_api_df


if __name__ == "__main__":
    # If you have any code outside the function, keep it here
    pass
