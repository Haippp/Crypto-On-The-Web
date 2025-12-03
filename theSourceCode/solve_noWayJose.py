from requests import get
import Solve_TokenApprec as JWT
from base64 import b64encode
import json

URL = 'https://web.cryptohack.org/no-way-jose/'

def createSession(username: str) -> str:
    URL_CREATE_SESSION = URL + 'create_session/' + username
    jwt_token = get(URL_CREATE_SESSION).json()
    return jwt_token['session']

def jwtEncode(header: dict, payload: dict) -> str:
    header = json.dumps(header)
    payload = json.dumps(payload)
    enc_h = b64encode(str(header).encode()).decode().replace('=', '')
    enc_p = b64encode(str(payload).encode()).decode().replace('=', '')
    jwt_token = enc_h + '.' + enc_p + '.'
    return jwt_token

def authorise(token: str) -> dict:
    URL_AUTHORISE = URL + '/authorise/' + token
    flag = get(URL_AUTHORISE).json()
    return flag

# Membuat session untuk mengetahui struktur token jwtnya
login_session = createSession('Haippp')
print("JWT Token Encode : ", login_session)
jwt_decode = JWT.decodeJWT(login_session)
print("JWT Token Decode : ", jwt_decode)

# Membuat jwt token palsu untuk bisa masuk sebagai admin dan dapat flag
header = {'typ': 'JWT', 'alg': 'none'}
payload = {'username': 'Haippp', 'admin': True}
fake_token = jwtEncode(header, payload)

print(authorise(fake_token))