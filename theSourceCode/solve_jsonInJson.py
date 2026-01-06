import requests as r

URL = 'https://web.cryptohack.org/json-in-json/'

def create_session(userame: str) -> str:
    url_session = URL + f'create_session/{userame}/'
    response = r.get(url_session).json()
    return response['session']

def auth(token: str) -> str:
    url_auth = URL + f'authorise/{token}/'
    response = r.get(url_auth).json()
    return response['response']

token = create_session('Haipp", "admin": "True')
result = auth(token)
print(result)