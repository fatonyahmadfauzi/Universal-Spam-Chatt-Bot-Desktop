# Release Notes

## [v1.2.0] - 2025-04-17

**Branch:** `clipboard-integration`

---

### 🚀 Fitur Baru

1. **Sistem Clipboard**:

   - Dukungan penuh emoji & karakter Unicode via `pyperclip`.
   - Fix bug input EOF (`Ctrl+Z`/`Ctrl+D`).

2. **Bot Status**:

   - Header `<Status: x/y>` untuk melacak progres pengiriman.

3. **Optimasi Universal**:
   - Kompatibel dengan semua aplikasi desktop (WhatsApp, Telegram, Line, dll).

---

### 🐛 Perbaikan Bug

- Memperbaiki masalah pesan terpotong saat menggunakan jeda <1 detik.
- Karakter khusus (seperti `▲` atau `✅`) kini terbaca sempurna.

---

### 📥 Cara Upgrade

```bash
pip install --upgrade pyperclip
```

---

### 🧑💻 Contoh Penggunaan

**Kirim pesan:**

```bash
Berapa kali dikirim? 3
Interval antar pesan (detik): 1.5
Tambahkan status pengiriman? (Y/N): Y

📋 Tempel pesan:
*REMINDER* 🔔
Jangan lupa bayar tagihan
sebelum 30 Mei!
```

**Hasil:**

```
🚩 Status: 1/3
*REMINDER* 🔔
Jangan lupa bayar tagihan
sebelum 30 Mei!
```

---
