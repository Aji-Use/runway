import pyautogui as gui
import time
import random
import pyfiglet


banner = pyfiglet.figlet_format("RunWay")
print(banner)
print("Created by @bagus._aji")
print()

print ("Selamat Datang di Tools Spam Pesan")
print()
print("Silahkan pilih mode Single Message atau Random Message untuk melakukan spam pesan")
print()
manualMode= print("1. Single Message")
autoMode= print("2. Random Message")

try:
    selectMode = int(input("> "))
except ValueError:
    print("Pilihan tidak valid, pilih angka 1 atau 2")
    exit()

print()


def singleMessage():
    message = input("Masukkan Pesan: ")
    total = int(input("Masukan Jumlah Pesan: "))

    time.sleep(2)

    for i in range (total):
        gui.typewrite(message)
        gui.press('Enter')
    
def randomMessage():
    randomText= []
    
    while True:
        text= input("Masukkan teks (atau ketik 'exit' untuk): ")
        
        if text.lower() == 'exit':
            break
        
        randomText.append(text)
    
    totalMsg= int(input("Masukkan jumlah pesan: "))
    
    time.sleep(3)
    
    for i in range (totalMsg):
        gui.typewrite(random.choice(randomText))
        gui.press('Enter')
   
if selectMode == 1:
    singleMessage()
elif selectMode ==2 :
    randomMessage()
else:
    print("pilihan tidak tersedia, silahkan pilih 1 atau 2.")