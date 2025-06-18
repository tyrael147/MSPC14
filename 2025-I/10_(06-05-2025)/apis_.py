# %% [markdown]
# # APIs in Python
#
# Apps and websites talk to each other and share data through **APIs**.  API stands for **Application Programming Interface**.

# %% [markdown]
# ## What is an API?
#
# An **API (Application Programming Interface)** is a set of rules, protocols, and tools that allows different software applications to communicate and exchange data or services. It defines the methods and data formats that applications can use to request and exchange information, abstracting the underlying implementation details.
#
# **Benefits**
# *   **Abstraction:** APIs hide the internal complexity of a system, exposing only necessary functionality.
# *   **Modularity:** Enables independent development, deployment, and scaling of software components.
# *   **Reusability:** A single API can be used by multiple applications to access the same service or data.
# *   **Automation:** Facilitates programmatic interaction between systems, enabling automation of tasks.

# %% [markdown]
# ## Types of APIs
#
# APIs can be categorized based on their scope and access method:
#
# 1.  **Web APIs (HTTP APIs):** Accessed over the web using the HTTP(S) protocol. These are central to modern web services and mobile applications. Common styles include:
#     *   **REST (Representational State Transfer):** An architectural style emphasizing statelessness and standard HTTP methods (GET, POST, PUT, DELETE). Data is often exchanged in JSON or XML.
#     *   **SOAP (Simple Object Access Protocol):** A protocol standard that relies heavily on XML for message format and is more rigid than REST.
#     *   **GraphQL:** A query language for APIs that allows clients to request precisely the data they need [(more info here)](https://realpython.com/python-api/).
#
# 2.  **Operating System APIs:** Provide interfaces for applications to interact with the operating system's functionalities (e.g., file system access, process management).
#
# 3.  **Library APIs:** Define how software components or libraries interact. When using a Python library (e.g., `numpy`, `pandas`), you are using its API.
#
# 4.  **Database APIs:** Allow applications to communicate with database management systems (e.g., Python's DB-API).
#

# %% [markdown]
# ## APIs in Python
#
# Python is well-suited for API interaction due to:
# *   **Extensive Libraries:** Libraries like `requests` simplify HTTP communication.
# *   **Data Processing Capabilities:** Python excels at handling common API data formats like JSON and XML.
# *   **Scripting and Automation:** Ideal for automating API-driven workflows.
#
# Common uses in Python include:
# *   Fetching data from public or private web services.
# *   Integrating third-party services (e.g., payment gateways, social media platforms).
# *   Building applications that expose their own APIs.

# %% [markdown]
# # HTTP APIs: The Foundation of Web Communication
#
# HTTP APIs use the Hypertext Transfer Protocol (HTTP) or its secure version (HTTPS) for communication. An application (the client) sends an **HTTP request** to a server, and the server returns an **HTTP response**.
#
# **An HTTP Request consists of:**
# *   **URL (Uniform Resource Locator):** The address of the API endpoint (e.g., `https://api.example.com/resource`).
# *   **HTTP Method:** The action to be performed (e.g., `GET`, `POST`).
# *   **Headers:** Metadata about the request (e.g., content type, authentication tokens).
# *   **Body (optional):** Data sent to the server, typically for `POST` or `PUT` requests (e.g., JSON payload).
#
# **An HTTP Response consists of:**
# *   **Status Code:** A 3-digit code indicating the outcome of the request (e.g., `200 OK`, `404 Not Found`).
# *   **Headers:** Metadata about the response (e.g., content type, server information).
# *   **Body (optional):** The data returned by the server or an error message.

# %% [markdown]
# # 3. Consuming APIs in Python with the `requests` Library
#
# The `requests` library is a popular and user-friendly Python library for making HTTP requests.

# %% [markdown]
# ## Test if installed

# %%
import requests
import json
from rich import print

# %% [markdown]
# ## Making a GET Request
#
# A `GET` request is used to retrieve data from a specified URL.

# %%
api_url = "https://jsonplaceholder.typicode.com/todos/1" # A public test API

print(f"Sending GET request to: {api_url}")
response = requests.get(api_url)
print(response)


# %% [markdown]
# ## Analyzing the Response Object
#
# The `response` object from `requests` provides several useful attributes:

# %%
#Indicates request success or failure.
print(f"Status Code: {response.status_code}")

# %%
#Response Content (as text)
print(f"Response Text: {response.text}")
# `response.content` provides the raw response body in bytes.
# `response.ok` is a boolean indicating if the status code was < 400.

