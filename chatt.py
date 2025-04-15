import time
import pyautogui

# Ambil input dari user
msg = input('Enter your message: ')
count = int(input('Enter how many times to send the message: '))
gap = float(input('Interval (in seconds) between messages: '))
bot_prompt = input('Do you want to add bot prompt to your message? (Y/N) ').strip().upper()

# Info untuk fokus ke jendela chat target
print("\n\n📌 Please open the target chat window and click on the text input field.")
print("You have 5 seconds to switch to the chat window...\n")
time.sleep(5)

# Kirim pesan berulang kali ke jendela yang aktif
for i in range(count):
    msg_final = f"<Status: {i+1}/{count}> {msg}" if bot_prompt == 'Y' else msg
    pyautogui.write(msg_final, interval=0.02)
    pyautogui.press("enter")
    time.sleep(gap)

# Pesan penutup
pyautogui.write("Pesan selesai dikirim.")
pyautogui.press("enter")

print("\n✅ Semua pesan telah berhasil dikirim.")
