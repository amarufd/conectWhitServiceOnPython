import http.client as cli
import json

def GetTokenCognito():
    conn = None
    params = {'username': '','password': '','userPoolId': ''}
    headers = {'Content-type': 'application/json','x-api-key': ''}
    url = ''
    metodo = ''
    try:
        conn = cli.HTTPSConnection(url)
        conn.request('POST',metodo,json.dumps(params),headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        data = response.read()
        return json.loads(data)
    except (Exception) as e:
        print('error ',e)
    finally:
        if (conn != None):
            conn.close()