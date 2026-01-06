# Token Appreciation
![](https://img.shields.io/badge/Jenis_enkripsi-JWT-purple) ![](https://img.shields.io/badge/Tingkat_kesulitan-Sedang-green)
## 📑Deskripi Challange
Berikut ini adalah potongan kodenya:
```python
import json
import jwt # note this is the PyJWT module, not python-jwt

FLAG = ?
SECRET_KEY = ?

@chal.route('/json-in-json/authorise/<token>/')
def authorise(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except Exception as e:
        return {"error": str(e)}

    if "admin" in decoded and decoded["admin"] == "True":
        return {"response": f"Welcome admin, here is your flag: {FLAG}"}
    elif "username" in decoded:
        return {"response": f"Welcome {decoded['username']}"}
    else:
        return {"error": "There is something wrong with your session, goodbye"}


@chal.route('/json-in-json/create_session/<username>/')
def create_session(username):
    body = '{' \
              + '"admin": "' + "False" \
              + '", "username": "' + str(username) \
              + '"}'
    encoded = jwt.encode(json.loads(body), SECRET_KEY, algorithm='HS256')
    return {"session": encoded}
```
## 🧩Penyelesaian
Kerentanannya itu terletak pada pembuatan json berikut:
```python
body = '{' \
        + '"admin": "' + "False" \
        + '", "username": "' + str(username) \
        + '"}'
```
Kode diatas membangun objek JSON secara manual menggunakan string concatenation, tanpa melakukan validasi atau sanitasi terhadap input username. Hal ini memungkinkan terjadinya JSON Injection.

Oleh karena itu kita bisa memanfaatkan input username untuk melakukan eksploitasi dengan payload seperti ini `Haippp", "admin": "True` jadi visualnya akan jadi seperti ini:
```json
{
    "admin": "False",
    "username": "Haippp",
    "admin": "True"
}
```
Dalam standar parsing JSON, jika terdapat ket yang sama, maka nilai yang terbaru/terakhirlah yang akan digunakan. Akibatnya, nilai dari admin akan bersifat True sehingga kita bisa masuk sebagai admin dan eksploitasinya berhasil

Untuk kode otomasi yang ku gunakan bisa dilihat di -> [solve_jsonInJson.py](./theSourceCode/solve_jsonInJson.py)