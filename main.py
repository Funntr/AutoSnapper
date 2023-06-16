import time
import pyautogui
import keyboard
import tkinter as tk


def printScore():
    # Create the window
    root = tk.Tk()
    root.title("Snaps Sent")
    root.geometry("300x50+844+91")

    # Create the label widget
    printScore.score_label = tk.Label(root, text="Score: 0", font=("Arial", 32))
    printScore.score_label.pack()
    root.attributes("-topmost", True)
    root.update()


printScore()

print("Press ENTER to start...")
keyboard.wait('enter')
snapsSent = 0
count = 0

root = tk.Tk()
root.title("Snaps Sent")

while True:
    username = ""  # Enter Username here
    if keyboard.is_pressed('delete'):
        break
    pyautogui.moveTo(747, 541, duration=0.0)
    pyautogui.leftClick()
    pyautogui.moveTo(747, 541, duration=0.0)
    pyautogui.leftClick()
    pyautogui.moveTo(820, 568, duration=0.0)
    pyautogui.leftClick()
    pyautogui.moveTo(730, 235, duration=0.0)
    pyautogui.leftClick()
    pyautogui.typewrite(username, interval=0.0)
    pyautogui.moveTo(753, 571, duration=0.0)
    pyautogui.leftClick()
    pyautogui.moveTo(747, 541, duration=0.0)
    pyautogui.leftClick()
    # time.sleep(1)
    snapsSent = snapsSent + 1
    printScore.score_label.config(text=f"Snaps: {snapsSent}")
    root.update()
    count = count + 1
    if count == 500:
        pyautogui.moveTo(83, 46, duration=0.25)
        time.sleep(1)
        pyautogui.leftClick()
        count = 0
        time.sleep(8)
