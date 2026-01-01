import jwt
import requests as r
from Crypto.PublicKey.RSA import import_key

URL = 'https://web.cryptohack.org/rsa-or-hmac/'

def get_pubkey():
    pubkey_url = URL + 'get_pubkey/'
    response = r.get(pubkey_url)
    return response.json()['pubkey']

def auth(token):
    auth_url = URL + 'authorise/' + token
    response = r.get(auth_url).json()
    return response['response']

public_key = get_pubkey()
payload = {'username': 'haippp', 'admin': True}
fake_token = jwt.encode(payload, public_key, 'HS256')
print(auth(fake_token))