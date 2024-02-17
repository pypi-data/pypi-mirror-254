# bacalhau_apiclient.OrchestratorApi

All URIs are relative to *http://bootstrap.production.bacalhau.org:1234/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orchestratorjob_executions**](OrchestratorApi.md#orchestratorjob_executions) | **GET** /api/v1/orchestrator/jobs/{id}/executions | Returns the executions of a job.
[**orchestratorjob_history**](OrchestratorApi.md#orchestratorjob_history) | **GET** /api/v1/orchestrator/jobs/{id}/history | Returns the history of a job.
[**orchestratorjob_results**](OrchestratorApi.md#orchestratorjob_results) | **GET** /api/v1/orchestrator/jobs/{id}/results | Returns the results of a job.
[**orchestratorlist_jobs**](OrchestratorApi.md#orchestratorlist_jobs) | **GET** /api/v1/orchestrator/jobs | Returns a list of jobs.
[**orchestratorput_job**](OrchestratorApi.md#orchestratorput_job) | **PUT** /api/v1/orchestrator/jobs | Submits a job to the orchestrator.
[**orchestratorstop_job**](OrchestratorApi.md#orchestratorstop_job) | **DELETE** /api/v1/orchestrator/jobs/{id} | Stops a job.

# **orchestratorjob_executions**
> ApiListJobExecutionsResponse orchestratorjob_executions(id, limit=limit, next_token=next_token, reverse=reverse, order_by=order_by)

Returns the executions of a job.

Returns the executions of a job.

### Example
```python
from __future__ import print_function
import time
import bacalhau_apiclient
from bacalhau_apiclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bacalhau_apiclient.OrchestratorApi()
id = 'id_example' # str | ID to get the job executions for
limit = 56 # int | Limit the number of executions returned (optional)
next_token = 'next_token_example' # str | Token to get the next page of executions (optional)
reverse = true # bool | Reverse the order of the executions (optional)
order_by = 'order_by_example' # str | Order the executions by the given field (optional)

try:
    # Returns the executions of a job.
    api_response = api_instance.orchestratorjob_executions(id, limit=limit, next_token=next_token, reverse=reverse, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrchestratorApi->orchestratorjob_executions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID to get the job executions for | 
 **limit** | **int**| Limit the number of executions returned | [optional] 
 **next_token** | **str**| Token to get the next page of executions | [optional] 
 **reverse** | **bool**| Reverse the order of the executions | [optional] 
 **order_by** | **str**| Order the executions by the given field | [optional] 

### Return type

[**ApiListJobExecutionsResponse**](ApiListJobExecutionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orchestratorjob_history**
> ApiListJobHistoryResponse orchestratorjob_history(id, since=since, event_type=event_type, execution_id=execution_id, node_id=node_id)

Returns the history of a job.

Returns the history of a job.

### Example
```python
from __future__ import print_function
import time
import bacalhau_apiclient
from bacalhau_apiclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bacalhau_apiclient.OrchestratorApi()
id = 'id_example' # str | ID to get the job history for
since = 'since_example' # str | Only return history since this time (optional)
event_type = 'event_type_example' # str | Only return history of this event type (optional)
execution_id = 'execution_id_example' # str | Only return history of this execution ID (optional)
node_id = 'node_id_example' # str | Only return history of this node ID (optional)

try:
    # Returns the history of a job.
    api_response = api_instance.orchestratorjob_history(id, since=since, event_type=event_type, execution_id=execution_id, node_id=node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrchestratorApi->orchestratorjob_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID to get the job history for | 
 **since** | **str**| Only return history since this time | [optional] 
 **event_type** | **str**| Only return history of this event type | [optional] 
 **execution_id** | **str**| Only return history of this execution ID | [optional] 
 **node_id** | **str**| Only return history of this node ID | [optional] 

### Return type

[**ApiListJobHistoryResponse**](ApiListJobHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orchestratorjob_results**
> ApiListJobResultsResponse orchestratorjob_results(id, limit=limit, next_token=next_token, reverse=reverse, order_by=order_by)

Returns the results of a job.

Returns the results of a job.

### Example
```python
from __future__ import print_function
import time
import bacalhau_apiclient
from bacalhau_apiclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bacalhau_apiclient.OrchestratorApi()
id = 'id_example' # str | ID to get the job results for
limit = 56 # int | Limit the number of results returned (optional)
next_token = 'next_token_example' # str | Token to get the next page of results (optional)
reverse = true # bool | Reverse the order of the results (optional)
order_by = 'order_by_example' # str | Order the results by the given field (optional)

try:
    # Returns the results of a job.
    api_response = api_instance.orchestratorjob_results(id, limit=limit, next_token=next_token, reverse=reverse, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrchestratorApi->orchestratorjob_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID to get the job results for | 
 **limit** | **int**| Limit the number of results returned | [optional] 
 **next_token** | **str**| Token to get the next page of results | [optional] 
 **reverse** | **bool**| Reverse the order of the results | [optional] 
 **order_by** | **str**| Order the results by the given field | [optional] 

### Return type

[**ApiListJobResultsResponse**](ApiListJobResultsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orchestratorlist_jobs**
> ApiListJobsResponse orchestratorlist_jobs(namespace=namespace, limit=limit, next_token=next_token, reverse=reverse, order_by=order_by)

Returns a list of jobs.

Returns a list of jobs.

### Example
```python
from __future__ import print_function
import time
import bacalhau_apiclient
from bacalhau_apiclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bacalhau_apiclient.OrchestratorApi()
namespace = 'namespace_example' # str | Namespace to get the jobs for (optional)
limit = 56 # int | Limit the number of jobs returned (optional)
next_token = 'next_token_example' # str | Token to get the next page of jobs (optional)
reverse = true # bool | Reverse the order of the jobs (optional)
order_by = 'order_by_example' # str | Order the jobs by the given field (optional)

try:
    # Returns a list of jobs.
    api_response = api_instance.orchestratorlist_jobs(namespace=namespace, limit=limit, next_token=next_token, reverse=reverse, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrchestratorApi->orchestratorlist_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Namespace to get the jobs for | [optional] 
 **limit** | **int**| Limit the number of jobs returned | [optional] 
 **next_token** | **str**| Token to get the next page of jobs | [optional] 
 **reverse** | **bool**| Reverse the order of the jobs | [optional] 
 **order_by** | **str**| Order the jobs by the given field | [optional] 

### Return type

[**ApiListJobsResponse**](ApiListJobsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orchestratorput_job**
> ApiPutJobResponse orchestratorput_job(body)

Submits a job to the orchestrator.

Submits a job to the orchestrator.

### Example
```python
from __future__ import print_function
import time
import bacalhau_apiclient
from bacalhau_apiclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bacalhau_apiclient.OrchestratorApi()
body = bacalhau_apiclient.Job() # Job | Job to submit

try:
    # Submits a job to the orchestrator.
    api_response = api_instance.orchestratorput_job(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrchestratorApi->orchestratorput_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Job**](Job.md)| Job to submit | 

### Return type

[**ApiPutJobResponse**](ApiPutJobResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orchestratorstop_job**
> ApiStopJobResponse orchestratorstop_job(id, reason=reason)

Stops a job.

Stops a job.

### Example
```python
from __future__ import print_function
import time
import bacalhau_apiclient
from bacalhau_apiclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bacalhau_apiclient.OrchestratorApi()
id = 'id_example' # str | ID to stop the job for
reason = 'reason_example' # str | Reason for stopping the job (optional)

try:
    # Stops a job.
    api_response = api_instance.orchestratorstop_job(id, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrchestratorApi->orchestratorstop_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID to stop the job for | 
 **reason** | **str**| Reason for stopping the job | [optional] 

### Return type

[**ApiStopJobResponse**](ApiStopJobResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

