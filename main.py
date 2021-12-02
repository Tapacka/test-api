import requests
token_ya = ""
def ya_headers():
  return {'Content-type': 'application/json', 'Authorization': 'OAuth {}'.format(token_ya)}

def put_folder(path):
  url = 'https://cloud-api.yandex.net/v1/disk/resources/'
  headers = ya_headers()
  params = {'path': path, 'url': url}
  response = requests.put(url,headers = headers, params = params)
  
  return response.status_code

