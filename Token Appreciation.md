# Token Appreciation
![](https://img.shields.io/badge/Jenis_enkripsi-JWT-purple) ![](https://img.shields.io/badge/Tingkat_kesulitan-Mudah-green)
## 📑Deskripi Challange
```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbGFnIjoiY3J5cHRve2p3dF9jb250ZW50c19jYW5fYmVfZWFzaWx5X3ZpZXdlZH0iLCJ1c2VyIjoiQ3J5cHRvIE1jSGFjayIsImV4cCI6MjAwNTAzMzQ5M30.shKSmZfgGVvd2OSB2CGezzJ3N6WAULo3w9zCl_T47KQ
```
Disini kita diberikan sebuah tantangan untuk melakukan decoding terhadap sebuah JSON Web Token diatas untuk mendapatkan flagnya.
## 🌿Pengenalan
Sebelum kita melakukan decoding kita harus tahu dulu bahwa JWT sebenarnya terbagi menjadi 2 metode yaitu JSON Web Signature(JWS) dan JSON Web Encryption(JWE). Perbedaan diantara keduanya adalah JWS bisa dibaca oleh siapapun yang memiliki token sedangkan JWE harus yang memiliki secret key serta token untuk dapat memacanya. Dari struktur sendiri JWS itu hanya 3 bagian sedangkan JWE 5.

Selengkapnya bisa kalian [baca disini](https://developer.okta.com/blog/2020/12/21/beginners-guide-to-jwt).

## 🧩Penyelesaian
Untuk token yang kita dapatkan sekarang itu merupakan JWS. Dimana seperti yang kita tahu sendiri JWS bisa kita baca tanpa menggunakan kunci. Nah, JWS sendiri hanyalah sebuah Encoding Base64 URL. Untuk menyelesaikannya sendiri banyak metode bisa dengan mengguanakan [JWT Debugger](https://token.dev/) yang ada di web dan bisa menggunakan python seperti ini
```python
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
```
Atau bisa juga kita menggunakan libray PyJWT seperti ini
```python
import jwt

enc_jwt = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbGFnIjoiY3J5cHRve2p3dF9jb250ZW50c19jYW5fYmVfZWFzaWx5X3ZpZXdlZH0iLCJ1c2VyIjoiQ3J5cHRvIE1jSGFjayIsImV4cCI6MjAwNTAzMzQ5M30.shKSmZfgGVvd2OSB2CGezzJ3N6WAULo3w9zCl_T47KQ'
dec_jwt = jwt.decode(enc_jwt, options={"verify_signature": False})

print(dec_jwt)
```