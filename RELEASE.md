# Release Notes

## [v1.3.0] - 2025-04-21

**Branch:** `multi-text-support`

---

### 🚀 Fitur Baru

1. **Multi-Teks Input**:

   - Dukungan input beberapa pesan sekaligus
   - Penomoran otomatis (Teks 1, Teks 2, dst)
   - Perintah "selesai" untuk mengakhiri input

2. **Sistem Pengiriman**:

   - Mengirim semua pesan secara berurutan tiap iterasi
   - Status tracking berlaku untuk seluruh rangkaian pesan

3. **Optimasi**:
   - Waktu jeda yang lebih konsisten antar pesan
   - Penanganan error yang lebih baik

---

### 🐛 Perbaikan Bug

- Memperbaiki masalah input kosong
- Meningkatkan respons waktu jeda
- Perbaikan minor pada tampilan prompt

---

### 📥 Cara Upgrade

```bash
git pull origin main
```

---

### 🧑💻 Contoh Penggunaan

**Input:**

```bash
Teks 1: Promo hari ini 🎉
Teks 2: *Diskon 50%* untuk 10 pembeli pertama
Teks 3: Jangan lewatkan! ✅
Teks 4: selesai
```

**Hasil:**

```
<Status: 1/3> Promo hari ini 🎉
<Status: 1/3> *Diskon 50%* untuk 10 pembeli pertama
<Status: 1/3> Jangan lewatkan! ✅
<Status: 2/3> Promo hari ini 🎉
... (dan seterusnya)
```
