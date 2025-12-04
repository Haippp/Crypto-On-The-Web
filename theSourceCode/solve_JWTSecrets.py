import jwt
import requests as r

URL = 'https://web.cryptohack.org/jwt-secrets/'
SECRET_KEY = 'secret'

def createSession(username: str) -> dict:
    URL_SESSION = URL + 'create_session/' + username
    token_session = r.get(URL_SESSION).json()
    return token_session

def authoriseJWT(jwt_token: str) -> dict:
    URL_AUTH = URL + 'authorise/' + jwt_token
    response = r.get(URL_AUTH).json()
    return response

# verifikasi bahwa secret key yang digunakan benar
jwt_token = createSession('admin')['session']
print(jwt_token)
print(jwt.decode(jwt_token, SECRET_KEY, algorithms='HS256'))

# melakukan serangan agar bisa masuk sebagai admin
evil_jwt = jwt.encode({'username': 'admin', 'admin': True}, SECRET_KEY, algorithm='HS256')
respons = authoriseJWT(evil_jwt)
print(respons)