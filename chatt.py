import time
import pyautogui

def get_multiple_messages():
    print("Enter your messages (type 'selesai' when finished):")
    messages = []
    while True:
        msg = input(f"Teks {len(messages)+1}: ")
        if msg.lower() == 'selesai':
            if len(messages) == 0:
                print("Please enter at least one message!")
                continue
            break
        messages.append(msg)
    return messages

# Ambil input dari user
messages = get_multiple_messages()
count = int(input('Enter how many times to send the messages: '))
gap = float(input('Interval (in seconds) between messages: '))
bot_prompt = input('Do you want to add bot prompt to your message? (Y/N) ').strip().upper()

# Info untuk fokus ke jendela chat target
print("\n\n📌 Please open the target chat window and click on the text input field.")
print("You have 5 seconds to switch to the chat window...\n")
time.sleep(5)

# Kirim pesan berulang kali ke jendela yang aktif
for i in range(count):
    for j, msg in enumerate(messages):
        msg_final = f"<Status: {i+1}/{count}> {msg}" if bot_prompt == 'Y' else msg
        pyautogui.write(msg_final, interval=0.02)
        pyautogui.press("enter")
        time.sleep(gap)

# Pesan penutup
pyautogui.write("Pesan selesai dikirim.")
pyautogui.press("enter")

print("\n✅ Semua pesan telah berhasil dikirim.")