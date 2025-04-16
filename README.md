# 🚀 Universal Chat Sender Bot (Clipboard Edition)

**Script Python untuk mengirim pesan otomatis ke aplikasi chat dengan dukungan emoji & format teks!**  
Menggunakan sistem clipboard untuk memastikan karakter khusus (seperti emoji) tidak rusak.

---

## 🌟 Fitur Utama

- ✅ **Emoji & Format Teks**: Kirim emoji (🎉, ✅), teks tebal/miring (`*tebal*`, `_miring_`), dan simbol khusus via clipboard.
- ✅ **Pengiriman Berulang**: Atur jumlah pengiriman dan jeda waktu.
- ✅ **Bot Status**: Tambahkan header `<Status: x/y>` untuk pelacakan.
- ✅ **Multi-Platform**: Bekerja di aplikasi desktop seperti WhatsApp, Telegram, Messenger, dll.
- ✅ **Anti-Error**: Penanganan khusus karakter EOF (`Ctrl+Z`/`Ctrl+D`).

---

## 🛠️ Instalasi

1. Pastikan Python 3.10+ terinstal.
2. Install dependensi:

```bash
pip install pyautogui pyperclip
```

---

## 🖥️ Cara Pakai

1. Jalankan script:

```bash
python chatt.py
```

2. Ikuti instruksi:

```bash
Berapa kali dikirim? 5
Interval antar pesan (detik): 2
Tambahkan status pengiriman? (Y/N): Y

📋 Tempel pesan (tekan Ctrl+V lalu Enter):
[HALO!] 🚀
*Promo Spesial* hari ini:
Beli 1 Gratis 1 ✅
```

3. Arahkan kursor ke kolom chat dalam 5 detik.
4. Script akan mengirim pesan secara otomatis.

---

## 🚨 Troubleshooting

- **Emoji tidak muncul?**
  Pastikan menempel pesan via `Ctrl+V` (bisa dari Notepad/Word).
- **Pesan terkirim tanpa format?**
  Gunakan sintaks aplikasi target (contoh: `*tebal*` untuk WhatsApp).
- **Karakter aneh (^Z)?**
  Hindari mengetik manual. Selalu salin-tempel pesan!

---

## 📜 Release Notes

Terbaru: **v1.2.0** - [Lihat catatan rilis]()

---

## ⚠️ Disclaimer

**Hanya untuk tujuan edukasi!**
Penggunaan untuk spam dapat melanggar kebijakan aplikasi.

---
