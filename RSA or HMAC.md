# RSA or HMAC
![](https://img.shields.io/badge/Jenis_enkripsi-JWT-purple) ![](https://img.shields.io/badge/Tingkat_kesulitan-Sedang-green)

## 📑Deskripi Challange
Disini kita disuruh agar bisa masuk sebagai admin, dimana algoritma jwt yang digunakan adalah RS256

Berikut ini adalah potongan kodenya:
```python
import jwt # note this is the PyJWT module, not python-jwt


# Key generated using: openssl genrsa -out rsa-or-hmac-private.pem 2048
with open('challenge_files/rsa-or-hmac-private.pem', 'rb') as f:
   PRIVATE_KEY = f.read()
with open('challenge_files/rsa-or-hmac-public.pem', 'rb') as f:
   PUBLIC_KEY = f.read()

FLAG = ?


@chal.route('/rsa-or-hmac/authorise/<token>/')
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


@chal.route('/rsa-or-hmac/create_session/<username>/')
def create_session(username):
    encoded = jwt.encode({'username': username, 'admin': False}, PRIVATE_KEY, algorithm='RS256')
    return {"session": encoded}


@chal.route('/rsa-or-hmac/get_pubkey/')
def get_pubkey():
    return {"pubkey": PUBLIC_KEY}
```
link tantangan : https://web.cryptohack.org/rsa-or-hmac/

 
Algoritma RS256 bekerja dengan dua buah kunci dimana kunci privat digunakan untuk melakukan penandatanganan sedangkan public untuk melakukan validasi. Sedangkan HS256 hanya menggunakan satu buah kunci untuk tanda tangan dan verifikasi. Nah disinilah celahnya, Karena public key digunakan sebagai verifikasi dan bisa kita akses, juga algoritma yang digunakan kita bisa memilih salah satu. Maka dari itu kita gunakan public key tersebut untuk melakukan penandatanganan dan kita ubah algoritmanya menjadi HS256. Dan yapp kita dapat flagnya

codenya bisa di lihat di -> [solve_RSAorHMAC.py](./theSourceCode/solve_RSAorHMAC.py).