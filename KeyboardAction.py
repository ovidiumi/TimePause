import keyboard

class keyboardDisable():
    def start(self):
        self.on = True
    def stop(self):
        self.on = False
    def __call__(self):
        while self.on:
            keyboard.wait('esc')
    def __init__(self):
        self.on = True
        #import msvcrt

if __name__ == '__main__':
    main()
