# Token Appreciation
![](https://img.shields.io/badge/Jenis_enkripsi-JWT-purple) ![](https://img.shields.io/badge/Tingkat_kesulitan-Sedang-green)
## 📑Deskripi Challange
Skenario ini kurang lebih sama seperti RSA or HMAC yang sebelumnya tapi disini tantangannya adalah PUBKEY itu tidak diberikan.

Berikut ini adalah potongan kodenya:
```python
import jwt # note this is the PyJWT module, not python-jwt


# Private key generated using: openssl genrsa -out rsa-or-hmac-2-private.pem 2048
with open('challenge_files/rsa-or-hmac-2-private.pem', 'rb') as f:
   PRIVATE_KEY = f.read()
# Public key generated using: openssl rsa -RSAPublicKey_out -in rsa-or-hmac-2-private.pem -out rsa-or-hmac-2-public.pem
with open('challenge_files/rsa-or-hmac-2-public.pem', 'rb') as f:
   PUBLIC_KEY = f.read()

FLAG = ?


@chal.route('/rsa-or-hmac-2/authorise/<token>/')
def authorise(token):
    try:
        decoded = jwt.decode(token, PUBLIC_KEY, algorithms=['HS256', 'RS256'])
    except Exception as e:
        return {"error": str(e)}

    if "admin" in decoded and decoded["admin"]:
        return {"response": f"Welcome admin, here is your flag: {FLAG}"}
    elif "username" in decoded:
        return {"response": f"Welcome {decoded['username']}"}
    else:
        return {"error": "There is something wrong with your session, goodbye"}


@chal.route('/rsa-or-hmac-2/create_session/<username>/')
def create_session(username):
    encoded = jwt.encode({'username': username, 'admin': False}, PRIVATE_KEY, algorithm='RS256')
    return {"session": encoded}

```

## 🧩Penyelesaian
Seperti yang bisa kita lihat pada source codenya tidak ada sama sekali route untuk mengambil public key. Oleh karena itu tahap pertama yang perlu kita lakukan adalah dengan merecover atau memulihkan public keynya. Disini saya menggunakan script [forgery.py](https://github.com/silentsignal/rsa_sign2n/blob/release/standalone/jwt_forgery.py) dari https://github.com/silentsignal/rsa_sign2n.