# %% [markdown]
# > **_NOTE:_**  JSON (JavaScript Object Notation) is a text-based data format used to store and exchange information in a structured, human-readable way.

# %%
#JSON Response Parsing
# If the response is json, `response.json()` parses it into a Python dictionary or list.
if "application/json" in response.headers.get("Content-Type", ""):
    try:
        json_data = response.json()
        print("Parsed JSON Data:")
        print(json.dumps(json_data, indent=2))
    except requests.exceptions.JSONDecodeError:
        print("Failed to decode JSON from response.")
else:
    print("Response content is not JSON.")


# %%
#Response Headers: A dictionary-like object.
print("Response Headers:")
print(dict(response.headers.items()))


# %% [markdown]
# ## HTTP Response Status Codes
#
# Status codes inform the client about the server's handling of the request.
#
# *   **2xx (Successful):**
#     *   `200 OK`: Standard success response.
#     *   `201 Created`: Resource successfully created (e.g., after a POST).
#     *   `204 No Content`: Success, but no data to return (e.g., after a DELETE).
# *   **4xx (Client Error):** Indicates an issue with the client's request.
#     *   `400 Bad Request`: Malformed request.
#     *   `401 Unauthorized`: Authentication required or failed.
#     *   `403 Forbidden`: Valid authentication, but no permission for the resource.
#     *   `404 Not Found`: Requested resource does not exist.
#     *   `429 Too Many Requests`: Rate limit exceeded.
# *   **5xx (Server Error):** Indicates an issue on the server's side.
#     *   `500 Internal Server Error`: Generic server error.
#     *   `503 Service Unavailable`: Server is temporarily overloaded or down for maintenance.
#
# The `requests` library allows checking status codes and raising exceptions for errors:

# %%
url_valid = "https://jsonplaceholder.typicode.com/posts/1"
url_invalid = "https://jsonplaceholder.typicode.com/nonexistent/123"

response_valid = requests.get(url_valid)
print(f"Request to '{url_valid}': Status {response_valid.status_code}")

response_invalid = requests.get(url_invalid)
print(f"Request to '{url_invalid}': Status {response_invalid.status_code}")

# `raise_for_status()` raises an `HTTPError` for 4xx or 5xx status codes.
try:
    response_invalid.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"HTTPError encountered: {e}")

if response_valid.ok:
    print(f"Request to {url_valid} was successful.")

# %% [markdown]
# ## HTTP Methods
#
# HTTP methods define the action to be performed on a resource.
#
# *   **`GET`**: Retrieves data.
# *   **`POST`**: Submits data to create a new resource.
# *   **`PUT`**: Updates an existing resource entirely.
# *   **`PATCH`**: Partially updates an existing resource.
# *   **`DELETE`**: Removes a resource.
#
# Examples using `requests`:

# %%
base_posts_url = "https://jsonplaceholder.typicode.com/posts"

# POST: Create a new resource
new_post_payload = {"title": "New Post", "body": "Content", "userId": 1}
print("\n--- POST Request ---")
post_resp = requests.post(base_posts_url, json=new_post_payload) # `json=` handles serialization and headers
print(f"POST Status: {post_resp.status_code}, Response: {json.dumps(post_resp.json(), indent=2) if post_resp.ok else post_resp.text}")
created_id = post_resp.json().get('id') if post_resp.ok else None

# DELETE: Remove a resource
delete_url = put_url # Using the same resource ID
print("\n--- DELETE Request ---")
delete_resp = requests.delete(delete_url)
print(f"DELETE Status: {delete_resp.status_code}, Response: {delete_resp.text or '(No content)'}") # JSONPlaceholder returns {} for DELETE

# %% [markdown]
# ## Request Headers
#
# Headers convey additional information with HTTP requests and responses.
#
# **Common Request Headers:**
# *   `Content-Type`: Specifies the format of the request body (e.g., `application/json`).
# *   `Accept`: Informs the server about the content types the client can understand.
# *   `Authorization`: Contains credentials for authentication (e.g., `Bearer <token>`).
# *   `User-Agent`: Identifies the client application.
#
# Custom headers can be passed via the `headers` parameter in `requests`:

# %%
httpbin_headers_url = "https://httpbin.org/headers" # Echoes request headers
custom_req_headers = {
    "User-Agent": "PythonDemoClient/1.0",
    "X-API-Key": "example_key_value" # Example custom header
}

print(f"\nSending request to {httpbin_headers_url} with custom headers...")
headers_response = requests.get(httpbin_headers_url, headers=custom_req_headers)

