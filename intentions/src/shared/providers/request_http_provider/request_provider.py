import requests

def request_provider(http_method, url, query_params, body):
  try:
    response = None
    if http_method == "get":
      get_res = requests.get(url, params=query_params)
      response = get_res.json()
      print(response)
    elif http_method == "post":
      post_res = requests.post(url, data=body)
      response = post_res.json()
    elif http_method == "put":
      put_res = requests.put(url, data=body)
      response = put_res.json()
    elif http_method == "delete":
      delete_res = requests.delete(url)
      response = delete_res.json()
    elif http_method == "patch":
      patch_res = requests.patch(url, data=body)
      response = patch_res.json()
  except Exception as exception:
    raise exception