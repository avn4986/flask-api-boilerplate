# Boilerplate for Flask API
This repository contains boilerplate code for Flask API which contains code for:
```
    1. Global Error Handler
    2. Custom Exception Handling.
    3. Docker Setup (NOTE: App is served through gunicorn in the container so that it has better performance)
```

## Terms
### duration
- This denotes the total amount of time taken in milliseconds by the API to process the request.
- In terms of flask, time taken between `@app.before_request` to (`@app.after_request` or `@app.error_handler`)

### data
- The actual response of the API 

### error_desc/error_code
- Suitable error code along with error description 

### request_id
- This is maintained by the `X-Request-Id` header. 
- If this is not present in the request, a UUID is generated and assigned 

## Directory Structure
```
.
├── Dockerfile
├── README.md
├── api.py
├── commons
│   ├── __init__.py
│   ├── api_exception.py
│   ├── constants.py
│   ├── error_definitions.py
│   └── response_obj.py
├── config
│   └── config.ini
├── logs
│   └── api.log
├── requirements.txt
├── start-api.sh
└── utils
    ├── __init__.py
    ├── api_log_filter.py
    ├── api_utils.py
    ├── path_utils.py
    └── utils.py
```

## Logging
- Two handlers have been added out of the box
    - Stream/Console Handler
    - Rotating File Handler
- Relevant properties can be seen in [Configuration File](./config/config.ini)
- Logging Format
    -   ```[2020-11-13 07:53:39,898] [t:Thread-1] [loc:__main__.after_request_func:24] [rid:45d93b91-e1f7-4878-98d8-4c140c076a27] [ip:127.0.0.1] INFO method="GET" uri="/success" query="" duration=0.37ms status=200 OK```
    - The above log message tracks the following: 
        - timestamp
        - thread
        - code
        - location
        - request-id
        - requester ip address
        - method
        - uri
        - query parameters
        - duration
        - status

## Config
- `.ini` file is used in the project to define the properties
- Timezones are overridden to UTC by default under `global -> timezone`
- Startup port can be defined in the environment variable as `PORT`
- You can have profile based configuration for logger by the environment variable `RUN_ENVIRONMENT`
- If the environment is `docker` then `docker_logger` section should be present in the ini file 

## Response Structure
### Success
```
{
  "data": {
    "message": "hello-word"
  },
  "error_desc": null,
  "error_code": null,
  "duration": 0,
  "request_id": "96fa6228-203e-4fab-928f-38750a204295"
}
```

### Failure
```
{
  "data": null,
  "error_desc": "Internal server occurred, please contact support team.",
  "error_code": "API-ERR-1000",
  "duration": 0,
  "request_id": "c709852c-9354-4ac5-b579-6d185f6b07ac"
}
```
