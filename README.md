### API's HTTP Requests

- GET
- POST
- PUT
- DELETE

### 1. GET
GET requests are used to retrieve data from a server. They are typically used for fetching information without modifying any data on the server.
#### Syntax in Python
```

  import requests

  response = requests.get('https://api.example.com/data')
  data = response.json()

  print(data)

```

### 2. POST
POST requests are used to send data to a server to create a resource. They are commonly used for submitting forms or uploading files.
#### Syntax in Python
```
  import requests

  payload = {'key1': 'value1', 'key2': 'value2'}
  response = requests.post('https://api.example.com/create', json=payload)

  print(response.text)

```
### 3. PUT
PUT requests are used to update a resource on the server. They are used when you want to modify an existing resource completely.
#### Syntax in Python
```

  import requests

  payload = {'key1': 'updated_value'}
  response = requests.put('https://api.example.com/update/1', json=payload)

  print(response.text)

```

### 4. DELETE
DELETE requests are used to delete a resource from the server. They are used when you want to remove a specific resource.
#### Syntax in Python
```

  import requests
  
  response = requests.delete('https://api.example.com/delete/1')

  print(response.text)

```
