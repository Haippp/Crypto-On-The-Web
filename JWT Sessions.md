# Token Appreciation
![](https://img.shields.io/badge/Jenis_enkripsi-JWT-purple) ![](https://img.shields.io/badge/Tingkat_kesulitan-Mudah-green)
## 📑Deskripi Challange
Untuk tantangan kali ini flagnya merupakan header HTTP yang digunakan oleh browser untuk mengirimkan JWT ke server.\

## Authorization Header
Header `Authorization` adalah header HTTP yang digunakan untuk mengirimkan kredensial (seperti token akses, kata sandi, atau kunci API) dari klien ke server untuk menautentikasi identitas klien. Nah ini lah yang digunakan saat klien perlu mengakses sumber daya yang dilindungi setelah login, klien menyertakan JWT di header `Authorization` pada permintaan selanjutnya. Format standart:
```http
Authorization: Bearer <token>
```
Misalnya:
```http
GET /resource HTTP/1.1
Host: server.example.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR...
```

Jadi jawabannya adalah `Authorization`