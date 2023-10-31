import View.UserMenu as ui
import Presenter.commands as com

def start():
    while True:
        ui.menuConsole()
        userInput = input()
        if userInput == '1':
            com.show("all")
        elif userInput == '2':
            com.show("all")
            com.changeNote()
        elif userInput == '3':
            com.addNote()
        elif userInput == '4':
            com.show("all")
            com.delNote()
        else:
            print("Программа Журнал заметок завершена")
            break    