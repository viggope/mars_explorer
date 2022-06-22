import menu, save

def about():
    pass

def main_menu():
    n = None
    while n != None or n == 1:
        if not save.save_exists():
            menu_ = menu.ChoiceMenu(["Start new game", "About", "Exit"])
        else:
            menu_ = menu.ChoiceMenu(["Start new game", "About", "Exit"])
        name, n = menu_.run()
        if n == 0:
            return 1
        elif n == 1:
            about()
        else:
            quit()

def main():
    state = 0
    if state == 0:
        main_menu()

main()