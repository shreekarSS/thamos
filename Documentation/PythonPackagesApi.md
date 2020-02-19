# thamos.swagger_client.PythonPackagesApi

All URIs are relative to *https://test.thoth-station.ninja/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_python_package_dependencies**](PythonPackagesApi.md#get_python_package_dependencies) | **GET** /python/dependencies | Get direct dependencies of Python libraries. If environment is provided, take into account environment markers that are evaluated during dependencies installation. If environment is not provided, any environment is considered. 
[**get_python_package_versions_count**](PythonPackagesApi.md#get_python_package_versions_count) | **GET** /python/packages/count | Retrieve information from the Knowledge Graph with regards to total number of Python packages. 

# **get_python_package_dependencies**
> PythonPackageDependencies get_python_package_dependencies(name, version, index, os_name=os_name, os_version=os_version, python_version=python_version, marker_evaluation_result=marker_evaluation_result)

Get direct dependencies of Python libraries. If environment is provided, take into account environment markers that are evaluated during dependencies installation. If environment is not provided, any environment is considered. 

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.PythonPackagesApi()
name = 'tensorflow' # str | Name of the Python Package. (default to tensorflow)
version = '2.0.0' # str | Version of the Python Package. (default to 2.0.0)
index = 'https://pypi.org/simple' # str | Index url of the Python Package. (default to https://pypi.org/simple)
os_name = 'os_name_example' # str | Name of operating system to consider as environment where package is installed in. (optional)
os_version = 'os_version_example' # str | Version of operating system to consider as environment where package is installed in. (optional)
python_version = 'python_version_example' # str | Version of Python interpreter used to install the given package. (optional)
marker_evaluation_result = true # bool | Consider marker evaluation result for the given environment. If set to None, marker evaluation result is not taken into account.  (optional)

try:
    # Get direct dependencies of Python libraries. If environment is provided, take into account environment markers that are evaluated during dependencies installation. If environment is not provided, any environment is considered. 
    api_response = api_instance.get_python_package_dependencies(name, version, index, os_name=os_name, os_version=os_version, python_version=python_version, marker_evaluation_result=marker_evaluation_result)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonPackagesApi->get_python_package_dependencies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the Python Package. | [default to tensorflow]
 **version** | **str**| Version of the Python Package. | [default to 2.0.0]
 **index** | **str**| Index url of the Python Package. | [default to https://pypi.org/simple]
 **os_name** | **str**| Name of operating system to consider as environment where package is installed in. | [optional] 
 **os_version** | **str**| Version of operating system to consider as environment where package is installed in. | [optional] 
 **python_version** | **str**| Version of Python interpreter used to install the given package. | [optional] 
 **marker_evaluation_result** | **bool**| Consider marker evaluation result for the given environment. If set to None, marker evaluation result is not taken into account.  | [optional] 

### Return type

[**PythonPackageDependencies**](PythonPackageDependencies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_python_package_versions_count**
> PythonPackagesCountInfoResponse get_python_package_versions_count()

Retrieve information from the Knowledge Graph with regards to total number of Python packages. 

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.PythonPackagesApi()

try:
    # Retrieve information from the Knowledge Graph with regards to total number of Python packages. 
    api_response = api_instance.get_python_package_versions_count()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PythonPackagesApi->get_python_package_versions_count: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PythonPackagesCountInfoResponse**](PythonPackagesCountInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
