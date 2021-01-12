import pyautogui, time
time.sleep(5)


f = open('friends_transcript.txt', 'r')

for i in range(675):
    pyautogui.typewrite(f.readline())
    pyautogui.press("enter")
    time.sleep(0.03)





