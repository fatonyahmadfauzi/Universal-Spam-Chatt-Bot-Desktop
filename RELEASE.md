# Release Notes

## [v1.0.0] - 2025-04-16

**Branch:** `text-only`

---

### 📦 Fitur Baru

- **Pengiriman Pesan Otomatis**: Script dapat mengirimkan pesan ke aplikasi apa pun yang aktif (WhatsApp Desktop, Telegram, Line, dll).
- **Mode Berulang**: Dapat mengirimkan pesan beberapa kali dengan interval waktu yang ditentukan.
- **Bot Prompt**: Pilihan untuk menambahkan prompt bot pada setiap pesan dengan format `<Status: x/y>`.
- **Portabilitas**: Tidak tergantung pada nama kontak atau grup, cukup gunakan aplikasi chat yang aktif.

---

### 🛠️ Perbaikan Bug

- Tidak ada perbaikan bug untuk rilis awal ini.

---

### 📈 Peningkatan

- Optimisasi pengiriman pesan dengan jeda waktu antar pesan menggunakan `time.sleep`.
- Penggunaan `pyautogui` untuk memastikan kompatibilitas dengan berbagai aplikasi chat desktop.

---

### 🚨 Catatan Penting

- **Peringatan Waktu Fokus**: Anda memiliki waktu 5 detik untuk berpindah ke jendela chat target sebelum pesan mulai dikirim.
- **Gunakan Secara Bijak**: Script ini dirancang untuk penggunaan edukasi dan eksperimen pribadi. Jangan digunakan untuk spam atau aktivitas tidak etis.

---

### 👷 Kontributor

- **Fatony Ahmad Fauzi**
  - Pengembang utama dan dokumentasi.

---

### 📥 Cara Upgrade

1. Pull branch `main`:
   ```bash
   git pull origin main
   ```
2. Pastikan dependensi telah diinstal:
   ```bash
   pip install pyautogui
   ```
3. Jalankan ulang script dengan perintah:
   ```bash
   python chatt.py
   ```
