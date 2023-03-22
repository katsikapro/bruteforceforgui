import pyautogui
import random
import cryptography
import string
import time
passwords = []
count = 0
letters= string.ascii_lowercase
length = random.randint(7,16)
yes = int(input("yes or no"))
timestoforce = int(input("times to bruteforce:"))
if yes == "yes":
  time.sleep(60)
  while count < timestoforce:
    pas = ''.join(random.choice(letters) for i in range(length))
    passwords.append(pas)
    pyautogui.write(passwords[count], interval=0.25)
    pyautogui.press('enter')
    count =+ 1
#for educational purposes only
  