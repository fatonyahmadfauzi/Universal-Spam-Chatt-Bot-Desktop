# 🚀 Universal Chat Sender Bot (Multi-Line Text Only)

**Script Python untuk mengirim pesan otomatis ke aplikasi chat dengan dukungan multi-teks & emoji!**  
Menggunakan sistem keyboard input untuk mengirim serangkaian pesan secara berurutan.

---

## 🌟 Fitur Utama

- ✅ **Multi-Teks**: Kirim beberapa pesan sekaligus dalam satu rangkaian (ketik "selesai" untuk mengakhiri input)
- ✅ **Pengiriman Berulang**: Atur jumlah pengiriman dan jeda waktu antar pesan
- ✅ **Bot Status**: Tambahkan header `<Status: x/y>` untuk pelacakan progres
- ✅ **Multi-Platform**: Bekerja di semua aplikasi desktop (WhatsApp, Telegram, Line, dll)
- ✅ **User Friendly**: Penomoran otomatis pesan (Teks 1, Teks 2, dst)

---

## 🛠️ Instalasi

1. Pastikan Python 3.10+ terinstal
2. Install dependensi:

```bash
pip install pyautogui
```

---

## 🖥️ Cara Pakai

1. Jalankan script:

```bash
python chatt.py
```

2. Ikuti instruksi:

```bash
Enter your messages (type 'selesai' when finished):
Teks 1: Halo semua!
Teks 2: Ini adalah pesan kedua
Teks 3: Terima kasih
Teks 4: selesai

Enter how many times to send the messages: 3
Interval (in seconds) between messages: 1.5
Do you want to add bot prompt to your message? (Y/N) Y
```

3. Arahkan kursor ke kolom chat dalam 5 detik
4. Script akan mengirim semua pesan secara berurutan

---

## � Contoh Output

```
<Status: 1/3> Halo semua!
<Status: 1/3> Ini adalah pesan kedua
<Status: 1/3> Terima kasih
<Status: 2/3> Halo semua!
... (dan seterusnya)
```

---

## 🚨 Troubleshooting

- **Pesan tidak terkirim?** Pastikan:
  - Aplikasi chat sudah terbuka
  - Kursor aktif di kolom input chat
  - Tidak ada popup yang menghalangi
- **Interval tidak akurat?** Sistem mungkin sibuk, tambahkan sedikit waktu jeda

---

## 📜 Release Notes

Terbaru: **v1.3.0** - [Lihat catatan rilis]()

---

## ⚠️ Disclaimer

**Hanya untuk tujuan edukasi!**
Penggunaan untuk spam dapat melanggar kebijakan aplikasi.
