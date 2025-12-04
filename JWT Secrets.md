# Token Appreciation
![](https://img.shields.io/badge/Jenis_enkripsi-JWT-purple) ![](https://img.shields.io/badge/Tingkat_kesulitan-Mudah-green)
## 📑Deskripi Challange
Berikut ini adalah potongan kode sumber dengan satu fungsi untuk membuat sesi dan fungsi lain untuk mengotorisasi sesi serta memeriksa izin admin. Namun, ada komentar aneh tentang kunci rahasia. Apa yang akan Anda lakukan?
```python
import jwt # note this is the PyJWT module, not python-jwt


SECRET_KEY = ? # TODO: PyJWT readme key, change later
FLAG = ?


@chal.route('/jwt-secrets/authorise/<token>/')
def authorise(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except Exception as e:
        return {"error": str(e)}

    if "admin" in decoded and decoded["admin"]:
        return {"response": f"Welcome admin, here is your flag: {FLAG}"}
    elif "username" in decoded:
        return {"response": f"Welcome {decoded['username']}"}
    else:
        return {"error": "There is something wrong with your session, goodbye"}


@chal.route('/jwt-secrets/create_session/<username>/')
def create_session(username):
    encoded = jwt.encode({'username': username, 'admin': False}, SECRET_KEY, algorithm='HS256')
    return {"session": encoded}
```
link tantangan : https://web.cryptohack.org/jwt-secrets/

## 🧩Penyelesaian
Komentar yang perlu di perhatikan disini adalah `# TODO: PyJWT readme key, change later`, dari komentar tersebut kita bisa mengambil dugaan bahwa mungkin saja secret key yang digunakan ada pada [dokumentasi library PyJWT](https://pyjwt.readthedocs.io/en/latest/usage.html). Dan secret key yang digunakan disana adalah `'secret'`, jadi saya coba dan ternyata berhasil! codenya bisa di lihat di -> [solve_JWTSecrets.py](./theSourceCode/solve_JWTSecrets.py).