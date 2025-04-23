# 🖥️ Universal Chat Sender Bot

Script Python sederhana untuk mengirim pesan otomatis ke aplikasi apa pun (WhatsApp Desktop, Telegram, Line, dll) menggunakan **PyAutoGUI**.  
Tidak perlu Selenium, browser, atau nama kontak — cukup posisikan kursor di kolom chat, dan bot akan mengirimkan pesan secara otomatis.

---

## 🚀 Fitur

- Mengirim pesan secara otomatis ke aplikasi yang aktif
- Tanpa tergantung pada nama kontak atau grup
- Dapat mengirim beberapa pesan berulang dengan interval waktu
- Opsi bot prompt (menampilkan `<Status: x/y>` pada setiap pesan)
- Ringan dan mudah digunakan

---

## 🔧 Cara Pakai

1. Pastikan Python 3 sudah terinstal.
2. Install PyAutoGUI:

```bash
pip install pyautogui
```

3. Jalankan script:

```bash
python chat.py
```

4. Isi pesan, jumlah, dan jeda.
5. Fokus ke aplikasi target dalam 5 detik.
6. Pesan akan diketik dan dikirim otomatis.

---

## 📝 Contoh Output

```vbnet
Enter your message: Halo bro!
Enter how many times to send the message: 3
Interval (in seconds) between messages: 1
Do you want to add bot prompt to your message? (Y/N) Y

📌 Please open the target chat window and click on the text input field.
You have 5 seconds to switch to the chat window...

✅ Semua pesan telah berhasil dikirim.
```

---

## ⚠️ Disclaimer

⚠️ Gunakan script ini secara bijak.
Script ini hanya untuk eksperimen dan edukasi pribadi.
Jangan digunakan untuk spam atau melanggar kebijakan aplikasi manapun.

---

## 👨‍💻 Dibuat oleh

- Revisi & versi PyAutoGUI oleh **Fatony Ahmad Fauzi**
- Terinspirasi dari WhatsApp Spam Bot berbasis Selenium
