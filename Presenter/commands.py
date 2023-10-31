import Model.loadFile as lF
import Model.saveFile as wF
import Model.Note

def addNote():
    title = input("Введите заголовок заметки:\n")
    body = input("Введите описание заметки:\n")
    note = Model.Note.Note(title=title, body=body)
    array_notes = lF.readFile()
    for i in array_notes:
        if Model.Note.Note.getId(note) == Model.Note.Note.setId(i):
            Model.Note.Note.setId(note)
    array_notes.append(note)
    wF.saveFile(array_notes,'a')
    print("Заметка добавлена в журнал!")  

def show(txt):
    array_notes = lF.readFile()
    if array_notes:
        if txt == "all":
          print("Журнал заметок:")
          for i in array_notes:
              print(Model.Note.Note.map_note(i))
    elif txt == "ID":
        for i in array_notes:
            print("ID: ", Model.Note.Note.map_note(i))
        id = input("\nВведите id заметки: ")  
        flag = True
        for i in array_notes:
            if id == Model.Note.Note.getId(i):
                print(Model.Note.Note.map_note(i))  
                flag = False
        if flag:
            print("Нет такого ID")   
    elif txt == "date":
        date = input("Введите дату в формате: dd.mm.yyyy: ")  
        flag = True
        for i in array_notes:
            dateNote = str(Model.Note.Note.getDate(i))  
            if date == dateNote[:10]:    
                print(Model.Note.Note.map_note(i)) 
                flag = False
        if flag:
            print("Нет такой даты") 
    else:
        print("Журнал заметок пустой!")   

def changeNote():
    id = input("введите ID изменяемой заметки: ")
    array_notes = lF.readFile()
    flag = True
    array_notes_new = []
    for i in array_notes:
        if id == Model.Note.Note.getId(i):
            i.title = input("Измените заголовок:\n")
            i.body = input("Измените описание:\n")
            Model.Note.Note.setDate(i)
            flag = False
        array_notes_new.append(i)

    if flag:
        wF.saveFile(array_notes_new,'a')
        print("Заметка c id:", id, "успешно изменена!")        
    else:
        print("нет такого id")


def delNote():
    id = input("Введите ID удаляемой заметки:\n ")
    array_note = lF.readFile()
    flag = False

    for i in array_note:
        if id == Model.Note.Note.getId(i):
            array_note.remove(i)
            flag = True

    if flag:
        wF.saveFile(array_note,'a')  
        print("Заметка с id: ", id, " успешно удалена!")  
    else:
        print("нет такого id")    
