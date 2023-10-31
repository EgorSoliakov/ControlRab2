import Model.Note as Note
def readFile():
    try:
        array = []
        file = open("note.txt", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Note.Note(
                id = split_n[0], title = split_n[1], body = split_n[2], date = split_n[3])
            array.append(note)
    except Exception:
        print('Журнал заметок пустой')        
    finally:
        return array