if headers_response.ok:
    print("Server received these headers:")
    print(json.dumps(headers_response.json().get("headers", {}), indent=2))
else:
    print(f"Request failed: {headers_response.status_code}")

# %% [markdown]
# ## Query Parameters
#
# Query parameters are appended to the URL (after `?`) to send additional data, typically for `GET` requests (e.g., for filtering, sorting, or pagination).
# Example: `https://api.example.com/items?category=electronics&sort=price`
#
# `requests` handles URL encoding and appends parameters passed as a dictionary to the `params` argument.

# %%
todos_api_url = "https://jsonplaceholder.typicode.com/todos"
request_params = {
    "userId": 1,
    "completed": "true" # Values are often strings; consult API docs
}

print(f"\nRequesting from {todos_api_url} with parameters: {request_params}")
params_response = requests.get(todos_api_url, params=request_params)

print(f"Constructed URL: {params_response.url}")
print(f"Status Code: {params_response.status_code}")

if params_response.ok:
    print("Filtered To-Do Items (first 2):")
    for i, todo in enumerate(params_response.json()):
        if i < 2:
            print(json.dumps(todo, indent=2))
        else:
            print("... and more.")
            break
else:
    print(f"Request failed: {params_response.text}")

# %% [markdown]
# # 4. Rate Limiting
#
# **Rate limiting** is a mechanism used by APIs to control the number of requests a client can make within a specific time period.
#
# **Purposes of Rate Limiting:**
# *   Prevent abuse and denial-of-service attacks.
# *   Ensure fair usage and service availability for all clients.
# *   Manage server load and resource consumption.
#
# **Exceeding Rate Limits:**
# If a client exceeds the rate limit, the API typically responds with a `429 Too Many Requests` status code.
#
# **Handling Rate Limits:**
# 1.  **Consult API Documentation:** Understand the specific rate limits.
# 2.  **Check Response Headers:** APIs often provide headers indicating current rate limit status:
#     *   `X-RateLimit-Limit`: Total requests allowed per window.
#     *   `X-RateLimit-Remaining`: Requests remaining in the current window.
#     *   `X-RateLimit-Reset`: Timestamp (often Unix epoch) when the limit resets.
#     *   `Retry-After`: Seconds to wait before retrying (often with a `429` response).
# 3.  **Implement Caching:** Store frequently accessed, non-volatile data locally.
# 4.  **Request Efficiently:** Fetch only necessary data.
# 5.  **Implement Backoff Strategies:** If a `429` is received, wait before retrying, potentially increasing wait time for subsequent retries (exponential backoff).

# %%
# Conceptual example of checking rate limit headers (using GitHub API for illustration)
github_api_url = "https://api.github.com/rate_limit" # GitHub provides a specific endpoint for this
gh_req_headers = {"User-Agent": "PythonRateLimitCheck/1.0"} # GitHub requires User-Agent

print(f"\nChecking rate limits at: {github_api_url}")
try:
    rate_limit_resp = requests.get(github_api_url, headers=gh_req_headers, timeout=5)
    print(f"Status: {rate_limit_resp.status_code}")

    if rate_limit_resp.ok:
        print("Rate Limit Information from Headers:")
        print(f"  Limit: {rate_limit_resp.headers.get('X-RateLimit-Limit')}")
        print(f"  Remaining: {rate_limit_resp.headers.get('X-RateLimit-Remaining')}")
        reset_ts = rate_limit_resp.headers.get('X-RateLimit-Reset')
        if reset_ts:
            from datetime import datetime, timezone
            reset_datetime = datetime.fromtimestamp(int(reset_ts), tz=timezone.utc)
            print(f"  Reset Timestamp: {reset_ts} (UTC: {reset_datetime.strftime('%Y-%m-%d %H:%M:%S %Z')})")

        
        print("\nRate Limit Information from JSON Body:")
        print(json.dumps(rate_limit_resp.json(), indent=2))
    else:
        print(f"Failed to get rate limit info: {rate_limit_resp.text}")

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")



# %%
import requests
import json

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"

MODEL_NAME = "tinyllama:latest" 
PROMPT = "What is the capital of France?"
payload = {
        "model": MODEL_NAME,
        "prompt": PROMPT,
        "stream": False  # Set to False for a single, complete response
    }

response = requests.post(OLLAMA_ENDPOINT, json=payload)

# Raise an exception for HTTP errors (e.g., 404, 500)
response.raise_for_status()

# Parse the JSON response
response_data = response.json()
print(response_data['response'])


# %%
