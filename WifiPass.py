import subprocess
import ctypes
import re

# ====================================================================================

# Get saved wifi password from windows
def WifiPass(**kwargs):
    for name in subprocess.check_output('netsh wlan show profile', shell=True).split('\n'):
        try:
            SSID = name.split(':')[1].strip()
            password = re.findall('Key Content(.*)\n',subprocess.check_output('netsh wlan show profile' +' name=' +SSID +' key=clear',shell=True))[0].strip().split(':')[1].strip()
            ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11), 0x02)
            print('[+] Password found !!!')
            ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11), 0x07)
            print('SSID: ' +SSID)
            print('Password: ' +password +'\n')
        except:
            pass

# ====================================================================================


if __name__ == '__main__':
    print('----------------------- Wifi passwords ----------------------\n')
    WifiPass()
    raw_input('=============================================================\nPress any key to continue...')
