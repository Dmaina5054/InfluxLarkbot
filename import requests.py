import requests
import pandas as pd
import json
url = "http://172.16.0.46/stok=cfe0b583b894ae5af60d483e5cbe9c70/ds"


payload = "{\"method\":\"get\",\"authentication\":{\"table\":\"auth_session_list\",\"para\":{\"start\":0,\"end\":9999}}}"
#payload2 = "{\"method\":\"get\",\"authentication\":{\"table\":\"auth_session_list\",\"para\":{\"start\":0,\"end\":9999}}}"
headers = {
#   'Accept': 'text/plain, */*; q=0.01',
#   'X-Requested-With': 'XMLHttpRequest',
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
  'Content-Type': 'application/json; charset=UTF-8'
}

response = requests.request("POST", url, headers=headers, data = payload)
dumm = response.json()

print(dumm)
#print(type(dumm['authentication']['auth_session_list']))
df = dumm['authentication']['auth_session_list']
fin_df = pd.DataFrame(list(df))
fin_df.to_csv('authed.csv')


print(type(df))

import requests
import io
#from rest_framework.parsers import JSONParser


url2 = "http://172.16.0.46/"
def keygen():
    payload = "{\"method\":\"do\",\"login\":{\"username\":\"admin\",\"password\":\"vWdRrnYHWwefbwK\"}}"
    headers = {
#   'Accept': 'text/plain, */*; q=0.01',
#   'X-Requested-With': 'XMLHttpRequest',
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
  'Content-Type': 'application/json; charset=UTF-8'
}

    response = requests.request("POST", url2, headers=headers, data = payload)
    stok_key = response.text.encode('utf8')
    streamf = io.BytesIO(stok_key)
    #data = JSONParser().parse(streamf)
    #print(type(data))
    print(stok_key.decode("utf-8").split(':')[1].split(',')[0])
    #print(stok_key.decode("utf-8").split(',')[1])
    print(len(stok_key))
if __name__ == "__main__":
    keygen()