import pyautogui
import pyperclip
import subprocess
import time
from groq import groqAi


def is_last_message_from_other_user(chat_history: str) -> bool:
    lines = chat_history.strip().split("\n")
    last_line = lines[-1].strip() if lines else ""

    try:
        # Split properly and clean whitespace
        senderName = last_line.split("]")[1].split(":")[0].strip()
        print(f"Sender Detected: '{senderName}'")
        return senderName != "Abdul Manan"  # Replace with your name
    except IndexError:
        print("Could not extract sender from:", last_line)
        return False


def main():
    while True:
        # Step 1: Focus Brave browser using wmctrl
        subprocess.run(["wmctrl", "-a", "brave"])  # Replace with your browser name
        time.sleep(1)

        # Step 2: Select the text from chat area
        pyautogui.moveTo(652, 213)
        pyautogui.mouseDown()
        pyautogui.moveTo(659, 930, duration=1.5)
        pyautogui.mouseUp()

        # Step 3: Copy the selected text to clipboard
        time.sleep(0.5)
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.5)
        pyautogui.click(652, 213)  # Optional: focus back

        # Step 4: Get chat history from clipboard
        chat_history = pyperclip.paste()
        if is_last_message_from_other_user(chat_history):
            print("Copied Text from Brave Browser:\n", chat_history)

            # Step 5: Generate response using Groq AI
            response = groqAi(chat_history)

            # Step 6: Click on input field and paste response
            pyautogui.click(775, 963)
            time.sleep(0.3)
            pyperclip.copy(response)
            pyautogui.hotkey("ctrl", "v")
            pyautogui.press("enter")
        else:
            print("Last message is from Abdul Manan — skipping response.")

        time.sleep(3)  # Optional: wait before checking again


if __name__ == "__main__":
    main()
