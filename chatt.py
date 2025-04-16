import time
import pyautogui
import pyperclip  # Tambahkan library ini

def tempel_pesan():
    print("📋 Tempel pesan (tekan Ctrl+V lalu Enter):")
    pyperclip.paste()  # Kosongkan clipboard
    input()  # Tunggu user menempel pesan
    return pyperclip.paste()  # Ambil teks dari clipboard

count = int(input("Berapa kali dikirim? "))
gap = float(input("Interval antar pesan (detik): "))
bot_prompt = input("Tambahkan status pengiriman? (Y/N) ").strip().upper()

msg = tempel_pesan()

print("\n🚀 Arahkan kursor ke kolom chat (5 detik)...")
time.sleep(5)

for i in range(count):
    if bot_prompt == "Y":
        header = f"🚩 Status: {i+1}/{count}\n"
        pyperclip.copy(header)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
    
    # Salin pesan ke clipboard dan tempel
    pyperclip.copy(msg)
    pyautogui.hotkey('ctrl', 'v')  # Tempel pesan dengan emoji
    pyautogui.press('enter')
    time.sleep(gap)

print("\n✅ Pesan terkirim dengan emoji!")