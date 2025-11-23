import json
from base64 import b64decode

def isPadded(b64_text: str) -> str:
    """
    Membenarkan padding dari base64
    """
    len_b64 = len(b64_text) % 4
    if len_b64:
        b64_text += '=' * (4 - len_b64)
    return b64_text

def decodeJWT(enc_jwt: str) -> dict:
    """
    Ini cuman melakukan decode terhadap header dan payload
    """
    header, payload, signature = enc_jwt.split('.')
    header = json.loads(b64decode(isPadded(header)).decode('utf-8'))
    payload = json.loads(b64decode(isPadded(payload)).decode('utf-8'))
    return header, payload

enc_jwt = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbGFnIjoiY3J5cHRve2p3dF9jb250ZW50c19jYW5fYmVfZWFzaWx5X3ZpZXdlZH0iLCJ1c2VyIjoiQ3J5cHRvIE1jSGFjayIsImV4cCI6MjAwNTAzMzQ5M30.shKSmZfgGVvd2OSB2CGezzJ3N6WAULo3w9zCl_T47KQ'
header, payload = decodeJWT(enc_jwt)

print(payload['flag'])