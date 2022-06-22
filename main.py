import time, keyboard, os

def slow_print(string):
    for char in string:
        print (char, end = "", flush=True)
        if char != " ":
            time.sleep(.01)
    print ("")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

title = r"""
                           ___
    |\    /|    /\    |\  |
    | \  / |   /  \   |/  |___
    |  \/  |  /----\  |\      |
    |      | /      \ | \  ___|

    -- Play now! --
    """

class Menu:
    def __init__(self, items, title = "") -> None:
        self.items = items
        self.title = title
        self.cursor = 0
        self.times_shown = 0
        self.item_time = time.time()
    
    def reset(self):
        self.cursor = 0
        self.times_shown = 0

    def __repr__(self) -> str:
        string = "" if self.title == "" else self.title + "\n"
        for n, item in enumerate(self.items):
            if n == self.cursor:
                string += "> "+item
            else:
                string += "  "+item
            if n != len(self.items)-1:
                string += "\n"
        return string

    def print(self):
        clear()
        if self.times_shown == 0:
            slow_print(str(self))
        else:
            print (self)

    def down(self, _):
        if time.time() - self.item_time < .5:
            return
        self.item_time = time.time()
        self.cursor += 1
        if self.cursor == len(self.items):
            self.cursor -= 1
        else:
            self.print()
        self.times_shown += 1
    
    def up(self, _):
        if time.time() - self.item_time < .5:
            return
        self.item_time = time.time()
        self.cursor -= 1
        if self.cursor == -1:
            self.cursor += 1
        else:
            self.print()
        self.times_shown += 1

    def run(self):
        self.print()
        self.times_shown += 1
        keyboard.hook_key("up", self.up)
        keyboard.hook_key("down", self.down)
        keyboard.wait("enter")
        keyboard.unhook_all()
        keyboard.send("ctrl+a")
        keyboard.send("delete")
        return self.items[self.cursor], self.cursor

print(Menu(["Mygga", "Leg", "Bob"], title).run())